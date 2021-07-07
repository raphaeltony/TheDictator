from gtts import gTTS
import os


text = open("draft.txt", "r").read().replace("\n", " ").split(".")
print(text)

final = ''

for sentence in text:
    words = sentence.split()
    phrase = []
    count = 0

    for i in range(0, len(words)):
        phrase.append(words[i])
        if(len(words[i]) > 3):
            count += 1

        if(count == 4):
            final = final + ' '.join(phrase)
            final = final + ' '.join(phrase)
            count = 0
            phrase = []


speech = gTTS(text=final, lang='en', slow=True)

speech.save("voice.mp3")

os.system("start voice.mp3")
