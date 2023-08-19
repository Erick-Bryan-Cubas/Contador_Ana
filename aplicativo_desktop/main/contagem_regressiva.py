import datetime
import tkinter as tk
import sys
import os
import pygame

caminho_usuario = os.environ['USERPROFILE']
musica = 'floating-cat.mp3'
pooh = 'pooh.gif'
caminho_musica = os.path.join(caminho_usuario, 'Área de Trabalho', 'Projetos', 'Contador_Maria', 'aplicativo_desktop', 'music', musica)
caminho_gif = os.path.join(caminho_usuario, 'Área de Trabalho', 'Projetos', 'Contador_Maria', 'aplicativo_desktop', 'images', pooh)

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

def criar_interface():
    pygame.init()

    janela = tk.Tk()
    janela.title("❤️Contagem Regressiva Para Te Ver❤️")
    
    # Carregar e exibir o GIF
    imagem_pooh = tk.PhotoImage(file=caminho_gif)
    gif_label = tk.Label(janela, image=imagem_pooh, bg='#ffc300')
    gif_label.pack()
    
    # Definir o tamanho da janela para o tamanho do GIF
    janela.geometry("{}x{}".format(imagem_pooh.width(), imagem_pooh.height()))

    # Alterando a cor de fundo
    janela.configure(bg='#ffc300')
    
    fonte_detalhada = ("Helvetica Bold", 16)

    frame_detalhada = tk.Frame(janela, relief="groove")
    frame_detalhada.pack(pady=1)

    label_detalhada = tk.Label(frame_detalhada, font=fonte_detalhada, padx=20, pady=20, bg='#ffc300', fg='white')
    label_detalhada.pack()

    atualizar_contagem_regressiva(label_detalhada)
    
    pygame.mixer.music.load(caminho_musica)
    pygame.mixer.music.play(-1)

    janela.mainloop()

if __name__ == "__main__":
    if getattr(sys, "frozen", False):
        criar_interface()
    else:
        criar_interface()
