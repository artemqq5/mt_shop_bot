# admin main menu
ADMIN-ORDERS = Orders
ADMIN-MANAGEMENT = Management
ADMIN-MESSAGING = Messaging
ADMIN-BAN = Ban


# MANAGEMENT CATEGORY
ADMIN-CATEGORY_INFO = <b>{$category}</b>
    Items in category: <b>{$count}</b>
ADMIN-ADD_ITEM = Add item
ADMIN-SHOW_ITEMS = Show items
ADMIN-HIDE = Hide
ADMIN-OPEN = Show
ADMIN-DELETE = Delete

# DELETE CATEGORY
ADMIN-DELETE_CATEGORY_APPROVE = Delete category (<b>{$category}</b>)?

    All items in the category will be deleted too❗
ADMIN-DELETE_SUCCESS = Successfully deleted
ADMIN-DELETE_FAIL = Deletion failed


# MANAGEMENT ITEMS
ADMIN-ITEMS_GROUP_INFO = Category: <b>{$category}</b>

# DELETE ITEM
ADMIN-DELETE_ITEM_APPROVE = Delete item (<b>{$item}</b>)?

# ADD ITEM
ADMIN-CHOICE_CATEGORY = Choose category
ADMIN-CREATE_NEW_CATEGORY = Create new

ADMIN-TITLE_ITEM = Title for the item (keep it within 20-30 characters to avoid truncation by Telegram):
ADMIN-TITLE_ITEM_ERROR = Title for the item {$count} characters, shorten it to at least 50:
ADMIN-DESC_ITEM = Description for the item (you can mention geo and use Telegram formatting, such as bold text, etc.):
ADMIN-COST_ITEM = Price per unit (must be a number, you can use decimal format like 4.5 or 8):
ADMIN-COST_ITEM_ERROR = Format is not a number! Enter something like 4.5 or 6:

ADMIN-PREVIEW_ITEM = 🎉 <b>Item offer</b>
    ━━━━━━━━━━━━━━━━
    🛒 <b>Title:</b> {$title}
    📁 <b>Category:</b> {$category}
    💵 <b>Price:</b> {$cost}

    📜 <b>Description:</b>
    {$desc}
    ━━━━━━━━━━━━━━━━

ADMIN-PUBLISH_ITEM = Publish item
ADMIN-RESTART_PUBLISH = Start over
ADMIN-SUCCESS_PUBLISHED = Item successfully published, publish another one?
ADMIN-FAIL_PUBLISHED = Publication failed

# CREATE CATEGORY
ADMIN-CATEGORY_NAME = Title for the category (keep it within 20-30 characters to avoid truncation by Telegram):
ADMIN-NAME_CATEGORY_ERROR = Title for the item {$count} characters, shorten it to at least 50:
ADMIN-CATEGORY_SUCCESS_ADD = Category <b>{$name}</b> successfully added! Add another one?
ADMIN-CATEGORY_FAIL_ADD = Creation failed


# MESSAGING CATEGORY
ADMIN-CHOICE_TYPE_MESSAGE = Choose recipient for the message
ADMIN-MESSAGE_ALL_CLIENTS = All clients
ADMIN-MESSAGE_INDIVIDUAL = Individually by Telegram ID

ADMIN-SET_USER_ID = Enter user Telegram ID:
ADMIN-SET_MESSAGE = Your message (Telegram formatting can be used):
ADMIN-SET_MEDIA = Send Photo/Video/GIF if desired:
ADMIN-MEDIA_WRONG = Wrong format, send (Photo/Video/GIF) in compressed format:
ADMIN-SET_BUTTON = Do you want to add a button?
ADMIN-SET_BUTTON_TEXT = Button text (20-30 characters recommended):
ADMIN-BUTTON_TEXT_ERROR = Shorten to at least 50 characters, currently {$count}
ADMIN-SET_BUTTON_URL = Button URL:
ADMIN-BUTTON_URL_ERROR = URL format is incorrect, it should start with https:// and contain a valid website or contact in Telegram, etc.
ADMIN-SET_BUTTON_NEXT = Do you want to add another button?
ADMIN-PREVIEW_MESSAGING = If everything is correct, you can send!
ADMIN-SEND = Send
ADMIN-RESTART = Start over

ADMIN-RESULT_NOTIFICATION = <b>-Messaging result-</b>

    Messages received: {$send}\{$users}
    Bot blocked: {$block}
    Other: {$other}


# BAN SYSTEM
ADMIN-BAN_SYSTEM = Ban system

ADMIN-BAN_USER = Ban user
ADMIN-UNBAN_USER = Unban user
ADMIN-BAN_LIST = Banned list

ADMIN-BAN_ONE_MORE = Ban another
ADMIN-UNBAN_ONE_MORE = Unban another

ADMIN-BAN_USER_ID = Enter Telegram ID (<b>348938590</b>) or
    username (<b>@nickname</b>):
ADMIN-UNBAN_USER_ID = Enter Telegram ID (<b>348938590</b>):

ADMIN-BAN_SUCCESS = User successfully banned
ADMIN-BAN_ERROR = Ban error
ADMIN-UNBAN_SUCCESS = User successfully unbanned
ADMIN-UNBAN_ERROR = Unban error

ADMIN-BAN_LIST_TEMPLATE = Username: @{$username}
    Telegram ID: <code>{$id}</code>
    User language: <b>{$lang}</b>
ADMIN-NO_BANNED_USERS = No banned users


# ORDERS
ADMIN-ORDERS_HISTORY = Order history
ADMIN-ORDERS_HISTORY_EMPTY = No orders
ADMIN-USERNAME_HAVNT = Username missing

ADMIN-ORDER_LIST_TEMPLATE = #{$id} {$category} ({$count} pcs.) =${$price}
ADMIN-ORDER_ITEM_TEMPLATE = 🛒 <b>Order #{$id}</b>
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
