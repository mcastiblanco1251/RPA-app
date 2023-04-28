import streamlit as st
import requests
from translate import Translator


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
    st.title("Chat Bot")
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
