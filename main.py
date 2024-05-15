import streamlit as st
import streamlit_antd_components as sac
import pages.Veiculos.FormVeiculos as fv  
import pages.Veiculos.FormPesquisaVeiculos as fpv  
from pages.Home.Create_Home import Create_Home    
from pages.Login.Login import login_page    
from Controllers.PadraoController import *  

def Main():
    # Limpar os parâmetros necessários aqui
    # Por exemplo, você pode limpar os parâmetros da sessão do Streamlit:
    st.session_state.Modelo = None
    st.session_state.Ano = None
    st.session_state.Descricao = ''
    st.session_state.Valor_Entrada = None
    st.session_state.Parcelas = None
    
    # Menu
    with st.sidebar:
        st.image('https://detectasat.com.br/wp-content/uploads/2017/10/gerenciamento-e-controle-de-frotas-detectasat-fortaleza.png', width=None, use_column_width='auto') 
        selected_usu = sac.menu([
            sac.MenuItem(f'Bem-vindo, "{st.session_state.Apelido_L}"!', icon=sac.BsIcon(name='person-bounding-box', color='rgb(20,80,90)')),   
            # Usuário Logado
            sac.MenuItem(type='divider'),
            sac.MenuItem('Logout', icon=sac.BsIcon(name='box-arrow-left', color='red')),
            sac.MenuItem(type='divider'),
        ], color='rgb(20,80,90)', open_all=False, return_index=False, index=0, key='Menu_login')
    
    if selected_usu == 'Logout':
        st.session_state.logged_in = False
        st.rerun()  
          
    with st.sidebar:
        selected = sac.menu([
            sac.MenuItem('Menu Principal', icon=sac.BsIcon(name='person-bounding-box', color='rgb(20,80,90)')),   
             # Empresa
            sac.MenuItem(type='divider'),
            sac.MenuItem('Novo Veículo',  icon=sac.BsIcon(name='car-front-fill', color='rgb(20,80,90)'), description='Adicionar novo Veículo'),
            # Clientes
            sac.MenuItem(type='divider'),
            sac.MenuItem('Listar Veículos', icon=sac.BsIcon(name='clipboard2-data', color='rgb(20,80,90)'), description='Listar os Veículos'),

        ], color='rgb(20,80,90)', open_all=False, return_index=False, index=0, key='Menu_principal')
    
    if selected == 'Menu Principal':
        Create_Home()
    elif selected == 'Novo Veículo':
        if __name__ == "__main__":
            fv.Form_veiculos()
    elif selected == 'Listar Veículos':
         if __name__ == "__main__":
            fpv.Form_PesquisaVeiculos()    
          
# Lógica para alternar entre as páginas com base na ação do usuário
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
 
st.set_page_config(
    page_title="Veículos",
    page_icon=":oncoming_automobile:",
    layout="wide",
    initial_sidebar_state="expanded"
)   
        
if __name__ == "__main__":
    if st.session_state.logged_in:        
        Main()
    else:
        opcao = st.radio("Escolha uma opção:", ["Login"], horizontal= True)
        if opcao == "Login":
            if __name__ == "__main__":
                login_page()
