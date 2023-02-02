from create_bot import bot, dp
from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.kb_client import get_kb_start, get_kb_drevrus, get_test, get_test1, \
    get_main  # , courses_inline, coulinary_inline
from database import mysql_db
from amplitude import *


# from database.mysql_db import my_sql_start


# async def set_default_commands(dp):
#    await dp.bot.set_my_commands(
#        [
#            types.BotCommand("start", "Запустить бота"),
#            types.BotCommand("help", "Вывести справку"),
#            types.BotCommand("onstarttest", "Пройти первый опрос"),
#        ]
#    )


# async def hello(message:types.Message):
#    if message.from_user.id != :
#        await bot.send_message(message.from_user.id, text='Привет! Напиши /start,чтобы начать изучать историю со мной!')


async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text='Привет\nТы пользуешься ботом по истории, меня зовут Альфред! В этом боте можно проходить тесты по истории, но скоро можно будет и поговорить с историческими личностями!\n Что бы ты хотел?',
                           reply_markup=get_kb_start())
    client = Amplitude('0aaff2f3e9d6bf83dffa4d85f7eb876e')
    event = BaseEvent(event_type="/start нажат",
                      user_id=f"Юзернейм:{message.from_user.username}, ID:{message.from_user.id}")
    client.track(event)


async def start_callback(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id,
                           text='Привет\nТы пользуешься ботом по истории, меня зовут Альфред! В этом боте можно проходить тесты по истории, но скоро можно будет и поговорить с историческими личностями!\n Что бы ты хотел?',
                           reply_markup=get_kb_start())


async def test_buttons(message: types.Message):
    await bot.send_message(message.from_user.id, text='К какому году относится крещение Руси?', reply_markup=get_test())
    # await bot.edit_message_reply_markup(message.chat.id, reply_markup=get_test1())


async def test_test(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, text='К какому году относится крещение Руси?',
                           reply_markup=get_test1())
    await bot.edit_message_reply_markup(callback.message.chat.id, reply_markup=get_test1())


class TestStatesGroup(StatesGroup):
    waiting = State()
    answer = State()


class UdStatesGroup(StatesGroup):
    waiting = State()
    answer = State()


count = 0
count_ud = 31
count_tatari = 0
count_moscow = 0
test_count = 0
count_vozvish = 0
count_groz = 0
count_smuta = 0
count_bunt = 0
test_passed = False
rights = 0


async def drevnerus_test_kresh(callback: types.CallbackQuery):
    await TestStatesGroup.waiting.set()
    await bot.send_poll(chat_id=callback.message.chat.id, question='К какому году относится крещение Руси?',
                        options=['882 г.', '988 г.', '945 г.', '962 г.'], type='quiz', correct_option_id=1,
                        is_anonymous=False)
    global test_count
    test_count = 0


async def handle_answer(quiz_answer: types.PollAnswer):
    global count_ud, count, test_count, test_passed, rights, count_tatari, count_moscow, count_vozvish, count_groz, count_smuta, count_bunt
    client = Amplitude('0aaff2f3e9d6bf83dffa4d85f7eb876e')
    event = BaseEvent(event_type="Тест пройден дальше первого вопроса",
                      user_id=f"Юзернейм:{quiz_answer.user.username}, ID:{quiz_answer.user.id}")
    client.track(event)
    # count = 0
    # count_ud = 31
    if test_passed == False:
        if test_count == 0:
            if count == 0:
                await bot.send_poll(quiz_answer.user.id, question='Летописный свод Древней Руси XII века – это ',
                                    options=[' «Русская правда»', '«Апостол» ', '«Домострой» ',
                                             '«Повесть временных лет» '],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count == 1:
                await bot.send_poll(quiz_answer.user.id,
                                    question='К памятникам зодчества Древней Руси IX – XI вв. относится',
                                    options=['Храм Василия Блаженного в Москве', 'Храм Святой Софии в Новгороде ',
                                             'Церковь Вознесения в селе Коломенском ', 'Троице-Сергиев монастырь '],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [3]:
                    rights += 1
                count += 1
            elif count == 2:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какой из названных памятников был построен в XII в.?',
                                    options=['Церковь Покрова на Нерли', 'Архангельский собор Московского Кремля',
                                             'Покровский собор (храм Василия Блаженного) в Москве',
                                             'Церковь Вознесения в селе Коломенском'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [1]:
                    rights += 1
                count += 1
            elif count == 3:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое произведение древнерусской литературы повествует о неудачном походе новгород-северского князя против половцев?',
                                    options=['«Повесть временных лет» XII век', '«Слово о Законе и Благодати» XI век',
                                             '«Слово о полку Игореве» XII век ',
                                             '«Сказание о Мамаевом побоище» XIV век'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [0]:
                    rights += 1
                count += 1
            elif count == 4:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое из названных литературных произведений было создано в XII в.?',
                                    options=['«Домострой»', '«Апостол»',
                                             '«Поучение детям»',
                                             '«Задонщина»'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [2]:
                    rights += 1
                count += 1
            elif count == 5:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком веке Русь приняла христианство как государственную религию?',
                                    options=['VI в.', 'VII в.',
                                             'VIII в.',
                                             'X в.'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [2]:
                    rights += 1
                count += 1
            elif count == 6:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Каким годом летописи датируют призвание варягов на Русь?',
                                    options=['862 г.', '988 г.',
                                             '1097 г.',
                                             '1111 г.'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [3]:
                    rights += 1
                count += 1
            elif count == 7:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Так не посрамим земли Русской, но ляжем здесь костьми, ибо мертвые сраму не имут…» – эти слова летописец связывает с походами в 970-971 гг. древнерусского князя ',
                                    options=['Олега', 'Игоря',
                                             'Святослава',
                                             'Рюрика'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [0]:
                    rights += 1
                count += 1
            elif count == 8:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто из названных князей Древней Руси правил с 879 по 912 гг.?',
                                    options=['Владимир Красное Солнышко', 'Александр Невский',
                                             'Олег Вещий',
                                             'Владимир Мономах'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [2]:
                    rights += 1
                count += 1
            elif count == 9:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Имя летописца Нестора связано с ',
                                    options=['VIII в.', 'IX в.',
                                             'XII в.',
                                             'XIII в.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [2]:
                    rights += 1
                count += 1
            elif count == 10:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Как назывался свод древнерусских законов XI – XII вв.? ',
                                    options=['«Русская правда»', '«Судебник» ',
                                             '«Соборное Уложение»',
                                             '«Стоглав»'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [2]:
                    rights += 1
                count += 1
            elif count == 11:
                await bot.send_poll(quiz_answer.user.id,
                                    question='С именем какого князя связаны расцвет Древнерусского государства, установление династических связей с европейскими и византийским дворами в XI веке?',
                                    options=['Святослава Игоревича', 'Ярослава Мудрого ',
                                             'Ивана Калиты',
                                             'Олега Вещего'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [0]:
                    rights += 1
                count += 1
            elif count == 12:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Княжение Ярослава Мудрого относится к ',
                                    options=['X в.', 'XI в.',
                                             'XIII в.',
                                             'XV в.'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [1]:
                    rights += 1
                count += 1
            elif count == 13:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какой из памятников древнерусского зодчества связан с княжением Ярослава Мудрого (1015-1054)?',
                                    options=['Успенский собор во Владимире', 'Софийский собор в Киеве',
                                             'Храм Покрова Богородицы на Нерли',
                                             'Дмитриевский собор во Владимире'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [1]:
                    rights += 1
                count += 1
            elif count == 14:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что из перечисленного относится к результатам правления древнерусского князя Олега (879-912)?',
                                    options=['Объединение Киева и Новгорода', 'Принятие Русью христианства',
                                             'Подавление восстания древлян',
                                             'Принятие Русской Правды'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [1]:
                    rights += 1
                count += 1
            elif count == 15:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Как назывался общерусский летописный свод XII века, содержавший сведения о жизни славян и их соседей в древности?',
                                    options=['«Поучение детям»', 'Русская Правда',
                                             '«Повесть временных лет»',
                                             'Соборное уложение'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [0]:
                    rights += 1
                count += 1

            elif count == 16:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В  XII веке после  победы над печенегами Ярослав Мудрый повелел построить  ',
                                    options=['Успенский собор во Владимире', 'Десятинную церковь в Киеве',
                                             'Софийский собор в Киеве',
                                             'церковь Покрова на Нерли'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [2]:
                    rights += 1
                count += 1
            elif count == 17:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В создании законов Древней Руси XI-XII веков принимали участие',
                                    options=['Ярослав Мудрый и Владимир Мономах', 'Рюрик и его братья',
                                             'Олег и Игорь',
                                             'Святослав и Святополк'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [3]:
                    rights += 1
                count += 1
            elif count == 18:
                await bot.send_poll(quiz_answer.user.id,
                                    question='К какому году летописи относят «призвание варягов» на Русь?',
                                    options=['862 г.', '988 г.',
                                             '1054 г.',
                                             '1062 г.'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [0]:
                    rights += 1
                count += 1
            elif count == 19:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Слово о полку Игореве» – памятник литературы',
                                    options=['X в.', 'XI в.',
                                             'XII в.',
                                             'XIII в.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [0]:
                    rights += 1
                count += 1
            elif count == 20:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В X веке первая часть Русской Правды была составлена во время  правления киевского князя',
                                    options=['Олега Вещего', 'Владимира Святославича',
                                             'Ярослава Мудрого',
                                             'Владимира Мономаха'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [2]:
                    rights += 1
                count += 1
            elif count == 21:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто из перечисленных князей правил позже остальных?',
                                    options=['Владимир Мономах', 'Ярослав Мудрый',
                                             'Олег Вещий',
                                             'Игорь Старый'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [2]:
                    rights += 1
                count += 1
            elif count == 22:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Ко времени правления Владимира Святославича (980-1015) относится',
                                    options=['Начало создания Русской Правды', 'Принятие Русью христианства',
                                             'Объединение Киева и Новгорода под властью одного князя',
                                             'Разгром Хазарского каганата'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [0]:
                    rights += 1
                count += 1
            elif count == 23:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Раньше других правил в Киеве',
                                    options=['Владимир Святославич', 'Олег Вещий',
                                             'Святослав Игоревич',
                                             'Ярослав Мудрый'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [1]:
                    rights += 1
                count += 1
            elif count == 24:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какой из перечисленных памятников архитектуры был построен в XII в.?',
                                    options=['Успенский собор во Владимире', 'Архангельский собор Московского Кремля',
                                             'Покровский собор что на Рву (храм Василия Блаженного) в Москве',
                                             'Церковь Покрова в Филях'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [1]:
                    rights += 1
                count += 1
            elif count == 25:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое из литературных произведений было создано раньше других?',
                                    options=['«Домострой»', '«Повесть временных лет»',
                                             '«Слово о полку Игореве»',
                                             '«Задонщина»'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [0]:
                    rights += 1
                count += 1
            elif count == 26:
                await bot.send_poll(quiz_answer.user.id,
                                    question='К итогам походов древнерусского князя Святослава в 964 году относится ',
                                    options=['Разгром Хазарского каганата', 'Покорение половцев',
                                             'Объединение Киева и Новгорода под единой княжеской властью',
                                             'Разгром печенегов'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [1]:
                    rights += 1
                count += 1
            elif count == 27:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое событие произошло в период правления киевского князя Ярослава Мудрого (1015-1054)?',
                                    options=['Начало составления первого письменного свода законов', 'Крещение Руси',
                                             'Созыв первого Земского собора',
                                             'Первое столкновение русского войска с монгольским войском'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [0]:
                    rights += 1
                count += 1
            elif count == 28:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто из перечисленных князей правил раньше других?',
                                    options=['Дмитрий Донской', 'Ярослав Мудрый',
                                             'Юрий Долгорукий',
                                             'Владимир Святославич'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [0]:
                    rights += 1
                count += 1
            elif count == 29:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Расположите в хронологической последовательности исторические события. Запишите цифры, которыми обозначены исторические события, в правильной последовательности в таблицу.',
                                    options=['Крещение Руси', 'Учреждение Государственного совета Российской империи',
                                             'Начало деятельности Долгого парламента в Англии'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [3]:
                    rights += 1
                count += 1
                count = 0
                test_count = 0
                test_passed = True
        # "Переключение на тест по удельной руси"#
        elif test_count == 1:
            global count_ud
            if count_ud == 31:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком году, согласно летописям, монголо-татары, возглавляемые ханом Батыем, захватили Рязань?',
                                    options=['1113 г.', '1237 г.', '1380 г.', '1480 г.'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_ud += 1
                print(quiz_answer.option_ids)
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_ud == 32:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что было одной из причин поражения Руси в борьбе с монголами в XIII в.?',
                                    options=['Cоздание военного союза между монголами и немецкими рыцарями',
                                             'Cоюз монголов с половецкими ханами',
                                             'Начало проведения военной реформы в русских землях',
                                             'Военная и политическая разобщённость русских земель'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_ud += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_ud == 33:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какой из названных памятников был построен в XII в.?',
                                    options=['церковь Покрова на Нерли', 'Архангельский собор Московского Кремля',
                                             'Покровский собор (храм Василия Блаженного) в Москве',
                                             'церковь Вознесения в селе Коломенском'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_ud += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_ud == 34:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Первое сражение русских дружин с монголо-татарами произошло в XIII веке на реке',
                                    options=['Калке', 'Воже',
                                             'Угре',
                                             'Неве'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_ud += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_ud == 35:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком веке Древнерусское государство окончательно распалось на удельные княжества, а Киев утратил роль единого центра Руси?',
                                    options=['IX в.', 'X в.',
                                             'XII в.',
                                             'XVI в.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_ud += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_ud == 36:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Отсутствие единства в русском стане и несогласованность во время боевых действий стало причиной поражения русско-половецких войск в битве XIII века на',
                                    options=['реке Калке', 'поле Куликовом',
                                             'реке Угре',
                                             'реке Воже'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_ud += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_ud == 37:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком году князь Юрий Долгорукий послал приглашение своему союзнику: «Прииди ко мне, брате, в Москов», считающееся первым упоминанием о Москве в письменных источниках?',
                                    options=['988 г.', '1147 г.',
                                             '1242 г.',
                                             '1325 г.'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_ud += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_ud == 38:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что из названного было причиной поражения русских войск на реке Калке в 1223 г.?',
                                    options=['вассальная зависимость русских земель от монголов',
                                             'союз монголов с немецкими рыцарями',
                                             'несогласованность в действиях русских князей',
                                             'выступление половцев на стороне монголов'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_ud += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_ud == 39:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое из названных событий произошло раньше других?',
                                    options=[' Невская битва', '«стояние» на реке Угре',
                                             'битва на реке Калке',
                                             'присоединение Новгорода Великого к Москве'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_ud += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_ud == 40:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Слово о полку Игореве» – памятник литературы',
                                    options=['X в.', 'XI в.',
                                             'XII в.',
                                             'XIII в.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_ud += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_ud == 41:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какой из перечисленных памятников архитектуры был построен в XII в.?',
                                    options=['Успенский собор во Владимире', 'Архангельский собор Московского Кремля',
                                             'Покровский собор что на Рву (храм Василия Блаженного) в Москве',
                                             'церковь Покрова в Филях'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                if quiz_answer.option_ids == [2]:
                    rights += 1
                count_ud += 1
                count_ud = 31
                test_count = 1
                test_passed = True
        elif test_count == 2:
            if count_tatari == 0:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое из перечисленных событий произошло раньше всех других?',
                                    options=['Невская битва', 'крещение Руси ',
                                             'присоединение Астраханского ханства к России ', 'Куликовская битва'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_tatari += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_tatari == 1:
                await bot.send_poll(quiz_answer.user.id,
                                    question='С событиями какого века связано имя Александра Невского?',
                                    options=['X в.', 'XI в.', 'XIII в.', 'XIV в.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_tatari += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_tatari == 2:
                await bot.send_poll(quiz_answer.user.id, question='Какое из названных событий произошло в XIII в.?',
                                    options=['походы на Русь хана Батыя', 'Куликовская битва', 'стояние на реке Угре',
                                             'присоединение к России Казанского ханства'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_tatari += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_tatari == 3:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто стоял во главе русских войск, одержавших победу на льду Чудского озера в 1242?',
                                    options=['Дмитрий Донской', 'Александр Невский', 'Святослав Игоревич',
                                             'Иван Калита'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_tatari += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_tatari == 4:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто стоял во главе русских войск, одержавших победу на льду Чудского озера в 1242?',
                                    options=['Дмитрий Донской', 'Александр Невский', 'Святослав Игоревич',
                                             'Иван Калита'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_tatari += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_tatari == 5:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какие из перечисленных дат относятся к монголо-татарскому нашествию на Русь?',
                                    options=['882 – 980 гг.', '980 – 1025 гг.', '1113 – 1125 гг.', '1237 – 1240 гг.'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_tatari += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_tatari == 6:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком году произошла битва «на Чудском озере на Узмени, у Воронья камня»?',
                                    options=['1111 г.', '1223 г.', '1242 г.', '1378 г.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_tatari += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_tatari == 7:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Зимой 1239–1240 гг. опустошили Южную Русь и взяли Киев войска хана',
                                    options=['Чингисхана', 'Батыя', 'Тамерлана', 'Мамая'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_tatari += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_tatari == 8:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое из названных событий относится к XIII в.?',
                                    options=['«стояние» на реке Угре', 'Куликовская битва', 'Ледовое побоище',
                                             'сражение на реке Воже'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_tatari += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_tatari == 9:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто из русских князей возглавлял в XIII в. борьбу с крестоносцами, вторгшимися на Русь?',
                                    options=['Владимир Мономах', 'Александр Невский', 'Юрий Долгорукий', 'Иван Калита'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_tatari += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_tatari == 10:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Укажите век, в котором произошло монгольское нашествие на Русь.',
                                    options=['XI в.', 'XII в.', 'XIII в.', 'XIV в.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_tatari += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_tatari == 11:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Русская рать в Невской битве в 1240 г. сражалась против',
                                    options=['поляков', 'шведов', 'ливонцев', 'половцев'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_tatari += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_tatari == 12:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Нашествие хана Батыя на Русь и установление ордынского владычества относятся к',
                                    options=['X в.', 'XII в.', 'XIII в.', 'XIV в.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_tatari += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
                count_tatari = 0
                test_count = 2
                test_passed = True
        elif test_count == 3:
            if count_moscow == 0:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое из перечисленных событий произошло позже всех других?',
                                    options=['Куликовская битва', 'набег хана Тохтамыша на Москву',
                                             '«великое стояние» на р. Угре', 'сражение на р. Калке'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_moscow == 1:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Первая победа русских войск над главными военными силами Орды в 1380 году  произошла на',
                                    options=['реке Калке', 'реке Шелони', 'реке Неве', 'Куликовом поле'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_moscow == 2:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Великий князь Владимирский в конце XIII в. - XIV в. имел право на княжение при условии',
                                    options=['согласия Земского собора', 'согласия Боярской думы',
                                             'передачи этого права от отца к сыну', 'получения ярлыка в Орде'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_moscow == 3:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто из названных исторических деятелей были современниками?',
                                    options=['Иван Калита и Ярослав Мудрый', 'Андрей Рублев и Александр Невский',
                                             'Дмитрий Донской и Мамай', 'Владимир Мономах и хан Ахмат'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_moscow == 4:
                await bot.send_poll(quiz_answer.user.id,
                                    question='После какого события XIV века «была и радость великая, но была и печаль большая по убитым от Мамая на Дону»?',
                                    options=['Ледового побоища', 'битвы на реке Калке', 'взятия Казани',
                                             'Куликовской битвы'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_moscow == 5:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто из названных лиц были современниками?',
                                    options=['Александр Невский и хан Тохтамыш', 'Иван III и хан Батый',
                                             'Иван IV и Субэдэй', 'Дмитрий Донской и Мамай'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_moscow == 6:
                await bot.send_poll(quiz_answer.user.id,
                                    question='С каким событием связано имя Дмитрия Донского?',
                                    options=['с завоеванием Астраханского ханства', 'с Куликовской битвой',
                                             'с присоединением Смоленска', 'со стоянием на реке Угре'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_moscow == 7:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто из московских князей в XIV веке первым получил право сбора дани в пользу Орды со всех русских земель?',
                                    options=['Иван Калита', 'Андрей Боголюбский', 'Юрий Долгорукий',
                                             'Василий II Тёмный'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_moscow == 8:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что из перечисленного относится к периоду княжения Дмитрия Донского (1359 – 1389)?',
                                    options=['поход хана Тохтамыша на Москву',
                                             'появление на гербе России двуглавого орла',
                                             'вхождение Твери в состав Московского княжества',
                                             'утверждение единой монетной системы'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_moscow == 9:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Современником князя Дмитрия Донского был',
                                    options=['Ярослав Мудрый', 'Сергий Радонежский', 'Андрей Курбский',
                                             'Юрий Долгорукий'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
                count_moscow = 0
                test_count = 3
                test_passed = True
        elif test_count == 4:
            if count_vozvish == 0:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Время перехода крестьян от одного владельца к другому, согласно Судебнику 1497 г., носило название',
                                    options=['Юрьева дня', 'заповедных лет',
                                             'урочных лет', 'отходничества'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_vozvish == 1:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Как называлась река, на берегах которой решался вопрос о независимости Руси в 1480 г.?',
                                    options=['Дон', 'Волга',
                                             'Угра', 'Нева'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_vozvish == 2:
                await bot.send_poll(quiz_answer.user.id,
                                    question='С какими из перечисленных исторических личностей связана война за московский престол вXVв.?',
                                    options=['Иван Калита и Александр Тверской', 'Дмитрий Донской и Ольгерд',
                                             'Василий II и Юрий Звенигородский', 'ИванIV и Владимир Старицкий'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_vozvish == 3:
                await bot.send_poll(quiz_answer.user.id,
                                    question='К XVв. относится',
                                    options=['ограничение перехода крестьян Юрьевым днём',
                                             'утверждение единой монетной системы',
                                             'созыв первого Земского собора', 'введение заповедных лет'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_vozvish == 4:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что из перечисленного относится к периоду правления Ивана III?',
                                    options=['присоединение к Московскому государству Рязани',
                                             'присоединение к Московскому государству Казанского ханства',
                                             'освоение русскими землепроходцами Восточной Сибири',
                                             'присоединение к Московскому государству Твери'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_vozvish == 5:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Новгородские и псковские земли вошли в состав Московского государства',
                                    options=['в XIII––XIVвв.', 'в XV––XVIвв.',
                                             'в первой половине XVIIв.', 'во второй половине XVIIв.'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_vozvish == 6:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что из перечисленного произошло в XVв.?',
                                    options=['начало проведения политики опричнины', '«стояние» на реке Угре',
                                             'присоединение к России Астраханского ханства', 'введение заповедных лет'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_vozvish == 7:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Чем завершился поход Ивана III на Великий Новгород в 1478 г.?',
                                    options=['разгромом московского войска',
                                             'присоединением к Московскому княжеству Новгорода',
                                             'подписанием договора Ивана III с новгородским вече о сохранении вечевых порядков',
                                             'изгнанием из Новгорода шведских войск'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_vozvish == 8:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое название получило время перехода крестьян от одного владельца к другому согласно Судебнику 1497 г.?',
                                    options=['«урочные лета»', '«заповедные лета»',
                                             'отходничество', 'Юрьев день'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_vozvish == 9:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Война за московский престол во второй четверти XVв. велась между',
                                    options=['Василием II Тёмным и его противниками', 'Василием III и его братьями',
                                             'Дмитрием Донским и удельными князьями', 'Иваном Калитой и его братьями'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_vozvish == 10:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какая новая форма землевладения складывалась на Руси в XIV–XVвв.?',
                                    options=['вотчина', 'земщина',
                                             'поместье', 'отруб'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_vozvish == 11:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какой из названных памятников был построен в XVI в.?',
                                    options=['церковь Покрова на Нерли', 'Храм Вознесения в селе Коломенском',
                                             'царский деревянный дворец в селе Коломенском',
                                             'Успенский собор во Владимире  '],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_vozvish == 12:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком веке произошло событие, вошедшее в историю как «стояние на реке Угре»?',
                                    options=['XIIIв.', 'XIVв.',
                                             'XVв.', 'XVIв.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_vozvish == 13:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В чье правление был принят Судебник – первый свод законов единого Русского государства?',
                                    options=['Дмитрия Донского', 'Ивана III',
                                             'Александра Невского', 'Ивана IV'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_vozvish == 14:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Первое общегосударственное ограничение свободного перехода крестьян к другому землевладельцу произошло вследствие принятия',
                                    options=['«Указа о заповедных летах»', 'Судебника 1497 г.',
                                             'Судебника 1550 г.', 'Соборного Уложения 1649 г.'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_vozvish == 15:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Творчество великого русского художника Андрея Рублева приходится на',
                                    options=['конец XIV– начало XVвв.', 'конец XIII – начало XIV вв.',
                                             'середину – вторую половину XV в.', 'конец XV – начало XVI вв.'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_vozvish == 16:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Как называлась форма землевладения, возникшая в XVв. и предоставляемая за службу?',
                                    options=['поместье', 'вотчина',
                                             'кормление', 'удел'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_vozvish == 17:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком веке была ликвидирована самостоятельность Великого Новгорода и он был присоединен к Москве?',
                                    options=['XIIIв.', 'XIVв.',
                                             'XVв.', 'XVIв.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_vozvish == 18:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Как называлась в XIII––XVвв. ордынская грамота на право княжения в русских землях?',
                                    options=['ясак', 'челобитное',
                                             'баскак', 'ярлык'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_vozvish == 19:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Княжение Ивана III – государя всея Руси – относится к веку',
                                    options=['XII–XIII', 'XIV',
                                             'XV – XVI', 'XVI'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_vozvish += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
                count_vozvish = 0
                test_count = 4
                test_passed = True
        elif test_count == 5:
            if count_groz == 0:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое из перечисленных событий относится к XVIв.?',
                                    options=['отмена кормлений', 'издание Новоторгового устава',
                                             'окончательная отмена местничества', 'учреждение Приказа Тайных дел'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_groz == 1:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что стало одним из результатов реформ в 40––50-е гг.XVIв. России?',
                                    options=['учреждение системы кормлений', 'введение подушной подати',
                                             'создание стрелецкого войска', 'принятие Соборного уложения'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_groz == 2:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Проведение реформ в России в середине XVI в. связано с деятельностью',
                                    options=['Совета всея земли', 'Совета господ',
                                             'Избранной Рады', 'Опричного двора'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_groz == 3:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что из перечисленного относится к достижениям культуры в России XVIв.?',
                                    options=['начало книгопечатания', 'возведение храма Покрова на Нерли',
                                             'творения иконописца Андрея Рублёва', 'творения зодчего Василия Баженова'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_groz == 4:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком году был созван первый в истории России Земский собор?',
                                    options=['1447 г.', '1549 г.',
                                             '1601 г.', '1613 г.'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_groz == 5:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какой ряд дат отражает события внешней политики Ивана IV?',
                                    options=['1380 – 1382 гг.', '1478 – 1485 гг.',
                                             '1552 – 1556 гг.', '1596 – 1597 гг.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_groz == 6:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В какие годы Иваном Грозным проводилась опричная политика?',
                                    options=['1325 – 1340 гг.', '1462 – 1505 гг.',
                                             '1565 – 1572 гг.', '1606 – 1610 гг.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_groz == 7:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Покоритель Сибири Ермак Тимофеевич был современником',
                                    options=['Михаила Романова', 'Ивана Калиты',
                                             'Василия Темного', 'Ивана Грозного'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_groz == 8:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В результате военной реформы XVIв. в России появились',
                                    options=['рекруты', 'стрельцы',
                                             'драгуны', 'гвардейцы'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_groz == 9:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком веке произошло присоединение Астраханского ханства к России?',
                                    options=['XIVв.', 'XVв.',
                                             'XVIв.', 'XVIIв.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_groz == 10:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Присоединение Сибири к Московскому государству началось в правление',
                                    options=['Ивана Калиты', 'Ивана III',
                                             'Ивана IV', 'Алексея Михайловича'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_groz == 11:
                await bot.send_poll(quiz_answer.user.id,
                                    question='1549 год – это год',
                                    options=['созыва первого Земского собора', 'окончания Ливонской войны',
                                             'стояния на реке Угре', 'Куликовской битвы'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_groz == 12:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Храм Василия Блаженного в Москве был построен в память',
                                    options=['освобождения Москвы от поляков в годы Смуты в 1612 г.',
                                             'победы в Отечественной войне 1812 г.',
                                             'взятия Казани в 1552 г.', 'прекращения зависимости Руси от Золотой Орды'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_groz == 13:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Пехотинцы с огнестрельным оружием, составлявшие в XVI–XVIIвв. постоянное войско, назывались',
                                    options=['стрельцами', 'опричниками',
                                             'рекрутами', 'казаками'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_groz == 14:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Как называлась система мер, предпринятых Иваном Грозным в 1565 – 1572 гг. для укрепления своей самодержавной власти?',
                                    options=['местничество', 'опричнина',
                                             'нестяжательство', 'земщина'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_groz == 15:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком ряду названы даты, связанные с принятием Судебников?',
                                    options=['1054 г., 1113 г.', '1223 г., 1242 г.',
                                             '1380 г., 1480 г.', '1497 г., 1550 г.'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_groz == 16:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Имена Алексея Адашева, Андрея Курбского, митрополита Филиппа связаны с царствованием',
                                    options=['Ивана III', 'Ивана IV',
                                             'Бориса Годунова', 'Василия Шуйского'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_groz == 17:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Важнейшим явлением российской культуры XVI в. стало начало',
                                    options=['иконописи', 'деревянного зодчества',
                                             'каменного зодчества', 'книгопечатания'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_groz == 18:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Ясачные люди в XVI−XVIIвв.−это',
                                    options=['рабочие мануфактур', 'помещичьи крестьяне, отпущенные на заработки',
                                             'запорожские казаки, выплачивающие дань крымским ханам',
                                             'коренное население Севера и Сибири, обязанное платить дань в казну пушниной'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_groz == 19:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Система кормлений была ликвидирована',
                                    options=['в первой половине XVв.', 'во второй половине XVв.',
                                             'в середине XVIв.', 'в начале XVIIв.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_groz == 20:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Книга житейских правил и наставлений, созданная в XVI в., известна под названием',
                                    options=['«Апостол»', '«Поучение детям»',
                                             '«Домострой»', '«Судебник»'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_groz == 21:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое из перечисленных событий произошло в XVIв.?',
                                    options=['венчание на царство Ивана IV',
                                             'восстание под предводительством И.И. Болотникова',
                                             'прекращение зависимости Руси от Орды',
                                             'присоединение к России Левобережной Украины'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_groz += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
                count_groz += 1
                count_groz = 0
                test_count = 5
                test_passed = True
        elif test_count == 6:
            if count_smuta == 0:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В честь освобождения Москвы от польских войск в XVIIв. построен(-а)',
                                    options=['Казанский собор на Красной площади', 'Исаакиевский собор',
                                             'колокольня Ивана Великого', 'Сухарева башня'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_smuta += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_smuta == 1:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Как называлось правительство Российского государства, образовавшееся после свержения царя Василия Шуйского в 1610 году?',
                                    options=['«семибоярщиной»', 'Верховным Тайным советом',
                                             'Советом всея земли', 'Уложенной комиссией'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_smuta += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_smuta == 2:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком году началось правление династии Романовых?',
                                    options=['в 1605 г.', 'в 1613 г.',
                                             'в 1645 г.', 'в 1682 г.'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_smuta += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_smuta == 3:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое из перечисленных событий произошло в 1613 г.?',
                                    options=['избрание на царство Бориса Годунова', 'начало польской интервенции',
                                             'освобождение Москвы от поляков', 'избрание на царство Михаила Романова'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_smuta += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_smuta == 4:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто в 1598 г. был избран на царство Земским собором?',
                                    options=['Борис Годунов', 'Лжедмитрий I',
                                             'Василий Шуйский', 'Лжедмитрий II'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_smuta += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_smuta == 5:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кого в период Смуты (начало XVIIв.) называли «тушинским вором»?',
                                    options=['Лжедмитрия II', 'Василия Шуйского',
                                             'Ивана Болотникова', 'Ивана Заруцкого'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_smuta += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_smuta == 6:
                await bot.send_poll(quiz_answer.user.id,
                                    question='К какому времени, явлению относится понятие «семибоярщина»?',
                                    options=['Смуте', 'преобразованиям Петра Первого',
                                             'опричнине Ивана Грозного', 'восстанию под руководством С. Разина'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_smuta += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_smuta == 7:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какая дата связана с образованием Второго ополчения и освобождением Москвы в годы Смуты?',
                                    options=['1589 г.', '1612 г.',
                                             '1662 г.', '1701 г.'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_smuta += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_smuta == 8:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком году Земский собор избрал царем Михаила Романова?',
                                    options=['1549 г.', '1613 г.',
                                             '1682 г.', '1711 г.'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_smuta += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_smuta == 9:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое из названных событий произошло позже других?',
                                    options=['правление Василия Шуйского', '«Угличская драма»',
                                             'правление Лжедмитрия I', 'воцарение династии Романовых'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_smuta += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_smuta == 10:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Сословно-представительным органом в XVIв. был(-а)',
                                    options=['Верховный Тайный Совет', 'Земский собор',
                                             'Избранная Рада', 'Государственный Совет'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_smuta += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_smuta == 11:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто из перечисленных государей был избран на царство Земским собором в 1598г.?',
                                    options=['Михаил Романов', 'Борис Годунов',
                                             'Василий Шуйский', 'Фёдор Иоаннович'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_smuta += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_smuta == 12:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В годы Смуты переворот 1610 г., в результате которого был свергнут Василий Шуйский, привел к власти',
                                    options=['правительство из семи бояр – «семибоярщину»', 'Бориса Годунова',
                                             'Лжедмитрия I', 'Михаила Романова'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_smuta += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
                count_smuta += 1
                count_smuta = 0
                test_count = 6
                test_passed = True
        elif test_count == 7:
            if count_bunt == 0:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что из перечисленного было одной из причин бунтов 1648г. и 1662г. в Москве?',
                                    options=['введение новых налогов и денег', 'ликвидация городского самоуправления',
                                             'введение рекрутской повинности',
                                             'появление самозванцев, поддержанных восставшими'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_bunt == 1:
                await bot.send_poll(quiz_answer.user.id,
                                    question='XVIIв. (после Смуты) управление на местах возглавляли',
                                    options=['губернаторы', 'воеводы',
                                             'фискалы', 'земские начальники'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 2:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какая из перечисленных территорий была присоединена к России в XVIIв.?',
                                    options=['Левобережная Украина', 'Западная Сибирь',
                                             'Прибалтика', 'Нижнее Поволжье'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 3:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что из перечисленного предусматривало Соборное уложение 1649 г.?',
                                    options=['ликвидацию «белых слобод» в городах',
                                             'увеличение срока розыска беглых крестьян до 15 лет',
                                             'отмену местничества', 'введение подушной подати'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 4:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что из перечисленного относится к экономической жизни России XVIIв.?',
                                    options=['утверждение единой монетной системы', 'появление первых мануфактур',
                                             'отмена внутренних таможенных пошлин', 'возникновение товарных бирж'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 5:
                await bot.send_poll(quiz_answer.user.id,
                                    question='По Столбовскому договору 1617 г. Россия',
                                    options=['присоединила порт Нарву', 'потеряла выход в Балтийское море',
                                             'получила выход в Белое море', 'стала союзником Речи Посполитой'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 6:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что было причиной восстания монахов Соловецкого монастыря в 1668–1676гг.?',
                                    options=['секуляризация монастырских земель', 'церковная реформа патриарха Никона',
                                             'упразднение в России патриаршества', 'создание Святейшего Синода'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 7:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Современниками были',
                                    options=['царь Алексей Михайлович и протопоп Аввакум',
                                             'императрица Анна Иоанновна и Дмитрий Пожарский',
                                             'Степан Разин и Емельян Пугачев',
                                             'царь Борис Годунов и императрица Елизавета Петровна'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 8:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Новым явлением в экономике России XVIIв. стало',
                                    options=['появление мануфактур', 'развитие цехового производства',
                                             'появление фабрик', 'появление заводов'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 9:
                await bot.send_poll(quiz_answer.user.id,
                                    question='При ком из правителей было принято «Соборное уложение»?',
                                    options=['Михаиле Федоровиче', 'Алексее Михайловиче',
                                             'Федоре Алексеевиче', 'Петре Великом'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 10:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что относится к решениям Переяславской Рады 1654 г.?',
                                    options=['создание Запорожской Сечи', 'упразднение гетманства на Украине',
                                             'объединение Левобережной Украины с Россией',
                                             'присоединение Правобережной Украины к России'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 11:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое из указанных явлений относится к ХVIIв.?',
                                    options=['появление поместного землевладения',
                                             'начало формирования единого российского рынка',
                                             'кризис крепостнической системы хозяйства',
                                             'перевод крестьян на месячину'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_bunt == 12:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто первым из династии Романовых получил царский престол по наследству от отца?',
                                    options=['Алексей Михайлович', 'Михаил Федорович',
                                             'Федор Алексеевич', 'Петр Алексеевич'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 13:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какой из названных ниже документов был составлен в XVIIв.?',
                                    options=['«Табель о рангах»', '«Указ о престолонаследии»',
                                             '«Соборное уложение»', '«Судебник»'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 14:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое из названных событий произошло во второй половине XVIIв.?',
                                    options=['«Медный бунт»', '«Соляной бунт»',
                                             'окончание Смуты', 'избрание на царство Михаила Романова'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_bunt == 15:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Имя первопечатника Ивана Федорова связано с веком',
                                    options=['XIIIв.', 'XIVв.',
                                             'XVв.', 'XVIв.'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 16:
                await bot.send_poll(quiz_answer.user.id,
                                    question='С городскими восстаниями XVIIв. связаны даты:',
                                    options=['1648 г., 1662 г.', '1606 г., 1607 г.',
                                             '1670 г., 1671 г.', '1617 г., 1618 г.'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_bunt == 17:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Чем знаменателен в истории России год 1649?',
                                    options=['принятием «Соборного Уложения»',
                                             'окончанием зависимости Руси от Золотой Орды',
                                             'присоединением Левобережной Украины к России',
                                             'принятием «Табели о рангах»'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 18:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое название получило восстание в Москве в 1662 г.?',
                                    options=['«Смута»', '«Медный бунт»',
                                             '«поход за зипунами»', '«чумной бунт»'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 19:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Во время царствования Алексея Михайловича произошло',
                                    options=['присоединение Казани', 'присоединение Аляски',
                                             'завоевание Крыма', 'воссоединение Украины с Россией'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 20:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком году произошел в Москве «Медный бунт»?',
                                    options=['1497 г.', '1533 г.',
                                             '1662 г.', '1707 г.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_bunt == 21:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что из названного произошло в XVIIв.?',
                                    options=['церковный раскол', 'Ливонская война',
                                             'Северная война', 'создание Священного Синода'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_bunt == 22:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком году в Москве вспыхнул Соляной бунт?',
                                    options=['1480 г.', '1648 г.',
                                             '1700 г.', '1762 г.'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 23:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Продвижение русских в Сибирь в XVIIв. связано с именем',
                                    options=['Ермака Тимофеевича', 'Семена Дежнева',
                                             'Степана Разина', 'Витуса Беринга'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 24:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Годы: 1497, 1581, 1597, 1649 – отражают основные этапы',
                                    options=['борьбы России за выход к морю',
                                             'образования Российского централизованного государства',
                                             'борьбы Руси с Золотой Ордой за независимость', 'закрепощения крестьян'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 25:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое событие произошло в 1654 г.?',
                                    options=['издание Жалованной грамоты дворянству',
                                             'присоединение к России Левобережной Украины',
                                             'принятие Соборного уложения', 'подписание Ништадтского мира со Швецией'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_bunt == 26:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком веке проводились экспедиции первопроходца Семена Дежнева?',
                                    options=['XVв.', 'XVIв.',
                                             'XVIIв.', 'XVIIIв.'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 27:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком веке произошли все названные события – «Соляной бунт» в Москве, восстания в Пскове и Новгороде, «Медный бунт» в Москве?',
                                    options=['XVв.', 'XVIв.',
                                             'XVIIв.', 'XVIIIв.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 28:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Одним из следствий принятия Соборного Уложения 1649 г. было',
                                    options=['установление бессрочного сыска беглых крестьян',
                                             'продление сроков поиска крестьян до 15 лет',
                                             'упразднение правила «с Дона выдачи нет»',
                                             'разрешение помещикам ссылать крестьян в Сибирь'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_bunt == 29:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В царствование царя Алексея Михайловича',
                                    options=['произошел церковный раскол', 'было учреждено патриаршество',
                                             'Русь приняла православие', 'был учрежден Синод'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 30:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какая дата связана с окончательным закрепощением крестьян?',
                                    options=['1480 г.', '1556 г.',
                                             '1649 г.', '1721 г.'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 31:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Понятие «церковный раскол» возникло в царствование',
                                    options=['Федора Алексеевича', 'Алексея Михайловича',
                                             'Петра I', 'Екатерины II'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_bunt == 32:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто из указанных лиц был современником царя Алексея Михайловича?',
                                    options=['И. Волоцкий', 'патриарх Никон',
                                             'митрополит Макарий', 'Сергий Радонежский'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 33:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Понятие «отмена урочных лет» связано с документом',
                                    options=['«Табель о рангах»', '«Соборное Уложение 1649 г.»',
                                             '«Судебник 1497 г.»', '«Жалованная грамота дворянству»'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 34:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Соборное уложение" царя Алексея Михайловича было принято в',
                                    options=['1649 г.', '1645 г.',
                                             '1646 г.', '1647 г.'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 35:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком из документов провозглашались отмена "урочных" лет и бессрочный сыск беглых крестьян?',
                                    options=['Соборном уложении 1649 г.', 'Судебнике 1497 г.',
                                             'Судебнике 1550 г.', 'указах об урочных летах'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 36:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В XVIIвеке в крепостной зависимости от помещика находились',
                                    options=['смерды', 'закупы',
                                             'черносошные крестьяне', 'частновладельческие крестьяне'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 37:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Высшее сословно-представительное учреждение в России в XVI–XVIIвв. – это',
                                    options=['Земский собор', 'Избранная рада',
                                             'Сенат', 'Государственный совет'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_bunt == 38:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Законодательный акт, окончательно закрепостивший крестьян, был принят в',
                                    options=['1613 г.', '1649 г.',
                                             '1654 г.', '1670 г.'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 39:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком веке состоялся Земский собор, принявший решение о присоединении к России Левобережной Украины и Киева?',
                                    options=['XVIв.', 'XVIIв.',
                                             'XVIIIв.', 'XIXв.'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 40:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какое из названных событий относится к XVIIв.?',
                                    options=['учреждение в России патриаршества', 'создание Священного Синода',
                                             'церковный раскол', 'борьба иосифлян и нестяжателей'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 41:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В каком ряду приведены годы казацко-крестьянских восстаний XVII–XVIIIвв.?',
                                    options=['1601–1605 гг., 1705–1706 гг.', '1613–1645 гг., 1761–1762 гг.',
                                             '1632–1634 гг., 1768–1774 гг.', '1670–1671 гг., 1773–1775 гг.'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_bunt == 42:
                await bot.send_poll(quiz_answer.user.id,
                                    question='К XVIIв. относится',
                                    options=['правление Елены Глинской', 'заключение «Вечного мира» с Речью Посполитой',
                                             'деятельность Стоглавого собора', 'гибель царевича Дмитрия в Угличе'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_bunt == 43:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какая из перечисленных территорий вошла в состав России позже других?',
                                    options=['Нижнее Поволжье', 'Левобережная Украина',
                                             'Западная Сибирь', 'Среднее Поволжье'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 44:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Какой из перечисленных городов в XVIIв. был центром морской торговли России со странами Западной Европы?',
                                    options=['Архангельск', 'Мурманск',
                                             'Рига', 'Кронштадт'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_bunt == 45:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Понятие «вечный мир» связано с отношениями России в XVIIв. с',
                                    options=['Польшей', 'Турцией',
                                             'Швецией', 'Англией'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 46:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В результате восстания в Москве в 1662 г. царь вынужден был',
                                    options=['отменить медные деньги', 'ликвидировать «белые слободы»',
                                             'отменить рекрутчину', 'ввести подушную подать'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_bunt == 47:
                await bot.send_poll(quiz_answer.user.id,
                                    question='В результате церковных реформ Никона в XVIIв. в России',
                                    options=['кафедра митрополита была перенесена в Москву',
                                             'было учреждено патриаршество',
                                             'была проведена секуляризация церковных земель',
                                             'произошёл церковный раскол'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_bunt += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
                count_bunt += 1
                count_bunt = 0
                test_count = 7
                test_passed = True
    else:
        if test_count == 1:
            if quiz_answer.option_ids == [0]:
                rights += 1
            if rights == 0:
                await bot.send_message(quiz_answer.user.id, text = 'У вас 0 правильных ответов. Тренируйтесь!', reply_markup=get_main())
            else:
                await bot.send_message(quiz_answer.user.id,
                                        text=f'Вы прошли тест, у вас {rights} правильных ответов из 12 вопросов\nВы решили правильно {round((rights / 12)*100)}% вопросов',
                                        reply_markup=get_main())
        elif test_count == 0:
            if quiz_answer.option_ids == [0]:
                rights += 1
            if rights == 0:
                await bot.send_message(quiz_answer.user.id, text = 'У вас 0 правильных ответов. Тренируйтесь!', reply_markup=get_main())
            else:
                await bot.send_message(quiz_answer.user.id,
                                        text=f'Вы прошли тест, у вас {rights} правильных ответов из 31 вопросов\nВы решили правильно {round((rights / 31)*100)}% вопросов',
                                        reply_markup=get_main())
        elif test_count == 2:
            if quiz_answer.option_ids == [2]:
                rights += 1
            if rights == 0:
                await bot.send_message(quiz_answer.user.id, text = 'У вас 0 правильных ответов. Тренируйтесь!', reply_markup=get_main())
            else:
                await bot.send_message(quiz_answer.user.id,
                                        text=f'Вы прошли тест, у вас {rights} правильных ответов из 14 вопросов\nВы решили правильно {round((rights / 14)*100)}% вопросов',
                                        reply_markup=get_main())
        elif test_count == 3:
            if quiz_answer.option_ids == [1]:
                rights += 1
            if rights == 0:
                await bot.send_message(quiz_answer.user.id, text = 'У вас 0 правильных ответов. Тренируйтесь!', reply_markup=get_main())
            else:
                await bot.send_message(quiz_answer.user.id,
                                        text=f'Вы прошли тест, у вас {rights} правильных ответов из 11 вопросов\nВы решили правильно {round((rights / 11)*100)}% вопросов',
                                        reply_markup=get_main())
        elif test_count == 4:
            if quiz_answer.option_ids == [2]:
                rights += 1
            if rights == 0:
                await bot.send_message(quiz_answer.user.id, text = 'У вас 0 правильных ответов. Тренируйтесь!', reply_markup=get_main())
            else:
                await bot.send_message(quiz_answer.user.id,
                                        text=f'Вы прошли тест, у вас {rights} правильных ответов из 21 вопросов\nВы решили правильно {round((rights / 21)*100)}% вопросов',
                                        reply_markup=get_main())
        elif test_count == 5:
            if quiz_answer.option_ids == [0]:
                rights += 1
            if rights == 0:
                await bot.send_message(quiz_answer.user.id, text = 'У вас 0 правильных ответов. Тренируйтесь!', reply_markup=get_main())
            else:
                await bot.send_message(quiz_answer.user.id,
                                        text=f'Вы прошли тест, у вас {rights} правильных ответов из 23 вопросов\nВы решили правильно {round((rights / 23)*100)}% вопросов',
                                        reply_markup=get_main())
        elif test_count == 6:
            if quiz_answer.option_ids == [0]:
                rights += 1
            if rights == 0:
                await bot.send_message(quiz_answer.user.id, text = 'У вас 0 правильных ответов. Тренируйтесь!', reply_markup=get_main())
            else:
                await bot.send_message(quiz_answer.user.id,
                                        text=f'Вы прошли тест, у вас {rights} правильных ответов из 14 вопросов\nВы решили правильно {round((rights / 14)*100)}% вопросов',
                                        reply_markup=get_main())
        elif test_count == 7:
            if quiz_answer.option_ids == [3]:
                rights += 1
            if rights == 0:
                await bot.send_message(quiz_answer.user.id, text='У вас 0 правильных ответов. Тренируйтесь!',
                                           reply_markup=get_main())
            else:
                await bot.send_message(quiz_answer.user.id,
                                           text=f'Вы прошли тест, у вас {rights} правильных ответов из 49 вопросов\nВы решили правильно {round((rights / 49) * 100)}% вопросов',
                                           reply_markup=get_main())
        rights = 0
        test_passed = False
        return


async def ud_drob(callback: types.CallbackQuery):
    await bot.send_poll(callback.from_user.id,
                        question='С именем какого князя связан рост могущества Владимиро-Суздальского княжества в XII в.?',
                        options=['Александра Невского', 'Ярослава Мудрого', 'Андрея Боголюбского', 'Олега Вещего'],
                        type='quiz', correct_option_id=2,
                        is_anonymous=False)
    global test_count
    test_count = 1


async def tatari(callback: types.CallbackQuery):
    global test_count
    await bot.send_poll(callback.from_user.id,
                        question='В 1242 г. произошло столкновение русских дружин с западно-европейскими рыцарями на',
                        options=['реке Неве', 'реке Угре', 'Чудском озере ', 'реке Ижоре'],
                        type='quiz', correct_option_id=2,
                        is_anonymous=False)
    test_count = 2


async def moscow(callback: types.CallbackQuery):
    global test_count
    await bot.send_poll(callback.from_user.id,
                        question='В 1242 г. произошло столкновение русских дружин с западно-европейскими рыцарями на',
                        options=['реке Неве', 'реке Угре', 'Чудском озере ', 'реке Ижоре'],
                        type='quiz', correct_option_id=2,
                        is_anonymous=False)
    test_count = 3


async def vozvish(callback: types.CallbackQuery):
    global test_count
    await bot.send_poll(callback.from_user.id,
                        question='Собирание русских земель вокруг Москвы происходило в',
                        options=['X – XI вв.', 'XI – XIIвв.', 'XII – XIII вв. ', 'XIV – XVI вв.'],
                        type='quiz', correct_option_id=3,
                        is_anonymous=False)
    test_count = 4


async def ivangroz(callback: types.CallbackQuery):
    global test_count
    await bot.send_poll(callback.from_user.id,
                        question='Какой из названных документов был принят позже других?',
                        options=['«Судебник» Ивана III', '«Указы об урочных летах»', '«Указы о заповедных летах»',
                                 '«Судебник» Ивана IV'],
                        type='quiz', correct_option_id=1,
                        is_anonymous=False)
    test_count = 5


async def smuta(callback: types.CallbackQuery):
    global test_count
    await bot.send_poll(callback.from_user.id,
                        question='Кто из русских царей был первым избран на престол Земским собором?',
                        options=['Борис Годунов', 'Василий Шуйский', 'Фёдор Иоаннович',
                                 'Михаил Фёдорович'],
                        type='quiz', correct_option_id=0,
                        is_anonymous=False)
    test_count = 6


async def bunt(callback: types.CallbackQuery):
    global test_count
    await bot.send_poll(callback.from_user.id,
                        question='В каком году было открыто первое в России высшее учебное заведение––Славяно-греко-латинская академия?',
                        options=['1645 г.', '1672 г.', '1687 г.',
                                 '1698 г.'],
                        type='quiz', correct_option_id=2,
                        is_anonymous=False)
    test_count = 7


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(test_buttons, commands=['test'])
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(drevnerus_test_kresh, text='1', state=None)
    dp.register_poll_answer_handler(handle_answer)
    dp.register_callback_query_handler(test_test, text='1')
    dp.register_callback_query_handler(ud_drob, text='2')
    dp.register_callback_query_handler(tatari, text='3')
    dp.register_callback_query_handler(moscow, text='4')
    dp.register_callback_query_handler(start_callback, text='back')
    dp.register_callback_query_handler(vozvish, text='5')
    dp.register_callback_query_handler(ivangroz, text='6')
    dp.register_callback_query_handler(smuta, text='7')
    dp.register_callback_query_handler(bunt, text='8')
