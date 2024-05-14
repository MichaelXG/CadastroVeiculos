import streamlit as st
from Controllers.PadraoController import *
import streamlit_antd_components as sac
import Utils as ut
from pages.Home.Create_Home import Create_Home 
    
def Form_veiculos():  
    if "widget" not in st.session_state:
        st.session_state.widget = ""
   
    if 'Modelo' not in st.session_state:
        st.session_state.Modelo = None
    
    if 'Ano' not in st.session_state:
        st.session_state.Ano = None     
        
    if 'Descricao' not in st.session_state:
        st.session_state.Descricao = ''
    
    if 'Valor_Entrada' not in st.session_state:
        st.session_state.Valor_Entrada = 0
        
    if 'Parcelas' not in st.session_state:
        st.session_state.Parcelas = None
 
    ut.Divisor('Adicionar veiculos', 'car-front-fill', 'rgb(20,80,90)', 'key_veiculo1')

    with st.form(key = 'form_veiculo', clear_on_submit = True):
        row_0_col1, row_0_col2, row_0_col3 = st.columns([2, 2, 4])  
        row_1_col1, row_1_col2 = st.columns([8, 0.01])  
        row_2_col1, row_2_col2 = st.columns([4, 4])  
        row_4_col1, row_4_col2, row_4_col3, row_4_col4, row_4_col5= st.columns([2, 2, 1, 2, 2]) 
        
        # Linha 00
        with row_0_col1:
            st.session_state.Modelo = st.selectbox('Modelo', modelos_carros, key='key_Modelos_carros', index=None, placeholder='Selecione o Modelo do veículo...')
            if not st.session_state.Modelo:
                st.error('O campo "Modelo" é Obrigatorio.')
                
        with row_0_col2:
            st.session_state.Ano = st.selectbox('Ano', anos_dinamico, key='key_Ano', index=None, placeholder='Selecione o Ano do veículo...')
            if not st.session_state.Ano:
                st.error('O campo "Ano" é Obrigatorio.')        
        
        with row_0_col3:
            st.write('')
            
        # Linha 01
        with row_1_col1:
            st.session_state.Descricao = st.text_input('Descrição', key='key_Descricao')
            if not st.session_state.Descricao:
                st.error('O campo "Descrição" é Obrigatorio.')
        
        with row_1_col2:   
            st.write('') 
        
        # Linha 02
        with row_2_col1:
            st.session_state.Valor_Entrada = st.number_input('Vr. Entrada', key='key_Valor_Entrada', min_value=1.00, max_value=100000.00, step=1.00, format="%.2f")

            if not st.session_state.Valor_Entrada:
                st.error('O campo "Vr. Entrada" é Obrigatorio.')
        
        with row_2_col2:   
            st.session_state.Parcelas = st.selectbox('Parcelas', parcelas, key='key_Parcelas', index=None, placeholder='Selecione as Parcelas...')
            if not st.session_state.Parcelas:
                st.error('O campo "Parcelas" é Obrigatorio.')   
         
        # Linha 04        
        with row_4_col1:
            sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key='key_divisor')
        with row_4_col2:   
            st.write('')

        with row_4_col1:   
            st.write('')
        
        with row_4_col2:
           st.write('')   
            
        with row_4_col3: 
            form_submit_button_veiculo = st.form_submit_button('Salvar')
            
        with row_4_col4: 
            st.write('') 
        
        with row_4_col5: 
            st.write('') 
            
        if form_submit_button_veiculo:
            if st.session_state.Modelo and st.session_state.Ano and st.session_state.Descricao and st.session_state.Valor_Entrada and st.session_state.Parcelas:
                adicionar_veiculos(st.session_state.Modelo, st.session_state.Ano, st.session_state.Descricao, st.session_state.Valor_Entrada, st.session_state.Parcelas)           
            else:
                ut.Alerta('','Parametros para incluir um veículo incompleto')   
    
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'key_veiculo2')