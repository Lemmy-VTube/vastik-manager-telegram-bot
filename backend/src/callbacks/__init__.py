from aiogram import Router

from src.callbacks import common, lang


def setup_callbacks_router() -> Router:
    router = Router()

    router.include_router(common.router)
    router.include_router(lang.router)

    return router