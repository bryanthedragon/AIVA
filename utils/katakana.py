
import re
import sys
import MeCab
import alkana
import pandas as pd
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

alphaReg = re.compile(r'^[a-zA-Z]+$')

def isalpha(s):
    return alphaReg.match(s) is not None

def katakana_converter(text):
    wakati = MeCab.Tagger('-Owakati')
    wakati_result = wakati.parse(text)

    df = pd.DataFrame(wakati_result.split(" "), columns=["word"])
    df = df[df["word"].str.isalpha()]  # Use direct boolean indexing
    df["english_word"] = df["word"].apply(isalpha)
    df = df[df["english_word"]]  # Use direct boolean indexing
    df["katakana"] = df["word"].apply(alkana.get_kana)

    dict_rep = dict(zip(df["word"], df["katakana"]))

    for word, read in dict_rep.items():
        try:
            text = text.replace(word, read)
        except Exception as e:  # Catch specific exceptions if possible
            print(f"Error replacing {word}: {e}")

    return text
