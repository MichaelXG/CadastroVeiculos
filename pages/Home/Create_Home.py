import streamlit as st
import Utils as ut

def Create_Home():  
    with st.container(): 
        ut.Divisor('Gerenciador de Veículos', 'car-front-fill','rgb(20,80,90)', 'Home01')
        st.write('\n \n')
        col1, col2, col3 = st.columns([1, 6, 1])

        with col1:
            st.write(' ')

        with col2:
            st.image('https://detectasat.com.br/wp-content/uploads/2017/10/gerenciamento-e-controle-de-frotas-detectasat-fortaleza.png', width=300, use_column_width='auto') 

        with col3:
            st.write(' ')
        
        st.write('\n \n')
        ut.Divisor('Copyright (c) 2024', '', 'rgb(20,80,90)', 'Home02')
