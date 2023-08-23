import random
from daten import fragen
import pygame
import time

#Intro/ Spielername abfragen
def main():
    print("Willkommen bei")
    print("Wer wird Gillinonär")
    print("Alle Fragen die Final Fantasy 14 betreffen, sind auf den Stand von August 2022")
    name = input("Verrate mir deinen Namen: ")

    while True:
        antwort = input("Ist " + name + " korrekt? Antworte mit Ja/Nein: ").lower()
        if antwort == "ja":
            print("Dann fangen wir an, " + name + ".")
            break
        elif antwort == "nein":
            name = input("Verrate mir deinen Namen: ")
        else:
            print("Ungültige Eingabe. Antworte mit Ja/Nein.")

    print("Willkommen, " + name + "!")

    def play_sound(sound_file):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    used_indices = []  # Liste für bereits verwendete Fragen-Indizes
    punkte = 0 # Fragenzähler/ Punktezähler
    while len(used_indices) < len(fragen):
        index = random.randint(0, len(fragen) - 1)
        if index not in used_indices:
            used_indices.append(index)
            frage_objekt = fragen[index]

            print(frage_objekt.text)

            answers = [frage_objekt.richtige_antwort] + frage_objekt.falsche_antworten
            random.shuffle(answers)

            for i, answer in enumerate(answers):
                letter = chr(65 + i)
                print(f"{letter}: {answer}")

            user_antwort = input("Deine Antwort (A/B/C): ").upper()
            if user_antwort == chr(65 + answers.index(frage_objekt.richtige_antwort)):
                print("Die Antwort ist Richtig!\n")
                punkte +=1
                sound_file = "richtige_antwort.mp3"
                play_sound(sound_file)
                time.sleep(4)
            else:
                print("Die Antwort ist Leider Falsch!\n")
                sound_file = "auslachen.mp3"
                play_sound(sound_file)
                input()
                break

    print("Vielen Dank fürs Spielen!")
    print(name + " hat " + str(punkte) + " Fragen Richtig beantwortet")
    input()

    print("Credits")
    print("Soundeffekte")
    print("https://pixabay.com/")

if __name__ == "__main__":
   
    main()
