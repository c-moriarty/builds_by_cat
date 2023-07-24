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
kazuha_ms='''Артефакты:\n\nЦветок: HP, в доп. статах МС и восстановление энергии %\n
Перо: сила атаки, в доп. статах МС и восстановление энергии %\nЧасы:МС, в доп. статах 
восстановление энергии %, шанс крита\nКубоок: МС, в доп. статах восстановление энергии %, 
шанс крита\nШапка: МС/Шанск крита %, в доп статах МС, шанс крита %, восстановление энергии %'''

def information(argument):
    set = sheet.cell(row=argument, column=3).value
    flower = sheet.cell(row=argument, column=4).value
    info = '''Сэты: {set}\n\n
      Цветок: {flower}\n\n
      Перо:'''