# вариант запроса Д
# вариант предметной области 10 : Браузер - Компьютер
from operator import itemgetter

class Browser:
    def __init__(self, id, name, popularity, computer_id):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.computer_id = computer_id

class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class BrowComp:
    def __init__(self, brow_id, comp_id):
        self.brow_id = brow_id
        self.comp_id = comp_id

computers = [
    Computer(1, "PC1"),
    Computer(2, "PC2"),
    Computer(3, "PC3"),
    Computer(4, "PC4"),
    Computer(5, "PC5"),
    Computer(6, "PC6")
]

browsers = [
    Browser(1, "Chrome", 100, 1),
    Browser(2, "Opera", 70, 2),
    Browser(3, "Firefox", 80, 2),
    Browser(4, "Safari", 50, 4),
    Browser(5, "Edge", 10, 5),
    Browser(6, "Vivaldi", 5, 6),
    Browser(7, "Yandex", 25, 6)
]

browsers_computers = [
    BrowComp(1, 1),
    BrowComp(2, 2),
    BrowComp(2, 3),
    BrowComp(3, 4),
    BrowComp(3, 5),
    BrowComp(3, 6),
    BrowComp(4, 7),
    BrowComp(4, 1),
    BrowComp(5, 1),
    BrowComp(5, 2),
    BrowComp(5, 3),
    BrowComp(5, 4),
    BrowComp(6, 4),
    BrowComp(6, 7),
]


def main():
    # соединение данных один-ко-многим
    one_to_many = [(br.name, br.popularity, co.name) for co in computers
                   for br in browsers if br.computer_id == co.id]

    # соединение данных многие-ко-многим

    many_to_many_temp = [(co.name, brco.comp_id, brco.brow_id)
                         for co in computers for brco in browsers_computers
                         if co.id == brco.comp_id]

    many_to_many = [(br.name, br.popularity, comp_name)
                    for comp_name, comp_id, brow_id in many_to_many_temp
                    for br in browsers if br.id == brow_id]

    print('Пункт Д1')
    res1 = []
    for i in one_to_many:
        if i[0][-1:] == "i":
            res1.append(i[0:3:2])
    print(res1)

    print('\nПункт Д2')
    res2_unsorted = []
    for co in computers:
        co_browsers = list(filter(lambda i: i[2] == co.name, one_to_many))
        if len(co_browsers) > 0:
            co_popularity = [listeners for _, listeners, _ in co_browsers]
            co_popularity_sum = sum(co_popularity)
            co_popularity_count = len(co_popularity)
            co_popularity_average = co_popularity_sum / co_popularity_count
            res2_unsorted.append((co.name, int(co_popularity_average)))
    res2 = sorted(res2_unsorted, key=itemgetter(1), reverse=True)
    print(res2)

    print('\nПункт Д3')
    res3 = {}
    for co in computers:
        if co.name[0] == "P":
            co_browsers = list(filter(lambda i: i[2] == co.name, many_to_many))
            dr_details_types = [x for x, _, _ in co_browsers]
            res3[co.name] = dr_details_types
    print(res3)


if __name__ == '__main__':
    main()
