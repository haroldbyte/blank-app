import streamlit as st

st.title("🎈 esta es mi nueva ")stre
st.write(
    "Por fin arrancates webis! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
salida = st.slider('seleccione la salida deseada')
st.write('la cantidad que escogiste es')
st.write(salida)
compra = salida * 900
st.write('todo eso le cuestas')
st.write(compra)