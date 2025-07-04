```markdown
# Ollama API - Guia de Acesso via URL

Este documento descreve como permitir que uma aplicação acesse um modelo LLM no Ollama via URL, incluindo a configuração do
Ollama, a configuração da aplicação e considerações importantes.

## 1. Configuração do Ollama para Exposição de API

*   **Verifique a Versão:** Certifique-se de estar usando uma versão recente do Ollama.
*   **Execute o Comando:** No terminal, navegue até o diretório onde o modelo está sendo executado e execute:

    ```bash
    ollama serve --api
    ```

    *   **Porta:**  Por padrão, a API estará disponível em `http://localhost:11434/`. Você pode alterar a porta usando a opção
`--port`:

        ```bash
        ollama serve --api --port 8080
        ```

*   **Documentação da API:** Consulte a documentação completa da API do Ollama:
[https://ollama.com/docs/api/](https://ollama.com/docs/api/)

## 2. Configuração da Aplicação para Consumir a API

*   **Escolha uma Linguagem:** Use uma linguagem de programação com bibliotecas HTTP (Python, JavaScript, Node.js, etc.).
*   **Bibliotecas HTTP:** Utilize uma biblioteca HTTP para fazer requisições (ex: `requests` em Python, `fetch` ou `axios` em
JavaScript).
*   **Formato da Requisição:** A API do Ollama usa JSON para enviar requisições.
*   **Autenticação:** Verifique se o modelo requer autenticação e como configurá-la (ex: incluindo um token de acesso na cabeçera
da requisição).

## Exemplo de Código Python (usando `requests`)

```python
import requests
import json

# Configurações da API do Ollama
API_URL = "http://localhost:11434/api/generate"  # Ajuste a URL se você usou uma porta diferente
MODEL_NAME = "llama2"  # Substitua pelo nome do seu modelo

def gerar_texto(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "model": MODEL_NAME,
        "temperature": 0.7,  # Ajuste a temperatura para controlar a aleatoriedade
        "max_tokens": 256      # Ajuste o número máximo de tokens
    }
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Lança uma exceção para erros HTTP
        response_json = response.json()
        return response_json["response"]
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

# Exemplo de uso
prompt = "Escreva um breve resumo sobre a história da inteligência artificial."
resumo = gerar_texto(prompt)

if resumo:
    print(resumo)
```

## Explicação do Código Python

*   **`API_URL`:** A URL da API do Ollama. Ajuste para a porta que você configurou.
*   **`MODEL_NAME`:** O nome do modelo que você está usando.
*   **`headers`:** Define o tipo de conteúdo da requisição como JSON.
*   **`data`:** Um dicionário Python que contém os parâmetros da requisição.
*   **`requests.post()`:** Envia uma requisição POST para a API do Ollama.
*   **`response.raise_for_status()`:** Verifica se a requisição foi bem-sucedida (código HTTP 200). Se houver um erro, lança uma
exceção.
*   **`response.json()`:** Converte a resposta JSON em um dicionário Python.
*   **`response_json["response"]`:** Extrai o texto gerado do campo `response` no dicionário da resposta.

## Considerações Importantes

*   **Segurança:**
    *   **Não exponha a API diretamente na internet:** Use um proxy ou um servidor reverso para proteger o modelo.
    *   **Autenticação:** Implemente um sistema de autenticação para proteger a API.
*   **Gerenciamento de Recursos:** Configure o gerenciador de recursos do Ollama para limitar o uso de CPU, memória e disco.
*   **Escalabilidade:** Se você precisar lidar com um grande número de requisições, use um servidor reverso ou um balanceador de
carga.
*   **Formato da Requisição:** Consulte a documentação da API do Ollama para o formato correto das requisições e respostas.
*   **Tratamento de Erros:** Implemente tratamento de erros em sua aplicação para lidar com falhas na API do Ollama.
*   **Limites de Taxa:** Implemente um mecanismo para lidar com limites de taxa.

## Recursos Adicionais

*   **Documentação do Ollama:** [https://ollama.com/docs/api/](https://ollama.com/docs/api/)
*   **Exemplos de Código:** Consulte os exemplos de código na documentação do Ollama.

## Resumo

Para permitir que sua aplicação acesse um modelo LLM no Ollama via URL, você precisa:

1.  **Expor o modelo:** Use o comando `ollama serve --api` para expor o modelo em uma API.
2.  **Configurar a aplicação:** Use uma biblioteca HTTP em sua linguagem de programação para fazer requisições POST para a API do
Ollama.
3.  **Formatar as requisições:** Use o formato JSON para enviar requisições e interpretar respostas.
4.  **Implementar tratamento de erros e segurança:** Implementar tratamento de erros e medidas de segurança para proteger sua
aplicação e o modelo.
```
