from drink import Drink

class Bubbletea(Drink):
    _PEARLS = ['타피오카', '코코', '알로에', '곤약젤리']
    def __init__(self, name, price):
        super().__init__(name, price)
        self.pearl = 0  #0: 타피오카, 1: 코코, 2: 알로에, 3: 곤약젤리

    def set_pearl(self):
        pearl = input('펄을 고르세요. 0: 타피오카, 1: 코코, 2: 알로에, 3: 곤약젤리')
        if pearl == '':
            self.pearl = 0
        else:
            self.pearl = int(pearl)

    def __str__(self):
        return super().__str__()+f'\t 펄: {Bubbletea._PEARLS[self.pearl]}'

if __name__ == '__main__':
    종아거 = Bubbletea('흑당 버블티', 4200)
    종아거.set_ice()
    종아거.set_pearl()
    print(종아거)