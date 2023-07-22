from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="Анемо", callback_data="anemo"),
    InlineKeyboardButton(text="Пиро", callback_data="pyro")],
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
    InlineKeyboardButton(text="Сяо", callback_data="xiao")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_anemo = InlineKeyboardMarkup(inline_keyboard=menu_anemo)

menu_pyro = [
    [InlineKeyboardButton(text="Эмбер", callback_data="amber"),
    InlineKeyboardButton(text="Беннет", callback_data="bennett")],
    [InlineKeyboardButton(text="Дэхья", callback_data="dehya"),
    InlineKeyboardButton(text="Дилюк", callback_data="diluc")],
    [InlineKeyboardButton(text="Ху Тао", callback_data="hu_tao"),
    InlineKeyboardButton(text="Кли", callback_data="klee")],
    [InlineKeyboardButton(text="Тома", callback_data="thoma"),
    InlineKeyboardButton(text="Сян Лин", callback_data="xiangling")], 
    [InlineKeyboardButton(text="Синь Янь", callback_data="xinyan"), 
    InlineKeyboardButton(text="Янь Фэй", callback_data="yanfei")],
    [InlineKeyboardButton(text="Ёимия", callback_data="yoimiya"), 
    InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_pyro = InlineKeyboardMarkup(inline_keyboard=menu_pyro)
