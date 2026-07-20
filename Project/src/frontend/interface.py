import streamlit as st
import requests

backend_url = "http://localhost:8000/query"
st.title("Simply Bot - Live Chat UI")

if prompt :=st.chat_input("Say something"):

    with st.chat_message("user"):
        st.markdown(prompt)


    adat = {
        "prompt": prompt
    }
    try:
        response = requests.post(backend_url, json=adat)

        if response.status_code == 200:
            valasz_adat = response.json()    

            ai_valasz = valasz_adat.get("status", "Nem érkezett válasz.")
            
            with st.chat_message("assistant"):
                st.markdown(ai_valasz)
        else:
            st.error(f"Backend hiba! Státuszkód: {response.status_code}")
            
    except Exception as e:
        st.error(f"Nem sikerült elérni a backend szervert: {str(e)}")