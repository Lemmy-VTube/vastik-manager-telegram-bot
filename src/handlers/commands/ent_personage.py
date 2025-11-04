from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InputMediaVideo, Message

from src.utils.i18n_aiogram import gettext as _
from src.utils.keyboards.inline import back_to_old_version_keyboard

router = Router()


@router.message(Command("ent_personage"))
@router.callback_query(F.data == "ent_personage")
async def cmd_ent_personage(message: Message | CallbackQuery, state: FSMContext) -> None | bool:
    await state.clear()
    
    msg = _("message_lor")
    file_id = "BAACAgIAAxkBAANGaQoUC9HqUbIJTCjyRx-sV676QewAAnOJAAIXtFBI_3R-LelmrGo2BA"

    if isinstance(message, CallbackQuery):
        await message.message.edit_media( # type: ignore
            media=InputMediaVideo(media=file_id, caption=msg),
            reply_markup=back_to_old_version_keyboard()
        )
        return await message.answer()
    await message.reply_video(file_id, caption=msg, reply_markup=back_to_old_version_keyboard())
