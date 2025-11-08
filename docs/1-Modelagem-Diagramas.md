### Modularidade
- **`main.py`**: Coordenação geral e medição de performance
- **`scraperBook.py`**: Lógica de extração e parsing
- **`saveDetails.py`**: Serialização para JSON

## Fluxograma Prospoto no Inicio
![](../img/Arquitetura_INICIAL%20-%20Book%20to%20Scraper.png)
Propus esse desenho para ajudar a desenvolver o crawler. Inicialmente, pensei em separar em dois arquivo o meu sistema, para separar as responsabilidades. Sendo em Crawler, percorrendo as páginas definidas e adicionando a uma lista. E o  Scarper, responsavel por percorrer cada página para extrair os dados estruturados.