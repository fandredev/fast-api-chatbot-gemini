# AnimeChat 🎌

An anime-specialized chatbot built with **FastAPI** following the **MVC** (Model-View-Controller) architecture. This project was designed to provide a chat experience focused exclusively on the otaku universe, filtering out unrelated topics.

## 🛠️ Stack Used

<img src="https://skillicons.dev/icons?i=python,fastapi,githubactions,vscode,git,html,css,javascript" alt="python,fastapi,githubactions,vscode,git,html,css,javascript" />

### Other tools:

- [Ruff](https://docs.astral.sh/ruff/)
- [uv](https://docs.astral.sh/uv/)
- [Antigravity](https://antigravity.google/)
- [Google Gemini](https://gemini.google/)

## 🏗️ Project Structure

```text
.
├── app/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── static/
│   ├── templates/
│   └── utils/
├── logs/
│   ├── chatbot.log
├── .gitignore
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## 🚀 How to Run

### 1. Prerequisites

Ensure you have [uv](https://github.com/astral-sh/uv) installed on your machine.

### 2. Set Up and Run

Clone the repository and run the application using `uv`:

```bash
uv run --env-file=.env main.py
```

Access the chat at: `http://127.0.0.1:8000`
Access the API docs at: `http://127.0.0.1:8000/docs`

## 🛠️ Code Quality

The project uses **Ruff** to ensure code quality and consistency. To run the lint check:

```bash
uv run ruff check .
```
