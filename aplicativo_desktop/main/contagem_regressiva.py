import datetime
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import sys
import os
import pygame

caminho_usuario = os.environ['USERPROFILE']
musicas = [
    "the_scientist.mp3",
    "01 - Sorriso Maroto - Eu Topo - Ao Vivo.mp3",
    "02 - Sorriso Maroto, Belo - 100 Likes - Ao Vivo.mp3",
    "03 - Sorriso Maroto, Dilsinho - 50 Vezes - Ao Vivo.mp3",
    "04 - Sorriso Maroto - Dependente - Ao Vivo.mp3",
    "05 - Sorriso Maroto - Lua de Mel_Brigas por Nada_1 Metro e 65 - Ao Vivo.mp3",
    "06 - Sorriso Maroto - Faz Assim.mp3",
    "07 - Sorriso Maroto - Clichê - Live.mp3",
    "08 - Sorriso Maroto - Reprise - Ao Vivo.mp3",
    "09 - Sorriso Maroto - A Primeira Namorada.mp3",
    "10 - Sorriso Maroto - Sinais - Live.mp3",
    "11 - Sorriso Maroto - Não Tem Perdão.mp3",
    "12 - Sorriso Maroto - Vai e Chora - Ao Vivo.mp3",
    "13 - Sorriso Maroto - Eu Vacilei_Preciso Viver_Nada de Pensar Em Despedida - Ao Vivo.mp3",
    "14 - Sorriso Maroto - Chave e Cadeado.mp3",
    "15 - Sorriso Maroto - Fica Combinado Assim.mp3",
    "16 - Sorriso Maroto - Futuro Prometido.mp3",
    "17 - Sorriso Maroto, Jorge & Mateus - Guerra Fria (feat. Jorge & Mateus).mp3",
    "18 - Sorriso Maroto - O Impossível.mp3",
    "19 - Sorriso Maroto - Instigante - Ao Vivo.mp3",
    "20 - Sorriso Maroto - Tá Bom, Aham_É Nóis Faze Parapapá_A Galera - Ao Vivo.mp3",
    "21 - Sorriso Maroto - Ainda Existe Amor Em Nós.mp3",
    "22 - Sorriso Maroto - Eu Já Te Quis um Dia.mp3",
    "23 - Sorriso Maroto - Assim Você Mata o Papai - Ao Vivo.mp3",
    "24 - Sorriso Maroto - Pot-Pourri_ Amanhã_O Que Tinha Que Dar - Ao Vivo.mp3",
    "25 - Sorriso Maroto - Ainda Gosto de Você_Me Espera_Coração Deserto.mp3",
    "26 - Sorriso Maroto - Indiferença - Ao Vivo.mp3",
    "27 - Sorriso Maroto - Pouco a Pouco - Ao Vivo.mp3",
    "28 - Sorriso Maroto - Pot-Pourri_ Em Suas Mãos_Disfarça_Fica Combinado Assim - Ao Vivo.mp3",
    "29 - Sorriso Maroto - Me Arrependi_É Natural_O Impossível - Ao Vivo.mp3",
    "30 - Sorriso Maroto - Pot-Pourri_ Tenho Medo_Não Tem Perdão - Ao Vivo.mp3",
    "31 - Sorriso Maroto - Pot-Pourri_ Pra Mim Não É_Se Eu Te Pego Te Envergo_Instigante - Ao Vivo.mp3",
    "32 - Sorriso Maroto - Já Era.mp3",
    "33 - Sorriso Maroto - Engano.mp3",
    "34 - Sorriso Maroto - Estrela Maior.mp3",
    "35 - Sorriso Maroto - É Diferente.mp3",
    "36 - Sorriso Maroto - Na Cama - Live.mp3",
    "37 - Sorriso Maroto - Loucura Do Seu Coração - Live.mp3",
    "38 - Sorriso Maroto - Boa Noite_Por Quê - Live.mp3",
    "39 - Sorriso Maroto - Se Eu Te Pego Te Envergo - Ao Vivo.mp3",
    "40 - Sorriso Maroto - Sinal Vital - Ao Vivo.mp3",
    "41 - Sorriso Maroto - Escondido dos seus Pais - Ao Vivo.mp3"
]


# Substitua com os nomes reais das suas músicas
musica_index = 0
caminho_musica = os.path.join(caminho_usuario, 'Área de Trabalho', 'Projetos', 'Contador_Maria', 'aplicativo_desktop', 'music', musicas[musica_index])

# Define a target date for the countdown
data_alvo = datetime.datetime(2023, 9, 7)

def calcular_tempo_restante():
    tempo_atual = datetime.datetime.now()
    tempo_restante = data_alvo - tempo_atual
    return tempo_restante

def atualizar_contagem_regressiva(label_detalhada):
    tempo_restante = calcular_tempo_restante()

    if tempo_restante.days < 0:
        label_detalhada.config(text="A data alvo já foi alcançada!")
    else:
        total_seconds = int(tempo_restante.total_seconds())
        dias, remainder = divmod(total_seconds, 86400)
        horas, remainder = divmod(remainder, 3600)
        minutos, segundos = divmod(remainder, 60)

        mensagem_detalhada = "Faltam {} dias, {} horas, {} minutos e {} segundos, meu Pãozinho de Mel 🍯".format(dias, horas, minutos, segundos)
        label_detalhada.config(text=mensagem_detalhada)

    label_detalhada.after(1000, lambda: atualizar_contagem_regressiva(label_detalhada))

def play_music():
    pygame.mixer.music.unpause()

def pause_music():
    pygame.mixer.music.pause()

def next_song():
    global musica_index
    musica_index = (musica_index + 1) % len(musicas)
    pygame.mixer.music.load(os.path.join(caminho_usuario, 'Área de Trabalho', 'Projetos', 'Contador_Maria', 'aplicativo_desktop', 'music', musicas[musica_index]))
    pygame.mixer.music.play()

def prev_song():
    global musica_index
    musica_index = (musica_index - 1) % len(musicas)
    pygame.mixer.music.load(os.path.join(caminho_usuario, 'Área de Trabalho', 'Projetos', 'Contador_Maria', 'aplicativo_desktop', 'music', musicas[musica_index]))
    pygame.mixer.music.play()

def criar_interface():
    pygame.init()

    janela = tk.Tk()
    janela.title("❤️ Contagem Regressiva Para Te Ver ❤️")
    janela.configure(bg='#e63946')

    fonte_detalhada = ("Helvetica Bold", 16)

    frame_detalhada = tk.Frame(janela, relief="groove", bg='#e63946')
    frame_detalhada.pack(pady=10)

    label_detalhada = tk.Label(frame_detalhada, font=fonte_detalhada, padx=20, pady=20, bg='#e63946', fg='white')
    label_detalhada.pack()

    atualizar_contagem_regressiva(label_detalhada)

    pygame.mixer.music.load(caminho_musica)
    pygame.mixer.music.play(-1)

    button_frame = tk.Frame(janela, bg='#e63946')
    button_frame.pack(pady=10)

    style = ThemedStyle(button_frame)
    style.configure("TButton", padding=10, font=("Helvetica", 12), borderwidth=0, relief="flat", background='#f1faee', foreground='#1d3557', bordercolor='#457b9d', focuscolor='#a8dadc')

    play_button = ttk.Button(button_frame, text="▶️ Play", command=play_music, style="TButton")
    play_button.grid(row=0, column=0, padx=10)

    pause_button = ttk.Button(button_frame, text="⏸️ Pause", command=pause_music, style="TButton")
    pause_button.grid(row=0, column=1, padx=10)

    prev_button = ttk.Button(button_frame, text="⏮️ Previous", command=prev_song, style="TButton")
    prev_button.grid(row=0, column=2, padx=10)

    next_button = ttk.Button(button_frame, text="⏭️ Next", command=next_song, style="TButton")
    next_button.grid(row=0, column=3, padx=10)

    janela.mainloop()

if __name__ == "__main__":
    if getattr(sys, "frozen", False):
        criar_interface()
    else:
        criar_interface()