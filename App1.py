import streamlit as st

# Configuração inicial da página (Título e Ícone na aba do navegador)
st.set_page_config(
    page_title="Calculadora Vibe Coding",
    page_icon="🧮",
    layout="centered"
)

# 1. Título principal com ícone amigável
st.title("🧮 Calculadora com Botões de Operação")
st.write("Um aplicativo elegante e interativo desenvolvido em Python com Streamlit para iniciantes.")

# Divisor visual
st.markdown("---")

# 2. Dois campos de entrada numérica com valores padrão definidos como 0.0
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Digite o primeiro número:", value=0.0, format="%.2f")

with col2:
    num2 = st.number_input("Digite o segundo número:", value=0.0, format="%.2f")

st.markdown("### Escolha a operação:")

# 3 & 4. Botões de ação para cada operação matemática
# Criamos 4 colunas para distribuir os botões lado a lado de forma elegante
btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4)

resultado = None
erro = None
operacao_realizada = None

with btn_col1:
    if st.button("➕ Soma", use_container_width=True):
        resultado = num1 + num2
        operacao_realizada = f"{num1} + {num2} = {resultado}"

with btn_col2:
    if st.button("➖ Subtração", use_container_width=True):
        resultado = num1 - num2
        operacao_realizada = f"{num1} - {num2} = {resultado}"

with btn_col3:
    if st.button("✖️ Multiplicação", use_container_width=True):
        resultado = num1 * num2
        operacao_realizada = f"{num1} × {num2} = {resultado}"

with btn_col4:
    if st.button("➗ Divisão", use_container_width=True):
        # 5. Se for divisão por zero, exiba uma mensagem de alerta/erro amigável (st.error)
        if num2 == 0:
            erro = "⚠️ Erro: Não é possível realizar divisão por zero!"
        else:
            resultado = num1 / num2
            operacao_realizada = f"{num1} ÷ {num2} = {resultado}"

# 5. Exibição dos resultados ou mensagens de erro após clicar em algum botão
if erro:
    st.markdown("---")
    st.error(erro)
elif resultado is not None:
    st.markdown("---")
    st.success("Cálculo realizado com sucesso! 🎉")
    
    # Formatando o resultado para remover decimais desnecessários caso seja inteiro
    valor_formatado = f"{resultado:.4f}".rstrip('0').rstrip('.')
    
    # Mostrando o resultado em grande destaque usando st.metric
    st.metric(label="Resultado Final", value=valor_formatado)
    st.caption(f"Expressão: {operacao_realizada}")

# Rodapé explicativo
st.markdown("---")
st.caption("Desenvolvido com ❤️ para iniciantes em Vibe Coding.")
