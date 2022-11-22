from src.model.Aspirador import Aspirador

class AspiradorInteligente(Aspirador):
    limit_x:int = 0
    limit_y:int = 0

    def mover(self, movimento:str):
        self.andar_norte(movimento)
        self.andar_sul(movimento)
        self.andar_leste(movimento)
        self.andar_oeste(movimento)

    def andar_norte(self, movimento:str):
        if self.get_orientacao() == 'N':
            if movimento == 'F' and self.get_coord_y() < self.limit_y:
                    self.set_coord_y(self.get_coord_y() + 1)
            elif movimento == 'T' and self.get_coord_y() > 0:
                self.set_coord_y(self.get_coord_y() - 1)
    
    def andar_leste(self, movimento:str):
        if self.get_orientacao() == 'L':
            if movimento == 'F' and self.get_coord_x() < self.limit_x:
                self.set_coord_x(self.get_coord_x() + 1)
            elif movimento == 'T' and self.get_coord_x() > 0:
                self.set_coord_x(self.get_coord_x() - 1)
    
    def andar_sul(self, movimento:str):
        if self.get_orientacao() == 'S':
            if movimento == 'F' and self.get_coord_y() > 0:
                self.set_coord_y(self.get_coord_y() - 1)
            elif movimento == 'T' and self.get_coord_y() < self.limit_y:
                self.set_coord_y(self.get_coord_y() + 1)
    
    def andar_oeste(self, movimento:str):
        if self.get_orientacao() == 'O':
            if movimento == 'F' and self.get_coord_x() > 0:
                self.set_coord_x(self.get_coord_x() - 1)
            elif movimento == 'T' and self.get_coord_x() < self.limit_x:
                self.set_coord_x(self.get_coord_x() + 1)

    # Atualiza a orientação do aspirador para a direita ou esquerda
    # de acordo com a orientação atual
    def orientar(self, rotacao:str):
        if rotacao == 'D' or rotacao == 'E':
            nova_orientacao:str = ''
            if rotacao == 'D':
                self.set_orientacoes(-1)
                nova_orientacao = self.get_orientacoes()[0]
            elif rotacao == 'E':
                self.set_orientacoes(1)
                nova_orientacao = self.get_orientacoes()[0]
            self.set_orientacao(nova_orientacao)

    def computer(self, x:int, y:int, comandos:list[str]):
        self.limit_x = x
        self.limit_y = y
        for comando in comandos:
            self.orientar(comando)
            self.mover(comando)
        return self.get_orientacao(), self.get_coord_x(), self.get_coord_y()
