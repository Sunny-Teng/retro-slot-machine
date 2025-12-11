# 🎰 Retro Arcade Slot Machine

A fun, retro arcade-themed prompt generator that gives you random 3-word combinations to spark creative ideas!

**Powered by Python, Flask, and AI.**

> 🤖 **Note:** This project was built with the assistance of an AI coding agent to learn Python, Flask, and web development 

🎰 **Live Demo:** https://retro-slot-machine.onrender.com

## ✨ Features

- **🎮 Retro Arcade Aesthetic**: Neon colors, scanline effects, and pixel art font ("Press Start 2P").
- **⚡ Smooth Animations**: Spinning reels, glowing text, and 3D functionality.
- **🎨 Creative Prompts**: Generates a random Verb + Adjective + Noun combination from over 150+ words.
- **🔤 Alliteration Mode**: Toggle this to make all words start with the same random letter (e.g., "Dancing Dark Dragon").
- **📱 Fully Responsive**: vertical stacking layout optimized for mobile devices - fits perfectly on phone screens!
- **⌨️ Keyboard Control**: Press `SPACE` to spin the reels.

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3 (animations, variables, media queries), Vanilla JavaScript
- **Deployment**: Render (Gunicorn)
- **Version Control**: Git & GitHub

## 📂 Project Structure

```
slot-machine-app/
├── app.py              # Flask application logic & API endpoints
├── words.py            # Word lists (verbs, adjectives, nouns)
├── requirements.txt    # Production dependencies
├── Procfile            # Deployment command for Render
└── templates/
    └── index.html      # Single-page app with embedded CSS/JS
```

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sunny-Teng/retro-slot-machine.git
   cd retro-slot-machine
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   Visit `http://0.0.0.0:5001` or `http://localhost:5001`

## 🌐 Deployment

This app is deployed on **Render**.

1. Connect GitHub repository to Render.
2. Settings:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

## ❤️ Credits

- **Creator**: Sunny
- **AI Co-pilot**: Google DeepMind Antigravity
- **Font**: [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) by CodeMan38
