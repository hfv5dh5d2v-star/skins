from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Привет! Я бот для помощи.")
    print(f'{message.from_user.id} - {message.from_user.username} - {message.from_user.first_name} - {message.from_user.last_name}')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f'/start - начать работу с ботом \n /help - помощь для ориентации')

@router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer(f'этот бот создан для помощи в регистрации на тестовом задании')

@router.message(F.text.lower() == 'пока')
async def cmd_bye(message: Message):
    await message.answer(f'До свидания!')

@router.message()
async def echo(message: Message):
    await message.answer(f'Ты написал: {message.text}')