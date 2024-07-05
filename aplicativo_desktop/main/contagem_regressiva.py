import datetime
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import sys
import os
import pygame

caminho_usuario = os.environ['USERPROFILE']
musicas = [
    "the_scientist.mp3"
]


# Substitua com os nomes reais das suas músicas
musica_index = 0
caminho_musica = os.path.join(caminho_usuario, 'Documents', 'GitHub', 'Contador_Ana', 'aplicativo_desktop', 'music', musicas[musica_index])

# Define a target date for the countdown
data_alvo = datetime.datetime(2024, 7, 6)

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
    pygame.mixer.music.load(os.path.join(caminho_usuario, 'Documents', 'GitHub', 'Contador_Ana', 'aplicativo_desktop', 'music', musicas[musica_index]))
    pygame.mixer.music.play()

def prev_song():
    global musica_index
    musica_index = (musica_index - 1) % len(musicas)
    pygame.mixer.music.load(os.path.join(caminho_usuario, 'Documents', 'GitHub', 'Contador_Ana', 'aplicativo_desktop', 'music', musicas[musica_index]))
    pygame.mixer.music.play()
    
def atualizar_nome_musica(label_musica):
    nome_musica = os.path.splitext(musicas[musica_index])[0]
    label_musica.config(text=nome_musica)
    label_musica.after(2000, lambda: atualizar_nome_musica(label_musica))

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
    
    # Cria uma label para exibir o nome da música
    label_nome_musica = tk.Label(janela, font=("Helvetica", 16), bg='#e63946', fg='white')
    label_nome_musica.pack()
    
    # Inicia a atualização do nome da música
    atualizar_nome_musica(label_nome_musica)

    janela.mainloop()

if __name__ == "__main__":
    if getattr(sys, "frozen", False):
        criar_interface()
    else:
        criar_interface()