class Drink:
    _SIZES = ['레귤러', '정보']   #0: 레귤러, 1: 정보
    _SUGARS = ['0%', '50%', '기본', '150%']   #0: 0%, 1: 50%, 2: 기본, 3: 150%
    _ICES = ['0%', '50%', '기본', '150%']   #0: 0%, 1: 50%, 2: 기본, 3: 150%

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.size = 0    #0:레귤러, 1: 점보
        self.suger  = 2  #0: 0%, 1: 50%, 2: 기본, 3: 150%
        self.ice  = 2    #0: 0%, 1: 50%, 2: 기본, 3: 150%

    def set_size(self):
        size = input('사이즈를 입력하세요 0: 레귤러, 1: 점보')
        if size == '':  #엔터 누르면 기본값 바로 나오게
            self.size = 0
        else:
            self.size = int(size)

    def set_suger(self):
        suger = input('당도를 입력하세요 0: 0%, 1: 50%, 2: 기본, 3: 150%')
        if suger == '':  # 엔터 누르면 기본값 바로 나오게
            self.suger = 2
        else:
            self.suger = int(suger)

    def set_ice(self):
        ice = input('얼음량을 입력하세요 0: 레귤러, 1: 점보')
        if ice == '':  # 엔터 누르면 기본값 바로 나오게
            self.ice = 2
        else:
            self.ice = int(ice)

    def __str__(self):
        return f'이름: {self.name}\t 가격: {self.price}원\t 사이즈: {Drink._SIZES[self.size]}\t 당도: {Drink._SUGARS[self.suger]}\t 얼음량: {Drink._ICES[self.ice]}'

if __name__ == '__main__':
    잎새거 = Drink('하동녹차오레오', 3900)
    잎새거.set_size()
    잎새거.set_suger()
    잎새거.set_ice()
    print(잎새거)