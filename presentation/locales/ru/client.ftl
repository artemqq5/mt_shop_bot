CLIENT-BUY = 📦 Купить
CLIENT-AVAILABILITY = 🛒 Наличие товаров
CLIENT-PROFILE = 👤 Профиль
CLIENT-SUPPORT = 💬 Поддержка

# OTHER
CLIENT-CONNECTION_WITH_SUPPORT = Чтобы связаться с поддержкой, нажмите кнопку ниже ⬇️
CLIENT-SUPPORT_CONTACT = Написать менеджеру 📪

# BUY MENU
CLIENT-BUY-EMPTY_ITEMS = В категории сейчас нет товаров

CLIENT-BUY-NOT_EXIST = Позиция больше не существует

CLIENT-BUY-CHOICE_CATEGORY = Выберите товар
CLIENT-BUY-CHOICE_ITEM = Текущая категория: <b>{$category}</b>
CLIENT-BUY-ITEM_LIST_TEMPLATE = {$title} | ${$cost}
CLIENT-BUY-ITEM_TEMPLATE = 🎉 <b>Предложение товара</b>
    ━━━━━━━━━━━━━━━━
    🛒 <b>Название:</b> {$title}
    📁 <b>Категория:</b> {$category}
    💵 <b>Цена:</b> {$cost}

    📜 <b>Описание:</b>
    {$desc}

CLIENT-BUY-COUNT = Количество:
CLIENT-BUY-COUNT_ERROR = Это должно быть целым числом и больше 0:
CLIENT-BUY-DESC = Комментарий к заказу:
CLIENT-BUY-DESC_ERROR = Слишком длинный текст ({$size} символов), сократите его хотя бы до 500 символов:
CLIENT-BUY-PREVIEW = <b>Предварительный просмотр заказа</b>
    ━━━━━━━━━━━━━━━━
    🛒 <b>Товар:</b> {$title}
    📍 <b>Количество:</b> {$count} шт.
    💵 <b>Общая цена:</b> {$cost}$

    💌 <b>Ваш комментарий:</b>
    {$desc}
CLIENT-BUY-SEND = Отправить заказ
CLIENT-BUY-SEND_SUCCESS = Заказ успешно отправлен ✅
CLIENT-BUY-SEND_ERROR = Не удалось отправить заказ ⛔️, свяжитесь с менеджером или попробуйте позже
CLIENT-BUY-RESTART = Начать заказ заново

# AVAILABILITY
CLIENT-AVAILABILITY-ITEM = {$title} | {$cost}$
CLIENT-AVAILABILITY-CATEGORY = 📲 <b>{$category}</b>
    ━━━━━━━━━━━━━━━━
CLIENT-AVAILABILITY-NO_ITEMS = <b>Товаров нет в наличии, но скоро мы пополним запасы!</b>

# PROFILE
CLIENT-PROFILE-MAIN_PAGE = Мой профиль
    ━━━━━━━━━━━━━━━━
    💰 Баланс: <b>{$balance}$</b>

    👤 <b>Telegram ID:</b> <code>{$telegram_id}</code>
    🛍️ Заказов сделано: <b>{$order_count}</b>

    🌐 Язык пользователя: <b>{$lang}</b>
    📅 Дата регистрации: <b>{$date}</b>
    ⏳ Вы с нами уже: <b>{$days}</b> дней!

CLIENT-PROFILE-ORDERS = 📋 Мои заказы
CLIENT-PROFILE-ORDER_LIST_TEMPLATE = {$title} | {$count} шт. | ={$price}$
CLIENT-PROFILE-ORDER_TEMPLATE = <b>Заказ #{$id}</b>
    ━━━━━━━━━━━━━━━━
    🛒 <b>Товар:</b> {$title}
    📍 <b>Количество:</b> {$count} шт.
    💵 <b>Общая цена:</b> {$cost}$

    💌 <b>Ваш комментарий:</b>
    {$desc}

    <b>Дата заказа:</b> {$date}
CLIENT-PROFILE-EMPTY_ORDERS = ️ У вас пока нет заказов 🤷‍♂️, чтобы это исправить, выберите категорию "{$buy_category_bot}" и сделайте свой первый заказ! 🚀

CLIENT-BALANCE_INSUFFICIENT = Недостаточно средств ❌

    Баланс: {$balance}$
    Счет: {$invoice}$

    Не хватает: {$difference}$
CLIENT-BALANCE_REPLENISH = Пополнить баланс 💰
CLIENT-BALANCE_SUM = Укажите сумму пополнения в USDT (мин 5$) 💵:
CLIENT-BALANCE_SUM_ERROR = Это должно быть число больше или равно 5.0:
CLIENT-BALANCE_INFO = <b>Информация о платеже</b> ℹ️
    ━━━━━━━━━━━━━━━━
    <b>⚠️Обязательно уплатите точную сумму, которую указали учитывая комиссии⚠️
    Если возникнут проблемы, обратитесь в сапорт, вам помогут</b>

    ID платежа: <code>{$id}</code>
    Сумма платежа: <b>{$sum} USDT</b> 💰

    Создание платежа: <b>{$created_at}</b>
CLIENT-BALANCE_CREATE_INVOICE_ERROR = Ошибка при создании счета оплаты ❌, свяжитесь с поддержкой
CLIENT-BALANCE_PAY_INVOICE = Оплатить счет 🧾
