import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_elements = set()
        self.items = items
        self.index = 0
        if len(kwargs) != 0:
            self.ignore_case = kwargs
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            for item in self.items:
                temp_item = item
                self.index += 1
                if (temp_item not in self.used_elements) \
                        and not(self.ignore_case and temp_item.swapcase() in self.used_elements):
                    self.used_elements.add(temp_item)
                    return temp_item
            else:
                raise StopIteration

    def __iter__(self):
        return self


def main():
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, ]
    print(data1)
    iter1 = Unique(data1)
    for i in iter1:
        print(i, end=' ')
    print('\n')
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(data2)
    iter2 = Unique(data2)
    for i in iter2:
        print(i, end=' ')
    print('\n')
    print(data2)
    iter3 = Unique(data2, ignore_case=True)
    for i in iter3:
        print(i, end=' ')
    print('\n')
    gen = gen_random.gen_random(3, 1, 3)
    iter4 = Unique(gen)
    for i in iter4:
        print(i, end=' ')


if __name__ == "__main__":
    main()