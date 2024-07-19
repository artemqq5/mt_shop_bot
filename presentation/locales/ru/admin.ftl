# admin main menu
ADMIN-ORDERS = Заказы
ADMIN-MANAGEMENT = Управление
ADMIN-MESSAGING = Рассылка
ADMIN-BAN = Заблокировать


# MANAGEMENT CATEGORY
ADMIN-CATEGORY_INFO = <b>{$category}</b>
    Товаров в категории: <b>{$count}</b>
ADMIN-ADD_ITEM = Добавить товар
ADMIN-SHOW_ITEMS = Просмотреть товары
ADMIN-HIDE = Скрыть
ADMIN-OPEN = Показать
ADMIN-DELETE = Удалить

# DELETE CATEGORY
ADMIN-DELETE_CATEGORY_APPROVE = Удалить категорию (<b>{$category}</b>)?

    Все товары категории будут удалены также❗
ADMIN-DELETE_SUCCESS = Успешно удалено
ADMIN-DELETE_FAIL = Ошибка удаления


# MANAGEMENT ITEMS
ADMIN-ITEMS_GROUP_INFO = Категория: <b>{$category}</b>

# DELETE ITEM
ADMIN-DELETE_ITEM_APPROVE = Удалить товар (<b>{$item}</b>)?

# ADD ITEM
ADMIN-CHOICE_CATEGORY = Выберите категорию
ADMIN-CREATE_NEW_CATEGORY = Создать новую

ADMIN-TITLE_ITEM = Название для товара (вложитесь в 20-30 символов, чтобы тг не обрезал текст для кнопки):
ADMIN-TITLE_ITEM_ERROR = Название для товара {$count} символов, сократите до 50 хотя бы:
ADMIN-DESC_ITEM = Описание для товара (можете написать про гео и использовать форматирование от тг, например жирный текст и т.д.):
ADMIN-COST_ITEM = Цена за единицу товара (обязательно число и можно формат через точку, например 4.5 или 8):
ADMIN-COST_ITEM_ERROR = Формат не является числом! Введите что-то типа 4.5 или 6:

ADMIN-PREVIEW_ITEM = 🎉 <b>Предложение товара</b>
    ━━━━━━━━━━━━━━━━
    🛒 <b>Название:</b> {$title}
    📁 <b>Категория:</b> {$category}
    💵 <b>Цена:</b> {$cost}

    📜 <b>Описание:</b>
    {$desc}
    ━━━━━━━━━━━━━━━━

ADMIN-PUBLISH_ITEM = Опубликовать товар
ADMIN-RESTART_PUBLISH = Начать сначала
ADMIN-SUCCESS_PUBLISHED = Товар успешно опубликован, опубликовать еще один?
ADMIN-FAIL_PUBLISHED = Ошибка публикации

# CREATE CATEGORY
ADMIN-CATEGORY_NAME = Название для категории (вложитесь в 20-30 символов, чтобы тг не обрезал текст для кнопки):
ADMIN-NAME_CATEGORY_ERROR = Название для товара {$count} символов, сократите до 50 хотя бы:
ADMIN-CATEGORY_SUCCESS_ADD = Категория <b>{$name}</b> успешно добавлена! Добавить еще?
ADMIN-CATEGORY_FAIL_ADD = Ошибка создания


# MESSAGING CATEGORY
ADMIN-CHOICE_TYPE_MESSAGE = Выберите для кого рассылка
ADMIN-MESSAGE_ALL_CLIENTS = Всем клиентам
ADMIN-MESSAGE_INDIVIDUAL = Лично по Telegram ID

ADMIN-SET_USER_ID = Введите Telegram ID пользователя:
ADMIN-SET_MESSAGE = Ваше сообщение (можно использовать формат Telegram):
ADMIN-SET_MEDIA = Отправьте Фото/Видео/Гифку по желанию:
ADMIN-MEDIA_WRONG = Неверный формат, отправьте (Фото/Видео/Гифку) в сжатом формате:
ADMIN-SET_BUTTON = Хотите добавить кнопку?
ADMIN-SET_BUTTON_TEXT = Текст для кнопки (20-30 символов желательно):
ADMIN-BUTTON_TEXT_ERROR = Сократите хотя бы до 50 символов, сейчас {$count}
ADMIN-SET_BUTTON_URL = Ссылка для кнопки:
ADMIN-BUTTON_URL_ERROR = Ссылка имеет неправильный формат, она должна начинаться с https:// и содержать сайт или настоящий контакт в Telegram и т.д.
ADMIN-SET_BUTTON_NEXT = Хотите добавить еще одну кнопку?
ADMIN-PREVIEW_MESSAGING = Если все правильно, можете отправлять!
ADMIN-SEND = Отправить
ADMIN-RESTART = Начать сначала

ADMIN-RESULT_NOTIFICATION = <b>-Результат рассылки-</b>

    Получили сообщение: {$send}\{$users}
    Заблокировали бота: {$block}
    Прочее: {$other}


# BAN SYSTEM
ADMIN-BAN_SYSTEM = Система банов

ADMIN-BAN_USER = Заблокировать пользователя
ADMIN-UNBAN_USER = Разблокировать пользователя
ADMIN-BAN_LIST = Список заблокированных

ADMIN-BAN_ONE_MORE = Заблокировать еще одного
ADMIN-UNBAN_ONE_MORE = Разблокировать еще одного

ADMIN-BAN_USER_ID = Введите Telegram ID (<b>348938590</b>) или
    никнейм пользователя (<b>@nickname</b>):
ADMIN-UNBAN_USER_ID = Введите Telegram ID (<b>348938590</b>):

ADMIN-BAN_SUCCESS = Пользователь успешно заблокирован
ADMIN-BAN_ERROR = Ошибка при блокировке
ADMIN-UNBAN_SUCCESS = Пользователь успешно разблокирован
ADMIN-UNBAN_ERROR = Ошибка при разблокировке

ADMIN-BAN_LIST_TEMPLATE = Юзернейм: @{$username}
    Telegram ID: <code>{$id}</code>
    Язык пользователя: <b>{$lang}</b>
ADMIN-NO_BANNED_USERS = Нет заблокированных пользователей


# ORDERS
ADMIN-ORDERS_HISTORY = История заказов
ADMIN-ORDERS_HISTORY_EMPTY = Нет заказов
ADMIN-USERNAME_HAVNT = Отсутствует юзернейм

ADMIN-ORDER_LIST_TEMPLATE = #{$id} {$category} ({$count} шт.) =${$price}
ADMIN-ORDER_ITEM_TEMPLATE = 🛒 <b>Заказ #{$id}</b>
    ━━━━━━━━━━━━━━━━
    📄 Номер заказа: <b>{$id}</b>
    📅 Дата: <b>{$date}</b>

    📦 Категория: <b>{$category}</b>
    🔢 Количество: <b>{$count} шт.</b>
    💵 Общая цена: <b>{$price}$</b>

    📝 <b>Описание:</b>
    {$desc}

    👤 <b>Пользователь:</b>
    🆔 Telegram ID: <code>{$user_id}</code>
    🔗 Юзернейм: {$username}
