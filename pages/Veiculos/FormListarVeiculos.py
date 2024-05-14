import streamlit as st
from Controllers.PadraoController import *
import Utils as ut

def Form_ListarVeiculos(pModelo, pAno, pParcelas):  
    
    ut.Divisor('Listar Veículos', 'ca', 'rgb(20,80,90)', 'ListarVeiculo01')

    with st.container(border=True):
        # Chama a função listar_Veiculos com os filtros selecionados
        df_filtrado = listar_veiculos(pModelo, pAno, pParcelas)

        # Mostra as Veiculos filtradas em um DataFrame do Pandas
        if not df_filtrado.empty:
            st.dataframe(df_filtrado, hide_index=True)
        else:
            st.write("Não há Veículos correspondentes aos filtros selecionados.")
           
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'ListarVeiculo02')
