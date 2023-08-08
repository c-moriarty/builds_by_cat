from openpyxl import load_workbook

db = load_workbook('./gen.xlsx')
sheet = db.get_sheet_by_name('Sheet1')

greet = "Привет, {name}, я помогу тебе собрать билд любого персонажа из 'Genshin impact'. Для начала выбери стихию персонажа:"

menu = "Главное меню"
menu_anemo = "Меню анемо персонажей"
menu_pyro = "Меню пиро персонажей"
menu_cryo = "Меню крио персонажей"
menu_geo = "Меню гео персонажей"
menu_electro="Меню электро персонажей"
menu_dendro="Меню дендро персонажей"
menu_hydro="Меню гидро персонажей"

menu_kazuha="Варианты сборки Кадзухи"
menu_jean="Варианты сборки Джин"
menu_faruzan="Варианты сборки Фарузан"
menu_venti="Варианты сборки Венти"
menu_wanderer="Варианты сборки Странника"
menu_thoma="Варианты сборки Томы"
menu_layla="Варианты сборки Лайлы"
menu_ningguang="Варианты сборки Нин Гуан"
menu_zhongli="Варианты сборки Чжун Ли"
menu_sara="Варианты сборки Сары"
menu_baizhu="Варианты сборки Бай Чжу"
menu_traveler_dendro="Варианты сборки дэндро Путешественника/цы"
menu_nahida="Варианты сборки Нахиды"
menu_yaoyao="Варианты сборки Яо Яо"
menu_candace="Варианты сборки Кандакии"

info = '''{builld}\n
_______________________________\n
Сэты: {set}\n
_______________________________\n
Цветок: {flower}\n
Перо: {feather}\n
Часы: {watches}\n
Кубок: {cup}\n
Корона: {crown}\n
_______________________________\n
Оружие: {weapon}\n
_______________________________\n
Ориентировачные значения: {maybe}'''