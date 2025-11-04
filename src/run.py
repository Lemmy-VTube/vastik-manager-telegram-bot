import asyncio
from logging import getLogger

from src.init_bot import bot, dp
from src.utils.logger import setup_logging
from src.utils.settings_bot import SettingsBotManager

logger = getLogger(__name__)


async def main() -> None:
    setup_logging()
    await SettingsBotManager(bot).setup()

    try:
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        logger.info("Бот остановлен")
    finally:
        await bot.session.close()


def start() -> None:
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен")
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")


if __name__ == "__main__":
    start()
