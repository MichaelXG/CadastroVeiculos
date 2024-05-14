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
        
    if 'descricao' not in st.session_state:
        st.session_state.descricao = ''
    
    if 'valor_entrada' not in st.session_state:
        st.session_state.valor_entrada = 0
        
    if 'parcelas' not in st.session_state:
        st.session_state.parcelas = None
 
    ut.Divisor('Adicionar veiculos', 'car-front-fill', 'rgb(20,80,90)', 'key_veiculo1')

    with st.form(key = 'form_veiculo', clear_on_submit = True):
        row_0_col1, row_0_col2, row_0_col3 = st.columns([2, 2, 4])  
        row_1_col1, row_1_col2 = st.columns([8, 0.01])  
        row_2_col1, row_2_col2 = st.columns([4, 4])  
        row_4_col1, row_4_col2, row_4_col3, row_4_col4, row_4_col5= st.columns([2, 2, 1, 2, 2]) 
        
        # Linha 00
        with row_0_col1:
            st.session_state.modelo = st.selectbox('Modelo', modelos_carros, key='key_modelos_carros', index=None, placeholder='Selecione o modelo do veículo...')
            if not st.session_state.Modelo:
                st.error('O campo "Modelo" é Obrigatorio.')
                
        with row_0_col2:
            st.session_state.ano = st.selectbox('Ano', anos_dinamico, key='key_ano', index=None, placeholder='Selecione o Ano do veículo...')
            if not st.session_state.ano:
                st.error('O campo "Ano" é Obrigatorio.')        
        
        with row_0_col3:
            st.write('')
            
        # Linha 01
        with row_1_col1:
            st.session_state.descricao = st.text_input('Descrição', key='key_Descricao')
            if not st.session_state.descricao:
                st.error('O campo "Descrição" é Obrigatorio.')
        
        with row_1_col2:   
            st.write('') 
        
        # Linha 02
        with row_2_col1:
            st.session_state.valor_entrada = st.number_input('Vr. Entrada', key='key_valor_entrada', min_value=1.00, max_value=100000.00, step=1.00, format="%.2f")

            if not st.session_state.valor_entrada:
                st.error('O campo "Vr. Entrada" é Obrigatorio.')
        
        with row_2_col2:   
            st.session_state.parcelas = st.selectbox('Parcelas', parcelas, key='key_parcelas', index=None, placeholder='Selecione as parcelas...')
            if not st.session_state.parcelas:
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
            if st.session_state.modelo and st.session_state.ano and st.session_state.descricao and st.session_state.valor_entrada and st.session_state.parcelas:
                adicionar_veiculos(st.session_state.modelo, st.session_state.ano, st.session_state.descricao, st.session_state.valor_entrada, st.session_state.parcelas)           
            else:
                ut.Alerta('','Parametros para incluir um veículo incompleto')   
    
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'key_veiculo2')