import streamlit as st
import Utils as ut

def Create_Home():  
    with st.container(): 
        ut.Divisor('Gerenciador de Veículos', 'car-front-fill','rgb(20,80,90)', 'Home01')
        st.write('\n \n')
        col1, col2, col3 = st.columns([1, 6, 1])

        with col1:
            st.write('')

        with col2:
            st.image('https://detectasat.com.br/wp-content/uploads/2017/10/gerenciamento-e-controle-de-frotas-detectasat-fortaleza.png', width=300, use_column_width='auto') 
            st.write('Exercício 4 - Uma empresa de automóveis está criando um sistema para cadastrar novos veículos, crie um algoritmo \
    capaz de registrar novos veículos a partir de entradas fornecidas pelo usuário. As informações necessárias\
    são: Modelo, ano, descrição, valor de entrada, valor de parcela e valor total. \
    O valor de entrada é sempre 12% do valor total do veículo e o número máximo de parcelas é sempre até 18 \
    parcelas do valor restante.')
        
        with col3:
            st.write('')
        
        st.write('\n \n')
        ut.Divisor('Copyright (c) 2024', '', 'rgb(20,80,90)', 'Home02')
