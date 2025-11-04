from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.config import config_telegram_bot
from src.utils.i18n_aiogram import gettext as _
from src.utils.keyboards.inline import admin_menu_keyboard

router = Router()


@router.message(Command("admin"))
async def cmd_schedule(message: Message, state: FSMContext) -> None | bool:
    if message.from_user.id in config_telegram_bot.ADMINS_ID: # type: ignore
        await state.clear()
        await message.reply(_("message_admin"), reply_markup=admin_menu_keyboard())
