import streamlit as st
import requests
from translate import Translator
from PIL import Image

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


def chat_bot(message):
    url = 'http://api.brainshop.ai/get'
    payload = {
        'bid': '174456', # Reemplaza esto con el ID de tu bot
        'key': 'O21PbXrjwmqdqn6k', # Reemplaza esto con tu clave de API
        'uid': '12345', # Esto es opcional, pero puedes usarlo para rastrear sesiones de chat
        'msg': message
    }
    response = requests.post(url, data=payload)
    return response.json()['cnt']

def main():
    #st.title("Chat Bot")
    message = st.text_input("Ingrese su mensaje")
    if st.button("Enviar"):

        translator = Translator(from_lang='es',to_lang="en")
        translation1 = translator.translate(message)
        response = chat_bot(translation1)
        translator = Translator(from_lang='en',to_lang="es")
        translation2 = translator.translate(response)
        st.text_area("Respuesta", value=translation2)

if __name__ == "__main__":
    main()
