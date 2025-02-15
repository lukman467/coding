import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush() 
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nHold my hands, dont-dont tell your friends", 0.06),
        ("Cerita kemaren, ku ingat permanen", 0.08),
        ("Manis mu kaya permen, I hope this never end", 0.08),
        ("Oh can you be my Gwen? and ill be the Spiderman", 0.06),
        ("\nSakit dadaku, ku mulai merindu", 0.09),
        ("Ku bayangkan jika kamu tidur di sampingku", 0.07),
        ("Di malam yang semu", 0.08),
        ("Pejamkan mataku", 0.07),
        ("Ku bayangkan tubuhmu jika di pelukanku", 0.07)
    ]
    delays = [0.3, 3.0, 6.3, 10.0, 13.0, 16.5, 19.9, 21.7, 23.3]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
