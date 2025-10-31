from datetime import datetime
from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).parent.parent
ENV_FILE = ROOT_DIR / "src" / ".env"
BABEL_CONFIG_FILE = ROOT_DIR / "babel.cfg"

LOCALES_DIR = ROOT_DIR / "locales"
IMAGES_DIR = ROOT_DIR / "images"
LOGS_DIR = ROOT_DIR / "logs"

now = datetime.now().replace(microsecond=0)
log_filename_time = now.strftime("%Y-%m-%d_%H-%M-%S")


if not ENV_FILE.exists():
    raise FileNotFoundError(f".env file not found at: {ENV_FILE}")

if not LOCALES_DIR.exists():
    LOCALES_DIR.mkdir(parents=True, exist_ok=True)

if not IMAGES_DIR.exists():
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

if not LOGS_DIR.exists():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)


class Config(BaseSettings):
    TOKEN_BOT: SecretStr

    REDIS_URL: SecretStr
    DB_URL: SecretStr

    PROJECT_VERSION: str = "v1.0.0-latest"
    DEVELOPER_USERNAME: str = "Kitty_Ilnazik"
    GITHUB_URL: str = "https://github.com/Kitty-Ilnazik/telegram-bot-template"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8"
    )


class ConfigTelegramBot(BaseSettings):
    ADMINS_ID: list[int] = Field(default_factory=lambda: [8042671345])

    COMMANDS_DEFAULT: list[str] = Field(default_factory=lambda: ["start", "language"])
    COMMANDS_ADMIN: list[str] = Field(default_factory=lambda: ["admin"])

    DEFAULT_LANGUAGE: str = "en"

    RATELIMIT_MAX_REQUESTS: int = 5
    RATELIMIT_WINDOW_SECONDS: int = 10
    RATELIMIT_BAN_SECONDS: int = 60


class ConfigLog(BaseSettings):
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - [%(levelname)s] - %(name)s: %(message)s"
    LOG_DATE_FORMAT: str = "%d.%m.%Y %H:%M:%S"
    LOG_FILE: Path = LOGS_DIR / f"app_{log_filename_time}.log"


config_telegram_bot = ConfigTelegramBot()
config_log = ConfigLog()
config = Config()