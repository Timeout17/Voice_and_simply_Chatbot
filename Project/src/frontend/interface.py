import streamlit as st
import requests


TEXT_BACKEND_URL = "http://localhost:8000/query"
VOICE_BACKEND_URL = "http://localhost:8000/query/voice"


st.title("Simply Bot - Live Chat UI")


# -----------------------------
# Szöveges chat
# -----------------------------

if prompt := st.chat_input("Say something"):

    with st.chat_message("user"):
        st.markdown(prompt)


    adat = {
        "prompt": prompt
    }

    try:
        response = requests.post(
            TEXT_BACKEND_URL,
            json=adat
        )

        if response.status_code == 200:

            valasz_adat = response.json()

            ai_valasz = valasz_adat.get(
                "status",
                "Nem érkezett válasz."
            )

            with st.chat_message("assistant"):
                st.markdown(ai_valasz)

        else:
            st.error(
                f"Backend hiba! Státuszkód: {response.status_code}"
            )


    except Exception as e:
        st.error(
            f"Nem sikerült elérni a backend szervert: {str(e)}"
        )


# -----------------------------
# Hangos chat
# -----------------------------

audio_file = st.audio_input(
    "Mondj valamit"
)


if audio_file:

    with st.chat_message("user"):
        st.audio(audio_file)


    # Hangfájl bájtok
    audio_bytes = audio_file.read()


    hang_adat = {
        "file": (
            "user_voice.wav",
            audio_bytes,
            "audio/wav"
        )
    }


    try:

        response = requests.post(
            VOICE_BACKEND_URL,
            files=hang_adat
        )


        if response.status_code == 200:

            valasz_adat = response.json()


            ai_valasz = valasz_adat.get(
                "answer",
                "Nem érkezett válasz."
            )


            with st.chat_message("assistant"):
                st.markdown(ai_valasz)

            st.audio(
                valasz_adat["audio_path"]
            )

        else:

            st.error(
                f"Backend hiba! Státuszkód: {response.status_code}"
            )


    except Exception as e:

        st.error(
            f"Hiba történt: {str(e)}"
        )