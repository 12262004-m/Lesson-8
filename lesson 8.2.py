from colorama import Fore, Back, Style
class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

k = input("Введите делимое: ")
l = input("Введите делитель: ")

try:
    k = int(k)
    l = int(l)
    if l == 0:
        raise MyOwnError(Fore.RED + "Делитель не может равняться 0! На 0 делить нельзя!")
except ValueError:
    print(Fore.RED+"Вы ввели не число!")
except MyOwnError as err:
    print(err)
else:
    print(k//l)