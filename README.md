# AnimeChat 🎌

[![Run tests](https://github.com/fandredev/fast-api-chatbot-gemini/actions/workflows/tests.yml/badge.svg)](https://github.com/fandredev/fast-api-chatbot-gemini/actions/workflows/tests.yml)
[![Ruff Lint Check](https://github.com/fandredev/fast-api-chatbot-gemini/actions/workflows/lint.yml/badge.svg)](https://github.com/fandredev/fast-api-chatbot-gemini/actions/workflows/lint.yml)

**AnimeChat** is a chatbot specialized in anime, manga, and Japanese pop culture, built with **FastAPI** and powered by the **Google Gemini API**. The project follows the **MVC** (Model-View-Controller) architecture and focus on delivering an interactive and thematic chat experience.

---

## ✨ Features

- 💬 **Streaming Responses**: Smooth chat experience with real-time response generation.
- 🎌 **Specialized Persona**: Knowledge focused exclusively on the otaku universe.
- 🔒 **Rate Limiting**: Protection against abuse using `slowapi`.
- 🌓 **Dark Mode**: Modern and adaptive user interface.
- 🧪 **Automated Tests**: Comprehensive coverage with `pytest` and validation via GitHub Actions.

---

## 🛠️ Tech Stack

<img src="https://skillicons.dev/icons?i=python,fastapi,githubactions,vscode,git,html,css,javascript" alt="Stack" />

### Other tools:

- [Ruff](https://docs.astral.sh/ruff/) (Linter & Formatter)
- [uv](https://docs.astral.sh/uv/) (Package Manager)
- [Antigravity](https://antigravity.google/) (Editor)
- [Google Gemini SDK](https://ai.google.dev/) (LLM)
- [pre-commit](https://pre-commit.com/) (Git Hooks)

---

## 🏗️ Project Structure

```text
.
├── app/
│   ├── controllers/   # Business logic and Gemini integration
│   ├── models/        # Data definitions (Pydantic)
│   ├── routes/        # API and View endpoints
│   ├── static/        # CSS, JS, and assets
│   ├── templates/     # HTML templates (Jinja2)
│   └── utils/         # Helpers and Logger
├── tests/             # Unit and integration tests
├── logs/              # Application logs
├── main.py            # Entry point (FastAPI)
├── pyproject.toml     # Project configuration and dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have [uv](https://github.com/astral-sh/uv) installed.

### 2. Environment Setup

Create a `.env` file in the project root based on `.env.example`:

```bash
cp .env.example .env
```

Fill in the variables:

- `GEMINI_API_KEY`: Your key from Google AI Studio.
- `GEMINI_MODEL_NAME`: Model to be used (e.g., `gemini-2.0-flash-exp`).
- `APP_PORT`: Server port (default: `8000`).

### 3. Run the Application

`uv` will handle dependencies automatically:

```bash
uv run --env-file=.env main.py
```

- **Chat**: `http://127.0.0.1:8000`
- **API Documentation**: `http://127.0.0.1:8000/docs`

---

## 🛠️ Development and Quality

The project uses strict tooling to maintain clean and functional code.

### Pre-commit Hooks

To install Git hooks (recommended):

```bash
uv run pre-commit install
```

They will run automatically on every `git commit`. To run manually on all files:

```bash
uv run pre-commit run --all-files
```

### Linting (Ruff)

```bash
uv run ruff check .
```

### Tests (Pytest)

```bash
uv run pytest
```

---

## 📄 License

This project is for educational and demonstration purposes. Feel free to explore!
