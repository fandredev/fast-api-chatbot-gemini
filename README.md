# AnimeChat 🎌

An anime-specialized chatbot built with **FastAPI** following the **MVC** (Model-View-Controller) architecture. This project was designed to provide a chat experience focused exclusively on the otaku universe, filtering out unrelated topics.

## 🛠️ Stack Used

<img src="https://skillicons.dev/icons?i=python,fastapi,vscode,git,html,css,javascript" alt="python,fastapi,vscode,git,html,css,javascript" />

### Other tools:

- [Pyrefly](https://pyrefly.org/)
- [Antigravity](https://antigravity.google/)
- [Google Gemini](https://gemini.google/)

## 🏗️ Project Structure

```text
.
├── app/
│   ├── controllers/    # Processing logic (MVC: Controller)
│   ├── routes/         # API and View routes
│   ├── static/         # CSS, JS, and Images
│   └── templates/      # HTML Templates (MVC: View)
├── venv/               # Python virtual environment
├── main.py             # Application entry point
├── requirements.txt    # Project dependencies
├── pyrefly.toml        # Linter configuration
└── README.md           # Documentation
```

## 🚀 How to Run

### 1. Prerequisites

Ensure you have Python 3.10+ installed on your machine.

### 2. Set Up the Virtual Environment

Clone the repository and create the isolated environment:

```bash
# Create the venv
python3 -m venv venv

# Activate the venv (Linux/macOS)
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

Access the chat at: `http://127.0.0.1:8000`

## 🛠️ Code Quality

The project uses **Pyrefly** to ensure type consistency and Python code quality. To run the verification:

```bash
./venv/bin/pyrefly check
```
