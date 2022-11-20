class Aspirador:
    _coord_x:int = 0
    _coord_y:int = 0
    _orientacao:str = 'N'

    
    def __init__(self):
        self._coord_x = 0
        self._coord_y = 0
        self._orientacao = 'N'

    get_coord_x = lambda self: self._coord_x
    get_coord_y = lambda self: self._coord_y
    get_orientacao = lambda self: self._orientacao
    set_coord_x = lambda self, x: setattr(self, '_Aspirador_coord_x', x)
    set_coord_y = lambda self, y: setattr(self, '_Aspirador_coord_y', y)
    set_orientacao = lambda self, o: setattr(self, '_Aspirador_orientacao', o)