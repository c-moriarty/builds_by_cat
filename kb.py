from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="Анемо", callback_data="anemo"),
    InlineKeyboardButton(text="Пиро", callback_data="pyro")],
    [InlineKeyboardButton(text="Крио", callback_data="cryo"),
    InlineKeyboardButton(text="Гео", callback_data="geo")],
    [InlineKeyboardButton(text="Электро", callback_data="electro"),
    InlineKeyboardButton(text="Дэндро", callback_data="dendro")],
    [InlineKeyboardButton(text="Гидро", callback_data="hydro")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

back = [
    [InlineKeyboardButton(text="Вернуться в главное меню", callback_data="menu")]
]
back = InlineKeyboardMarkup(inline_keyboard=back)

menu_anemo = [
    [InlineKeyboardButton(text="Фарузан", callback_data="faruzan"),
    InlineKeyboardButton(text="Хэйдзо", callback_data="heizou")],
    [InlineKeyboardButton(text="Джин", callback_data="jean"),
    InlineKeyboardButton(text="Кадзуха", callback_data="kazuha")],
    [InlineKeyboardButton(text="Саю", callback_data="sayu"),
    InlineKeyboardButton(text="Сахароза", callback_data="sucrose")],
    [InlineKeyboardButton(text="Путешественник/ца", callback_data="traveler_anemo"),
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

menu_cryo = [
    [InlineKeyboardButton(text="Элой", callback_data="aloy"),
    InlineKeyboardButton(text="Аяка", callback_data="ayaka")],
    [InlineKeyboardButton(text="Чун Юнь", callback_data="chongyun"),
    InlineKeyboardButton(text="Диона", callback_data="diona")],
    [InlineKeyboardButton(text="Эола", callback_data="eula"),
    InlineKeyboardButton(text="Гань Юй", callback_data="ganyu")],
    [InlineKeyboardButton(text="Кэйя", callback_data="kaeya"),
    InlineKeyboardButton(text="Лайла", callback_data="layla")], 
    [InlineKeyboardButton(text="Мика", callback_data="mika"), 
    InlineKeyboardButton(text="Ци Ци", callback_data="qiqi")],
    [InlineKeyboardButton(text="Розария", callback_data="rosara"), 
    InlineKeyboardButton(text="Шэнь Хэ", callback_data="shenhe")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_cryo = InlineKeyboardMarkup(inline_keyboard=menu_cryo)

menu_geo = [
    [InlineKeyboardButton(text="Альбедо", callback_data="albedo"),
    InlineKeyboardButton(text="Горо", callback_data="gorou")],
    [InlineKeyboardButton(text="Итто", callback_data="itto"),
    InlineKeyboardButton(text="Нин Гуан", callback_data="ningguang")],
    [InlineKeyboardButton(text="Ноэлль", callback_data="noelle"),
    InlineKeyboardButton(text="Путешественник/ца", callback_data="traveler_geo")],
    [InlineKeyboardButton(text="Юнь Цзинь", callback_data="yun_jin"),
    InlineKeyboardButton(text="Чжун Ли", callback_data="zhongli")], 
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_geo = InlineKeyboardMarkup(inline_keyboard=menu_geo)

menu_electro = [
    [InlineKeyboardButton(text="Бэй Доу", callback_data="beidou"),
    InlineKeyboardButton(text="Сайно", callback_data="cyno")],
    [InlineKeyboardButton(text="Дори", callback_data="dori"),
    InlineKeyboardButton(text="Фишль", callback_data="fischl")],
    [InlineKeyboardButton(text="Кэ Цин", callback_data="keqing"),
    InlineKeyboardButton(text="Путешественник/ца", callback_data="traveler_electro")],
    [InlineKeyboardButton(text="Кики Синобу", callback_data="kuki_shinobu"),
    InlineKeyboardButton(text="Лиза", callback_data="lisa")],
    [InlineKeyboardButton(text="Райдэн", callback_data="raiden"),
    InlineKeyboardButton(text="Рэйзор", callback_data="razor")],
    [InlineKeyboardButton(text="Сара", callback_data="sara"),
    InlineKeyboardButton(text="Яэ Мико", callback_data="yae_miko")], 
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_electro = InlineKeyboardMarkup(inline_keyboard=menu_electro)

menu_dendro = [
    [InlineKeyboardButton(text="Кирара", callback_data="kirara"),
    InlineKeyboardButton(text="Аль-Хайтам", callback_data="alhaitham")],
    [InlineKeyboardButton(text="Бай Чжу", callback_data="baizhu"),
    InlineKeyboardButton(text="Коллеи", callback_data="collei")],
    [InlineKeyboardButton(text="Кавех", callback_data="kaveh"),
    InlineKeyboardButton(text="Путешественник/ца", callback_data="traveler_dendro")],
    [InlineKeyboardButton(text="Нахида", callback_data="nahida"),
    InlineKeyboardButton(text="Тигнари", callback_data="tighnari")],
    [InlineKeyboardButton(text="Яо Яо", callback_data="yaoyao"), 
    InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_dendro = InlineKeyboardMarkup(inline_keyboard=menu_dendro)

menu_hydro = [
    [InlineKeyboardButton(text="Аято", callback_data="ayato"),
    InlineKeyboardButton(text="Барбара", callback_data="barbara")],
    [InlineKeyboardButton(text="Кандакия", callback_data="candace"),
    InlineKeyboardButton(text="Тарталья", callback_data="childe")],
    [InlineKeyboardButton(text="Кокоми", callback_data="kokomi"),
    InlineKeyboardButton(text="Мона", callback_data="mona")],
    [InlineKeyboardButton(text="Нилу", callback_data="nilou"),
    InlineKeyboardButton(text="Син Цю", callback_data="xingqiu")],
    [InlineKeyboardButton(text="E Лань", callback_data="yelan"), 
    InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_hydro = InlineKeyboardMarkup(inline_keyboard=menu_hydro)

menu_kazuha = [
    [InlineKeyboardButton(text="Мастерство стихий", callback_data="kazuha_ms"),
    InlineKeyboardButton(text="Крит. шанс и крит. урон", callback_data="kazuha_krit")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_kazuha = InlineKeyboardMarkup(inline_keyboard=menu_kazuha)

menu_faruzan = [
    [InlineKeyboardButton(text="Саппорт", callback_data="faruzan_sup"),
    InlineKeyboardButton(text="ДД", callback_data="faruzan_dd")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_faruzan = InlineKeyboardMarkup(inline_keyboard=menu_faruzan)

menu_venti = [
    [InlineKeyboardButton(text="Мастерство стихий", callback_data="venti_ms"),
    InlineKeyboardButton(text="Крит. шанс и крит. урон", callback_data="venti_krit")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_venti = InlineKeyboardMarkup(inline_keyboard=menu_venti)

menu_wanderer = [
    [InlineKeyboardButton(text="Драйвер", callback_data="wanderer_driver"),
    InlineKeyboardButton(text="Анемо DPS", callback_data="wanderer_dps")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_wanderer = InlineKeyboardMarkup(inline_keyboard=menu_wanderer)

menu_jean = [
    [InlineKeyboardButton(text="ДД", callback_data="jean_dd"),
    InlineKeyboardButton(text="Саппорт", callback_data="jean_sup")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_jean = InlineKeyboardMarkup(inline_keyboard=menu_jean)

menu_thoma = [
    [InlineKeyboardButton(text="Саб-дд", callback_data="thoma_supdd"),
    InlineKeyboardButton(text="Щитовик", callback_data="thoma_shit")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_thoma = InlineKeyboardMarkup(inline_keyboard=menu_jean)

menu_layla = [
    [InlineKeyboardButton(text="Саб-дд", callback_data="layla_supdd"),
    InlineKeyboardButton(text="Саппорт", callback_data="layla_support")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_layla = InlineKeyboardMarkup(inline_keyboard=menu_jean)

menu_mika = [
    [InlineKeyboardButton(text="Саб-дд", callback_data="mika_dd"),
    InlineKeyboardButton(text="Саппорт", callback_data="mika_support")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_mika = InlineKeyboardMarkup(inline_keyboard=menu_jean)

menu_ningguang = [
    [InlineKeyboardButton(text="Саб-дд", callback_data="ningguang_dd"),
    InlineKeyboardButton(text="Саппорт", callback_data="ningguang_supdd")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_ningguang = InlineKeyboardMarkup(inline_keyboard=menu_jean)

menu_zhongli = [
    [InlineKeyboardButton(text="Саб-дд", callback_data="zhongli_supdd"),
    InlineKeyboardButton(text="Саппорт", callback_data="zhongli_support")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_zhongli = InlineKeyboardMarkup(inline_keyboard=menu_jean)

menu_sara = [
    [InlineKeyboardButton(text="Второстепенный дд", callback_data="sara_supdd"),
    InlineKeyboardButton(text="Саппорт", callback_data="sara_support")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_sara = InlineKeyboardMarkup(inline_keyboard=menu_jean)

menu_baizhu = [
    [InlineKeyboardButton(text="Саб-дд", callback_data="baizhu_supdd"),
    InlineKeyboardButton(text="Щитовик", callback_data="baizhu_shit")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_baizhu = InlineKeyboardMarkup(inline_keyboard=menu_jean)

menu_traveler_dendro = [
    [InlineKeyboardButton(text="Саб-дд", callback_data="traveler_dendro_supdd"),
    InlineKeyboardButton(text="Саппорт", callback_data="traveler_dendro_support")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_traveler_dendro = InlineKeyboardMarkup(inline_keyboard=menu_jean)

menu_nahida = [
    [InlineKeyboardButton(text="Основной DPS", callback_data="nahida_dps"),
    InlineKeyboardButton(text="Саппорт", callback_data="nahida_support")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_nahida = InlineKeyboardMarkup(inline_keyboard=menu_jean)

menu_yaoyao = [
    [InlineKeyboardButton(text="Реактор", callback_data="yaoyao_react"),
    InlineKeyboardButton(text="Саппорт-хиллер", callback_data="yaoyao_support")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_yaoyao = InlineKeyboardMarkup(inline_keyboard=menu_jean)

menu_candace = [
    [InlineKeyboardButton(text="Мэйн-дд", callback_data="candace_dd"),
    InlineKeyboardButton(text="Саппорт", callback_data="candace_support")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
]
menu_candace = InlineKeyboardMarkup(inline_keyboard=menu_jean)
