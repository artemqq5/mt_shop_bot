NOTIFICATION-NEW_USER = 👤 <b>Новый пользователь присоединился к боту!</b>
    ━━━━━━━━━━━━━━━━
    Имя: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>
    Присоединился: <b>{$join_at}</b>

NOTIFICATION-NEW_ORDER = 🛒 <b>Новый заказ #{$id}</b>
    ━━━━━━━━━━━━━━━━
    📄 Номер заказа: <b>{$id}</b>
    📅 Дата: <b>{$date}</b>

    📍 Название: <b>{$name}</b>
    📦 Категория: <b>{$category}</b>
    🔢 Количество: <b>{$count} шт.</b>
    💵 Общая цена: <b>{$price}$</b>

    📝 <b>Описание:</b>
    {$desc}

    👤 <b>Пользователь:</b>
    🆔 Telegram ID: <code>{$user_id}</code>
    🔗 Имя пользователя: {$username}

NOTIFICATION-BALANCE_INSUFFICIENT = <b>Недостаточно средств для заказа!</b>

    Баланс пользователя: <b>{$balance}$</b>
    Сумма счета: <b>{$invoice}$</b>
    Недостаток для заказа: <b>{$difference}$</b>
    ━━━━━━━━━━━━━━━━
    <b>Детали заказа</b>

    📅 Дата: <b>{$date}</b>

    📍 Название: <b>{$name}</b>
    📦 Категория: <b>{$category}</b>
    🔢 Количество: <b>{$count} шт.</b>
    💵 Общая цена: <b>{$invoice}$</b>

    📝 <b>Описание:</b>
    {$desc}

    👤 <b>Пользователь:</b>
    🆔 Telegram ID: <code>{$user_id}</code>
    🔗 Имя пользователя: {$username}

NOTIFICATION-INVOICE_INIT = <b>Пользователь создал счет на пополнение баланса!</b>

    Баланс пользователя: <b>{$balance}$</b>
    Сумма пополнения: <b>{$value}$</b>

    Номер транзакции: <code>{$number}</code>
    ID транзакции: <code>{$id}</code>

    📅 Дата: <b>{$date}</b>

    👤 <b>Пользователь:</b>
    🆔 Telegram ID: <code>{$user_id}</code>
    🔗 Имя пользователя: {$username}

NOTIFICATION-INVOICE_COMPLETED = <b>Пользователь успешно пополнил баланс!</b>

    Баланс пользователя: <b>{$balance}$</b>
    Сумма пополнения: <b>{$value}$</b>

    Номер транзакции: <code>{$number}</code>
    ID транзакции: <code>{$id}</code>

    📅 Дата: <b>{$date}</b>

    👤 <b>Пользователь:</b>
    🆔 Telegram ID: <code>{$user_id}</code>
    🔗 Имя пользователя: {$username}
