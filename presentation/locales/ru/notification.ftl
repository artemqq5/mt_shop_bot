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
    🔗 Юзернейм: {$username}

NOTIFICATION-BALANCE_INSUFFICIENT = <b>Недостаточный баланс для заказа!</b>

    Пользователь имеет баланс: <b>{$balance}$</b>
    Счет: <b>{$invoice}$</b>
    Не хватает для заказа: <b>{$difference}$</b>
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
    🆔 Телеграм ID: <code>{$user_id}</code>
    🔗 Юзернейм: {$username}
