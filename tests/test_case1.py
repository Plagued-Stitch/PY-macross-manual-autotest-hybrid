
import time

from bugreport import BugReport
from pycaw.pycaw import AudioUtilities
from dragonfly import Window
from pynput.keyboard import Controller as KController
from pynput.keyboard import Key

#Макросс фокусируется на кнопке воспроизведения звука и нажимает её, функция проверяет запись в мишкере windows если приложение воспроизводит звук
def test_step1():
    """Тест-кейс № 1: Проверка воспроизведения звука - Шаг № 1: проверка события кнопки 'Звук2'"""

    time.sleep(1)

    for window in Window.get_all_windows():
        if '1cv8' in window.executable and 'Конфигурация' in window.title:
            convertstring = str.replace(str(window), 'Win32Window(handle=', '')
            convertstring = int(str.replace(convertstring, ')', ''))
            Window(convertstring).set_foreground()
    
    time.sleep(1)

    keyboard = KController()
    keyboard.press(Key.shift_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.shift_l)

    keyboard.press(Key.space)
    keyboard.release(Key.space)

    time.sleep(0.3)

    try:
        sessions = AudioUtilities.GetAllSessions()
        foundApplication = False

        for session in sessions:
            if session.Process and '1cv8' in session.Process.name():
                foundApplication = True

        assert foundApplication == True

    except AssertionError:
        BugReport.write('1','1','Воспроизводится звуковой файл','Звуковой файл не воспроизвёлся')

        assert False, 'Шаг 1 - ПРОВАЛ, Причина: Звуковой файл не воспроизвёлся'

#Макросс фокусируется на кнопке воспроизведения звука и нажимает её, функция проверяет запись в мишкере windows если приложение воспроизводит звук
def test_step2():
    """Тест-кейс № 1: Проверка воспроизведения звука - Шаг № 2: проверка события кнопки 'Звук1'"""

    time.sleep(1)

    keyboard = KController()
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    time.sleep(1)

    keyboard.press(Key.shift_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.shift_l)

    keyboard.press(Key.space)
    keyboard.release(Key.space)

    time.sleep(0.3)

    try:
        sessions = AudioUtilities.GetAllSessions()
        foundApplication = False

        for session in sessions:
            if session.Process and '1cv8' in session.Process.name():
                foundApplication = True

        assert foundApplication == True

    except AssertionError:
        BugReport.write('1','2','Воспроизводится звуковой файл','Звуковой файл не воспроизвёлся')

        assert False, 'Шаг 2 - ПРОВАЛ, Причина: Звуковой файл не воспроизвёлся'
