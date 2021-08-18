import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self, uptime):
        while uptime > 0:
            if self.__color == 'red':
                self.__color = 'green'
                uptime -= 9
                print('\033[31m\033[41mкрасный')
                time.sleep(7)
                print('\033[33m\033[43mжелтый')
                time.sleep(2)
            elif self.__color == 'green':
                self.__color = 'red'
                uptime -= 9
                print('\033[32m\033[42mзеленый')
                time.sleep(7)
                print('\033[33m\033[43mжелтый')
                time.sleep(2)


traffic_light = TrafficLight('red')
traffic_light.running(12)

traffic_light = TrafficLight('green')
traffic_light.running(12)
