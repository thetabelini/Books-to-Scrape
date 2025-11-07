import requests
import time

from bs4 import BeautifulSoup
from datetime import datetime, timezone
from alive_progress import alive_bar

# Create a session for connection reuse and set timeout
session = requests.Session()

# Function to send HTTP GET request with timeout and session reuse
def get_html(url):
    return session.get(url, timeout=10)

# Parse HTML content using BeautifulSoup with lxml parser for better performance
def get_html_content(html):
    return BeautifulSoup(html.text, 'lxml')

# Extract book URLs from specified variable (PAGES_TO_SCRAPE) of the website
def get_book_urls(pages: int, homepage: str, book_urls: list) -> list:
    print()
    print('get_book_urls()')

    with alive_bar(pages) as bar:
        for page_number in range(1, pages + 1):
            
            new_url = homepage.replace("-1.html", f"-{page_number}.html")
            bar()
            
            try:
                html = get_html(new_url)
                soup = get_html_content(html)

                article_rows = soup.find_all('article', class_='product_pod')

                for row in article_rows:
                    link_element = row.find('h3').find('a')
                    link_element['href'] = 'https://books.toscrape.com/catalogue/' + link_element['href']
                    book_urls.append(link_element['href'])      

            except Exception as e:  
                print(f"Error ao requisitar nova url {new_url}: {e}")

    return book_urls

# Extract detailed information from a single book page
def get_book_details(url: str) -> dict:
    try:
        html = get_html(url)
        soup = get_html_content(html)
        
        # Extract all elements
        product_table = soup.find('table', class_='table-striped')
        genre = soup.find('ul', class_='breadcrumb').find_all('a')[2].text
        title = soup.find('h1').text
        rating_classes = soup.find('p', class_='star-rating')['class']
        description_tag = soup.find('div', id='product_description')
        
        # Process table data efficiently
        table_data = {row.find('th').text: row.find('td').text for row in product_table.find_all('tr')}
        price = table_data.get('Price (incl. tax)')
        availability = table_data.get('Availability')
        upc = table_data.get('UPC')
        product_type = table_data.get('Product Type')
        
        rating = f"{rating_classes[1]} out of 5"
        
        description = description_tag.find_next_sibling('p').text if description_tag else "N/A"

        extraction_timestamp = datetime.now(timezone.utc).isoformat()

        return {
            'title': title,
            'price': price,
            'genre': genre,
            'availability': availability,
            'rating': rating,
            'description': description,
            'upc': upc,
            'product_type': product_type,
            'product_url': url,
            'extraction_timestamp': extraction_timestamp
        }
    
    except Exception as e:
        return {"error": f"Erro ao extrair detalhes do livro em {url}: {e}"}