from aiogram import Router

from src.handlers.commands import admin as admin_command
from src.handlers.commands import ent_personage as ent_personage_command
from src.handlers.commands import information as information_command
from src.handlers.commands import lang as lang_command
from src.handlers.commands import links as links_command
from src.handlers.commands import references as references_command
from src.handlers.commands import schedule as schedule_command
from src.handlers.commands import start as start_command
from src.handlers.commands import tepropose_ideast as te_propose_ideast_command


def setup_handlers_router() -> Router:
    router = Router()

    router.include_router(start_command.router)
    router.include_router(lang_command.router)
    router.include_router(information_command.router)
    router.include_router(ent_personage_command.router)
    router.include_router(links_command.router)
    router.include_router(references_command.router)
    router.include_router(te_propose_ideast_command.router)
    router.include_router(schedule_command.router)
    router.include_router(admin_command.router)

    return router