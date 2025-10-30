from logging import getLogger

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat

from src.config import config, config_telegram_bot
from src.services.i18n_service import i18n_manager

logger = getLogger(__name__)

get_languages = i18n_manager.get_languages()
_ = i18n_manager.gettext


class SettingsBotManager:
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    async def setup(self) -> None:
        await self.setup_title(self.bot)
        await self.setup_list_commands(self.bot)
        await self.setup_description(self.bot)
        await self.setup_short_description(self.bot)

    async def setup_title(self, bot: Bot) -> None:
        logger.debug("Installing bot titles...")
        try:
            for lang in get_languages:
                logger.debug(f"Installing bot title for language {lang}...")
                await bot.set_my_name(name=_("bot_title", lang), language_code=lang)
                logger.debug(f"Bot title for language {lang} installed successfully")
            logger.debug("Bot titles installed successfully")
        except Exception as e:
            logger.error(f"Error when installing bot titles: {e}")

    async def setup_list_commands(self, bot: Bot) -> None:
        logger.debug("Installing bot list commands...")
        try:
            commands_default = config_telegram_bot.COMMANDS_DEFAULT
            commands_admin = config_telegram_bot.COMMANDS_ADMIN

            for lang in get_languages:
                logger.debug(f"Installing bot list commands for language {lang}...")
                await bot.set_my_commands(
                    commands=[
                        BotCommand(command=c, description=_(f"command_{c}", lang))
                        for c in commands_default
                    ],
                    language_code=lang
                )
                logger.debug(f"Bot list commands for language {lang} installed successfully")

                for admin_id in config_telegram_bot.ADMINS_ID:
                    logger.debug(
                        f"Installing bot list commands for admin {admin_id} in language {lang}..."
                    )
                    await bot.set_my_commands(
                        commands=[
                            BotCommand(
                                command=c,
                                description=_(f"command_{c}", lang)
                            )
                            for c in commands_default + commands_admin
                        ],
                        scope=BotCommandScopeChat(chat_id=admin_id),
                        language_code=lang,
                    )
                logger.debug(f"Bot list admin commands for language {lang} installed successfully")
            logger.debug("Bot list commands installed successfully")
        except Exception as e:
            logger.error(f"Error when installing bot list commands: {e}")

    async def setup_description(self, bot: Bot) -> None:
        logger.debug("Installing bot description...")
        try:
            for lang in get_languages:
                logger.debug(f"Installing bot description for language {lang}...")
                await bot.set_my_description(
                    description=_("bot_description", lang).format(
                        github_url=config.GITHUB_URL,
                        project_version=config.PROJECT_VERSION,
                        developer_username=config.DEVELOPER_USERNAME
                    ),
                    language_code=lang
                )
                logger.debug(f"Bot description for language {lang} installed successfully")
            logger.debug("Bot descriptions installed successfully")
        except Exception as e:
            logger.error(f"Error when installing bot description: {e}")

    async def setup_short_description(self, bot: Bot) -> None:
        logger.debug("Installing bot short description...")
        try:
            for lang in get_languages:
                logger.debug(f"Installing bot short description for language {lang}...")
                await bot.set_my_short_description(
                    short_description=_("bot_short_description", lang),
                    language_code=lang
                )
                logger.debug(f"Bot short description for language {lang} installed successfully")
            logger.debug("Bot short descriptions installed successfully")
        except Exception as e:
            logger.error(f"Error when installing bot short description: {e}")