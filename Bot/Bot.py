from vkbottle import Bot, Keyboard, KeyboardButtonColor, Text
from vkbottle.bot import Message
from config import VK_group_token



bot = Bot(VK_group_token)

vk_session = vk_api.VkApi(token=VK_group_token)
vk = vk_session.get_api()

print("Бот запущен...")

# Инлайн клавиатура для добавления лайка на фото.
keyboard_inline = Keyboard(one_time=True, inline=True)
keyboard_inline.add(Text('Убрать лайк👎'), color=KeyboardButtonColor.NEGATIVE)
keyboard_inline.add(Text('Лайк👍'), color=KeyboardButtonColor.POSITIVE)

# Основная клавиатура для работы взаимодействия с пользователем
keyboard_main = Keyboard(one_time=False, inline=False)
keyboard_main.add(Text('В избранное✏️'))
keyboard_main.add(Text('Дальше➡️'))
keyboard_main.row()
keyboard_main.add(Text('В черный список❌'))
keyboard_main.add(Text('Список избранных'))
keyboard_main.row()
keyboard_main.add(Text('Сменить токен VK'))

class Commands:

    start = ['начать', 'start']
    search_dating = ['Поехали🚀', 'Дальше➡️']
    blacklist = ['В черный список❌']
    favorites = ['В избранное✏️']
    like = ['Лайк👍']
    dislike = ['Убрать лайк👎']
    all_favorites = ['Список избранных']
    change_token = ['Сменить токен VK']


@bot.on.message(func=lambda message: message.text.lower() in Commands.start)
async def start(message: Message):
    """Функция запуска бота"""

    keyboard_start = Keyboard(one_time=True, inline=False)
    keyboard_start.add(Text('Поехали🚀'))
    user_id = message.from_id
    user_info = await bot.api.users.get(user_ids=user_id)
    text = (f'Привет, {user_info[0].first_name}!👋\nЯ бот для поиска новых знакомств💑\n'
            'Жми на кнопку ниже и давай начинать!\n'
            'Для улучшения возможностей бота, а именно:\n'
            '- видеть общих друзей,\n'
            '- возможность ставить и убирать лайки на фото,\n'
            'добавь свой пользовательский токен VK, просто скопировав его в чат.')
    await message.answer(text, keyboard=keyboard_start)


@bot.on.message(func=lambda message: message.text in Commands.search_dating)
async def search_dating(message: Message):
    """Функция поиска новых людей"""

    await message.answer(f'Здесь я вывожу нового человека', keyboard=keyboard_main)


@bot.on.message(func=lambda message: message.text in Commands.blacklist)
async def add_blacklist(message: Message):
    """Функция добавления человека в черный список"""

    await message.answer(f'Здесь я добавляю человека в черный список')


@bot.on.message(func=lambda message: message.text in Commands.favorites)
async def add_favorites(message: Message):
    """Функция человека добавления в избранные"""

    await message.answer(f'Здесь я добавляю человека в избранные')


@bot.on.message(func=lambda message: message.text in Commands.like)
async def like(message: Message):
    """Функция ставит лайк на фото"""

    await message.answer(f'Здесь я ставлю лайк')


@bot.on.message(func=lambda message: message.text in Commands.dislike)
async def dislike(message: Message):
    """Функция убирает лайк с фото"""

    await message.answer(f'Здесь я убираю лайк')


@bot.on.message(func=lambda message: message.text in Commands.all_favorites)
async def all_favorites(message: Message):
    """Функция выводит список все людей добавленных в избранное"""

    await message.answer(f'Здесь вывожу всех избранных')


@bot.on.message(func=lambda message: message.text in Commands.change_token)
async def change_token(message: Message):
    """Функция смены токена пользователя"""

    await message.answer(f'Здесь я удаляю старый и жду новый токен.')

@bot.on.message()
async def change_token(message: Message):
    """Ловит остальные сообщения от пользователя"""

    await message.answer(f'Не понял команды😕\nИспользуй кнопки из меню:')

bot.run_forever()
