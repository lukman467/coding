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
        ("Falling from cloud nine", 0.12),
        ("Crashing from the high", 0.11),
        ("I'm letting go tonight", 0.11),
        ("I'm Falling from cloud nine", 0.12),
        ("Thunder rumbling", 0.10),
        ("Castles crumbling", 0.10),
        ("I am trying to hold on", 0.11)
    ]
    delays = [0.3, 5.7, 11.0, 16.2, 22.5, 25.2, 27.8]
    
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
