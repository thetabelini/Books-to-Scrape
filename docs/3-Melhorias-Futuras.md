# Sugestões de Melhorias Futuras

## 1. Armazenamento

Faria a alteração do arquivo JSON, pois é uma estrutura "difícil" de se ler, além de  crescer muito. Pois realizamos a extração apenas de 5 páginas, o nosso arquivo gerado possui cerca 1200 linhas.

Solução: Banco de Dados MongoDB
Substituiria o arquivo que salva em json e criar uma nova classe para banco, assim poderia ter mais controles dos livros cadastrados ou não.

## 3. Melhorias Extras (Para Aprender Gradualmente) 

### 3.1 Logs: Acompanhar o que acontece 
Só vemos prints no terminal. Se der erro, perdemos a informação.
Adicionária um outro bloco que teria a função de salvar os logs, com informações pertinentes da execução. Salvando em arquivos a inicialização da extração do scraper, erros de processar livros e entre outros.

### 3.2 Configurações: Não deixar valores "grudados" no código
URLs, números de páginas estão fixos no código. Adicionária valores padrão que podem sobrescritos. 

### 3.3 Rate Limiting
Sei que fazer muitas requisições muito rápido pode derrubar o site ou nos bloquear. Adicionaria uma nova biblioteca ou uma função simples que permitisse dar esse delay para fazer novas requisições.
