from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    KeyboardButton


# from database.mysql_db import mysql_read_courses_list, mysql_read_coulinary_list
def get_main():
    back = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton('Вернуться в главное меню', callback_data='back')
    back.add(b1)
    return back

def get_kb_start():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Древнерусское государство', callback_data='1')
    b2 = InlineKeyboardButton('Удельная раздробленность 1132-1237', callback_data='2')
    b3 = InlineKeyboardButton('Начало татаро-монгольского ига 1237-1267 г.', callback_data='3')
    b4 = InlineKeyboardButton('Возвышение Москвы 1267-1389', callback_data='4')
    b5 = InlineKeyboardButton('1389-1521 Возвышение Москвы', callback_data='5')
    b6 = InlineKeyboardButton('1530-1598 Иван Грозный и Фёдор Иоанович', callback_data='6')
    b7 = InlineKeyboardButton('1598-1613 Смутное время', callback_data='7')
    b8 = InlineKeyboardButton('Бунташный век 1613-1682', callback_data='8')
    start_inline.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7).add(b8)
    return start_inline


def get_kb_drevrus():
    drevRusinline = InlineKeyboardMarkup(row_width=1)
    b1=InlineKeyboardButton('882 г.', callback_data='kresh1')
    b2=InlineKeyboardButton('988 г.', callback_data='kresh2')
    b3=InlineKeyboardButton('945 г.', callback_data='kresh3')
    b4=InlineKeyboardButton('962 г.', callback_data='kresh4')
    drevRusinline.add(b1).add(b2).add(b3).add(b4)
    return drevRusinline

def get_test():
    test = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton('882 г.', callback_data='1')
    b2 = InlineKeyboardButton('988 г.', callback_data='1')
    b3 = InlineKeyboardButton('945 г.', callback_data='1')
    b4 = InlineKeyboardButton('962 г.', callback_data='1')
    test.add(b1).add(b2).add(b3).add(b4)
    return test

def get_test1():
    test = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton('882 г.❌', callback_data='1')
    b2 = InlineKeyboardButton('988 г.✅', callback_data='1')
    b3 = InlineKeyboardButton('945 г.❌', callback_data='1')
    b4 = InlineKeyboardButton('962 г ❌.', callback_data='1')
    test.add(b1).add(b2).add(b3).add(b4)
    return test