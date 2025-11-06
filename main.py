from typing import List, Dict, Any

from src.scraperBook import get_book_urls, get_book_details
from src.saveDetails import update_json


pages_to_scrap = 5
homepage = 'https://books.toscrape.com/catalogue/page-1.html'
all_books_data: List[Dict[str, Any]] = []

output_file = 'books_data.json'
book = []

def crawler() -> None:

    book_urls = get_book_urls(pages_to_scrap, homepage, book)
    print(book_urls)

    if not book_urls:
        print("Nenhuma URL encontrada. Encerrando.")
        return

    for url in book_urls:
        details = get_book_details(url)
        if details:
            all_books_data.append(details)
            print(f"Detalhes extraídos para {url}")
            print(details)
    

    if all_books_data:
        update_json(all_books_data, output_file)
    else:
        print("Nenhum dado de livro foi extraído.")

if __name__ == "__main__":
    crawler()