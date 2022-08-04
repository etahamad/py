import translate as t


translator = t.Translator(to_lang="ja")

try:
    with open('./english.txt', 'r', encoding="utf-8") as f:
        text = f.read()
        translation = translator.translate(text)
        with open('./japanese.txt', 'w', encoding="utf-8") as f:
            f.write(translation)
except FileNotFoundError:
    print('File not found')
    exit()
