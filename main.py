
from dragonfly import RunCommand
import pytest

#Проверяем установленные пакеты Python, если компонентов не достаточно - докачиваем из списка
cmd = RunCommand('python -B -m pip install -r requirements.txt')
cmd.execute()
cmd.process.wait()

#Запускаем тесты
cmd = RunCommand('python -B -m pytest -v tests/ -p no:cacheprovider')
cmd.execute()

input()