from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from tools.keybuttons import reply_buttons, inline_buttons, questions_buttons
from tools.questions import QUESTIONS

router = Router()

class StartTest(StatesGroup):
    waiting_answer = State()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Привет! Я бот для помощи.", reply_markup = reply_buttons)
    print(f'{message.from_user.id} - {message.from_user.username} - {message.from_user.first_name} - {message.from_user.last_name}')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f'/start - начать работу с ботом \n /help - помощь для ориентации', reply_markup = questions_buttons)

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


@router.callback_query(F.data == "start_test")
async def start_test(callback: CallbackQuery, state: FSMContext):
    await callback.answer()


    await state.update_data(questions=QUESTIONS, index=0, score=0)
    await state.set_state(StartTest.waiting_answer)

    await callback.message.answer(f"Вопрос 1: {QUESTIONS[0]['q']}")



@router.message(StartTest.waiting_answer)
async def user_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    questions = data["questions"]
    index = data["index"]
    score = data["score"]

    q = questions[index]

    is_correct = message.text.strip().lower() == q["a"].strip().lower()
    

    if is_correct:
        score += 1
        await message.answer("Правильно, +1")
    else:
        await message.answer(f"Неверно. Правильный ответ: {q["a"]}")



    index += 1
    if index == len(questions):
        await message.answer(f"Конец! Счет: {score}/{len(questions)} \n хочешь пройти тест заново?", reply_markup = questions_buttons)
        await state.clear()
    else:
        await state.update_data(index=index, score=score)
        await message.answer(f"Вопрос {index + 1}: {questions[index]["q"]}")
        
    
@router.message()
async def echo(message: Message):
    await message.answer(f'Ты написал: {message.text}')