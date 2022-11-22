from abc import ABC, abstractmethod
from collections import deque
class Aspirador(ABC):
    _coord_x:int = 0
    _coord_y:int = 0
    _orientacao:str = 'N'
    _orientacoes:deque[str] = deque(['N', 'L', 'S', 'O'])

    
    def __init__(self):
        self._coord_x = 0
        self._coord_y = 0
        self._orientacao = 'N'

    def get_coord_x(self) -> int:
        return self._coord_x
    

    def get_coord_y(self) -> int :
        return self._coord_y
    

    def get_orientacao(self) -> int:
        return self._orientacao
    
    def get_orientacoes(self) -> deque[str]:
        return self._orientacoes

    def set_coord_x(self, x:int) -> None:
        self._coord_x = x
    
    def set_coord_y(self, y:int) -> None:
        self._coord_y = y
    
    def set_orientacao(self, orientacao:str) -> None:
        self._orientacao = orientacao
    
    def set_orientacoes(self, r:int) -> None:
        self._orientacoes.rotate(r)