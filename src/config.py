from datetime import datetime
from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).parent.parent
ENV_FILE = ROOT_DIR / ".env"
BABEL_CONFIG_FILE = ROOT_DIR / "babel.cfg"

LOCALES_DIR = ROOT_DIR / "locales"
IMAGES_DIR = ROOT_DIR / "images"
LOGS_DIR = ROOT_DIR / "logs"

now = datetime.now().replace(microsecond=0)
log_filename_time = now.strftime("%Y-%m-%d_%H-%M-%S")


if not ENV_FILE.exists():
    raise FileNotFoundError(f".env file not found at: {ENV_FILE}")

for dir in [LOCALES_DIR, IMAGES_DIR, LOGS_DIR]:
    dir.mkdir(parents=True, exist_ok=True)


class Config(BaseSettings):
    TOKEN_BOT: SecretStr

    REDIS_URL: SecretStr
    RABBITMQ_URL: SecretStr

    WEBAPP_URL: SecretStr
    BACKEND_URL: SecretStr
    WEBAPP_URL_ADMIN: SecretStr

    PROJECT_VERSION: str = "v2.0.1-latest"

    STREAMER_USERNAME: str = "lemmychka"
    DEVELOPER_USERNAME: str = "Kitty_Ilnazik"
    GITHUB_URL: str = "https://github.com/Lemmy-VTube/vastik-manager-telegram-bot"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8"
    )


class ConfigTelegramBot(BaseSettings):
    ADMINS_ID: list[int] = Field(default_factory=lambda: [8042671345, 1283679412])

    COMMANDS_DEFAULT: list[str] = Field(
        default_factory=lambda: [
            "start", "information", "tepropose_ideast", "links",
            "references", "ent_personage", "schedule", "language",
        ]
    )
    COMMANDS_ADMIN: list[str] = Field(default_factory=lambda: ["admin"])

    VALID_DAYS: dict[int, int] = { 0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 0 }

    DEFAULT_LANGUAGE: str = "ru"

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
config = Config() # type: ignore