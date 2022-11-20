import pandas as pd
from src.AspiradorInteligente import AspiradorInteligente

if '__main__' == __name__:
    input:pd.DataFrame = pd.read_csv('files/dataset.csv')
    vetor:list[str] = [x for x in input['caminho'].tolist()[0]]
    aspirador:AspiradorInteligente = AspiradorInteligente()
    print(aspirador.computer(10, 10, 'N', ['F', 'D']))