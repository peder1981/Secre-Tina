@echo off
:: Secre-Tina - Script de Instalação para Windows
:: Este script configura o ambiente virtual e instala as dependências necessárias

echo ======================================
echo 🎙️ Instalação da Secre-Tina 🤖
echo ======================================

:: Verificar se Python está instalado
python --version > NUL 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python não encontrado. Por favor, instale Python 3.12 ou superior.
    exit /b 1
)

:: Exibir versão do Python
python --version

:: Criar ambiente virtual
echo Criando ambiente virtual...
python -m venv venv

:: Ativar ambiente virtual
echo Ativando ambiente virtual...
call venv\Scripts\activate

:: Instalar dependências
echo Instalando dependências...
pip install --upgrade pip
pip install numpy sounddevice soundfile openai requests python-dotenv git+https://github.com/openai/whisper.git pytest

:: Criar arquivo .env exemplo se não existir
if not exist .env (
    echo Criando arquivo .env exemplo...
    echo # Configurações da Secre-Tina > .env
    echo. >> .env
    echo # Chave de API da OpenAI (opcional se usar Ollama) >> .env
    echo OPENAI_API_KEY=your_openai_api_key_here >> .env
    echo. >> .env
    echo # URL do Ollama (padrão: http://localhost:11434) >> .env
    echo OLLAMA_URL=http://localhost:11434 >> .env
    echo. >> .env
    echo # Modelo padrão (gpt-3.5-turbo, gpt-4, etc) >> .env
    echo MODEL=gpt-3.5-turbo >> .env
    echo. >> .env
    echo # Modelo Whisper para transcrição de áudio (tiny, base, small, medium, large) >> .env
    echo WHISPER_MODEL=base >> .env
    echo. >> .env
    echo # Idioma da interface e dos resumos (pt, en, es) >> .env
    echo LANGUAGE=pt >> .env
    echo. >> .env
    echo # Diretório de saída para arquivos gerados >> .env
    echo OUTPUT_DIR=./output >> .env
)

:: Criar diretório de output se não existir
if not exist output mkdir output

echo ✅ Instalação concluída com sucesso!
echo Para ativar o ambiente virtual:
echo     venv\Scripts\activate
echo Para executar a Secre-Tina:
echo     python secre_tina.py
echo ======================================

pause
