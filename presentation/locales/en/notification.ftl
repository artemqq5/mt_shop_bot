NOTIFICATION-NEW_USER = 👤 <b>New user joined the bot!</b>
    ━━━━━━━━━━━━━━━━
    Name: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>
    Joined: <b>{$join_at}</b>

NOTIFICATION-NEW_ORDER = 🛒 <b>New order #{$id}</b>
    ━━━━━━━━━━━━━━━━
    📄 Order Number: <b>{$id}</b>
    📅 Date: <b>{$date}</b>

    📍 Name: <b>{$name}</b>
    📦 Category: <b>{$category}</b>
    🔢 Quantity: <b>{$count} pcs</b>
    💵 Total Price: <b>{$price}$</b>

    📝 <b>Description:</b>
    {$desc}

    👤 <b>User:</b>
    🆔 Telegram ID: <code>{$user_id}</code>
    🔗 Username: {$username}

NOTIFICATION-BALANCE_INSUFFICIENT = <b>Insufficient balance for the order!</b>

    User's balance: <b>{$balance}$</b>
    Invoice amount: <b>{$invoice}$</b>
    Shortage: <b>{$difference}$</b>
    ━━━━━━━━━━━━━━━━
    <b>Order Details</b>

    📅 Date: <b>{$date}</b>

    📍 Name: <b>{$name}</b>
    📦 Category: <b>{$category}</b>
    🔢 Quantity: <b>{$count} pcs</b>
    💵 Total Price: <b>{$invoice}$</b>

    📝 <b>Description:</b>
    {$desc}

    👤 <b>User:</b>
    🆔 Telegram ID: <code>{$user_id}</code>
    🔗 Username: {$username}

NOTIFICATION-INVOICE_INIT = <b>User has created an invoice to top up the balance!</b>

    User's balance: <b>{$balance}$</b>
    Invoice amount: <b>{$value}$</b>

    Transaction number: <code>{$number}</code>
    Transaction ID: <code>{$id}</code>

    📅 Date: <b>{$date}</b>

    👤 <b>User:</b>
    🆔 Telegram ID: <code>{$user_id}</code>
    🔗 Username: {$username}

NOTIFICATION-INVOICE_COMPLETED = <b>User has successfully topped up the balance!</b>

    User's balance: <b>{$balance}$</b>
    Topped up amount: <b>{$value}$</b>

    Transaction number: <code>{$number}</code>
    Transaction ID: <code>{$id}</code>

    📅 Date: <b>{$date}</b>

    👤 <b>User:</b>
    🆔 Telegram ID: <code>{$user_id}</code>
    🔗 Username: {$username}
