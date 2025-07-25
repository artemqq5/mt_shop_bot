CLIENT-BUY = 📦 Buy
CLIENT-AVAILABILITY = 🛒 Product Availability
CLIENT-PROFILE = 👤 Profile
CLIENT-SUPPORT = 💬 Support

# OTHER
CLIENT-CONNECTION_WITH_SUPPORT = To contact support, click the button below ⬇️
CLIENT-SUPPORT_CONTACT = Contact Manager 📪

# BUY MENU
CLIENT-BUY-EMPTY_ITEMS = There are no items in the category at the moment

CLIENT-BUY-NOT_EXIST = The item no longer exists

CLIENT-BUY-CHOICE_CATEGORY = Choose a product
CLIENT-BUY-CHOICE_ITEM = Current category: <b>{$category}</b>
CLIENT-BUY-ITEM_LIST_TEMPLATE = {$title} | ${$cost}
CLIENT-BUY-ITEM_TEMPLATE = 🎉 <b>Product Offer</b>
    ━━━━━━━━━━━━━━━━
    🛒 <b>Name:</b> {$title}
    📁 <b>Category:</b> {$category}
    💵 <b>Price:</b> {$cost}

    📜 <b>Description:</b>
    {$desc}

CLIENT-BUY-COUNT = Quantity:
CLIENT-BUY-COUNT_ERROR = It must be an integer greater than 0:
CLIENT-BUY-DESC = Order comment:
CLIENT-BUY-DESC_ERROR = The text is too long ({$size} characters), shorten it to at least 500 characters:
CLIENT-BUY-PREVIEW = <b>Order Preview</b>
    ━━━━━━━━━━━━━━━━
    🛒 <b>Product:</b> {$title}
    📍 <b>Quantity:</b> {$count} pcs
    💵 <b>Total Price:</b> {$cost}$

    💌 <b>Your Comment:</b>
    {$desc}
CLIENT-BUY-SEND = Submit Order
CLIENT-BUY-SEND_SUCCESS = Order Successfully Sent ✅
CLIENT-BUY-SEND_ERROR = Failed to send the order ⛔️, please contact the manager or try again later
CLIENT-BUY-RESTART = Restart Order

# AVAILABILITY
CLIENT-AVAILABILITY-ITEM = {$title} | {$cost}$
CLIENT-AVAILABILITY-CATEGORY = 📲 <b>{$category}</b>
    ━━━━━━━━━━━━━━━━
CLIENT-AVAILABILITY-NO_ITEMS = <b>No items available at the moment, but we'll restock soon!</b>

# PROFILE
CLIENT-PROFILE-MAIN_PAGE = My Profile
    ━━━━━━━━━━━━━━━━
    💰 Balance: <b>{$balance}$</b>

    👤 <b>Telegram ID:</b> <code>{$telegram_id}</code>
    🛍️ Orders placed: <b>{$order_count}</b>

    🌐 User language: <b>{$lang}</b>
    📅 Registration date: <b>{$date}</b>
    ⏳ You've been with us for: <b>{$days}</b> days!

CLIENT-PROFILE-ORDERS = 📋 My Orders
CLIENT-PROFILE-ORDER_LIST_TEMPLATE = {$title} | {$count} pcs | ={$price}$
CLIENT-PROFILE-ORDER_TEMPLATE = <b>Order #{$id}</b>
    ━━━━━━━━━━━━━━━━
    🛒 <b>Product:</b> {$title}
    📍 <b>Quantity:</b> {$count} pcs
    💵 <b>Total Price:</b> {$cost}$

    💌 <b>Your Comment:</b>
    {$desc}

    <b>Order Date:</b> {$date}
CLIENT-PROFILE-EMPTY_ORDERS = ️ You don't have any orders yet 🤷‍♂️, to fix this, choose the category "{$buy_category_bot}" and place your first order! 🚀

CLIENT-BALANCE_INSUFFICIENT = Insufficient balance ❌

    Balance: {$balance}$
    Invoice: {$invoice}$

    Shortage: {$difference}$
CLIENT-BALANCE_REPLENISH = Replenish balance 💰
CLIENT-BALANCE_SUM = Enter the replenishment amount in USDT (min 5$) 💵:
CLIENT-BALANCE_SUM_ERROR = It must be a number greater than or equal to 5.0:
CLIENT-BALANCE_INFO = <b>Payment Information</b> ℹ️
    ━━━━━━━━━━━━━━━━
    <b>⚠️Be sure to pay the exact amount indicated, including commissions⚠️
    If you have problems, contact support, they will help you</b>

    Payment ID: <code>{$id}</code>
    Payment amount: <b>{$sum} USDT</b> 💰

    Payment creation: <b>{$created_at}</b>
CLIENT-BALANCE_CREATE_INVOICE_ERROR = Error creating payment invoice ❌, please contact support
CLIENT-BALANCE_PAY_INVOICE = Pay the invoice 🧾
