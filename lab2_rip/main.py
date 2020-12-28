from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from prettytable import PrettyTable


def main():
    r = Rectangle("красного", 1, 2)
    c = Circle("зеленого", 3)
    s = Square("жёлтого", 4)    
    table = PrettyTable()
    table.field_names = ['Таблица фигур']
    table.add_row([r])
    table.add_row([c])
    table.add_row([s])
    print(table)


if __name__ == "__main__":
    main()