from coffee import  Coffee
from bubbletea import  Bubbletea

class Order:
    def __init__(self):
        self.menu = []
        self.order_menu = []
        self.set_menu()

    def set_menu(self):
        self.menu.append(Coffee('아메리카노', 1800))
        self.menu.append(Bubbletea('타로버블티', 3200))

    def show_menu(self):
        for i, drink in enumerate(self.menu):
            print(f'{i+1}. {drink}')

    def add_order_menu(self):
        #무한 반복
        while True:
            #show menu
            self.show_menu()
            #메뉴 선택
            number = input('메뉴를 선택하세요: ')
            #음료 생성
            if number == '1':
                new_drink = Coffee('아메리카노', 1800)
            elif number == '2':
                new_drink = Bubbletea('타로버블티', 3200)
            #음료 옵션 주문하자
            new_drink.order()
            #order_menu에 추가하자
            self.order_menu.append(new_drink)
            # 더 주문하시겠습니까 문자 enter, n:면 break, y면 반복
            is_add = input('더 주문하시겠습니까? (y/n) ')
            if is_add  == 'n' or is_add == '':
                break

    def sum_price(self):
        total_price = 0
        for drink in self.order_menu:
            total_price += drink.price
        return  total_price

    def __str__(self):
        s = '-' * 20 + '주문 내역' + '-' * 20 + '\n'
        for drink in self.order_menu:
            s += str(drink) + '\n'
        s += f'총 금액은 {self.sum_price()}원 입니다.'
        return  s

if __name__ == '__main__':
    order = Order()
    #order.show_menu()
    order.add_order_menu()
    print(order)