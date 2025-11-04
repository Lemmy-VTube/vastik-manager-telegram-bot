from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto, Message

from src.config import IMAGES_DIR
from src.states.tepropose_ideast import TeproposeIdeast
from src.utils.i18n_aiogram import gettext as _
from src.utils.keyboards.inline import back_to_old_version_keyboard

router = Router()


@router.message(Command("tepropose_ideast"))
@router.callback_query(F.data == "tepropose_ideast")
async def cmd_tepropose_ideast(message: Message | CallbackQuery, state: FSMContext) -> None | bool:
    msg = _("message_propose_ideast")
    photo = FSInputFile(IMAGES_DIR / "suggestions.jpg")

    await state.set_state(TeproposeIdeast.suggestions)
    if isinstance(message, CallbackQuery):
        await message.message.edit_media( # type: ignore
            media=InputMediaPhoto(media=photo, caption=msg),
            reply_markup=back_to_old_version_keyboard()
        )
        return await message.answer()
    await message.reply_photo(photo, caption=msg, reply_markup=back_to_old_version_keyboard())