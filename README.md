<div align="center">
# 🌸 Telegram Bot Template

_A modern, modular, and elegant boilerplate for building Telegram bots with aiogram._

![anime-banner](https://static.zenmarket.jp/images/blog/12ygrg1y.gif)

[![Stars](https://img.shields.io/github/stars/Kitty-Ilnazik/telegram-bot-template?color=ffb3d1&style=for-the-badge)](https://github.com/Kitty-Ilnazik/telegram-bot-template/stargazers)
[![Forks](https://img.shields.io/github/forks/Kitty-Ilnazik/telegram-bot-template?color=ffc8a2&style=for-the-badge)](https://github.com/Kitty-Ilnazik/telegram-bot-template/network/members)
[![Issues](https://img.shields.io/github/issues/Kitty-Ilnazik/telegram-bot-template?color=a5d8ff&style=for-the-badge)](https://github.com/Kitty-Ilnazik/telegram-bot-template/issues)
[![License](https://img.shields.io/github/license/Kitty-Ilnazik/telegram-bot-template?color=caffbf&style=for-the-badge)](LICENSE)

</div>

---

## 🐾 Overview

Telegram Bot Template is a flexible boilerplate for creating Telegram bots in Python using aiogram. It features a modular architecture, support for SQLite and MySQL databases, Redis for caching, an internationalization (i18n) system, and anti-spam protection. The project is easily configurable via environment variables, providing a convenient foundation for rapid development and deployment.

---

## 🌍 Translations

| 🌐 Language | 🏷 Code | 🔗 Link                                     |
| :---------- | :----- | :------------------------------------------ |
| Russian     | `ru`   | [README.ru.md](readme_locales/README.ru.md) |
| Ukrainian   | `uk`   | [README.uk.md](readme_locales/README.uk.md) |
| Tatar       | `tt`   | [README.tt.md](readme_locales/README.tt.md) |
| Uzbek       | `uz`   | [README.uz.md](readme_locales/README.uz.md) |
| Kazakh      | `kk`   | [README.kk.md](readme_locales/README.kk.md) |
| English     | `en`   | [README.md](README.md)                      |

---

## 🛠️ Tools and Libraries

- ⚙️ **aiogram** — an asynchronous library for developing Telegram bots in Python.
- 🧩 **pydantic-settings** — settings management using Pydantic.
- 💾 **sqlalchemy + aiosqlite** — async ORM and DB driver.
- 🔁 **redis** — a client for Redis, used for caching.
- 🌐 **babel** — a tool for internationalization and localization.
- 🧱 **alembic** — a database migration tool.
- ✨ **ruff** — an extremely fast Python linter and formatter.
- 🚀 **uv** — an extremely fast package manager and bundler for Python.

---

## 📁 Project Structure

```
// Directory tree (3 levels, limited to 200 entries)
├── .gitignore
├── .python-version
├── Dockerfile
├── LICENSE
├── README.md
├── babel.cfg
├── example.alembic.ini
├── images\
│   ├── heart.webp
│   └── hello.jpg
├── locales\
│   ├── en\
│   │   └── LC_MESSAGES\
│   ├── messages.pot
│   └── ru\
│       └── LC_MESSAGES\
├── pyproject.toml
├── ruff.toml
├── src\
│   ├── .env.example
│   ├── alembic\
│   │   ├── README
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions\
│   ├── callbacks\
│   │   ├── __init__.py
│   │   ├── common.py
│   │   └── lang.py
│   ├── config.py
│   ├── database\
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── models\
│   │   └── repositories\
│   ├── handlers\
│   │   ├── __init__.py
│   │   └── commands\
│   ├── init_bot.py
│   ├── middlewares\
│   │   ├── i18n.py
│   │   └── rate_limit.py
│   ├── run.py
│   ├── schemas\
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services\
│   │   ├── i18n_service.py
│   │   ├── messenger_service.py
│   │   ├── redis_service.py
│   │   └── user_service.py
│   └── utils\
│       ├── babel_locale.py
│       ├── command_runner.py
│       ├── i18n_aiogram.py
│       ├── keyboards\
│       │   ├── __init__.py
│       │   ├── builders.py
│       │   ├── inline.py
│       │   └── reply.py
│       ├── logger.py
│       ├── migration_database.py
│       └── settings_bot.py
└── uv.lock
```

---

## 📄 Description of Important Files

| 📂 File / Folder   | 🧠 Description                                                                |
| :----------------- | :---------------------------------------------------------------------------- |
| `pyproject.toml`   | Project definition and its dependencies.                                      |
| `src/.env.example` | Example environment variables file.                                           |
| `src/run.py`       | Entry point of the application, starts the bot.                               |
| `src/config.py`    | Project configuration, loads environment variables.                           |
| `src/init_bot.py`  | Initializes the aiogram bot and dispatcher, registers middleware and routers. |
| `src/database/`    | DB models, repositories, initialization                                       |
| `src/handlers/`    | Telegram command/message handlers                                             |
| `src/middlewares/` | Internationalization & rate limiting                                          |
| `src/services/`    | Logic services (Redis, i18n, etc.)                                            |
| `src/alembic/`     | Database migrations                                                           |
| `src/utils/`       | Keyboards, logging, migrations                                                |
| `locales/`         | Localization files for different languages.                                   |

---

## 🚀 Setup and Running

### Installing Redis

Redis is used for caching and rate limiting.

**For Windows:**

1.  Download the `.msi` installer from the Microsoft's repository: [https://github.com/microsoftarchive/redis/releases](https://github.com/microsoftarchive/redis/releases)
2.  Run the `.msi` file and follow the installer instructions.

**For Linux:**

- **Arch Linux:**
  ```bash
  sudo pacman -S redis
  sudo systemctl start redis
  sudo systemctl enable redis
  ```
- **Debian/Ubuntu:**
  ```bash
  sudo apt update
  sudo apt install redis-server
  sudo systemctl enable redis-server
  sudo systemctl start redis-server
  ```
- **Fedora:**
  ```bash
  sudo dnf install redis
  sudo systemctl start redis
  sudo systemctl enable redis
  ```

**For macOS:**

```bash
brew install redis
brew services start redis
```

### Running without Docker

#### Using `uv` (recommended)

1.  **Install `uv`:**

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

    Or for Windows:

    ```powershell
    irm https://astral.sh/uv/install.ps1 | iex
    ```

2.  **Clone the repository and navigate to the folder:**

    ```bash
    git clone https://github.com/Kitty-Ilnazik/telegram-bot-template.git
    cd telegram-bot-template
    ```

3.  **Configure environment variables:**
    Copy the example `.env` file and fill it with your data:

    ```bash
    cp src/.env.example src/.env
    ```

    Open `src/.env` and enter values for `TOKEN_BOT`, `REDIS_URL`, and `DB_URL`.

4.  **Install dependencies and run:**
    ```bash
    uv run start
    ```

#### Without `uv`

1.  **Clone the repository and navigate to the folder:**

    ```bash
    git clone https://github.com/Kitty-Ilnazik/telegram-bot-template.git
    cd telegram-bot-template
    ```

2.  **Configure environment variables:**
    Copy the example `.env` file and fill it with your data:

    ```bash
    cp src/.env.example src/.env
    ```

    Open `src/.env` and enter values for `TOKEN_BOT`, `REDIS_URL`, and `DB_URL`.

3.  **Create and activate a virtual environment:**

    - **Windows:**
      ```bash
      python -m venv .venv
      .venv/Scripts/activate
      ```
    - **macOS/Linux:**
      ```bash
      python3 -m venv .venv
      . .venv/bin/activate
      ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the bot:**
    ```bash
    python src/run.py
    ```

### Running with Docker

1.  **Install Docker:**

    - **Arch Linux:**
      ```bash
      sudo pacman -S docker
      sudo systemctl start docker
      sudo systemctl enable docker
      sudo usermod -aG docker $USER # Add user to docker group
      newgrp docker # Apply group changes
      ```
    - **Debian/Ubuntu:**
      ```bash
      sudo apt update
      sudo apt install docker.io
      sudo systemctl start docker
      sudo systemctl enable docker
      sudo usermod -aG docker $USER
      newgrp docker
      ```
    - **Fedora:**
      ```bash
      sudo dnf install docker
      sudo systemctl start docker
      sudo systemctl enable docker
      sudo usermod -aG docker $USER
      newgrp docker
      ```
    - **Windows/macOS:** Install Docker Desktop from the official Docker website.

2.  **Build and run the Docker image:**

    ```bash
    docker build -t telegram-bot-template .
    ```

    - `docker build`: Command to build a Docker image.
    - `-t telegram-bot-template`: Assigns the tag (name) `telegram-bot-template` to the created image.
    - `.`: Indicates that the Dockerfile is in the current directory.

    ```bash
    docker run -d --name my-telegram-bot --env-file src/.env telegram-bot-template
    ```

    - `docker run`: Command to run a Docker container.
    - `-d`: Runs the container in detached mode.
    - `--name my-telegram-bot`: Assigns the name `my-telegram-bot` to the running container.
    - `--env-file src/.env`: Instructs Docker to use environment variables from `src/.env` inside the container.
    - `telegram-bot-template`: The name of the Docker image to run.

## 🗄 Using DB Migrations (Alembic)

1.  **Alembic Configuration:**
    Copy the example Alembic configuration file:

    ```bash
    cp example.alembic.ini alembic.ini
    ```

    Open `alembic.ini` and change the path to the `.env` file in the `[alembic]` section to `src/.env`.

2.  **Create and apply a migration:**

    ```bash
    uv run migrate commit "Initial migration"
    ```

## 🌐 Using PyBabel for Localization

1.  **Extract strings for translation:**

    ```bash
    uv run babel extract
    ```

2.  **Initialize a new language (e.g., Ukrainian):**

    ```bash
    uv run babel init -l uk
    ```

3.  **Update existing translations:**

    ```bash
    uv run babel update
    ```

4.  **Compile translations:**

    ```bash
    uv run babel compile
    ```

5.  **Update and compile translations:**
    ```bash
    uv run babel update-compile
    ```

## 🧹 Using Ruff

Ruff is used for code formatting and error checking.

```bash
uv run ruff check .
uv run ruff format .
```
