
import time
import pytest
import string

from bugreport import BugReport
from pynput.keyboard import Controller as KController
from pynput.keyboard import Key

#Функция представляет набор Макросс сценариев и ввод данных используя прасинг Python посредством обращения с данными для ввода к процессору и их классификации
@pytest.mark.xfail(reason='Сценарий кнопки "проверить" не взаимодействует с полем для ввода')
def test_step1():
    """Тест-кейс № 2: Проверка вводимых типов данных - Шаг № 1: проверка пустого поля для ввода"""
    
    time.sleep(1)

    keyboard = KController()
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    time.sleep(0.2)

    keyboard.press(Key.space)
    keyboard.release(Key.space)

    time.sleep(1)

    BugReport.write('2','1','Message Box с предупреждением','Сообщение "Верно, это цифра!"')

#Функция представляет набор Макросс сценариев и ввод данных используя прасинг Python посредством обращения с данными для ввода к процессору и их классификации
@pytest.mark.xfail(reason='Сценарий кнопки "проверить" не взаимодействует с полем для ввода')
def test_step2():
    """Тест-кейс № 2: Проверка вводимых типов данных - Шаг № 2: ввод целочисленных данных"""

    time.sleep(1)

    keyboard = KController()
    keyboard.press(Key.shift_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.shift_l)

    stringToWrite = str(int('q11234567890wadsd'.strip(string.ascii_letters)))
    for char in stringToWrite:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.02)

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    time.sleep(0.2)

    keyboard.press(Key.space)
    keyboard.release(Key.space)

#Функция представляет набор Макросс сценариев и ввод данных используя прасинг Python посредством обращения с данными для ввода к процессору и их классификации
@pytest.mark.xfail(reason='Сценарий кнопки "проверить" не взаимодействует с полем для ввода')
def test_step3():
    """Тест-кейс № 2: Проверка вводимых типов данных - Шаг № 3: ввод строковых данных"""

    time.sleep(1)

    keyboard = KController()
    keyboard.press(Key.shift_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.shift_l)

    stringToWrite = 'qqwerty'
    for char in stringToWrite:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.02)

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    time.sleep(0.2)

    keyboard.press(Key.space)
    keyboard.release(Key.space)

    time.sleep(1)

    BugReport.write('2','3','Message Box с предупреждением','Сообщение "Верно, это цифра!"')

#Функция представляет набор Макросс сценариев и ввод данных используя прасинг Python посредством обращения с данными для ввода к процессору и их классификации
@pytest.mark.xfail(reason='Сценарий кнопки "проверить" не взаимодействует с полем для ввода')
def test_step4():
    """Тест-кейс № 2: Проверка вводимых типов данных - Шаг № 4: ввод символьных данных"""

    time.sleep(1)

    keyboard = KController()
    keyboard.press(Key.shift_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.shift_l)

    stringToWrite = '**'
    for char in stringToWrite:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.02)

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    time.sleep(0.2)

    keyboard.press(Key.space)
    keyboard.release(Key.space)

    time.sleep(1)

    BugReport.write('2','4','Message Box с предупреждением','Сообщение "Верно, это цифра!"')