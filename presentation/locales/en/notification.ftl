NOTIFICATION-NEW_USER = 👤 <b>A new user has joined the bot!</b>
    ━━━━━━━━━━━━━━━━
    Name: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>
    Joined: <b>{$join_at}</b>

NOTIFICATION-NEW_ORDER = 🛒 <b>New order #{$id}</b>
    ━━━━━━━━━━━━━━━━
    📄 Order number: <b>{$id}</b>
    📅 Date: <b>{$date}</b>

    📍 Name: <b>{$name}</b>
    📦 Category: <b>{$category}</b>
    🔢 Quantity: <b>{$count} pcs.</b>
    💵 Total price: <b>{$price}$</b>

    📝 <b>Description:</b>
    {$desc}

    👤 <b>User:</b>
    🆔 Telegram ID: <code>{$user_id}</code>
    🔗 Username: {$username}

NOTIFICATION-BALANCE_INSUFFICIENT = <b>Insufficient balance for the order!</b>

    User has a balance: <b>{$balance}$</b>
    Invoice: <b>{$invoice}$</b>
    Shortfall for the order: <b>{$difference}$</b>
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
