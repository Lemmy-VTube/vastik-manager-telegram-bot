from aiogram import Router

from src.handlers.commands import lang as lang_command
from src.handlers.commands import start as start_command


def setup_handlers_router() -> Router:
    router = Router()

    router.include_router(start_command.router)
    router.include_router(lang_command.router)

    return router