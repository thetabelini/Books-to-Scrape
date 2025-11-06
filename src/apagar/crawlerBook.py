import requests
import scraperBook
from bs4 import BeautifulSoup, soup

paginaParaScrapear = 5
homePage = 'https://books.toscrape.com/catalogue/page-1.html'
book_urls = []


def get_html(url):
    return requests.get(url)

# talvez otimizaria aqui utilizando o lxml. Documentacao informa que é "Very fast" e html é descente kkk
# Ponto para se medir a performance depois
def get_html_content(html):
    return BeautifulSoup(html.text, 'html.parser')

def get_book_urls(pages: int, homePage: str):

    for numPagina in range(1, pages + 1):
        nova_url = homePage.replace("-1.html", f"-{numPagina}.html")
        
        try:
            html = get_html(nova_url)
            soup = get_html_content(html)

            article_rows = soup.find_all('article', class_='product_pod')

            for row in article_rows:
                    link_element = row.find('h3').find('a')
                    link_element['href'] = 'https://books.toscrape.com/catalogue/' + link_element['href']
                    book_urls.append(link_element['href'])
                    
        except Exception as e:  
            print(f"Error ao requisitar nova url {nova_url}: {e}")

    return book_urls

def crawler():
    
    urls = get_book_urls(paginaParaScrapear, homePage)
    print(urls)



if __name__ == "__main__":
    crawler()
    
    scraperBook()