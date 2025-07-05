#!/bin/bash

# Secre-Tina - Script de Instalação para Linux/macOS
# Este script configura o ambiente virtual e instala as dependências necessárias

# Cores para saída no terminal
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}======================================${NC}"
echo -e "${GREEN}🎙️ Instalação da Secre-Tina 🤖${NC}"
echo -e "${BLUE}======================================${NC}"

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}Python 3 não encontrado. Por favor, instale Python 3.12 ou superior.${NC}"
    exit 1
fi

# Verificar versão do Python
python_version=$(python3 --version | cut -d " " -f2)
echo -e "${BLUE}Versão do Python detectada: ${python_version}${NC}"

# Criar ambiente virtual
echo -e "${YELLOW}Criando ambiente virtual...${NC}"
python3 -m venv venv

# Ativar ambiente virtual
echo -e "${YELLOW}Ativando ambiente virtual...${NC}"
source venv/bin/activate

# Instalar dependências
echo -e "${YELLOW}Instalando dependências...${NC}"
pip install --upgrade pip
pip install numpy sounddevice soundfile openai requests python-dotenv git+https://github.com/openai/whisper.git pytest

# Criar arquivo .env exemplo se não existir
if [ ! -f .env ]; then
    echo -e "${YELLOW}Criando arquivo .env exemplo...${NC}"
    cp .env.example .env 2>/dev/null || cat > .env << EOF
# Configurações da Secre-Tina

# Chave de API da OpenAI (opcional se usar Ollama)
OPENAI_API_KEY=your_openai_api_key_here

# URL do Ollama (padrão: http://localhost:11434)
OLLAMA_URL=http://localhost:11434

# Modelo padrão (gpt-3.5-turbo, gpt-4, etc)
MODEL=gpt-3.5-turbo

# Modelo Whisper para transcrição de áudio (tiny, base, small, medium, large)
WHISPER_MODEL=base

# Idioma da interface e dos resumos (pt, en, es)
LANGUAGE=pt

# Diretório de saída para arquivos gerados
OUTPUT_DIR=./output
EOF
fi

# Criar diretório de output se não existir
mkdir -p output

echo -e "${GREEN}✅ Instalação concluída com sucesso!${NC}"
echo -e "${BLUE}Para ativar o ambiente virtual:${NC}"
echo -e "    source venv/bin/activate"
echo -e "${BLUE}Para executar a Secre-Tina:${NC}"
echo -e "    python secre_tina.py"
echo -e "${BLUE}======================================${NC}"
