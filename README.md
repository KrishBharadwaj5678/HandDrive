# ✋ HandDrive

**HandDrive** is a Python based computer vision project that lets you control the car in **Hill Climb Racing** using hand gestures.

![HandDriveDemo](https://github.com/KrishBharadwaj5678/HandDrive/raw/main/HandDriveDemo.gif)

## 🧠 Features

| Feature                                  | Description                                                        |
| ---------------------------------------- | ------------------------------------------------------------------ |
| 🖐️ **Real time hand gesture detection** | Uses **MediaPipe** for fast and efficient hand tracking            |
| 🚗 **Intuitive gesture controls**        | 🖐️ **Open Hand** – Triggers the **Accelerate** command  <br/> ✊ **Closed Hand** – Triggers the **Brake** command |
| 🕹️ **Game automation**                   | Designed for **Hill Climb Racing**                                 |
| 🖥️ **Webcam based control**              | No additional hardware required - just a webcam                    |
| 🎯 **Accurate finger detection**         | Performs well even under varied lighting conditions                |
| 🔄 **Hands free experience**             | Play the game without touching keyboard or mouse                   |
| 📊 **Real-time visual feedback**         | Displays hand landmarks and gesture detection live                 |

---

## 🛠️ Tech Stack

| Technology                                              | Description                                    |
| ------------------------------------------------------- | ---------------------------------------------- |
| 🐍 **Python 3**                                         | Core programming language used for the project |
| 🤖 **MediaPipe**                                        | Real time hand and finger tracking             |
| 🖥️ **OpenCV**                                           | For webcam access and image/video processing   |
| 🧰 **CVZone**                                           | Simplifies working with OpenCV and MediaPipe   |
| 🎮 **pyautogui**                                        | Simulates keyboard presses to control the game |

---

## 🚀 How It Works

1. 🖐️ **Open Hand (All fingers extended)**
   → Simulates pressing the **accelerate** key to move the car **forward**.

2. ✊ **Closed Fist (All fingers folded)**
   → Simulates pressing the **brake** key to **stop** the car and move it **backward**.

---

## 📦 Installation

### 1️⃣ Clone the Repository

   ```bash
   git clone https://github.com/KrishBharadwaj5678/HandDrive.git
   ```

### 2️⃣ Navigate to the Folder

   ```bash
   cd HandDrive
   ```

### 3️⃣ Install the Dependencies

   ```bash
   pip install -r requirements.txt
   ```

### 4️⃣ Run the Project

   ```bash
   python main.py
   ```
