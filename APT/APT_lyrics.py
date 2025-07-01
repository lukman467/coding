
import time
import sys
import pygame
import os
import platform

# Clear terminal
def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")  # clear scrn win
    else:
        os.system("clear")  # Clear screen selain win

clear_terminal()  # sesuia nama

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

pygame.mixer.init()



music_file = 'APT.MP3' # pake yang APT2 suara mang bruno mars, kalau ini suara ayang gw


# ngeload
pygame.mixer.music.load(music_file)

# MULAI MUSIK CUY
pygame.mixer.music.play()
def print_with_transition(phrases):
    for phrase in phrases:
        for word, delay in phrase.items():
            for letter in word:
                print(letter, end='', flush=True)  # munculin setiap kata tanpa newline
                time.sleep(0.06)  # delay antar kata
            print(' ', end='', flush=True)  # ngasih spasi
            time.sleep(delay)  
        print()  # ganti kata abis kelarin kata
        time.sleep(0.1)  # Pause antar kata

def main():
    # paling malas sesuaikan lagu sama lirik
    phrases = [
        { "Don't": 0.08, "you": 0.091, "want": 0.091, "me": 0.091, "like": 0.1, "I": 0.091, "Want": 0.091, "you,": 0.12, "baby": 0.44},
        { "Don't": 0.08, "you": 0.082, "Need": 0.082, "me": 0.12, "like": 0.082, "I": 0.082, "need": 0.08, "You": 0.15, "now": 0.49},
        { "Sleep": 0.1, "tomorrow": 0.2, "but": 0.15, "tonight": 0.15, "go": 0.13, "crazy": 0.49},
        { "All": 0.082, "you": 0.082, "gotta": 0.082, "do": 0.082, "is": 0.02, "just": 0.092, "meet": 0.12, "me": 0.082, "at": 0.34, "the": 0.3},
        { "Apateu": 0.52, "pateu": 0.47},
        { "Apateu": 0.5, "pateu": 0.39},
        { "Apateu": 0.4, "pateu": 0.45},
        { "Uh,": 0.1, "uh huh": 0.03, "Uh huh": 0.05}
    ]
    
    print_with_transition(phrases)



if __name__ == "__main__":
    main()

while pygame.mixer.music.get_busy():
    time.sleep(0.1)

# gabut bang