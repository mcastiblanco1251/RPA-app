import streamlit as st
import requests
from translate import Translator
from PIL import Image
from streamlit_chat import message
#from streamlit_extras.colored_header import colored_header
#from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat
import gradio as gr

im = Image.open("log.png")

st.set_page_config(page_title='SmartBot', layout="wide", page_icon=im)
#st.set_option('deprecation.showPyplotGlobalUse', False)

# LAYING OUT THE TOP SECTION OF THE APP

row1_1, row1_2 = st.columns((1,3))

with row1_1:
    image = Image.open('bot.png')
    ni=image.resize((250, 220))
    st.image(ni)#, use_column_width=True)
    st.markdown('Web App by [Manuel Castiblanco](http://ia.smartecorganic.com.co/index.php/contact/)')
with row1_2:
    st.write("""
    # SmartEcoBot
    Esta app podrás preguntarle a nuestro asistente virtual lo que te interese!
    """)
    with st.expander("Contacto 👉"):
        with st.form(key='contact', clear_on_submit=True):
            name=st.text_input('Nombre')
            mail = st.text_input('Email')
            q=st.text_area("Consulta")

            submit_button = st.form_submit_button(label='Enviar')
            if submit_button:
                subject = 'Consulta'
                to = 'macs1251@hotmail.com'
                sender = 'macs1251@hotmail.com'
                smtpserver = smtplib.SMTP("smtp-mail.outlook.com",587)
                user = 'macs1251@hotmail.com'
                password = '1251macs'
                smtpserver.ehlo()
                smtpserver.starttls()
                smtpserver.ehlo()
                smtpserver.login(user, password)
                header = 'To:' + to + '\n' + 'From: ' + sender + '\n' + 'Subject:' + subject + '\n'
                message = header + '\n'+name + '\n'+mail+'\n'+ q
                smtpserver.sendmail(sender, to, message)
                smtpserver.close()


st.header('Aplicación')
st.write('_______________________________________________________________________________________________________')



# Función para generar respuestas del modelo
def generate_response(prompt):
    chatbot = hugchat.ChatBot(cookie_path="cookies.json")
    response = chatbot.chat(prompt)
    return response

# Interfaz de Streamlit
#st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Qué quieres saber"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = generate_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})




#
# prompt = st.chat_input("Qué quieres saber")
# if prompt:
#     response = generate_response(prompt)
#     st.text_area("Respuesta del Chatbot:", response)
