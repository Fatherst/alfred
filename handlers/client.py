from create_bot import bot, dp
from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.kb_client import get_kb_start, get_kb_drevrus, get_test, get_test1  # , courses_inline, coulinary_inline
from database import mysql_db

# from database.mysql_db import my_sql_start


# async def set_default_commands(dp):
#    await dp.bot.set_my_commands(
#        [
#            types.BotCommand("start", "Запустить бота"),
#            types.BotCommand("help", "Вывести справку"),
#            types.BotCommand("onstarttest", "Пройти первый опрос"),
#        ]
#    )

count = 0


# async def hello(message:types.Message):
#    if message.from_user.id != :
#        await bot.send_message(message.from_user.id, text='Привет! Напиши /start,чтобы начать изучать историю со мной!')

async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text='Привет\nВы пользуетесь ботом по истории. Наш бот предназначен для изучения истории. Что бы вы хотели?',
                           reply_markup=get_kb_start())


async def test_buttons(message: types.Message):
    await bot.send_message(message.from_user.id, text='К какому году относится крещение Руси?', reply_markup=get_test())
    #await bot.edit_message_reply_markup(message.chat.id, reply_markup=get_test1())

async def test_test(callback:types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, text='К какому году относится крещение Руси?', reply_markup=get_test1())
    await bot.edit_message_reply_markup(callback.message.chat.id, reply_markup=get_test1())
class TestStatesGroup(StatesGroup):
    waiting = State()
    answer = State()


async def drevnerus_test_kresh(call):
    await TestStatesGroup.waiting.set()
    # await callback.message.answer('К какому году относится крещение Руси?', reply_markup=get_kb_drevrus())
    await bot.send_poll(chat_id=call.message.chat.id, question='К какому году относится крещение Руси?',
                        options=['882 г.', '988 г.', '945 г.', '962 г.'], type='quiz', correct_option_id=1,
                        is_anonymous=False)


async def handle_answer(quiz_answer: types.PollAnswer):
    global count
    if count == 0:
        await bot.send_poll(quiz_answer.user.id, question='Летописный свод Древней Руси XII века – это ',
                            options=[' «Русская правда»', '«Апостол» ', '«Домострой» ', '«Повесть временных лет» '],
                            type='quiz', correct_option_id=3,
                            is_anonymous=False)
        count = count + 1
    elif count == 1:
        await bot.send_poll(quiz_answer.user.id, question='К памятникам зодчества Древней Руси IX – XI вв. относится',
                            options=['Храм Василия Блаженного в Москве', 'Храм Святой Софии в Новгороде ',
                                     'Церковь Вознесения в селе Коломенском ', 'Троице-Сергиев монастырь '],
                            type='quiz', correct_option_id=1,
                            is_anonymous=False)
        count += 1
    elif count == 2:
        await bot.send_poll(quiz_answer.user.id, question='Какой из названных памятников был построен в XII в.?',
                            options=['Церковь Покрова на Нерли', 'Архангельский собор Московского Кремля',
                                     'Покровский собор (храм Василия Блаженного) в Москве',
                                     'Церковь Вознесения в селе Коломенском'],
                            type='quiz', correct_option_id=0,
                            is_anonymous=False)
        count += 1
    elif count == 3:
        await bot.send_poll(quiz_answer.user.id,
                            question='Какое произведение древнерусской литературы повествует о неудачном походе новгород-северского князя против половцев?',
                            options=['«Повесть временных лет» XII век', '«Слово о Законе и Благодати» XI век',
                                     '«Слово о полку Игореве» XII век ',
                                     '«Сказание о Мамаевом побоище» XIV век'],
                            type='quiz', correct_option_id=2,
                            is_anonymous=False)
        count += 1
    elif count == 4:
        await bot.send_poll(quiz_answer.user.id,
                            question='Какое из названных литературных произведений было создано в XII в.?',
                            options=['«Домострой»', '«Апостол»',
                                     '«Поучение детям»',
                                     '«Задонщина»'],
                            type='quiz', correct_option_id=2,
                            is_anonymous=False)
        count += 1
    elif count == 5:
        await bot.send_poll(quiz_answer.user.id,
                            question='В каком веке Русь приняла христианство как государственную религию?',
                            options=['VI в.', 'VII в.',
                                     'VIII в.',
                                     'X в.'],
                            type='quiz', correct_option_id=3,
                            is_anonymous=False)
        count += 1
    elif count == 6:
        await bot.send_poll(quiz_answer.user.id,
                            question='Каким годом летописи датируют призвание варягов на Русь?',
                            options=['862 г.', '988 г.',
                                     '1097 г.',
                                     '1111 г.'],
                            type='quiz', correct_option_id=0,
                            is_anonymous=False)
        count += 1
    elif count == 7:
        await bot.send_poll(quiz_answer.user.id,
                            question='Так не посрамим земли Русской, но ляжем здесь костьми, ибо мертвые сраму не имут…» – эти слова летописец связывает с походами в 970-971 гг. древнерусского князя ',
                            options=['Олега', 'Игоря',
                                     'Святослава',
                                     'Рюрика'],
                            type='quiz', correct_option_id=2,
                            is_anonymous=False)
        count += 1
    elif count == 8:
        await bot.send_poll(quiz_answer.user.id,
                            question='Кто из названных князей Древней Руси правил с 879 по 912 гг.?',
                            options=['Владимир Красное Солнышко', 'Александр Невский',
                                     'Олег Вещий',
                                     'Владимир Мономах'],
                            type='quiz', correct_option_id=2,
                            is_anonymous=False)
        count += 1
    elif count == 9:
        await bot.send_poll(quiz_answer.user.id,
                            question='Имя летописца Нестора связано с ',
                            options=['VIII в.', 'IX в.',
                                     'XII в.',
                                     'XIII в.'],
                            type='quiz', correct_option_id=2,
                            is_anonymous=False)
        count += 1
    elif count == 10:
        await bot.send_poll(quiz_answer.user.id,
                            question='Как назывался свод древнерусских законов XI – XII вв.? ',
                            options=['«Русская правда»', '«Судебник» ',
                                     '«Соборное Уложение»',
                                     '«Стоглав»'],
                            type='quiz', correct_option_id=0,
                            is_anonymous=False)
        count += 1
    elif count == 11:
        await bot.send_poll(quiz_answer.user.id,
                            question='С именем какого князя связаны расцвет Древнерусского государства, установление династических связей с европейскими и византийским дворами в XI веке?',
                            options=['Святослава Игоревича', 'Ярослава Мудрого ',
                                     'Ивана Калиты',
                                     'Олега Вещего'],
                            type='quiz', correct_option_id=1,
                            is_anonymous=False)
        count += 1
    elif count == 12:
        await bot.send_poll(quiz_answer.user.id,
                            question='Княжение Ярослава Мудрого относится к ',
                            options=['X в.', 'XI в.',
                                     'XIII в.',
                                     'XV в.'],
                            type='quiz', correct_option_id=1,
                            is_anonymous=False)
        count += 1
    elif count == 13:
        await bot.send_poll(quiz_answer.user.id,
                            question='Какой из памятников древнерусского зодчества связан с княжением Ярослава Мудрого (1015-1054)?',
                            options=['Успенский собор во Владимире', 'Софийский собор в Киеве',
                                     'Храм Покрова Богородицы на Нерли',
                                     'Дмитриевский собор во Владимире'],
                            type='quiz', correct_option_id=1,
                            is_anonymous=False)
        count += 1
    elif count == 14:
        await bot.send_poll(quiz_answer.user.id,
                            question='Что из перечисленного относится к результатам правления древнерусского князя Олега (879-912)?',
                            options=['Объединение Киева и Новгорода', 'Принятие Русью христианства',
                                     'Подавление восстания древлян',
                                     'Принятие Русской Правды'],
                            type='quiz', correct_option_id=0,
                            is_anonymous=False)
        count += 1
    elif count == 15:
        await bot.send_poll(quiz_answer.user.id,
                            question='Как назывался общерусский летописный свод XII века, содержавший сведения о жизни славян и их соседей в древности?',
                            options=['«Поучение детям»', 'Русская Правда',
                                     '«Повесть временных лет»',
                                     'Соборное уложение'],
                            type='quiz', correct_option_id=2,
                            is_anonymous=False)
        count += 1

    elif count == 16:
        await bot.send_poll(quiz_answer.user.id,
                            question='В  XII веке после  победы над печенегами Ярослав Мудрый повелел построить  ',
                            options=['Успенский собор во Владимире', 'Десятинную церковь в Киеве',
                                     'Софийский собор в Киеве',
                                     'церковь Покрова на Нерли'],
                            type='quiz', correct_option_id=3,
                            is_anonymous=False)
        count += 1
    elif count == 17:
        await bot.send_poll(quiz_answer.user.id,
                            question='В создании законов Древней Руси XI-XII веков принимали участие',
                            options=['Ярослав Мудрый и Владимир Мономах', 'Рюрик и его братья',
                                     'Олег и Игорь',
                                     'Святослав и Святополк'],
                            type='quiz', correct_option_id=0,
                            is_anonymous=False)
        count += 1
    elif count == 18:
        await bot.send_poll(quiz_answer.user.id,
                            question='К какому году летописи относят «призвание варягов» на Русь?',
                            options=['862 г.', '988 г.',
                                     '1054 г.',
                                     '1062 г.'],
                            type='quiz', correct_option_id=0,
                            is_anonymous=False)
        count += 1
    elif count == 19:
        await bot.send_poll(quiz_answer.user.id,
                            question='Слово о полку Игореве» – памятник литературы',
                            options=['X в.', 'XI в.',
                                     'XII в.',
                                     'XIII в.'],
                            type='quiz', correct_option_id=2,
                            is_anonymous=False)
        count += 1
    elif count == 20:
        await bot.send_poll(quiz_answer.user.id,
                            question='В X веке первая часть Русской Правды была составлена во время  правления киевского князя',
                            options=['Олега Вещего', 'Владимира Святославича',
                                     'Ярослава Мудрого',
                                     'Владимира Мономаха'],
                            type='quiz', correct_option_id=2,
                            is_anonymous=False)
        count += 1
    elif count == 21:
        await bot.send_poll(quiz_answer.user.id,
                            question='Кто из перечисленных князей правил позже остальных?',
                            options=['Владимир Мономах', 'Ярослав Мудрый',
                                     'Олег Вещий',
                                     'Игорь Старый'],
                            type='quiz', correct_option_id=0,
                            is_anonymous=False)
        count += 1
    elif count == 22:
        await bot.send_poll(quiz_answer.user.id,
                            question='Ко времени правления Владимира Святославича (980-1015) относится',
                            options=['Начало создания Русской Правды', 'Принятие Русью христианства',
                                     'Объединение Киева и Новгорода под властью одного князя',
                                     'Разгром Хазарского каганата'],
                            type='quiz', correct_option_id=1,
                            is_anonymous=False)
        count += 1
    elif count == 23:
        await bot.send_poll(quiz_answer.user.id,
                            question='Раньше других правил в Киеве',
                            options=['Владимир Святославич', 'Олег Вещий',
                                     'Святослав Игоревич',
                                     'Ярослав Мудрый'],
                            type='quiz', correct_option_id=1,
                            is_anonymous=False)
        count += 1
    elif count == 24:
        await bot.send_poll(quiz_answer.user.id,
                            question='Какой из перечисленных памятников архитектуры был построен в XII в.?',
                            options=['Успенский собор во Владимире', 'Архангельский собор Московского Кремля',
                                     'Покровский собор что на Рву (храм Василия Блаженного) в Москве',
                                     'Церковь Покрова в Филях'],
                            type='quiz', correct_option_id=0,
                            is_anonymous=False)
        count += 1
    elif count == 25:
        await bot.send_poll(quiz_answer.user.id,
                            question='Какое из литературных произведений было создано раньше других?',
                            options=['«Домострой»', '«Повесть временных лет»',
                                     '«Слово о полку Игореве»',
                                     '«Задонщина»'],
                            type='quiz', correct_option_id=1,
                            is_anonymous=False)
        count += 1
    elif count == 26:
        await bot.send_poll(quiz_answer.user.id,
                            question='К итогам походов древнерусского князя Святослава в 964 году относится ',
                            options=['Разгром Хазарского каганата', 'Покорение половцев',
                                     'Объединение Киева и Новгорода под единой княжеской властью',
                                     'Разгром печенегов'],
                            type='quiz', correct_option_id=0,
                            is_anonymous=False)
        count += 1
    elif count == 27:
        await bot.send_poll(quiz_answer.user.id,
                            question='Какое событие произошло в период правления киевского князя Ярослава Мудрого (1015-1054)?',
                            options=['Начало составления первого письменного свода законов', 'Крещение Руси',
                                     'Созыв первого Земского собора',
                                     'Первое столкновение русского войска с монгольским войском'],
                            type='quiz', correct_option_id=0,
                            is_anonymous=False)
        count += 1
    elif count == 28:
        await bot.send_poll(quiz_answer.user.id,
                            question='Кто из перечисленных князей правил раньше других?',
                            options=['Дмитрий Донской', 'Ярослав Мудрый',
                                     'Юрий Долгорукий',
                                     'Владимир Святославич'],
                            type='quiz', correct_option_id=3,
                            is_anonymous=False)
        count += 1
    elif count == 29:
        await bot.send_poll(quiz_answer.user.id,
                            question='Расположите в хронологической последовательности исторические события. Запишите цифры, которыми обозначены исторические события, в правильной последовательности в таблицу.',
                            options=['Крещение Руси', 'Учреждение Государственного совета Российской империи',
                                     'Начало деятельности Долгого парламента в Англии'],
                            type='quiz', correct_option_id=0,
                            is_anonymous=False)
        count += 1
# def get_cancel():

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(test_buttons, commands=['test'])
    # dp.register_message_handler(hello)
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(drevnerus_test_kresh, text='1', state=None)
    # dp.register_callback_query_handler()
    dp.register_poll_answer_handler(handle_answer)
    dp.register_callback_query_handler(test_test, text='1')
