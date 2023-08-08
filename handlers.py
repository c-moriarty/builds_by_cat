from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

from aiogram import flags
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery
from states import Gen

import kb
import text
import states

from openpyxl import load_workbook

router = Router()
db = load_workbook('./gen.xlsx')
sheet = db.get_sheet_by_name('Sheet1')


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "menu")
async def menu(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "anemo")
async def menu_anemo(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_anemo, reply_markup=kb.menu_anemo)

@router.callback_query(F.data == "pyro")
async def menu_pyro(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_pyro, reply_markup=kb.menu_pyro)

@router.callback_query(F.data == "cryo")
async def menu_cryo(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_cryo, reply_markup=kb.menu_cryo)

@router.callback_query(F.data == "geo")
async def menu_anemo(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_geo, reply_markup=kb.menu_geo)

@router.callback_query(F.data == "electro")
async def menu_geo(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_electro, reply_markup=kb.menu_electro)

@router.callback_query(F.data == "dendro")
async def menu_dendro(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_dendro, reply_markup=kb.menu_dendro)

@router.callback_query(F.data == "hydro")
async def menu_hydro(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_hydro, reply_markup=kb.menu_hydro)

@router.callback_query(F.data == "back")
async def back(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu, reply_markup=kb.menu)
#Anemo
@router.callback_query(F.data == "kazuha")
async def menu_kazuha(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_kazuha, reply_markup=kb.menu_kazuha)

@router.callback_query(F.data == "kazuha_ms")
async def menu_kazuha(clbck: CallbackQuery, state: FSMContext):
    argument = 2
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)
@router.callback_query(F.data == "kazuha_krit")
async def menu_kazuha(clbck: CallbackQuery, state: FSMContext):
    argument = 3
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)

@router.callback_query(F.data == "faruzan")
async def menu_faruzan(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_faruzan, reply_markup=kb.menu_faruzan)

@router.callback_query(F.data == "faruzan_sup")
async def menu_faruzan(clbck: CallbackQuery, state: FSMContext):
    argument = 4
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)
@router.callback_query(F.data == "faruzan_dd")
async def menu_faruzan(clbck: CallbackQuery, state: FSMContext):
    argument = 5
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)

@router.callback_query(F.data == "heizou")
async def menu_heizou(clbck: CallbackQuery, state: FSMContext):
    argument = 6
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)

@router.callback_query(F.data == "venti")
async def menu_venti(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_venti, reply_markup=kb.menu_venti)

@router.callback_query(F.data == "venti_ms")
async def menu_venti(clbck: CallbackQuery, state: FSMContext):
    argument = 7
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)
@router.callback_query(F.data == "venti_krit")
async def menu_venti(clbck: CallbackQuery, state: FSMContext):
    argument = 8
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)

@router.callback_query(F.data == "wanderer")
async def menu_wanderer(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_wanderer, reply_markup=kb.menu_wanderer)

@router.callback_query(F.data == "wanderer_driver")
async def menu_wanderer(clbck: CallbackQuery, state: FSMContext):
    argument = 9
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)

@router.callback_query(F.data == "wanderer_dps")
async def menu_wanderer(clbck: CallbackQuery, state: FSMContext):
    argument = 10
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)

@router.callback_query(F.data == "jean")
async def menu_jean(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_jean, reply_markup=kb.menu_jean)

@router.callback_query(F.data == "jean_dd")
async def menu_jean(clbck: CallbackQuery, state: FSMContext):
    argument = 11
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)

@router.callback_query(F.data == "jean_sup")
async def menu_jean(clbck: CallbackQuery, state: FSMContext):
    argument = 12
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)

@router.callback_query(F.data == "sayu")
async def menu_sayu(clbck: CallbackQuery, state: FSMContext):
    argument = 13
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)

@router.callback_query(F.data == "xiao")
async def menu_xiao(clbck: CallbackQuery, state: FSMContext):
    argument = 14
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)

@router.callback_query(F.data == "bennett")
async def menu_bennett(clbck: CallbackQuery, state: FSMContext):
    argument = 17
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)

@router.callback_query(F.data == "xiangling")
async def menu_xiangling(clbck: CallbackQuery, state: FSMContext):
    argument = 18
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)

@router.callback_query(F.data == "hu_tao")
async def menu_hu_tao(clbck: CallbackQuery, state: FSMContext):
    argument = 19
    await clbck.message.answer(text.info.format(builld = sheet.cell(row=argument, column=2).value, set = sheet.cell(row=argument, column=3).value, flower = sheet.cell(row=argument, column=4).value, feather = sheet.cell(row=argument, column=5).value, watches = sheet.cell(row=argument, column=6).value, cup = sheet.cell(row=argument, column=7).value, crown = sheet.cell(row=argument, column=8).value, weapon= sheet.cell(row=argument, column=9).value, maybe= sheet.cell(row=argument, column=10).value), reply_markup=kb.back)
