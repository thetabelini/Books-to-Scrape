import datetime

from typing import List, Dict, Any

from src.scraperBook import get_book_urls, get_book_details
from src.saveDetails import update_json


pages_to_scrap = 5
homepage = 'https://books.toscrape.com/catalogue/page-1.html' #retirar -1.html depois
all_books_data: List[Dict[str, Any]] = []

output_file = 'books_data.json'
book = []

def crawler() -> None:
    # Medição de tempo de execução
    inicio = datetime.datetime.now().strftime('%H:%M:%S')
    print("Iniciando o crawler em: ", inicio)

    book_urls = get_book_urls(pages_to_scrap, homepage, book)
    print(f"Total de URLs de livros encontradas: {len(book_urls)}")

    if not book_urls:
        print("Nenhuma URL encontrada. Encerrando.")
        return

    for url in book_urls:
        details = get_book_details(url)
        if details:
            all_books_data.append(details)
    print("finalizei a extração dos detalhes dos livros.")

    

    if all_books_data:
        update_json(all_books_data, output_file)
        print("fazendo a atualização do arquivo JSON.")
    else:
        print("Nenhum dado de livro foi extraído.")

    # Medição de tempo de execução
    fim = datetime.datetime.now().strftime('%H:%M:%S')
    print("Crawler finalizado em: ", fim)

    teste = datetime.datetime.strptime(fim, '%H:%M:%S') - datetime.datetime.strptime(inicio, '%H:%M:%S')
    print("Tempo total de execução: ", teste)

if __name__ == "__main__":
    crawler()
