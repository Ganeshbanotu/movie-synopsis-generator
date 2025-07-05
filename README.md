# 🎬 Movie Synopsis Generator

> AI-powered web application that generates multilingual movie synopses using Google Gemini or OpenRouter APIs. Built with Flask, Tailwind CSS, and SQLite, this project supports login, tone/genre customization, and download features.

---

## 📌 Table of Contents

- [✨ Features](#-features)
- [🧠 LLM Model Logic](#-llm-model-logic)
- [🖼️ UI Design Overview](#-ui-design-overview)
- [📂 Project Structure](#-project-structure)
- [🚀 Setup Instructions](#-setup-instructions)
- [🔧 Usage Guide](#-usage-guide)
- [📦 Deployment Notes](#-deployment-notes)
- [🛠 Tech Stack](#-tech-stack)
- [🤝 Contribution](#-contribution)
- [📄 License](#-license)
- [🙋‍♂️ Contact](#-contact)

---

## ✨ Features

- 🔐 **Authentication:** Register/Login using Flask-Login & bcrypt.
- 🧠 **AI Synopsis Generator:** Uses Google Gemini or OpenRouter for realistic, creative synopses.
- 🎭 **Custom Controls:** Genre, tone, length, language, and batch options.
- 🌍 **Multilingual Output:** English, Telugu, Hindi, Tamil, and more.
- 📂 **History Management:** All generated synopses saved per user.
- 📎 **Download:** Export any synopsis as `.txt`.
- 🐳 **Docker Support:** Easily containerized for deployment.

---

## 🧠 LLM Model Logic

LLM generation is handled in `llm.py` using:

- ✅ Gemini Pro API (preferred if key available)
- ✅ OpenRouter fallback
- ✅ Prompt templating based on:
  - Movie title
  - Genre
  - Style (Netflix-style, Classic plot, Logline)
  - Tone (Suspenseful, Comedic, etc.)
  - Language
  - Length

---

## 🖼️ UI Design Overview

| Page           | Design Summary |
|----------------|----------------|
| **Home**       | Hero section with form (tailored input fields: dropdowns, checkboxes). |
| **History**    | Paginated list of all synopses for the logged-in user. |
| **Auth Pages** | Minimal login/register with flash messaging support. |

Built using **Tailwind CSS** for clean, responsive design and layout.

---

## 📂 Project Structure

```

movie-synopsis-generator/
├── app/
│   ├── **init**.py
│   ├── auth.py
│   ├── routes.py
│   ├── models.py
│   ├── llm.py
│   ├── templates/
│   │   ├── layout.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── history.html
│   └── static/
├── database/
│   └── app.db
├── requirements.txt
├── .env
├── Dockerfile
├── docker-compose.yaml
└── README.md

````

---

## 🚀 Setup Instructions

### 🧪 Local Setup (Python venv)

```bash
# Clone the repo
git clone https://github.com/Ganeshbanotu/movie-synopsis-generator.git
cd movie-synopsis-generator

# Setup virtual environment
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup database
python
>>> from app import create_app, db
>>> app = create_app()
>>> with app.app_context(): db.create_all()
>>> exit()

# Start the server
flask --app app run
````

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

### 🐳 Docker Setup

```bash
docker-compose up --build
```

App will run at [http://localhost:5000](http://localhost:5000) or [http://localhost:5001](http://localhost:5001) (check your `docker-compose.yaml`)

---

## 🔧 Usage Guide

1. Register/login using your email and password.
2. Fill in the movie title, genre, style, tone, length, and language.
3. (Optional) Enable "Generate 3 versions".
4. Click "Generate" to get the AI synopsis.
5. Go to the "History" page to download or view previous synopses.

---

## 📦 Deployment Notes

* Can be hosted on:

  * Render (Flask + Docker)
  * Hugging Face Spaces
  * Streamlit Cloud (LLM frontend alternative)
* `.env` used for secure API key management.

---

## 🛠 Tech Stack

| Layer       | Tech Used                      |
| ----------- | ------------------------------ |
| Backend     | Flask, Flask-Login, SQLAlchemy |
| Frontend    | HTML5, Jinja2, Tailwind CSS    |
| Database    | SQLite3                        |
| AI/LLM      | Google Gemini API / OpenRouter |
| Deployment  | Docker, docker-compose         |
| Auth & Hash | bcrypt                         |

---

## 🤝 Contribution

Developed as an internship task by **Ganesh Banotu**.
Feel free to fork and enhance the project!

---

## 📄 License

This project is open for educational and demo purposes.

---

## 🙋‍♂️ Contact

**Ganesh Banotu**
📧 [ganeshbanothu1912@gmail.com](mailto:ganeshbanothu1912@gmail.com)
🔗 [GitHub](https://github.com/Ganeshbanotu)

---

> ⭐ If this project helped you, give it a star!
