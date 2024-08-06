
import json
import sys
import openai
import requests
from googletrans import Translator, LANGUAGES
from AIVA.run import openai_answer, conversation, owner_name
from AIVA.utils.classextensions.DetectExtension.DetectErrorExt import DetectError
from AIVA.utils.classextensions.TranscribeExtension.TranscribeErrorExt import TranscribeError
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

# You can use DeepL or Google Translate to translate the text
# DeepL can translate more casual text in Japanese
# DeepLx is a free and open-source DeepL API, i use this because DeepL Pro is not available in my country
# but sometimes i'm facing request limit, so i use Google Translate as a backup
def translate_deeplx(text, source, target):
    url = "http://localhost:1188/translate"
    headers = {"Content-Type": "application/json"}

    # define the parameters for the translation request
    params = {
        "text": text,
        "source_lang": source,
        "target_lang": target
    }

    # convert the parameters to a JSON string
    payload = json.dumps(params)

    # send the POST request with the JSON payload
    response = requests.post(url, headers=headers, data=payload)

    # get the response data as a JSON object
    data = response.json()

    # extract the translated text from the response
    translated_text = data['data']

    return translated_text

def translate_google(text, source, target):
    try:
        translator = Translator()
        result = translator.translate(text, src=source, dest=target)
        return result.text
    except ValueError as e:
        print(f"ValueError: {e}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

def detect_google(text):
    try:
        translator = Translator()
        result = translator.detect(text)
        if result.lang not in LANGUAGES:
            raise DetectError(f"Detected language '{result.lang}' is not a valid language code.")
        return result.lang.upper()
    except DetectError as de:
        print(f"Detected error: {de.message}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
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
    except TranscribeError:
        print("Error transcribing audio")
        return

    result = owner_name + " said " + chat_now
    conversation.append({'role': 'user', 'content': result})
    openai_answer()

if __name__ == "__main__":
    text = "aku tidak menyukaimu"
    source = translate_deeplx(text, "ID", "JA")
    print(source)
