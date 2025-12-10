# Retro Arcade Slot Machine

A fun, retro arcade-themed prompt generator that gives you random 3-word combinations to spark creative ideas!

🎰 **Live Demo:** [Coming soon after deployment]

## Features
- 🎮 Retro arcade aesthetic with neon colors and pixel font
- ✨ Smooth spinning animations
- 🎨 Three word categories: Verbs, Adjectives, Nouns
- 🔤 Alliteration mode - all words start with the same letter
- ⌨️ Keyboard support - press SPACE to spin
- 📱 Responsive design

## How to Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   python app.py
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:5001
   ```

4. Click SPIN (or press SPACE) and get creative prompts!

## Project Structure
```
slot-machine-app/
├── app.py              # Flask backend
├── words.py            # Word lists (verbs, adjectives, nouns)
├── requirements.txt    # Python dependencies
└── templates/
    └── index.html      # Retro arcade frontend
```

## Deployment

This app is configured to deploy on platforms like Render, Railway, or PythonAnywhere.

### Deploy to Render

1. Push this code to GitHub
2. Create a new Web Service on [Render](https://render.com)
3. Connect your GitHub repository
4. Render will automatically detect the Flask app and deploy it!

## Customization

- **Add more words**: Edit `words.py`
- **Change colors/styles**: Modify the CSS in `templates/index.html`
- **Adjust animation speed**: Change the timeout values in the JavaScript

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Font**: Press Start 2P (Google Fonts)
- **Hosting**: Render (or any Python hosting platform)

---

Built with ❤️ as a learning project
