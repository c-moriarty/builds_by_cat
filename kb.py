from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="Анемо", callback_data="anemo"),
    InlineKeyboardButton(text="Пиро", callback_data="piro")],
    [InlineKeyboardButton(text="Крио", callback_data="crio"),
    InlineKeyboardButton(text="Гео", callback_data="geo")],
    [InlineKeyboardButton(text="Электро", callback_data="electro"),
    InlineKeyboardButton(text="Дэндро", callback_data="dendro")],
    [InlineKeyboardButton(text="Гидро", callback_data="gidro")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

menu_anemo = [
    [InlineKeyboardButton(text="Фарузан", callback_data="faruzan"),
    InlineKeyboardButton(text="Хэйдзо", callback_data="heizou")],
    [InlineKeyboardButton(text="Джин", callback_data="jean"),
    InlineKeyboardButton(text="Кадзуха", callback_data="kazuha")],
    [InlineKeyboardButton(text="Саю", callback_data="sayu"),
    InlineKeyboardButton(text="Сахароза", callback_data="sucrose")],
    [InlineKeyboardButton(text="Путешественник", callback_data="traveler"),
    InlineKeyboardButton(text="Венти", callback_data="venti")], 
    [InlineKeyboardButton(text="Странник", callback_data="wanderer"), 
    InlineKeyboardButton(text="Сяо", callback_data="xiao")]
]
menu_anemo = InlineKeyboardMarkup(inline_keyboard=menu_anemo)