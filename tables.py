from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from bot import dp

class FSMAdmin(StatesGroup):
    photo = State()
    group = State()
    name = State()
    price = State()

# @dp.message_handlers(commands="update", state=None)
async def update_product(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузите фото')


# @dp.message_handlers(content_types=["photo"], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Дальше: введите класс продукта")

# @dp.message_handlers(state=FSMAdmin.group)
async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await FSMAdmin.next()
    await message.reply("Дальше: введите название продукта")

# @dp.message_handlers(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await FSMAdmin.next()
    await message.reply("Дальше: укажите цену продукта")

# @dp.message_handlers(state = FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["price"] = float(message.text)

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(update_product, commands="update", state=None)
    dp.register_message_handler(load_photo, content_types=["photo"], state=FSMAdmin.photo)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_price, state=FSMAdmin.price)