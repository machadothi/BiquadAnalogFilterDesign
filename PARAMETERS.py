import numpy as np
import pandas as pd


def parameters(a, b, c, d):

    f = pd.read_excel('valores.xls',)
    df1 = pd.DataFrame(f, columns=['RESISTORES','CAPACITORES'])
    res = df1['RESISTORES']
    cap = df1['CAPACITORES']
    cap = cap[~cap.isnull()]
    res_ind = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10']

    res_com = np.zeros([10, 1])
    ct = 0

    #CALCULANDO OS COMPONENTES TEÓRICOS
    k = 1
    R1 = 1 / a
    R2 = 1 / (np.sqrt(b))
    R7 = R2
    R10 = R2
    R3 = R2
    R4 = 1 / ((a - c) * k)
    R9 = 1 / (k * np.sqrt(b))
    R8 = (a - c) / (b - d)
    C1 = 1
    C2 = C1
    R5 = 0.001
    R6 = R5

    #MANIPULANDO PARA VALORES REAIS

    val = {'Resistores': [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10], 'Capacitores': [C1, C2]}
    res_calc = pd.Series(val['Resistores'])
    cap_calc = pd.Series(val['Capacitores'])
    t = res_calc.min()

    while t < 1000:

        res_calc = res_calc * 1000
        cap_calc = cap_calc / 1000
        t = res_calc.min()

    #GUARDANDO NOS VETORES

    RES = pd.DataFrame(res_calc.values, index=res_ind, columns=['R. CALCULADOS'])
    CAP = pd.DataFrame(cap_calc.values, columns=['C. CALCULADOS'])

    #SELECIONANDO VALORES COMERCIAIS

    for ind in res_calc.values:

        res_com[ct] = np.min(res[res > ind])
        ct = ct+1

    #UNINDO NUM SÓ VETOR

    RES = pd.concat([RES, pd.DataFrame(res_com, index=res_ind, columns=['R. COMERCIAIS'])], axis=1)

    return RES, CAP
