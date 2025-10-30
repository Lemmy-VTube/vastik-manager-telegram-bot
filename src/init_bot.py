from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.callbacks import setup_callbacks_router
from src.config import config
from src.handlers import setup_handlers_router
from src.middlewares.i18n import I18nMiddleware
from src.middlewares.rate_limit import RateLimitMiddleware

bot = Bot(
    token=config.TOKEN_BOT.get_secret_value(),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()

dp.message.middleware(RateLimitMiddleware())
dp.callback_query.middleware(I18nMiddleware())
dp.message.middleware(I18nMiddleware())

dp.include_router(setup_handlers_router())
dp.include_router(setup_callbacks_router())