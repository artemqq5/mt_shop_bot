NOTIFICATION-NEW_USER = 👤 <b>Новий користувач доєднався до боту!</b>
    ━━━━━━━━━━━━━━━━
    Ім'я: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>
    Приєднався: <b>{$join_at}</b>

NOTIFICATION-NEW_ORDER = 🛒 <b>Нове замовлення #{$id}</b>
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

NOTIFICATION-BALANCE_INSUFFICIENT = <b>Недостатній баланс для замовлення!</b>

    Користувач має баланс: <b>{$balance}$</b>
    Рахунок: <b>{$invoice}$</b>
    Не вистачає до замовлення: <b>{$difference}$</b>
    ━━━━━━━━━━━━━━━━
    <b>Деталі замовлення</b>

    📅 Дата: <b>{$date}</b>

    📍 Назва: <b>{$name}</b>
    📦 Категорія: <b>{$category}</b>
    🔢 Кількість: <b>{$count} шт.</b>
    💵 Загальна Ціна: <b>{$invoice}$</b>

    📝 <b>Опис:</b>
    {$desc}

    👤 <b>Користувач:</b>
    🆔 Телеграм ID: <code>{$user_id}</code>
    🔗 Юзернейм: {$username}

NOTIFICATION-INVOICE_INIT = <b>Користувач створив інвойс на поповнення балансу!</b>

    Користувач має баланс: <b>{$balance}$</b>
    Рахунок на поповнення: <b>{$value}$</b>

    Номер транзакції: <code>{$number}</code>
    ID транзакції: <code>{$id}</code>

    📅 Дата: <b>{$date}</b>

    👤 <b>Користувач:</b>
    🆔 Телеграм ID: <code>{$user_id}</code>
    🔗 Юзернейм: {$username}

NOTIFICATION-INVOICE_COMPLETED = <b>Користувач успішно поповнив баланс!</b>

    Користувач має баланс: <b>{$balance}$</b>
    Поповнив на суму: <b>{$value}$</b>

    Номер транзакції: <code>{$number}</code>
    ID транзакції: <code>{$id}</code>

    📅 Дата: <b>{$date}</b>

    👤 <b>Користувач:</b>
    🆔 Телеграм ID: <code>{$user_id}</code>
    🔗 Юзернейм: {$username}