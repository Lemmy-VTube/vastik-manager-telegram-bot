from gettext import translation
from logging import getLogger

from src.config import LOCALES_DIR

logger = getLogger(__name__)


class I18nManager:
    def __init__(self) -> None:
        self.translations = {
            lang: translation(
                domain="messages",
                localedir=LOCALES_DIR,
                languages=[lang],
                fallback=True
            )
            for lang in self.get_languages()
        }

    def get_languages(self) -> list[str]:
        i18n_path = LOCALES_DIR
        languages = [f.stem for f in i18n_path.iterdir() if f.is_dir()]
        logger.debug(f"Found languages: {languages}")
        return languages

    def get_translator(self, lang: str = "ru"):
        logger.debug(f"Get translator for lang: {lang}")
        return self.translations.get(lang, self.translations["ru"])

    def gettext(self, message: str, lang: str = "ru") -> str:
        return self.get_translator(lang).gettext(message)


i18n_manager = I18nManager()