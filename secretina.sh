#!/bin/bash

# Cores para saída no terminal
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}======================================${NC}"
echo -e "${GREEN}🎙️ Secre-Tina - Verificando dependências 🤖${NC}"
echo -e "${BLUE}======================================${NC}"

# Verificar se ambiente virtual existe
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Ambiente virtual não encontrado. Criando...${NC}"
    python3 -m venv venv
fi

# Ativar ambiente virtual
echo -e "${YELLOW}Ativando ambiente virtual...${NC}"
source venv/bin/activate

# Garantir que todas as dependências estejam instaladas
echo -e "${YELLOW}Instalando/atualizando dependências...${NC}"
pip install --upgrade pip
pip install numpy sounddevice soundfile openai requests python-dotenv
pip install git+https://github.com/openai/whisper.git

# Verificar se .env existe
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}Criando arquivo .env padrão...${NC}"
    echo "# Configurações da Secre-Tina\n\n# Chave de API da OpenAI (opcional se usar Ollama)\nOPENAI_API_KEY=\n\n# URL do Ollama (padrão: http://localhost:11434)\nOLLAMA_URL=http://localhost:11434\n\n# Modelo a ser usado\nMODEL=gpt-3.5-turbo\n\n# Modelo Whisper para transcrição\nWHISPER_MODEL=base\n\n# Idioma da interface (pt, en, es)\nLANGUAGE=pt\n\n# Diretório de saída\nOUTPUT_DIR=output" > .env
fi

echo -e "${GREEN}Iniciando Secre-Tina...${NC}"

# Executar a aplicação
python secre_tina.py

# Desativar ambiente virtual ao sair
deactivate

echo -e "${BLUE}======================================${NC}"
echo -e "${GREEN}Até a próxima! 👋${NC}"
echo -e "${BLUE}======================================${NC}"
