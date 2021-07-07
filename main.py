import os
import pyttsx3
import time


WORD_READ_RATE = 3
MIN_WORD_COUNT = 2
FIRST_READ_SPEED = 95
SECOND_READ_SPEED = 75


def dictate(s):
    # print(s)
    engine.say(s)
    engine.runAndWait()
    time.sleep(1.2)
    engine.setProperty('rate', SECOND_READ_SPEED)
    engine.say(s)
    engine.runAndWait()
    engine.setProperty('rate', FIRST_READ_SPEED)


engine = pyttsx3.init()
engine.setProperty('rate', FIRST_READ_SPEED)

# Splitting the text into sentences
text = open("draft.txt", "r").read().replace("\n", " ").split(".")


# Taking every sentence and splitting it into words. Then speaking 3 words at a time. 2 letter words (is, in etc) are spoken and not counted as a word.
for sentence in text:
    # print(sentence)
    words = sentence.split()
    phrase = []
    count = 0

    for i in range(0, len(words)):
        phrase.append(words[i])

        # Excluding 2 letter words:
        if(len(words[i]) > MIN_WORD_COUNT):
            count += 1

        # Once 3 words are found(excluding 2-letter words), it is then dictated
        if(count == WORD_READ_RATE):
            dictate(' '.join(phrase))
            count = 0
            phrase = []

    dictate(' '.join(phrase))
    count = 0
    phrase = []
