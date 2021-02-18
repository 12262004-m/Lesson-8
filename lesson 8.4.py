class Sclad:
    def init(self, name, price, number, year, *args):
        self.name = name
        self.price = price
        self.number = number
        self.year = year
        self.my_d = []
        self.all = []
        self.new_dict = {'Модель:': self.name, "Год производства": self.year, 'Цена за ед': self.price,
        'Количество': self.number}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.number}'

    def new(self):
        try:
            model = input(f"Введите модель: ")
            year = int(input(f"Введите год производства: "))
            price = int(input(f"Стоимость: "))
            number = int(input(f"Нужно напечатать: "))
            d = {'Модель устройства': model, "Год выпуска": year, 'Цена за ед': price, 'Количество страниц': number}
            self.my_d.append(d)
            self.new_dict.update(d)
            print(f'Список оргтехники на складе: {self.new_dict}')
        except:
            return f"Вы неправильно ввели данные!"

        print(f'Для выхода - S(stop), для продолжение - C(continue)')
        s = input(f'---> ')
        if s == 'S' or s == 's':
            self.all.append(self.new_dict)
            print(f'Весь склад -\n {self.all}')
            return f'Выход'
        else:
            return Sclad.new(self)
class Printer(Sclad):
    def p(self):
        return f'Нужно напечатать {self.number} страниц'

class Scanner(Sclad):
    def s(self):
        return f'Нужно отсканировть {self.number} страниц'

class Xerox(Sclad):
    def x(self):
        return f'Нужно отксерокопировать {self.number} страниц'

unit_1 = Printer()
unit_2 = Scanner()
unit_3 = Xerox()
print(unit_1.new())
print(unit_2.new())
print(unit_3.new())
print(unit_1.p())
print(unit_3.x())




