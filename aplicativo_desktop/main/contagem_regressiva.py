import datetime
import tkinter as tk
import sys
import os
import pygame

caminho_usuario = os.environ['USERPROFILE']
musica = 'floating-cat.mp3'
caminho_musica = os.path.join(caminho_usuario, 'Área de Trabalho', 'Projetos', 'Contador_Maria', 'aplicativo_desktop', 'music', musica)


# Define a target date for the countdown
data_alvo = datetime.datetime(2023, 9, 7)

def calcular_tempo_restante():
    tempo_atual = datetime.datetime.now()
    tempo_restante = data_alvo - tempo_atual
    return tempo_restante

def atualizar_contagem_regressiva(label_detalhada, label_hora):
    tempo_restante = calcular_tempo_restante()

    if tempo_restante.days < 0:
        label_detalhada.config(text="A data alvo já foi alcançada!")
        label_hora.config(text="00:00:00")
    else:
        total_seconds = int(tempo_restante.total_seconds())
        dias, remainder = divmod(total_seconds, 86400)
        horas, remainder = divmod(remainder, 3600)
        minutos, segundos = divmod(remainder, 60)

        mensagem_detalhada = "Faltam {} dias, {} horas, {} minutos e {} segundos, meu Lírio 🌸".format(dias, horas, minutos, segundos)
        label_detalhada.config(text=mensagem_detalhada)

        total_horas = total_seconds // 3600
        remainder = total_seconds % 3600
        minutos, segundos = divmod(remainder, 60)
        mensagem_hora = "{:02d}:{:02d}:{:02d}".format(total_horas, minutos, segundos)
        label_hora.config(text=mensagem_hora)

    label_detalhada.after(1000, lambda: atualizar_contagem_regressiva(label_detalhada, label_hora))
    label_hora.after(1000, lambda: atualizar_contagem_regressiva(label_detalhada, label_hora))

def criar_interface():
    pygame.init()

    janela = tk.Tk()
    janela.title("❤️Contagem Regressiva Para Te Ver❤️")
    
    # Alterando a cor de fundo
    janela.configure(bg='#e63946')
    
    fonte_hora = ("Digital-7", 18)
    fonte_detalhada = ("Helvetica Bold", 16)

    frame_detalhada = tk.Frame(janela, relief="groove")
    frame_detalhada.pack(pady=1)

    label_detalhada = tk.Label(frame_detalhada, font=fonte_detalhada, padx=20, pady=20, bg='#e63946', fg='white')
    label_detalhada.pack()

    frame_hora = tk.Frame(janela, bd=5, relief="groove", bg='black')
    frame_hora.pack(pady=10)

    label_hora = tk.Label(frame_hora, font=fonte_hora, bg='white', fg='#e63946', bd=2, relief="groove", padx=20, pady=20)
    label_hora.pack()

    atualizar_contagem_regressiva(label_detalhada, label_hora)
    
    pygame.mixer.music.load(caminho_musica)
    pygame.mixer.music.play(-1)

    janela.mainloop()

if __name__ == "__main__":
    if getattr(sys, "frozen", False):
        criar_interface()
    else:
        criar_interface()