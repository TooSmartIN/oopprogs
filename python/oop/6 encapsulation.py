from typing import Deque


class Sq1:
    def __init__(self):
        self.__no = 9

    def square(self):
        return(self.__no*self.__no)

s = Sq1()
print("the square of is=", s.square())