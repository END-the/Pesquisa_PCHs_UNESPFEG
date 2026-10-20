import pandas as pd
from openpyxl import load_workbook
import xlrd

potencia = []
Usaveis = []

workbook = xlrd.open_workbook('HidreletricasInfo.xls')
sheet = workbook.sheet_by_index(0)

row_data_nome = sheet.col_values(1)
print("Nome", row_data_nome)

row_data_alt = sheet.col_values(5)
print("Altura Queda", row_data_alt)

row_data_va = sheet.col_values(7)
print("Vazão", row_data_va)

for i in range(1, len(row_data_nome)):
    if row_data_alt[i] == '' or row_data_va[i]=='' :
        print(row_data_nome[i], "Não é abitivel")
    else:
        print(row_data_nome[i], "É abitivel")
        Usaveis.append(row_data_nome[i])
        p = 1*1*9.8*row_data_alt[i]*row_data_va[i]
        potencia.append(p)
        '''considerando rendimento de 100%, densidade da agua de 1g/m³, gravidade 9.8m/s'''

print(Usaveis)
print(potencia)

row_data_p = sheet.col_values(4)
print("Potencia nominal", row_data_p)

for i in range(len(Usaveis)):
    print("\nNome: ", Usaveis[i])
    print("Potencia: ", potencia[i])