from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from django_bot.models import TelegramUser
import menu as menu

from dotenv import load_dotenv, find_dotenv
from environs import Env
import logging

from asgiref.sync import sync_to_async

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from django.core.management.base import BaseCommand


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

env = Env()
load_dotenv(find_dotenv())
bot = Bot(token=env.str('TELEGRAMBOT_KEY'))
storage = MemoryStorage()  # For example use simple MemoryStorage for Dispatcher.
dp = Dispatcher(bot, storage=storage)


class FormDataUserSetStatus(StatesGroup):
    user_id = State()
    user_type = State()


async def aget_or_create(self, **kwargs):
    return await sync_to_async(self.get_or_create)(**kwargs)

# ============================================================================================================================================================================================================================
@dp.message_handler(CommandStart())
async def command_start(message: types.Message):
    # await bot.send_message(message.from_user.id, "---", reply_markup=menu.main_menu)
    # т.е. если первый раз - заносим в БД
    telegram_user, new_user = await TelegramUser.objects.aget_or_create(chat_id=message.from_user.id)
    user = str(await sync_to_async(telegram_user.get_user)())

    if not new_user:
        logging.info("user есть в БД")
        await bot.send_message(message.from_user.id, "Зареган в БД !\n"+user, reply_markup=menu.main_menu)
    else:
        logging.info("New user")
        await bot.send_message(message.from_user.id, "Новый Зареган в БД !\nТут можно сразу выдать не рабочее меню, а меню настроек\n"+user, reply_markup=menu.main_menu)


# ============================================================================================================================================================================================================================
@dp.message_handler(commands=['help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, "!", reply_markup=menu.supportUserMenu)


# ============================================================================================================================================================================================================================
@dp.message_handler(state='*', commands='stop')  # You can use state '*' if you need to handle all states
@dp.message_handler(Text(equals='stop', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Операция прервана 🆑', reply_markup=menu.StartHelpUserMenu)


# ============================================================================================================================================================================================================================
@dp.message_handler()
async def bot_message(message: types.Message):
    print(message.text)
    # if (getUserInfo(message.from_user.id) == ""):  # баг
    #         "Внимание ⁉\n⚠ Для правильной работы бота вам необходимо в меню (вверху справа) очистить историю и запустить бота заново !\n⚠ Иначе корректная работа - не гарантируется 😱",

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if message.text == 'Готовые торты 🍰':
        await bot.send_message(message.from_user.id,'😋',
                               reply_markup=menu.ReadyCakeRoot)

    if message.text == 'О нас ...':
        await bot.send_message(message.from_user.id,'😎\nМега-крутой бот оформления заказов на тортики...')

    if message.text == 'Ванильные':
        await bot.send_message(message.from_user.id, 'Ванильные торты',  reply_markup=menu.ReadyCakeVanila)

    if message.text == 'Шоколадные':
        await bot.send_message(message.from_user.id, 'Шоколадные торты\n🚧 в разработке...')

    if message.text == 'Ягодные':
        await bot.send_message(message.from_user.id,'Ягодные торты\n🚧 в разработке...')

    if message.text == 'От шефа':
        await bot.send_message(message.from_user.id,'От шефа торты\n🚧 в разработке...')

    if message.text == 'Ванильная мечта':
        await bot.send_message(message.from_user.id,'Тут обработка добавления в корзину - 🚧 в разработке...')

    if message.text == 'Ванилька-манилька':
        await bot.send_message(message.from_user.id,'Тут обработка добавления в корзину - 🚧 в разработке...')

    if message.text == 'Леди Ваниль':
        await bot.send_message(message.from_user.id,'Тут обработка добавления в корзину - 🚧 в разработке...')

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif message.text == '📰 Главное меню':
        await bot.send_message(message.from_user.id, '🥮', reply_markup=menu.main_menu)

    elif message.text == 'Корзина':
        await bot.send_message(message.from_user.id, '🛒',
                               reply_markup=menu.btnMenuBasket)

    elif message.text == 'Посмотреть корзину':
        await bot.send_message(message.from_user.id, 'Тут - показать что в корзине из БД')

    elif message.text == 'Очистить корзину':
        await bot.send_message(message.from_user.id, 'Тут - очистить что в корзине из БД')

    elif message.text == 'Оформить заказ':
        await bot.send_message(message.from_user.id, 'Тут - Оформить заказ из БД\nЕсли не указаны настройки по умолчанию-адресовать в меню настройки')

    elif message.text == 'Конструктор тортов 🏗':
        await bot.send_message(message.from_user.id, 'Уже скоро\n🚧 в разработке...')

    elif message.text == 'Мои настройки ⚙️':
        await bot.send_message(message.from_user.id, 'Уже скоро\n🚧 в разработке...')

    else:
        await bot.send_message(message.from_user.id, "\n", reply_markup=types.ReplyKeyboardRemove())


class Command(BaseCommand): # Название класса обязательно - "Command"
  	# Используется как описание команды обычно
    help = 'Implemented to Django application telegram bot setup command'
    def handle(self, *args, **kwargs):
        executor.start_polling(dp, skip_updates=False)