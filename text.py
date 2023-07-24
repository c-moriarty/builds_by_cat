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
menu_faruzan="Варианты сборки Фарузан"
menu_venti="Варианты сборки Венти"


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