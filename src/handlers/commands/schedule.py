from datetime import datetime, timedelta

from aiogram import F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InputMediaPhoto, Message

from src.config import config_telegram_bot
from src.services.schedule_service import schedule_service
from src.utils.i18n_aiogram import gettext as _
from src.utils.keyboards.inline import back_to_old_version_keyboard

router = Router()


@router.message(Command("schedule"))
@router.callback_query(F.data == "schedule")
async def cmd_schedule(message: Message | CallbackQuery, state: FSMContext) -> None | bool:
    await state.clear()

    schedule = await schedule_service.get_schedule()
    if not schedule or not schedule.photo_id:
        return await reply_no_schedule(message)
    try:
        await message.bot.get_file(schedule.photo_id)  # type: ignore
    except TelegramBadRequest:
        return await reply_no_schedule(message)

    updated_day = schedule.created_at.weekday()
    valid_days = config_telegram_bot.VALID_DAYS.get(updated_day, 7)
    expiry_date = schedule.created_at + timedelta(days=valid_days)
    is_old = datetime.now() > expiry_date

    if is_old:
        caption = _("message_schedule_old").format(
            schedule_created_at=schedule.created_at.strftime("%d.%m.%Y %H:%M")
        )
    else:
        caption = _("message_schedule_actual")
        if schedule.message_streamer_text:
            caption += _("message_schedule_message").format(
                message_streamer_text=schedule.message_streamer_text
            )

    photo = schedule.photo_id
    if isinstance(message, CallbackQuery):
        await message.message.edit_media(  # type: ignore
            media=InputMediaPhoto(media=photo, caption=caption),
            reply_markup=back_to_old_version_keyboard(),
        )
        return await message.answer()
    await message.reply_photo(photo, caption=caption, reply_markup=back_to_old_version_keyboard())


async def reply_no_schedule(message: Message | CallbackQuery) -> None:
        text = _("message_no_schedule")
        if isinstance(message, CallbackQuery):
            await message.message.edit_caption(  # type: ignore
                caption=text,
                reply_markup=back_to_old_version_keyboard(),
            )
            await message.answer()
        else:
            await message.reply(text, reply_markup=back_to_old_version_keyboard())