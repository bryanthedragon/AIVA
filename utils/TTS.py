import os
import torch
import requests
import urllib.parse
import utils.katakana
# https://github.com/snakers4/silero-models#text-to-speech
def silero_tts(tts, language, model, speaker):
    device = torch.device('cpu')
    torch.set_num_threads(4)
    local_file = 'model.pt'

    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file(f'https://models.silero.ai/models/tts/{language}/{model}.pt',
                                    local_file)

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    # the person who make the fork is asking the original person you can use # as comments so when you dont really need a set variable like this example_text variable you can comment it out

    # example_text = "i'm fine thank you and you?"
    sample_rate = 48000

    # the person who make the fork is asking the original person if your using audio_paths variable you have to use it to access the model.save_wav() function and the sample_rate

    audio_paths = model.save_wav(text=tts,speaker=speaker,sample_rate=sample_rate)

def voicevox_tts(tts):
    # You need to run VoicevoxEngine.exe first before running this script
    voicevox_url = 'http://localhost:50021'
    # Convert the text to katakana. Example: ORANGE -> オレンジ, so the voice will sound more natural
    katakana_text = utils.katakana.katakana_converter(tts)
    # You can change the voice to your liking. You can find the list of voices on speaker.json
    # or check the website https://voicevox.hiroshiba.jp
    params_encoded = urllib.parse.urlencode({'text': katakana_text, 'speaker': 46})
    request = requests.post(f'{voicevox_url}/audio_query?{params_encoded}')
    params_encoded = urllib.parse.urlencode({'speaker': 46, 'enable_interrogative_upspeak': True})
    request = requests.post(f'{voicevox_url}/synthesis?{params_encoded}', json=request.json())

    with open("test.wav", "wb") as outfile:
        outfile.write(request.content)

if __name__ == "__main__":
    silero_tts()
