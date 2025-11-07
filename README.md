# Books-to-Scrape

Código sendo repassado e avaliado casos de type hint e a utilização do PEP8

Para esse desafio proponho como um bonus de entrega, proponho realizar Test Unitário (taxa 80%)


## Otimização do Código
- Na priomeira execução o RPA estava gastando aproximadamente (1:40 ~ 2:00) minutos:
![First Test](img/first_test.png)

Preciso reduzir esse tempo, pelo menos em 50%.

- Segundo teste modifiquei algumas configurações do print no console. Nessa imagem abaixo é a configuração utilzando:
```
    def get_html_content(html):
        return BeautifulSoup(html.text, 'lxml') 
```
```
    def get_html_content(html):
        return BeautifulSoup(html.text, 'html') 
```

Adotado pois na [documentação requests](https://beautiful-soup-4.readthedocs.io/en/latest/) informa que xmlx é muito rápida. Mas o resultado obtido não teve grandes impactos.