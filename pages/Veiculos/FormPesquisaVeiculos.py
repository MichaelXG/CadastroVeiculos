import streamlit as st
from Controllers.PadraoController import *
import streamlit_antd_components as sac
import Utils as ut
from pages.Home.Create_Home import Create_Home 
    
def Form_PesquisaVeiculos():  

    ut.Divisor('Pesquisar Veículos', 'search', 'rgb(20,80,90)', 'key_Veiculos01')

    with st.form(key = 'form_Veiculos_pesquisar', clear_on_submit = False):
        row_0_col1, row_0_col2, row_0_col3 = st.columns([2, 2, 2])  
        row_1_col1, row_1_col2 = st.columns([8, 0.01])  
        row_2_col1, row_2_col2, row_2_col3, row_2_col4, row_2_col5= st.columns([2, 2, 1, 2, 2]) 
        
         # Linha 00
        with row_0_col1:
            prioridade = st.selectbox('Modelo', modelos_carros_p, index=0, placeholder='Selecione o Modelo do Veiculos...')
                
        with row_0_col2:
            categoria = st.selectbox('Ano', anos_p, index=0, placeholder='Selecione a Ano do Veiculos...')
        
        with row_0_col3:
            concluida = st.selectbox('Parcelas', parcelas_p, index=0, placeholder='Selecione a Parcela...')
 
        with row_1_col1:
            sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key='key_divisor')
        with row_1_col2:   
            st.write('')

        with row_2_col1:   
            st.write('')
        
        with row_2_col2:
           st.write('')   
            
        with row_2_col3: 
            form_submit_button_peqsuisar = st.form_submit_button('Pesquisar')
            
        with row_2_col4: 
            st.write('') 
        
        with row_2_col5: 
            st.write('') 
            
        if form_submit_button_peqsuisar:
            if prioridade is not None and categoria is not None and concluida is not None:
                # Chama a função listar_Veiculos com os filtros selecionados
                df_filtrado = listar_veiculos(prioridade, categoria, concluida)

                # Mostra as Veiculos filtradas em um DataFrame do Pandas
                if not df_filtrado.empty:
                    st.dataframe(df_filtrado, use_container_width=True)
                else:
                    st.write("Não há Veiculos correspondentes aos filtros selecionados.")        
            else:
                ut.Alerta('','Parametros para a pesguisa incompleto')   
    
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'key_Veiculos02')