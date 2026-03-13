class CarMixIn:
    def ready(self):
        print("Car is ready to drive")
    def start(self):
        print(f"{self.name}가 {self.speed} 속도로 달립니다." )

class Performance():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.ready()

class SuperCar( CarMixIn, Performance):
    def show_info(self):
        print(f"SuperCar name: {self.name}는, speed: {self.speed}의 성능을 가지고 있습니다.")
    # def start(self):
    #     print("메롱")  이함수로 오버라이딩됨

supercar = SuperCar("람보르기니", 300)
supercar.show_info()
supercar.start()