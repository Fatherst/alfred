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


# async def hello(message:types.Message):
#    if message.from_user.id != :
#        await bot.send_message(message.from_user.id, text='Привет! Напиши /start,чтобы начать изучать историю со мной!')

async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text='Привет\nВы пользуетесь ботом по истории. Наш бот предназначен для изучения истории. Что бы вы хотели?',
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
    global count_ud, count, test_count, test_passed, rights, count_tatari, count_moscow
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
                                    options=['Куликовская битва', 'набег хана Тохтамыша на Москву', '«великое стояние» на р. Угре', 'сражение на р. Калке'],
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
                                    options=['согласия Земского собора', 'согласия Боярской думы', 'передачи этого права от отца к сыну', 'получения ярлыка в Орде'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_moscow == 3:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто из названных исторических деятелей были современниками?',
                                    options=['Иван Калита и Ярослав Мудрый', 'Андрей Рублев и Александр Невский', 'Дмитрий Донской и Мамай', 'Владимир Мономах и хан Ахмат'],
                                    type='quiz', correct_option_id=2,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_moscow == 4:
                await bot.send_poll(quiz_answer.user.id,
                                    question='После какого события XIV века «была и радость великая, но была и печаль большая по убитым от Мамая на Дону»?',
                                    options=['Ледового побоища', 'битвы на реке Калке', 'взятия Казани', 'Куликовской битвы'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [2]:
                    rights += 1
            elif count_moscow == 5:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто из названных лиц были современниками?',
                                    options=['Александр Невский и хан Тохтамыш', 'Иван III и хан Батый', 'Иван IV', 'Дмитрий Донской и Мамай'],
                                    type='quiz', correct_option_id=3,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_moscow == 6:
                await bot.send_poll(quiz_answer.user.id,
                                    question='С каким событием связано имя Дмитрия Донского?',
                                    options=['с завоеванием Астраханского ханства', 'с Куликовской битвой', 'с присоединением Смоленска', 'со стоянием на реке Угре'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [3]:
                    rights += 1
            elif count_moscow == 7:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Кто из московских князей в XIV веке первым получил право сбора дани в пользу Орды со всех русских земель?',
                                    options=['Иван Калита', 'Андрей Боголюбский', 'Юрий Долгорукий', 'Василий II Тёмный'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [1]:
                    rights += 1
            elif count_moscow == 8:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Что из перечисленного относится к периоду княжения Дмитрия Донского (1359 – 1389)?',
                                    options=['поход хана Тохтамыша на Москву', 'появление на гербе России двуглавого орла', 'вхождение Твери в состав Московского княжества', 'утверждение единой монетной системы'],
                                    type='quiz', correct_option_id=0,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
            elif count_moscow == 9:
                await bot.send_poll(quiz_answer.user.id,
                                    question='Современником князя Дмитрия Донского был',
                                    options=['Ярослав Мудрый', 'Сергий Радонежский', 'Андрей Курбский', 'Юрий Долгорукий'],
                                    type='quiz', correct_option_id=1,
                                    is_anonymous=False)
                count_moscow += 1
                if quiz_answer.option_ids == [0]:
                    rights += 1
                count_moscow = 0
                test_count = 3
                test_passed = True
    else:
        if test_count == 1:
            if quiz_answer.option_ids == [0]:
                rights += 1
        elif test_count == 0:
            if quiz_answer.option_ids == [0]:
                rights += 1
        elif test_count == 2:
            if quiz_answer.option_ids == [2]:
                rights += 1
        elif test_count == 3:
            if quiz_answer.option_ids == [1]:
                rights += 1
        await bot.send_message(quiz_answer.user.id, text=f'Вы прошли тест, у вас {rights} правильных ответов')
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


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(test_buttons, commands=['test'])
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(drevnerus_test_kresh, text='1', state=None)
    dp.register_poll_answer_handler(handle_answer)
    dp.register_callback_query_handler(test_test, text='1')
    dp.register_callback_query_handler(ud_drob, text='2')
    dp.register_callback_query_handler(tatari, text='3')
    dp.register_callback_query_handler(moscow, text='4')
