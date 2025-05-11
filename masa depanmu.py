import time
from threading import Thread, Lock
import sys

lock = Lock()
RED = '\033[91m'
RESET = '\033[0m'

def animate_text(text, delay=0.1, color_info=None):
    with lock:
        use_red = True
        for char in text:
            if color_info and char == color_info:
                color = f"{RED}{char}{RESET}" if use_red else char
                sys.stdout.write(color)
                use_red = not use_red
            else:
                sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed, color_char):
    time.sleep(delay)
    animate_text(lyric, speed, color_char)

def sing_song():
    lyrics = [
        ("\nA A A A A A A A A A Aku akan beritahu pada dunia", 0.08, 'A'),
        ("kau begitu indah", 0.08, None),
        ("yang pernah ku punya", 0.08, None),
        ("A A A A Aku akan selalu menemani dirimu", 0.08, 'A'),
        ("U U U U U U Ucap Terima kasih untuk dirimu", 0.09, 'U'),
        ("kita membuat memori sampai ahkhir hayat nanti", 0.08, None),
        ("cinta ku tak pernah mati jadi kau tak perlu worry", 0.07, None),
        ("genggam tanganku tak perlu ragu", 0.08, None),
        ("habiskan waktu hanya bersama dirimu", 0.08, None),
    ]
    
    delays = [0.3, 5.0, 6.8, 8.0, 11.3, 15.3, 18.6, 22.7, 26.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed, color_char = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed, color_char))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()