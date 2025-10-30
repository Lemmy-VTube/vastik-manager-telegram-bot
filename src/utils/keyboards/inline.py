from aiogram.types import InlineKeyboardMarkup

from src.services.i18n_service import i18n_manager
from src.utils.i18n_aiogram import gettext as _
from src.utils.keyboards.builders import keyboard_builder


def change_language_keyboard() -> InlineKeyboardMarkup:
    languages = i18n_manager.get_languages()
    return keyboard_builder.inline(
        text=[
            _(f"button_language_{lang}")
            for lang in languages
        ] + [_("button_back_to_main_menu")],
        callback_data=[f"change_language_{lang}" for lang in languages] + ["main_menu"]
    )


def main_menu_keyboard() -> InlineKeyboardMarkup:
    return keyboard_builder.inline(
        text=[_("command_language")],
        callback_data=["change_language"]
    )


def back_to_main_menu_keyboard() -> InlineKeyboardMarkup:
    return keyboard_builder.inline(
        text=[_("button_back_to_main_menu")],
        callback_data=["main_menu"]
    )