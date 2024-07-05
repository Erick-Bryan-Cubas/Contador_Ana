# Contador Regressivo ❤️

Este é um programa de contador regressivo que foi criado com amor para expressar os sentimentos em direção a uma parceira. Ele exibirá quanto tempo resta até uma data especial para vocês dois. O programa utiliza a biblioteca tkinter para criar uma interface gráfica amigável e envolvente.

## Funcionalidades

**Contagem Regressiva Personalizada**: O programa é ajustado para calcular o tempo restante até uma data específica que você deseja celebrar com sua parceira.

**Exibição Detalhada**: O programa exibirá uma contagem regressiva detalhada, informando quantos dias, horas, minutos e segundos restam até a data alvo. A cada segundo, a contagem é atualizada para manter você constantemente informado.

**Mensagem de Carinho**: Uma mensagem carinhosa é exibida junto com a contagem regressiva, criando um clima romântico enquanto a data especial se aproxima.

**Trilha Sonora**: Uma trilha sonora adicionada em "music", com player de músicas.

## Torne o programa em executável

Para tornar o programa em um executável, você pode usar o PyInstaller. Primeiro, instale o PyInstaller usando o seguinte comando:

```bash
pyinstaller --onefile --add-data "src/app/music/*:src/app/music" src/app/contagem_regressiva.py
```
