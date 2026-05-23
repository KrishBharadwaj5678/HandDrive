[English](README.md) | **Português** | [日本語](README.ja.md) | [Русский](README.ru.md)

# ✋ HandDrive

**HandDrive** é um projeto de visão computacional em Python que permite controlar o carro no jogo **Hill Climb Racing** usando gestos das mãos.

![HandDriveDemo](https://github.com/KrishBharadwaj5678/HandDrive/raw/main/HandDriveDemo.gif)

## 🧠 Funcionalidades

| Funcionalidade                                 | Descrição                                                       |
| ---------------------------------------------- | --------------------------------------------------------------- |
| 🖐️ **Detecção de gestos em tempo real**       | Usa **MediaPipe** para rastreamento rápido e eficiente das mãos |
| 🚗 **Controles intuitivos por gestos**         | 🖐️ **Mão aberta** – acelera <br/> ✊ **Mão fechada** – freia    |
| 🕹️ **Automação de jogos**                     | Desenvolvido para o **Hill Climb Racing**                       |
| 🖥️ **Controle via webcam**                    | Não requer hardware adicional, apenas uma webcam                |
| 🎯 **Detecção precisa dos dedos**              | Funciona bem em diferentes condições de iluminação              |
| 🔄 **Experiência sem uso das mãos no teclado** | Jogue sem teclado ou mouse                                      |
| 📊 **Feedback visual em tempo real**           | Mostra os pontos da mão e o gesto detectado                     |

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia       | Descrição                                       |
| ---------------- | ----------------------------------------------- |
| 🐍 **Pitão 3**  | Linguagem principal do projeto                  |
| 🤖 **MediaPipe** | Rastreamento de mãos e dedos em tempo real      |
| 🖥️ **OpenCV**   | Acesso à webcam e processamento de imagem/vídeo |
| 🧰 **Zona CV**    | Facilita o uso de OpenCV e MediaPipe            |
| 🎮 **pyautogui** | Simula teclas para controlar o jogo             |

---

## 🚀 Como Funciona

1. 🖐️ **Mão aberta (todos os dedos estendidos)**
   → Simula a tecla de **aceleração**, fazendo o carro andar **para frente**

2. ✊ **Punho fechado (todos os dedos dobrados)**
   → Simula a tecla de **freio**, parando o carro ou fazendo ele ir **para trás**

---

## 📦 Instalação

### 1️⃣ Clonar o repositório

```bash id="7k2hpl"
git clone https://github.com/KrishBharadwaj5678/HandDrive.git
```

### 2️⃣ Entrar na pasta

```bash id="a9wq3m"
cd HandDrive
```

### 3️⃣ Instalar dependências

```bash id="m2xv7q"
pip install -r requirements.txt
```

### 4️⃣ Executar o projeto

```bash id="p8r0sd"
python main.py
```
