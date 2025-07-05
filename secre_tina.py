#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Secre-Tina: Assistente Virtual para Reuniões e Diários
======================================================

Este script implementa um assistente virtual para gravação, transcrição 
e sumarização de reuniões e diários pessoais usando IA.

Autor: Secre-Tina Team
"""

import os
import sys
import time
import json
import argparse
from datetime import datetime
from pathlib import Path
import sounddevice as sd
import numpy as np
import whisper
from dotenv import load_dotenv

# Tentar importar bibliotecas para OpenAI ou Ollama
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import requests
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False

# Carregar configurações do arquivo .env
load_dotenv()

# Configurações a partir do arquivo .env
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://localhost:11434')
DEFAULT_MODEL = os.getenv('MODEL', 'gpt-3.5-turbo')
WHISPER_MODEL = os.getenv('WHISPER_MODEL', 'base')
LANGUAGE = os.getenv('LANGUAGE', 'pt')
OUTPUT_DIR = os.getenv('OUTPUT_DIR', './output')

# Configurar diretório de saída
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

# Strings de interface em diferentes idiomas
UI_STRINGS = {
    'pt': {
        'welcome': "🎙️ Bem-vindo à Secre-Tina! 🤖\n",
        'mode_select': "Escolha o modo:\n1. Reunião\n2. Diário\n> ",
        'meeting_mode': "📋 Modo Reunião selecionado",
        'diary_mode': "📔 Modo Diário selecionado",
        'recording_start': "🔴 Gravação iniciada. Pressione Enter quando terminar...",
        'recording_stop': "⏹️ Gravação finalizada!",
        'transcribing': "🔄 Transcrevendo o áudio...",
        'transcript_saved': "📝 Transcrição salva em: ",
        'summarizing': "💭 Gerando resumo com IA...",
        'complete': "✅ Processo completo! Resumo salvo em: ",
        'error': "❌ Erro: ",
        'no_ai': "Nem OpenAI nem Ollama estão disponíveis. Verifique suas configurações.",
    },
    'en': {
        'welcome': "🎙️ Welcome to Secre-Tina! 🤖\n",
        'mode_select': "Choose mode:\n1. Meeting\n2. Diary\n> ",
        'meeting_mode': "📋 Meeting Mode selected",
        'diary_mode': "📔 Diary Mode selected",
        'recording_start': "🔴 Recording started. Press Enter when finished...",
        'recording_stop': "⏹️ Recording stopped!",
        'transcribing': "🔄 Transcribing audio...",
        'transcript_saved': "📝 Transcript saved at: ",
        'summarizing': "💭 Generating AI summary...",
        'complete': "✅ Process complete! Summary saved at: ",
        'error': "❌ Error: ",
        'no_ai': "Neither OpenAI nor Ollama are available. Check your settings.",
    },
    'es': {
        'welcome': "🎙️ ¡Bienvenido a Secre-Tina! 🤖\n",
        'mode_select': "Elija el modo:\n1. Reunión\n2. Diario\n> ",
        'meeting_mode': "📋 Modo Reunión seleccionado",
        'diary_mode': "📔 Modo Diario seleccionado",
        'recording_start': "🔴 Grabación iniciada. Presione Enter cuando termine...",
        'recording_stop': "⏹️ ¡Grabación finalizada!",
        'transcribing': "🔄 Transcribiendo el audio...",
        'transcript_saved': "📝 Transcripción guardada en: ",
        'summarizing': "💭 Generando resumen con IA...",
        'complete': "✅ ¡Proceso completo! Resumen guardado en: ",
        'error': "❌ Error: ",
        'no_ai': "Ni OpenAI ni Ollama están disponibles. Verifique su configuración.",
    }
}

# Usar o idioma selecionado ou padrão para PT
if LANGUAGE not in UI_STRINGS:
    LANGUAGE = 'pt'
ui = UI_STRINGS[LANGUAGE]

def record_audio(timestamp, fs=16000):
    """
    Grava áudio do microfone até que o usuário pressione Enter.
    
    Args:
        timestamp: Timestamp para nomear o arquivo
        fs: Taxa de amostragem (padrão: 16000 Hz)
    
    Returns:
        Caminho para o arquivo de áudio temporário
    """
    print(ui['recording_start'])
    
    # Iniciar gravação
    frames = []
    
    def callback(indata, frame_count, time_info, status):
        frames.append(indata.copy())
        return (indata, sd.paContinue)
    
    stream = sd.InputStream(samplerate=fs, channels=1, callback=callback)
    stream.start()
    
    # Esperar o usuário finalizar
    input()
    
    # Parar gravação
    stream.stop()
    stream.close()
    print(ui['recording_stop'])
    
    # Salvar em arquivo temporário
    audio_data = np.concatenate(frames, axis=0)
    audio_file = os.path.join(OUTPUT_DIR, f"recording_{timestamp}.wav")
    import soundfile as sf
    sf.write(audio_file, audio_data, fs)
    
    return audio_file

def transcribe_audio(audio_file):
    """
    Transcreve o áudio usando o modelo Whisper.
    
    Args:
        audio_file: Caminho para o arquivo de áudio
    
    Returns:
        Texto transcrito
    """
    print(ui['transcribing'])
    
    # Carregar modelo Whisper
    model = whisper.load_model(WHISPER_MODEL)
    
    # Transcrever
    result = model.transcribe(audio_file, language=LANGUAGE)
    
    return result["text"]

def generate_summary(text, mode):
    """
    Gera um resumo do texto transcrito usando IA.
    
    Args:
        text: Texto transcrito
        mode: Modo (reunião ou diário)
    
    Returns:
        Resumo gerado
    """
    print(ui['summarizing'])
    
    # Determinar o tipo de prompt baseado no modo
    if mode == "meeting":
        prompt = get_meeting_prompt(text)
    else:
        prompt = get_diary_prompt(text)
    
    # Tentar usar OpenAI
    if OPENAI_AVAILABLE and OPENAI_API_KEY:
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model=DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    
    # Tentar usar Ollama como alternativa
    elif OLLAMA_AVAILABLE:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": DEFAULT_MODEL,
                "prompt": f"{prompt}\n\n{text}",
                "stream": False
            }
        )
        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            raise Exception(f"Erro ao chamar Ollama: {response.status_code}")
    
    else:
        raise Exception(ui['no_ai'])

def get_meeting_prompt(text):
    """Retorna o prompt para modo reunião no idioma correto"""
    if LANGUAGE == 'pt':
        return """
        Você é um assistente especializado em resumir reuniões. 
        Com base na transcrição fornecida, crie um resumo estruturado em formato Markdown com as seguintes seções:
        
        # Resumo de Reunião
        
        ## Participantes
        (Liste os nomes mencionados)
        
        ## Pauta
        (Identifique os principais tópicos discutidos)
        
        ## Pontos Principais
        (Resuma os pontos-chave de cada tópico)
        
        ## Decisões
        (Liste as decisões tomadas)
        
        ## Ações
        (Liste as tarefas atribuídas e prazos)
        
        ## Próximos Passos
        (Indique encaminhamentos e planejamento futuro)
        """
    elif LANGUAGE == 'en':
        return """
        You are an assistant specialized in summarizing meetings.
        Based on the provided transcript, create a structured summary in Markdown format with the following sections:
        
        # Meeting Summary
        
        ## Participants
        (List the names mentioned)
        
        ## Agenda
        (Identify the main topics discussed)
        
        ## Key Points
        (Summarize the key points of each topic)
        
        ## Decisions
        (List the decisions made)
        
        ## Actions
        (List the assigned tasks and deadlines)
        
        ## Next Steps
        (Indicate follow-ups and future planning)
        """
    else:  # 'es'
        return """
        Eres un asistente especializado en resumir reuniones.
        Basado en la transcripción proporcionada, crea un resumen estructurado en formato Markdown con las siguientes secciones:
        
        # Resumen de Reunión
        
        ## Participantes
        (Enumera los nombres mencionados)
        
        ## Agenda
        (Identifica los principales temas discutidos)
        
        ## Puntos Clave
        (Resume los puntos clave de cada tema)
        
        ## Decisiones
        (Enumera las decisiones tomadas)
        
        ## Acciones
        (Enumera las tareas asignadas y plazos)
        
        ## Próximos Pasos
        (Indica seguimientos y planificación futura)
        """

def get_diary_prompt(text):
    """Retorna o prompt para modo diário no idioma correto"""
    if LANGUAGE == 'pt':
        return """
        Você é um assistente especializado em organizar reflexões pessoais.
        Com base no áudio gravado, crie um resumo estruturado em formato Markdown com as seguintes seções:
        
        # Diário Pessoal
        
        ## Data
        (Data atual)
        
        ## Atividades
        (Liste as principais atividades mencionadas)
        
        ## Desafios
        (Identifique os problemas ou dificuldades mencionados)
        
        ## Conquistas
        (Destaque as realizações e pontos positivos)
        
        ## Reflexões
        (Capture os pensamentos e reflexões pessoais)
        
        ## Planejamento
        (Liste os planos ou intenções futuras mencionados)
        """
    elif LANGUAGE == 'en':
        return """
        You are an assistant specialized in organizing personal reflections.
        Based on the recorded audio, create a structured summary in Markdown format with the following sections:
        
        # Personal Journal
        
        ## Date
        (Current date)
        
        ## Activities
        (List the main activities mentioned)
        
        ## Challenges
        (Identify problems or difficulties mentioned)
        
        ## Achievements
        (Highlight accomplishments and positive points)
        
        ## Reflections
        (Capture thoughts and personal reflections)
        
        ## Planning
        (List future plans or intentions mentioned)
        """
    else:  # 'es'
        return """
        Eres un asistente especializado en organizar reflexiones personales.
        Basado en el audio grabado, crea un resumen estructurado en formato Markdown con las siguientes secciones:
        
        # Diario Personal
        
        ## Fecha
        (Fecha actual)
        
        ## Actividades
        (Enumera las principales actividades mencionadas)
        
        ## Desafíos
        (Identifica problemas o dificultades mencionados)
        
        ## Logros
        (Destaca los logros y puntos positivos)
        
        ## Reflexiones
        (Captura pensamientos y reflexiones personales)
        
        ## Planificación
        (Enumera planes o intenciones futuras mencionadas)
        """

def save_transcript(transcript, timestamp):
    """
    Salva a transcrição em um arquivo texto.
    
    Args:
        transcript: Texto transcrito
        timestamp: Timestamp para nomear o arquivo
    
    Returns:
        Caminho para o arquivo salvo
    """
    # Criar nome do arquivo baseado no timestamp
    filename = f"transcript_{timestamp}.txt"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # Salvar arquivo
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(transcript)
    
    print(ui['transcript_saved'] + filepath)
    return filepath

def save_summary(summary, mode, timestamp):
    """
    Salva o resumo em um arquivo markdown.
    
    Args:
        summary: Texto do resumo
        mode: Modo (reunião ou diário)
        timestamp: Timestamp para nomear o arquivo
    
    Returns:
        Caminho para o arquivo salvo
    """
    # Criar nome do arquivo baseado no timestamp
    mode_name = "meeting" if mode == "meeting" else "diary"
    filename = f"{mode_name}_{timestamp}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # Salvar arquivo
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    return filepath

def main():
    """Função principal do programa"""
    try:
        # Exibir mensagem de boas-vindas
        print(ui['welcome'])
        
        # Escolher modo (reunião ou diário)
        mode_choice = input(ui['mode_select'])
        if mode_choice == "1":
            mode = "meeting"
            print(ui['meeting_mode'])
        else:
            mode = "diary"
            print(ui['diary_mode'])
        
        # Timestamp único para todos os arquivos relacionados a esta sessão
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Gravar áudio
        audio_file = record_audio(timestamp)
        
        # Transcrever áudio
        transcript = transcribe_audio(audio_file)
        
        # Salvar transcrição
        transcript_file = save_transcript(transcript, timestamp)
        
        # Gerar resumo
        summary = generate_summary(transcript, mode)
        
        # Salvar resumo
        output_file = save_summary(summary, mode, timestamp)
        
        # Exibir mensagem de conclusão
        print(ui['complete'] + output_file)
        
    except Exception as e:
        print(f"{ui['error']}{str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
