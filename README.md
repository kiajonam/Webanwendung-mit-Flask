Notizen-Webanwendung mit Flask

Dies ist eine einfache Webanwendung zum Erstellen und Löschen von Notizen. Sie wurde mit Flask, Jinja2, Flask-Login und SQLite erstellt.
🔧 Voraussetzungen

Bevor du die App startest, stelle sicher, dass du folgende Tools installiert hast:

    Python 3.x

    pip (Python Package Installer)

    Virtualenv (optional, aber empfohlen)

Installation

# 1. Repository klonen
git clone https://github.com/dein-benutzername/notizen-app.git
cd notizen-app

# 2. Virtuelle Umgebung erstellen (optional)
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# 3. Abhängigkeiten installieren
pip install -r requirements.txt


Anwendung starten

python main.py


Die Anwendung läuft dann standardmäßig unter:
🔗 http://127.0.0.1:5000
🔐 Funktionen

    Benutzerregistrierung und Login (via Flask-Login)

    Notizen hinzufügen

    Notizen löschen (über AJAX)

    Flash-Meldungen für Benutzerfeedback

    Projectstruktur

/website
│
├── static/
│   └── index.js             # JavaScript für das Löschen von Notizen
├── templates/
│   ├── base.html
│   ├── home.html
│   └── login.html
│
├── __init__.py              # Flask App Factory
├── models.py                # Datenbankmodelle
├── views.py                 # Routen für Notizen
└── auth.py                  # Routen für Authentifizierung

main.py                      # Einstiegspunkt

    
