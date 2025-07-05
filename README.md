<div align="center">

# 🎙️ Secre-Tina 🤖

**Sua Assistente Virtual para Reuniões e Diários**

[![Python Version](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Multilingual](https://img.shields.io/badge/Idiomas-PT%20%7C%20EN%20%7C%20ES-orange.svg)](#suporte-a-múltiplos-idiomas)

</div>

<p align="center">
<i>Transforme suas reuniões e ideias em resumos estruturados com a pura magia da IA!</i>
</p>

## 🚀 Visão Geral

**Secre-Tina** é uma assistente virtual inteligente que automatiza completamente a gravação, transcrição e sumarização de suas reuniões e reflexões pessoais. Diga adeus às notas espalhadas e olá para um futuro sem estresse e mais organizado.

### 🔥 Por que Secre-Tina?

- **📝 Zero Esforço na Documentação**: Pare de tomar notas, apenas fale e deixe a Secre-Tina fazer o trabalho!
- **🌐 Suporte Trilingue**: Comunique-se em Português, Inglês ou Espanhol - você decide!
- **💾 Flexibilidade de IA**: Escolha entre OpenAI (online) ou modelos Ollama (locais) para processamento
- **📃 Resumos Estruturados**: Obtenha resumos limpos em formato Markdown com tópicos e ações destacadas
- **📡 Sem Dependências Externas**: Sem necessidade de hardware especial ou serviços de terceiros para executar

## ✨ Recursos

| Recurso | Descrição |
|---------|-------------|
| **Modo Reunião** | Gera notas de reunião estruturadas com ações, decisões e notas |
| **Modo Diário** | Organiza seus pensamentos em atividades, desafios, conquistas e planejamento |
| **Revisão de Áudio** | Permite processar novamente áudios já gravados para novas transcrições e resumos |
| **Configurações Acessíveis** | Configure OpenAI, Ollama, modelos Whisper e idioma diretamente da interface |
| **Gravação Fácil** | Gravação com um clique usando seu microfone padrão |
| **Transcrição Local** | Utiliza Whisper para transcrever seu áudio localmente, sem enviar para a nuvem |
| **Arquivos de Transcrição** | Salva automaticamente as transcrições em arquivos `.txt` para referência futura |
| **IA Flexível** | Escolha entre OpenAI ou modelos Ollama locais para geração de resumos |
| **Processamento Rápido** | Otimizado para processamento eficiente, mesmo em hardware modesto |
| **Sair da Aplicação** | Opção para sair da aplicação quando necessário |

## 💻 Requisitos

- **Python 3.12+** (testado e otimizado para versões mais recentes)
- **Microfone funcional** para gravação de áudio
- **2GB+ de RAM** para processamento de transcrição
- **Chave de API OpenAI** (opcional se estiver usando Ollama)

## 📍 Instalação Rápida

### Linux/macOS

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/secre-tina.git
cd secre-tina

# Configure o ambiente
chmod +x install.sh
./install.sh
```

### Windows

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/secre-tina.git
cd secre-tina

# Configure o ambiente (clique duas vezes no arquivo ou execute via PowerShell)
install.bat
```

### Configuração

Copie o arquivo de configuração de exemplo:
```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações preferidas:

```ini
# Configurações de API
OPENAI_API_KEY=sua_chave_api_aqui
MODEL=gpt-3.5-turbo
OLLAMA_URL=http://localhost:11434

# Configurações do Whisper
WHISPER_MODEL=base

# Configuração de Idioma (pt, en, es)
LANGUAGE=pt
```

## 💬 Como Usar

Execute o script principal:
```bash
python secre_tina.py
```

Siga o fluxo intuitivo:

1. **Escolha a ação**:
   - Nova Gravação
   - Revisar Áudio Existente
   - Configurações
   - Sair
2. **Se nova gravação**:
   - Escolha o modo (Reunião ou Diário)
   - Grave seu áudio e pressione Enter quando terminar
3. **Se revisar áudio existente**:
   - Selecione o arquivo de áudio da lista
   - Escolha o modo (Reunião ou Diário) para o resumo
4. **Se configurações**:
   - Ajuste OpenAI, Ollama, modelo Whisper ou idioma
   - As alterações são salvas automaticamente
5. **Aguarde o processamento**: Transcrição, salvamento da transcrição e sumarização automáticas
6. **Aproveite o resultado**: Transcrição salva em formato de texto e resumo formatado em Markdown

## 🚀 Exemplos de Uso

### Nova Gravação
```bash
python secre_tina.py
> 1  # Seleciona nova gravação
> 1  # Seleciona modo reunião
# [Fale durante a gravação]
# Pressione Enter para finalizar
```

### Revisão de Áudio
```bash
python secre_tina.py
> 2  # Seleciona revisar áudio existente
> 1  # Seleciona o arquivo de áudio da lista
> 1  # Seleciona modo reunião para o novo resumo
```

### Configurações
```bash
python secre_tina.py
> 3  # Seleciona configurações
> 1  # Configura API OpenAI
# Digite sua chave de API
> 0  # Voltar ao menu principal
```

### Sair da Aplicação
```bash
python secre_tina.py
> 0  # Sair da aplicação
```

### Reuniões de Equipe
Grave sua reunião e obtenha um resumo estruturado com participantes, pontos discutidos e ações a serem tomadas.

### Anotações Rápidas
Use o modo Diário para capturar rapidamente ideias e reflexões sem interromper seu fluxo de pensamento.

### Acompanhamento de Projetos
Documente o progresso falando sobre o andamento do projeto e obtenha resumos estruturados para compartilhar.

## 👩‍💻 Contribuindo

Contribuições são muito bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novos recursos
- Enviar pull requests
- Melhorar documentação

## 💬 Suporte a Múltiplos Idiomas

Secre-Tina é totalmente trilingue:

- 🇧🇷 Português (padrão)
- 🇺🇸 Inglês
- 🇪🇸 Espanhol

Altere o idioma no arquivo `.env` ou nas configurações do aplicativo.

## 🔥 Próximos Passos

- [ ] Interface gráfica de usuário (GUI)
- [ ] Reconhecimento de múltiplos falantes
- [ ] Integração com serviços de calendário
- [ ] Suporte a mais idiomas
- [ ] Exportação para diferentes formatos

## ❤️ Agradecimentos

- OpenAI pelo modelo de linguagem e Whisper
- Comunidade Ollama pelos modelos LLM locais
- Todos os contribuidores e testadores

## 📜 Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

---

<p align="center">
<i>Desenvolvido com ❤️ para aumentar a produtividade e reduzir o estresse.</i>
</p>
