import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

class CountdownApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        self.label_detalhada = Label(font_size=16, color=(1, 1, 1, 1))
        self.label_hora = Label(font_size=18, color=(1, 1, 1, 1))

        layout.add_widget(self.label_detalhada)
        layout.add_widget(self.label_hora)

        Clock.schedule_interval(self.atualizar_contagem_regressiva, 1)
        return layout
    
    def calcular_tempo_restante(self):
        tempo_atual = datetime.datetime.now()
        tempo_restante = data_alvo - tempo_atual
        return tempo_restante

    def atualizar_contagem_regressiva(self, dt):
        tempo_restante = self.calcular_tempo_restante()

        if tempo_restante.days < 0:
            self.label_detalhada.text = "A data alvo já foi alcançada!"
            self.label_hora.text = "00:00:00"
        else:
            total_seconds = int(tempo_restante.total_seconds())
            dias, remainder = divmod(total_seconds, 86400)
            horas, remainder = divmod(remainder, 3600)
            minutos, segundos = divmod(remainder, 60)

            mensagem_detalhada = "Faltam {} dias, {} horas, {} minutos e {} segundos, meu Lírio 🌸".format(dias, horas, minutos, segundos)
            self.label_detalhada.text = mensagem_detalhada

            total_horas = total_seconds // 3600
            remainder = total_seconds % 3600
            minutos, segundos = divmod(remainder, 60)
            mensagem_hora = "{:02d}:{:02d}:{:02d}".format(total_horas, minutos, segundos)
            self.label_hora.text = mensagem_hora

if __name__ == "__main__":
    data_alvo = datetime.datetime(2023, 9, 7)
    CountdownApp().run()
