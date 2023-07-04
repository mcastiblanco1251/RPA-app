import streamlit as st
import requests
from translate import Translator
from PIL import Image
from streamlit_chat import message
#from streamlit_extras.colored_header import colored_header
#from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

im = Image.open("log.png")

st.set_page_config(page_title='ChatBot', layout="wide", page_icon=im)
st.set_option('deprecation.showPyplotGlobalUse', False)

# LAYING OUT THE TOP SECTION OF THE APP

row1_1, row1_2 = st.columns((1,3))

with row1_1:
    image = Image.open('bot.png')
    ni=image.resize((250, 220))
    st.image(ni)#, use_column_width=True)
    st.markdown('Web App by [Manuel Castiblanco](http://ia.smartecorganic.com.co/index.php/contact/)')
with row1_2:
    st.write("""
    # ChatBot
    Esta app ilustra chatbot!
    """)
    with st.expander("Contact us 👉"):
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


# Generate empty lists for bot_response and user_input.
## bot_response stores AI generated responses
if 'bot_response' not in st.session_state:
    st.session_state['bot_response'] = ["Hola, SmartChat, Como Puedo Ayudarte?"]
## user_input stores User's questions
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ['Hola!']

# Layout of input/response containers
input_container = st.container()
#colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

# User input
## Function for taking user provided prompt as input
def get_input():
    input_text = st.text_input("Tu: ", "", key="input")
    return input_text
## Applying the user input box
with input_container:
    user_input = get_input()

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = hugchat.ChatBot(cookie_path="cookies.json")
    response = chatbot.chat(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.user_input.append(user_input)
        st.session_state.bot_response.append(response)

    if st.session_state['bot_response']:
        for i in range(len(st.session_state['bot_response'])):
            message(st.session_state['user_input'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['bot_response'][i], key=str(i))
