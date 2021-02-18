from colorama import Fore, Back, Style
class Error:
    def __init__(self, *args):
        self.list_1 = []
    def t(self):
        while True:
            try:
                    k = int(input(Fore.WHITE + "Введите элементы для добавления в список: "))
                    self.list_1.append(k)
                    print(Fore.GREEN + f"Ваш список: {self.list_1}")
            except:
                print(Fore.RED + "Вы введи неправильный тип переменной!")
                break


l = Error()
print(l.t())

