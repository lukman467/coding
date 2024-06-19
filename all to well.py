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
        ("Just between us, I remember it, all too well", 0.11),
        ("Wind in my hair, I was there, I was there", 0.08),
        ("Down the stairs, I was there, I was there", 0.08),
        ("Sacred prayer, I was there, I was there", 0.09),
        ("It was rare, you remember it all too well", 0.10),
    ]
    delays = [0.3, 6.4, 11.5, 16.5, 21.5]
    
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