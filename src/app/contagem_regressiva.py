import datetime
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import sys
import os
import pygame

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

musicas = [
    "Coldplay - The Scientist.mp3",
    "Creep (Live) - Kelly Clarkson.mp3",
    "Dandis - Guria - DandisOficial.mp3",
    "Ingrid Michaelson - Light Me Up.mp3",
    "James Arthur - Certain Things.mp3",
    "We Were Raised Under Grey Skies - JP Cooper.mp3"
]

musica_index = 0
caminho_musica = resource_path(os.path.join('music', musicas[musica_index]))

data_alvo = datetime.datetime(2024, 7, 6)

def calcular_tempo_restante():
    tempo_atual = datetime.datetime.now()
    tempo_restante = data_alvo - tempo_atual
    return tempo_restante

def atualizar_contagem_regressiva(label_detalhada):
    tempo_restante = calcular_tempo_restante()

    if tempo_restante.days < 0:
        label_detalhada.config(text="Finalmente chegou o dia! Te amo, Ana 💙")
    else:
        total_seconds = int(tempo_restante.total_seconds())
        dias, remainder = divmod(total_seconds, 86400)
        horas, remainder = divmod(remainder, 3600)
        minutos, segundos = divmod(remainder, 60)

        mensagem_detalhada = "Faltam {} dias, {} horas, {} minutos e {} segundos, minha querida Ana 💙".format(dias, horas, minutos, segundos)
        label_detalhada.config(text=mensagem_detalhada)

    label_detalhada.after(1000, lambda: atualizar_contagem_regressiva(label_detalhada))

def play_music():
    pygame.mixer.music.unpause()

def pause_music():
    pygame.mixer.music.pause()

def next_song():
    global musica_index
    musica_index = (musica_index + 1) % len(musicas)
    pygame.mixer.music.load(resource_path(os.path.join('music', musicas[musica_index])))
    pygame.mixer.music.play()

def prev_song():
    global musica_index
    musica_index = (musica_index - 1) % len(musicas)
    pygame.mixer.music.load(resource_path(os.path.join('music', musicas[musica_index])))
    pygame.mixer.music.play()

def atualizar_nome_musica(label_musica):
    nome_musica = os.path.splitext(musicas[musica_index])[0]
    label_musica.config(text=nome_musica)
    label_musica.after(2000, lambda: atualizar_nome_musica(label_musica))

def criar_interface():
    pygame.init()

    janela = tk.Tk()
    janela.title("❤️ Contagem Regressiva Para Te Ver ❤️")
    janela.configure(bg='#3a86ff')

    fonte_detalhada = ("Helvetica Bold", 16)

    frame_detalhada = tk.Frame(janela, relief="groove", bg='#3a86ff')
    frame_detalhada.pack(pady=10)

    label_detalhada = tk.Label(frame_detalhada, font=fonte_detalhada, padx=20, pady=20, bg='#3a86ff', fg='white')
    label_detalhada.pack()

    atualizar_contagem_regressiva(label_detalhada)

    pygame.mixer.music.load(caminho_musica)
    pygame.mixer.music.play(-1)

    button_frame = tk.Frame(janela, bg='#3a86ff')
    button_frame.pack(pady=10)

    style = ThemedStyle(button_frame)
    style.configure("TButton", padding=10, font=("Helvetica", 12), borderwidth=0, relief="flat", background='#3a86ff', foreground='#3a86ff', bordercolor='#3a86ff', focuscolor='#3a86ff')

    play_button = ttk.Button(button_frame, text="▶️ Play", command=play_music, style="TButton")
    play_button.grid(row=0, column=0, padx=10)

    pause_button = ttk.Button(button_frame, text="⏸️ Pause", command=pause_music, style="TButton")
    pause_button.grid(row=0, column=1, padx=10)

    prev_button = ttk.Button(button_frame, text="⏮️ Previous", command=prev_song, style="TButton")
    prev_button.grid(row=0, column=2, padx=10)

    next_button = ttk.Button(button_frame, text="⏭️ Next", command=next_song, style="TButton")
    next_button.grid(row=0, column=3, padx=10)
    
    label_nome_musica = tk.Label(janela, font=("Helvetica", 16), bg='#3a86ff', fg='white')
    label_nome_musica.pack()
    
    atualizar_nome_musica(label_nome_musica)

    janela.mainloop()

if __name__ == "__main__":
    if getattr(sys, "frozen", False):
        criar_interface()
    else:
        criar_interface()
