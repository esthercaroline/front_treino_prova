import streamlit as st
import api_utils as uts

st.title("Cardápio Online")

st.write('Cadastro de pratos')
st.divider()
with st.form("Formulário de cadastro",clear_on_submit=True):
    col1 = st.columns(2) 
    with col1:
        nome = st.text_input("Digite o Nome do prato",placeholder="Nome do prato")
        descricao = st.text_input("Digite a descrição do prato",placeholder="Descrição")
        tipo = st.text_input("Digite o o tipo do prato",placeholder="Tipo")
        preco = st.text_input("Digite o preço",placeholder="Preço")

    if st.form_submit_button("Enviar Formulário"):
        if not (nome and descricao and tipo and preco):
                st.error("Por favor, preencha todos os campos antes de enviar o formulário.")
        data = {'nome': nome ,'descricao': descricao, 'preco':preco, 'tipo': tipo}
        salvou, mensagem = uts.registra_prato(data)
        if salvou:
            st.balloons()
            st.success(f'Prato {nome} cadastrado com sucesso!')
        else: 
            st.error(mensagem)
