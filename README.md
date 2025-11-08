<p align="center">
  <a href="https://github.com/thetabelini/Books-to-Scrape">
    <img loading="lazy" alt="Scrape" src="https://github.com/thetabelini/Books-to-Scrape/blob/main/img/aquivo_home.png" width="100%"/>
  </a>
</p>

# Books-to-Scrape

Crawler em Python capaz de extrair as informações requisitadas da página [Books to Scrape](https://books.toscrape.com/index.html).
O projeto extrai informações detalhadas de livros das primeiras 5 páginas e salva os dados em formato JSON.


## Desenvolvedor

* Felipe Tabelini Pena

## Pré-requisitos

- Python 3.13+
- Pipenv

## ⚙️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/thetabelini/Books-to-Scrape.git
cd Books-to-Scrape
```

2. Instale as dependências usando Pipenv:
```bash
pipenv install
```

## 🎯 Execução

Execute o crawler com o comando:
```bash
pipenv run python main.py
```

O arquivo `books_data.json` será gerado na raiz do projeto com todos os dados extraídos.


# Documentação

<ol>
<li><a href="docs/1-Modelagem-Diagramas.md"> Otimizações de Performance </a></li>
<li><a href="docs/2-Performance"> Modelagem e diagramas arquiteturais </a></li>
<li><a href="docs/3-Melhorias-Futuras"> Melhorias Futuras </a></li>
</ol>

# Código

<li><a href="main.py"> Código Fonte</a></li>
