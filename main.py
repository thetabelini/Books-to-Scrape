import datetime

from typing import List, Dict, Any
from alive_progress import alive_bar

from src.scraperBook import get_book_urls, get_book_details
from src.saveDetails import update_to_json


# Configuration constants
PAGES_TO_SCRAPE = 5
HOMEPAGE = 'https://books.toscrape.com/catalogue/page-1.html'
OUTPUT_FILE = 'books_data.json'

# Global data containers
all_books_data: List[Dict[str, Any]] = []
book_urls_list = []

def crawler() -> None:
    """
    This function scrapes book data from the books.toscrape.com,
    extracts book details and saves them to a JSON file. It also measures
    and displays the total execution time.
    """
    
    # Console write start time
    inicio = datetime.datetime.now().strftime('%H:%M:%S')
    print("Iniciando o crawler em: ", inicio)

    # Step 1: Get all book URLs
    book_urls = get_book_urls(PAGES_TO_SCRAPE, HOMEPAGE, book_urls_list)

    print()
    print(f'Total de URLs de livros encontradas: {len(book_urls)}')
    print('get_book_details()')


    if not book_urls:
        print('Nenhuma URL encontrada. Encerrando.')
        return
    
    # Step 2: Get details for each book URL
    with alive_bar(len(book_urls)) as bar:
        for url in book_urls:
            details = get_book_details(url)
            if details:
                all_books_data.append(details)
            bar()

    # Step 3: Save all book details to JSON
    if all_books_data: 
        update_to_json(all_books_data, OUTPUT_FILE)
    else: print("Nenhum dado de livro foi extraído.")

    # Measure time of execution
    fim = datetime.datetime.now().strftime('%H:%M:%S')
    teste = datetime.datetime.strptime(fim, '%H:%M:%S') - datetime.datetime.strptime(inicio, '%H:%M:%S')
    print()
    print("Tempo total de execução: ", teste)

if __name__ == "__main__":
    crawler()
