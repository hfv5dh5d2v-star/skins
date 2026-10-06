from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from tools.keybuttons import reply_buttons, inline_buttons

router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Привет! Я бот для помощи.", reply_markup = reply_buttons)
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

@router.message(Command('docs'))
async def cmd_docs(message: Message):
    await message.answer(f'Выбери язык, чтобы перейти к официальной документации:', reply_markup = inline_buttons)

@router.message(F.text == 'Python')
async def cmd_python(message: Message):
    await message.answer('Python - это высокоуровневый язык ' \
    'программирования с простым и понятным синтаксисом. Широко ' \
    'используется в веб-разработке, анализе данных, искусственном ' \
    'интеллекте, автоматизации и создании Telegram-ботов.')

@router.message(F.text == 'JavaScript')
async def cmd_javascript(message: Message):
    await message.answer('JavaScript - это главный язык веб-разработки, ' \
    'который исполняется прямо в браузере. Позволяет создавать ' \
    'интерактивные веб-страницы, а с помощью платформы Node.js ' \
    'используется и для написания серверной части приложений (backend). ')

@router.message(F.text == 'Java')
async def cmd_java(message: Message):
    await message.answer('Java - это строго типизированный о' \
    'бъектно-ориентированный язык программирования. ' \
    'Известен принципом «напиши один раз, запускай где угодно» '
    '(благодаря JVM). Активно используется в корпоративной разработке, ' \
    'банках и создании Android-приложений. ')

    
@router.message()
async def echo(message: Message):
    await message.answer(f'Ты написал: {message.text}')