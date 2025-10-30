from aiogram.utils.i18n import I18n

from src.config import LOCALES_DIR, config_telegram_bot

i18n = I18n(
    domain="messages",
    path=LOCALES_DIR,
    default_locale=config_telegram_bot.DEFAULT_LANGUAGE
)
gettext = i18n.gettext
