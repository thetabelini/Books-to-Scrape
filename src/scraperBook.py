import requests
import time

from bs4 import BeautifulSoup
from datetime import datetime, timezone
from alive_progress import alive_bar

def get_html(url):
    return requests.get(url)

# talvez otimizaria aqui utilizando o lxml. Documentacao informa que é "Very fast" e html é descente kkk
# Ponto para se medir a performance depois
def get_html_content(html):
    return BeautifulSoup(html.text, 'html.parser')

def get_book_urls(pages: int, homepage: str, book_urls: list) -> list:
 
    print()
    print('get_book_urls()')
    somatorio = 0

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

def get_book_details(url: str) -> dict:
    try:
        html = get_html(url)
        soup = get_html_content(html)

        product_table = soup.find('table', class_='table-striped')
        table_data = {row.find('th').text: row.find('td').text for row in product_table.find_all('tr')}

        title = soup.find('h1').text
        price = table_data.get('Price (incl. tax)')
        genre = soup.find('ul', class_='breadcrumb').find_all('a')[2].text
        availability = table_data.get('Availability')
        rating_classes = soup.find('p', class_='star-rating')['class']
        rating = f"{rating_classes[1]} out of 5"
        description_tag = soup.find('div', id='product_description')
        description = description_tag.find_next_sibling('p').text if description_tag else "N/A"
        upc = table_data.get('UPC')
        product_type = table_data.get('Product Type')
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