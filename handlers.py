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

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.message(F.text == "Анемо")
@router.message(F.text == "анемо")
@router.callback_query(F.data == "anemo")
async def menu_anemo(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_anemo, reply_markup=kb.menu_anemo)

@router.message(F.text == "Пиро")
@router.message(F.text == "пиро")
@router.callback_query(F.data == "pyro")
async def menu_anemo(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.menu_pyro, reply_markup=kb.menu_pyro)