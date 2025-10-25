# ✋ HandDrive

Welcome to **HandDrive**, a Python based computer vision project that lets you control the car in **Hill Climb Racing** using hand gestures. 🚀

![HandDriveDemo](https://github.com/KrishBharadwaj5678/HandDrive/raw/main/HandDriveDemo.gif)

---

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

1. **Clone the repository**  
   ```bash
   git clone https://github.com/KrishBharadwaj5678/HandDrive.git
   cd HandDrive
   ```

2. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🤝 Contributing

Contributions are welcome and appreciated!

1. 🍴 **Fork the repository**  
   - Click the Fork button at the top-right of this page to create your own copy of the project.

2. 📥 **Clone your forked repository**
     
   ```bash
   git clone https://github.com/KrishBharadwaj5678/HandDrive.git
   cd HandDrive
   ```

4. 🌱 **Create a new branch**
   
   ```bash
   git checkout -b feature-name
   ```

5. ✍️ **Make your changes**  

6. ✅ **Commit your changes**
   
   ```bash
   git add .
   git commit -m "Added left-turn gesture support"
   ```

8. 📤 **Push to your forked repo**
   
   ```bash
   git push origin feature-name
   ```

10. 📩 **Create a Pull Request (PR)**  
     - Go to the repo and open a PR from your forked branch. Include a clear title and description of what you changed.
