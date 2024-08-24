CLIENT-BUY = 📦 Купити
CLIENT-AVAILABILITY = 🛒 Наявність товарів
CLIENT-PROFILE = 👤 Профіль
CLIENT-SUPPORT = 💬 Підтримка

# OTHERR
CLIENT-CONNECTION_WITH_SUPPORT = Щоб за'язатися з підтримкою натисніть на кнопку нижче ⬇️
CLIENT-SUPPORT_CONTACT = Написати Менеджеру 📪

# BUY MENU
CLIENT-BUY-EMPTY_ITEMS = В категорії зараз відсутні товари

CLIENT-BUY-NOT_EXIST = Позиції вже не існує

CLIENT-BUY-CHOICE_CATEGORY = Оберіть товар
CLIENT-BUY-CHOICE_ITEM = Поточна категорія: <b>{$category}</b>
CLIENT-BUY-ITEM_LIST_TEMPLATE = {$title} | ${$cost}
CLIENT-BUY-ITEM_TEMPLATE = 🎉 <b>Пропозиція товару</b>
    ━━━━━━━━━━━━━━━━
    🛒 <b>Назва:</b> {$title}
    📁 <b>Категорія:</b> {$category}
    💵 <b>Ціна:</b> {$cost}

    📜 <b>Опис:</b>
    {$desc}

CLIENT-BUY-COUNT = Кількість:
CLIENT-BUY-COUNT_ERROR = Це має бути цілим числом та більше 0:
CLIENT-BUY-DESC = Коментар до замовлення:
CLIENT-BUY-DESC_ERROR = Занадто великий текст ({$size}) символів, скоротіть хоча б до 500 символів:
CLIENT-BUY-PREVIEW = <b>Попередній перегляд замовлення</b>
    ━━━━━━━━━━━━━━━━
    🛒 <b>Товар:</b> {$title}
    📍 <b>Кількість:</b> {$count} шт.
    💵 <b>Загальна ціна:</b> {$cost}$

    💌 <b>Ваш коментар:</b>
    {$desc}
CLIENT-BUY-SEND = Відправити замовлення
CLIENT-BUY-SEND_SUCCESS = Замовлення Успішно відправлено ✅
CLIENT-BUY-SEND_ERROR = Не вийшло віправити замовленя ⛔️, напишіть менеджеру або спробуйте пізніше
CLIENT-BUY-RESTART = Замовлення спочатку

# AVAILABILITY
CLIENT-AVAILABILITY-ITEM = {$title} | {$cost}$
CLIENT-AVAILABILITY-CATEGORY = 📲 <b>{$category}</b>
    ━━━━━━━━━━━━━━━━
CLIENT-AVAILABILITY-NO_ITEMS = <b>Немає товарів в наявності, але скоро ми поповнимось!</b>

# POFILE
CLIENT-PROFILE-MAIN_PAGE = Мій профіль
    ━━━━━━━━━━━━━━━━
    💰 Баланс: <b>{$balance}$</b>

    👤 <b>Телеграм ID:</b> <code>{$telegram_id}</code>
    🛍️ Замовлень зроблено: <b>{$order_count}</b>

    🌐 Мова користувача: <b>{$lang}</b>
    📅 Дата реєстрації: <b>{$date}</b>
    ⏳ Ти з нами вже: <b>{$days}</b> днів!



CLIENT-PROFILE-ORDERS = 📋 Мої замовлення
CLIENT-PROFILE-ORDER_LIST_TEMPLATE = {$title} | {$count} шт. | ={$price}$
CLIENT-PROFILE-ORDER_TEMPLATE = <b>Замовлення #{$id}</b>
    ━━━━━━━━━━━━━━━━
    🛒 <b>Товар:</b> {$title}
    📍 <b>Кількість:</b> {$count} шт.
    💵 <b>Загальна ціна:</b> {$cost}$

    💌 <b>Ваш коментар:</b>
    {$desc}

    <b>Дата замовлення:</b> {$date}
CLIENT-PROFILE-EMPTY_ORDERS = ️ У вас поки немає замовлень 🤷‍♂️, щоб виправити це можете обрати категорію "{$buy_category_bot}" та зробити своє перше замовлення! 🚀

CLIENT-BALANCE_INSUFFICIENT = Недостатній баланс ❌

    Баланс: {$balance}$
    Рахунок: {$invoice}$

    Не вистачає: {$difference}$
CLIENT-BALANCE_REPLENISH = Поповнити баланс 💰
CLIENT-BALANCE_SUM = Вкажіть суму поповнення у USDT (мін 5$) 💵:
CLIENT-BALANCE_SUM_ERROR = Це має бути число більше або рівне 5.0:
CLIENT-BALANCE_INFO = <b>Інформація про платіж</b> ℹ️
    ━━━━━━━━━━━━━━━━
    ID Платежу: <code>{$id}</code>
    Сума платежу: <b>{$sum} USDT</b> 💰

    Створення платежу: <b>{$created_at}</b>
CLIENT-BALANCE_CREATE_INVOICE_ERROR = Помилка при створенні рахунку оплати ❌, зверніться у підтримку
CLIENT-BALANCE_PAY_INVOICE = Сплатіть рахунок 🧾
