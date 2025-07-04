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
| **Modo Reunião** | Gera resumos de reuniões com participantes, pauta, pontos principais e ações |
| **Modo Diário** | Organiza seus pensamentos em atividades, desafios, conquistas e planejamento |
| **Gravação Fácil** | Gravação com um clique usando seu microfone padrão |
| **Transcrição Local** | Utiliza Whisper para transcrever seu áudio localmente, sem enviar para a nuvem |
| **IA Flexível** | Escolha entre OpenAI ou modelos Ollama locais para geração de resumos |
| **Processamento Rápido** | Otimizado para processamento eficiente, mesmo em hardware modesto |
| **Personalizável** | Configure facilmente para suas necessidades específicas |

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

1. **Escolha o modo**: Reunião ou Diário
2. **Grave seu áudio**: Pressione Enter quando terminar
3. **Aguarde o processamento**: Transcrição e sumarização automáticas
4. **Aproveite o resultado**: Resumo formatado salvo em Markdown

## 🚀 Exemplos de Uso

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
