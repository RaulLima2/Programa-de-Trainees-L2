import pandas as pd
from src.AspiradorInteligente import AspiradorInteligente

if '__main__' == __name__:
    input:pd.DataFrame = pd.read_csv('files/dataset.csv')
    x:int = input['x'][1]
    y:int = input['y'][1]
    vetor:list[str] = [x for x in input['caminho'].tolist()[1]]
    aspirador:AspiradorInteligente = AspiradorInteligente()
    print(aspirador.computer(x, y, vetor))