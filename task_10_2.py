from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def textile(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = int(size)

    @property
    def textile(self):
        return round(self.size/6.5 + 0.5, 1)


class Suit(Clothes):
    def __init__(self, height):
        self.height = int(height)

    @property
    def textile(self):
        return round((2*self.height + 0.3)/100, 1)


coat_1 = Coat(input('Введите размер пальто '))
suit_1 = Suit(input('Введите рост '))
print(f'На пальто потребуется {coat_1.textile} метров ткани')
print(f'На костюм потребуется {suit_1.textile} метров ткани')
print(f'Всего потребуется {round(coat_1.textile + suit_1.textile, 1)} метров ткани')
