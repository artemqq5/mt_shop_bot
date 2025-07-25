# admin main menu
ADMIN-ORDERS = Замовлення
ADMIN-MANAGEMENT = Управління
ADMIN-MESSAGING = Розсилка
ADMIN-BAN = Заблокувати


# MANAGMENT CATEGORY
ADMIN-CATEGORY_INFO = <b>{$category}</b>
    Товарів у категорії: <b>{$count}</b>
ADMIN-ADD_ITEM = Додати товар
ADMIN-SHOW_ITEMS = Переглянути товари
ADMIN-HIDE = Скрити
ADMIN-OPEN = Показати
ADMIN-DELETE = Видалити

# DELETE CATEGORY
ADMIN-DELETE_CATEGORY_APPROVE = Видалити категорію (<b>{$category}</b>)?

    Всі товари категорії буде видалено також❗
ADMIN-DELETE_SUCCESS = Успішно видалено
ADMIN-DELETE_FAIL = Помилка видалення


# MANAGMENT ITEMS
ADMIN-ITEMS_GROUP_INFO = Категорія: <b>{$category}</b>

# DELETE ITEM
ADMIN-DELETE_ITEM_APPROVE = Видалити товар (<b>{$item}</b>)?

# ADD ITEM
ADMIN-CHOICE_CATEGORY = Оберіть категорію
ADMIN-CREATE_NEW_CATEGORY = Створити нову

ADMIN-TITLE_ITEM = Назва для товару (вкладіться у 20-30 симолів, щоб тг не обрізав текст для кнопки):
ADMIN-TITLE_ITEM_ERROR = Назва для товару {$count} символів, скороти до 50 хоча б:
ADMIN-DESC_ITEM = Опис для товару (Можете написати про гео та використати форматування від тг, наприклад жирний текст тощо):
ADMIN-COST_ITEM = Ціна за одиницю товару (Обов'язково число та можна формат через крапку, наприклад 4.5 або 8):
ADMIN-COST_ITEM_ERROR = Формат не є числом! Введіть щось типу 4.5 або 6:

ADMIN-PREVIEW_ITEM = 🎉 <b>Пропозиція товару</b>
    ━━━━━━━━━━━━━━━━
    🛒 <b>Назва:</b> {$title}
    📁 <b>Категорія:</b> {$category}
    💵 <b>Ціна:</b> {$cost}

    📜 <b>Опис:</b>
    {$desc}
    ━━━━━━━━━━━━━━━━

ADMIN-PUBLISH_ITEM = Публікувати товар
ADMIN-RESTART_PUBLISH = Почати спочатку
ADMIN-SUCCESS_PUBLISHED = Товар успішно опубліковано, публікуємо ще один?
ADMIN-FAIL_PUBLISHED = Помилка публікації

# CREATE CATEGORY
ADMIN-CATEGORY_NAME = Назва для категорії (вкладіться у 20-30 симолів, щоб тг не обрізав текст для кнопки):
ADMIN-NAME_CATEGORY_ERROR = Назва для товару {$count} символів, скороти до 50 хоча б:
ADMIN-CATEGORY_SUCCESS_ADD = Категорію <b>{$name}</b> успішно додано! Додати ще?
ADMIN-CATEGORY_FAIL_ADD = Помилка cтворення


# MESSAGING CATEGORY
ADMIN-CHOICE_TYPE_MESSAGE = Оберіть для кого розсилка
ADMIN-MESSAGE_ALL_CLIENTS = Всім клієнтам
ADMIN-MESSAGE_INDIVIDUAL = Особисто по Telegram ID

ADMIN-SET_USER_ID = Введіть Telegram ID користувача:
ADMIN-SET_MESSAGE = Ваше повідомлення (Можна використовувати формат телеграма):
ADMIN-SET_MEDIA = Надішліть Фото/Відео/Гіфку за бажанням:
ADMIN-MEDIA_WRONG = Невірний формат, надішліть (Фото/Відео/Гіфку) у стисненому форматі:
ADMIN-SET_BUTTON = Бажаєте додати кнопку?
ADMIN-SET_BUTTON_TEXT = Текст для кнопки (20-30 символів бажано):
ADMIN-BUTTON_TEXT_ERROR = Скороти хоча б до 50 символів, зараз {$count}
ADMIN-SET_BUTTON_URL = Посилання для кнопки:
ADMIN-BUTTON_URL_ERROR = Посилання має неправильний формат, воно має починатися з https:// та містити сайт або справжній контакт в тг тощо
ADMIN-SET_BUTTON_NEXT = Бажаєте додати ще кнопку?
ADMIN-PREVIEW_MESSAGING = Якщо все правильно, можете відправляти!
ADMIN-SEND = Відправити
ADMIN-RESTART = Почати спочатку

ADMIN-RESULT_NOTIFICATION = <b>-Результат розсилки-</b>

    Отримали повідомлення: {$send}\{$users}
    Заблокували бота: {$block}
    Інше: {$other}


# BAN SYSTEM
ADMIN-BAN_SYSTEM = Система банів

ADMIN-BAN_USER = Заблокувати користувача
ADMIN-UNBAN_USER = Розблокувати користувача
ADMIN-BAN_LIST = Список заблокованих

ADMIN-BAN_ONE_MORE = Заблокувати ще одного
ADMIN-UNBAN_ONE_MORE = Розблокувати ще одного

ADMIN-BAN_USER_ID = Введіть Telegram ID (<b>348938590</b>) або
    нікнейм користувача (<b>@nickname</b>):
ADMIN-UNBAN_USER_ID = Введіть Telegram ID (<b>348938590</b>):

ADMIN-BAN_SUCCESS = Користувача успішно заблоковано
ADMIN-BAN_ERROR = Помилка при блокуванні
ADMIN-UNBAN_SUCCESS = Користувача успішно розблоковано
ADMIN-UNBAN_ERROR = Помилка при розблокуванні

ADMIN-BAN_LIST_TEMPLATE = Юзернейм: @{$username}
    Телеграм ID: <code>{$id}</code>
    Мова користувача: <b>{$lang}</b>
ADMIN-NO_BANNED_USERS = Немає заблокованих користувачів


# ORDERS
ADMIN-ORDERS_HISTORY = Історія замовлень
ADMIN-ORDERS_HISTORY_EMPTY = Немає замовлень
ADMIN-USERNAME_HAVNT = Відстутній юзернейм

ADMIN-ORDER_LIST_TEMPLATE = #{$id} {$category} ({$count} шт.) =${$price}
ADMIN-ORDER_ITEM_TEMPLATE = 🛒 <b>Замовлення #{$id}</b>
    ━━━━━━━━━━━━━━━━
    📄 Номер: <b>{$id}</b>
    📅 Дата: <b>{$date}</b>

    📍 Назва: <b>{$name}</b>
    📦 Категорія: <b>{$category}</b>
    🔢 Кількість: <b>{$count} шт.</b>
    💵 Загальна Ціна: <b>{$price}$</b>

    📝 <b>Опис:</b>
    {$desc}

    👤 <b>Користувач:</b>
    🆔 Телеграм ID: <code>{$user_id}</code>
    🔗 Юзернейм: {$username}
