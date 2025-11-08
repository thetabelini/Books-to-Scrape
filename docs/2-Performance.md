## Otimizações de Performance
### Teste 1 - Implementação Inicial
- **Tempo inicial**: ~1:40-2:00 minutos
- **Parser**: BeautifulSoup com parser padrão
- **Resultado**: Baseline para comparação

![First Test](img/first_test.png)

### Teste 2 - Otimização do Parser
**Mudança implementada:**
```python
# Antes
def get_html_content(html):
    return BeautifulSoup(html.text, 'html.parser')

# Depois  
def get_html_content(html):
    return BeautifulSoup(html.text, 'lxml') 
```

**Resultado**: Pequena melhoria de performance utilizando o parser `lxml`, conforme [documentação oficial](https://beautiful-soup-4.readthedocs.io/en/latest/).

![Second Test](img/second_test.png)

### Teste 3 - Reutilização de Sessão HTTP
**Otimização implementada:**
```python
# Criação de sessão global para reutilização
session = requests.Session()

def get_html(url):
    return session.get(url, timeout=10)
```

**Resultado**: 
- ✅ **Redução de 87% no tempo de execução**
- ⚡ Tempo final: ~17 segundos
- 🔄 Reutilização da conexão TCP/SSL entre requisições

![Third Test](img/third_test.png)

| Versão | Tempo Execução | Otimização | 
|--------|----------------|------------|
| V1     | ~1:40-2:00 min | Baseline   |
| V2     | ~1:30 min      | Parser lxml|
| V3     | ~17 segundos   | Session HTTP |