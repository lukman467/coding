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
        ("\n""And I don't know what I'm crying for", 0.11),
        ("I don't think I could love you more", 0.11),
        ("It might not be long, but baby, I", 0.11),
        ("I'll love you 'til the day that I die", 0.08),
        ("Til the day that I die", 0.08),
        ("Til the light leaves my eyes", 0.08),
        ("Til the day that I die""\n", 0.08)
    ]
    delays = [0.3, 5.0, 9.6, 15.6, 21.3, 25.6, 30.6]
    
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