from colorama import Fore, Back, Style
class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def n1(cls, date):
        new = []
        for i in date.split():
            if i!="-":
                new.append(i)
        return int(new[0]), int(new[1]), int(new[2])

    @staticmethod
    def checking(day, month, year):
        if 0<day<32:
            if 0<month<13:
                if 1900<year<2022:
                    print(Fore.GREEN + "Дата корректна!")
                else:
                    print(Fore.RED + "Год введен неверно!")
            else:
                print(Fore.RED + "Месяц введен неверно!")
        else:
            print(Fore.RED + "День введен неверно!")
    def __str__(self):
        return f"data: {Date.n1(self.date)}"

m = Date("12 - 12 - 2021")
print(m)
print(Date.checking(12, 12, 2004))
print(Date.n1("12 - 22 - 2004"))
print(Date.checking(33, 13, 1907))

