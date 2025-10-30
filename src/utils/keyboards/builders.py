from typing import Any, List, Optional, Union

from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


class KeyboardBuilder:
    def _ensure_list(self, value: Any) -> List[Any]:
        if not isinstance(value, list):
            return [value]
        return value
    
    def inline(
        self,
        text: Union[str, List[str]],
        callback_data: Optional[Union[str, List[str]]] = None,
        sizes: Union[int, List[int]] = 2,
        url: Optional[Union[str, List[str]]] = None,
        web_app: Optional[Union[str, List[str]]] = None,
        **kwargs
    ) -> InlineKeyboardMarkup:
        """Creates an Inline keyboard for Telegram bot.

        Args:
            text (Union[str, List[str]]): Button text. Can be a string for a single button
                or a list of strings for multiple buttons.
            callback_data (Union[str, List[str]], optional): Callback data for buttons.
                Must match the number of text elements. Defaults to None.
            sizes (Union[int, List[int]], optional): Number of buttons per row. Can be a number
                for uniform row sizes or a list of numbers for different sizes.
                Defaults to 2.
            url (Union[str, List[str]], optional): URL links for buttons. Defaults to None.
            web_app (Union[str, List[str]], optional): Mini App links for buttons.
                Defaults to None.
            **kwargs: Additional parameters for InlineKeyboardMarkup constructor.

        Returns:
            InlineKeyboardMarkup: Ready-to-use inline keyboard.

        Examples:
            # Simple keyboard with callback_data
            kb = inline(["Yes", "No"], callback_data=["yes", "no"])

            # Keyboard with URL buttons
            kb = inline(
                ["Наш сайт", "Telegram"],
                url=["https://example.com", "https://t.me/channel"],
                sizes=1
            )

            # Keyboard with different number of buttons per row
            kb = inline(
                ["1", "2", "3", "4", "5"],
                callback_data=["1", "2", "3", "4", "5"],
                sizes=[2, 1, 2]
            )

        ----

        Создает встроенную Inline клавиатуру для Telegram бота.

        Args:
            text (Union[str, List[str]]): Текст кнопок. Может быть строкой для одной кнопки
                или списком строк для нескольких кнопок.
            callback_data (Union[str, List[str]], optional): Данные обратного вызова для кнопок.
                Должны соответствовать количеству текстовых элементов. По умолчанию None.
            sizes (Union[int, List[int]], optional): Количество кнопок в ряду. Может быть числом
                для одинакового размера всех рядов или списком чисел для разных размеров.
                По умолчанию 2.
            url (Union[str, List[str]], optional): URL-ссылки для кнопок. По умолчанию None.
            web_app (Union[str, List[str]], optional): Ссылки на mini-приложения для кнопок.
                По умолчанию None.
            **kwargs: Дополнительные параметры для конструктора InlineKeyboardMarkup.

        Returns:
            InlineKeyboardMarkup: Готовая встроенная клавиатура.

        Examples:
            # Простая клавиатура с callback_data
            kb = inline(["Да", "Нет"], callback_data=["yes", "no"])

            # Клавиатура с URL-кнопками
            kb = inline(
                ["Наш сайт", "Telegram"],
                url=["https://example.com", "https://t.me/channel"],
                sizes=1
            )

            # Клавиатура с разным количеством кнопок в рядах
            kb = inline(
                ["1", "2", "3", "4", "5"],
                callback_data=["1", "2", "3", "4", "5"],
                sizes=[2, 1, 2]
            )
        """
        builder = InlineKeyboardBuilder()
        
        text_list = self._ensure_list(text)
        callback_data_list = self._ensure_list(callback_data) if callback_data else None
        sizes_list = self._ensure_list(sizes)
        url_list = self._ensure_list(url) if url else None
        web_app_list = self._ensure_list(web_app) if web_app else None
        
        for i, txt in enumerate(text_list):
            if callback_data_list and i < len(callback_data_list) and callback_data_list[i]:
                builder.button(text=txt, callback_data=callback_data_list[i])
            elif url_list and i < len(url_list) and url_list[i]:
                builder.button(text=txt, url=url_list[i])
            elif web_app_list and i < len(web_app_list) and web_app_list[i]:
                builder.button(text=txt, web_app=WebAppInfo(url=web_app_list[i]))
            else:
                raise ValueError(f"No action specified for button '{txt}' at index {i}")
        builder.adjust(*sizes_list)
        return builder.as_markup(**kwargs)
    
    def reply(
        self, 
        text: Union[str, List[str]], 
        sizes: Union[int, List[int]] = 2,
        resize: bool = True, 
        one_time: bool = True,
        **kwargs
    ) -> ReplyKeyboardMarkup:
        """
        Создает Reply-клавиатуру с одной или несколькими кнопками.

        Args:
            text (str | list[str]): Текст кнопки или списка кнопок.
            resize (bool, optional): Сжимать ли клавиатуру по ширине. По умолчанию True.
            one_time (bool, optional): Скрывать клавиатуру после нажатия. По умолчанию True.

        Returns:
            ReplyKeyboardMarkup: Готовая клавиатура.
        """
        builder = ReplyKeyboardBuilder()
        
        text_list = self._ensure_list(text)
        sizes_list = self._ensure_list(sizes)
        
        for txt in text_list:
            builder.button(text=txt)
        builder.adjust(*sizes_list)
        return builder.as_markup(
            resize_keyboard=resize, 
            one_time_keyboard=one_time,
            **kwargs
        )


keyboard_builder = KeyboardBuilder()
