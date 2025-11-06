from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from faststream.rabbit import RabbitBroker

from src.brokers import setup_brokers_router
from src.callbacks import setup_callbacks_router
from src.config import config
from src.handlers import setup_handlers_router
from src.middlewares.i18n import I18nMiddleware
from src.middlewares.rate_limit import RateLimitMiddleware

bot = Bot(
    token=config.TOKEN_BOT.get_secret_value(),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
broker = RabbitBroker(config.RABBITMQ_URL.get_secret_value())
dp = Dispatcher()

dp.message.middleware(RateLimitMiddleware())
dp.callback_query.middleware(I18nMiddleware())
dp.message.middleware(I18nMiddleware())

broker.include_router(setup_brokers_router())
dp.include_router(setup_handlers_router())
dp.include_router(setup_callbacks_router())