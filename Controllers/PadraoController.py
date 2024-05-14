'''
Class for do PadraoController
'''
import datetime

# criar lista de Login
login = []

login = [{"Apelido":'Suporte',"Password": '123'},
         {"Apelido":'Visitante',"Password": 'visitante123'},
         {"Apelido":'Maria',"Password": 'Maria@123'}
        ]
apelidos = ['Suporte', 'Visitante', 'Maria']

# Lista para armazenar as veiculos
veiculos = []

veiculos = [{"Modelo":'Creta', "Ano":'2017'," Descrição": 'Creta pulse 1.6',"Vr. Entrada": 12000.00,"Parcelas": '10',"Vr. Parcela":8800.00 ,"Vr. Total":100000.00}]

import Utils as ut
import pandas as pd 
import streamlit as st

def calcular_Valor_Parcelas(Parcelas, Valor_Entrada):
    vr_total =  Valor_Entrada / (12 / 100)
    # print('vr_total', vr_total)
    vr_parcela =  (vr_total - Valor_Entrada) / int(Parcelas)
    return vr_parcela
 
def calcular_Valor_Total(Valor_Entrada):
    vr_total =  Valor_Entrada / (12 / 100)
    return vr_total
   
#  Função para adicionar uma novo veículo
#  Modelo, ano, descrição, valor de entrada, valor de parcela e valor total.
def adicionar_veiculos(Modelo, Ano, Descricao, Valor_Entrada, Parcelas):
    veiculo = {
        "Modelo": Modelo,
        "Ano": Ano,
        "Descrição": Descricao,
        "Vr. Entrada": Valor_Entrada,
        "Parcelas": Parcelas,
        "Vr. Parcela": calcular_Valor_Parcelas(Parcelas, Valor_Entrada),
        "Vr. Total": calcular_Valor_Total(Valor_Entrada)
    }
    
    veiculos.append(veiculo)
    st.write("Veículo adicionado com sucesso!")

# Função para listar todas as veiculos ou usando um filtro
def listar_veiculos(pModelo, pAno, pParcelas):
    if not veiculos:
        return pd.DataFrame()  # Retorna um DataFrame vazio se não houver veiculos
        
    df = pd.DataFrame(veiculos)
    df['Vr. Entrada'] = df['Vr. Entrada'].map(ut.format_money)
    df['Vr. Parcela'] = df['Vr. Parcela'].map(ut.format_money)
    df['Vr. Total']   = df['Vr. Total'].map(ut.format_money)
    df.insert(0, 'ID', range(1, len(df) + 1))
    
    # Aplicar os filtros
    if (pModelo == 'Todos' and pAno == 'Todos' and pParcelas == 'Todas') or \
       (pModelo is None and pAno is None and pParcelas is None):
        df_filtrado = df
    elif pModelo == 'Todos' and pAno == 'Todos':
        df_filtrado = df[df['Parcelas'] == pParcelas]
    elif pModelo == 'Todos' and pParcelas == 'Todas':
        df_filtrado = df[df['Ano'] == pAno]
    elif pAno == 'Todos' and pParcelas == 'Todas':
        df_filtrado = df[df['Modelo'] == pModelo]
    elif pParcelas == 'Todas':
        df_filtrado = df[(df['Modelo'] == pModelo) & (df['Ano'] == pAno)]
    elif pModelo == 'Todas':
        df_filtrado = df[(df['Ano'] == pAno) & (df['Parcelas'] == pParcelas)]
    elif pAno == 'Todos':
        df_filtrado = df[(df['Modelo'] == pModelo) & (df['Parcelas'] == pParcelas)]
    elif pModelo is None:
        df_filtrado = df[(df['Ano'] == pAno) & (df['Parcelas'] == pParcelas)]
    elif pAno is None:
        df_filtrado = df[(df['Modelo'] == pModelo) & (df['Parcelas'] == pParcelas)]
    else:
        df_filtrado = df[(df['Modelo'] == pModelo) & (df['Ano'] == pAno) & (df['Parcelas'] == pParcelas)]
    
    return df_filtrado

# Paramentros para cadastro
modelos_carros = ["Gol","Palio","Onix","HB20","Civic","Corolla","Fiesta","Creta","Celta","Uno","Fusca","Sandero","Fox","Focus","Prisma","Siena","Etios","Ecosport","Kwid","Captur","Tracker"]

parcelas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
# Parametros para pesquisa
modelos_carros_p = ["Todos","Gol","Palio","Onix","HB20","Civic","Corolla","Fiesta","Celta","Uno","Fusca","Sandero","Fox","Focus","Prisma","Siena","Etios","Ecosport","Kwid","Captur","Tracker"]

parcelas_p = ['Todas', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']

#  Gerar uma lista de anos  dinamica
# Obter o ano atual
ano_atual = datetime.datetime.now().year
# Número de anos para incluir após o ano atual
ultimos_anos = 49

# Criar a lista dos últimos 50 anos
anos_dinamico = [str(ano) for ano in range(ano_atual, ano_atual - ultimos_anos, -1)]
anos_p = ['Todos'] + anos_dinamico