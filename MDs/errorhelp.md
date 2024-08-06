# AIVA Errorhelper

## error: transcribing audio

"""
def transcribe_audio(file):
    global chat_now
    try:
        audio_file= open(file, "rb")
        # Translating the audio to English
        # transcript = openai.Audio.translate("whisper-1", audio_file)
        # Transcribe the audio to detected language
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        chat_now = transcript.text
        print ("Question: " + chat_now)
    except:
        print("Error transcribing audio")
        return

    result = owner_name + " said " + chat_now
    conversation.append({'role': 'user', 'content': result})
    openai_answer()
"""

Change this Line of Code to this. This will help you to get more information about the error

"""
def transcribe_audio(file):
    global chat_now
    audio_file= open(file, "rb")
    # Translating the audio to English
    # transcript = openai.Audio.translate("whisper-1", audio_file)
    # Transcribe the audio to detected language
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    chat_now = transcript.text
    print ("Question: " + chat_now)

    result = owner_name + " said " + chat_now
    conversation.append({'role': 'user', 'content': result})
    openai_answer()
"""

Another option to solve this problem, you can upgrade the OpenAI library to the latest version. Make sure the program capture your voice/sentence, try to hear the `input.wav`

2.Mecab Error

this library is a little bit tricky to install. If you facing this problem, you can just delete and don't use the `katakana_converter` on `utils/TTS.py`. That function is optional, you can run the program without it. Delete this two line on `utils/TTS.py`

"""

from utils.katakana import *
katakana_text = katakana_converter(tts)

"""

and just pass the `tts` to next line of the code

"""

params_encoded = urllib.parse.urlencode({'text': tts, 'speaker': 46})

"""
