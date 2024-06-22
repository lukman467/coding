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
        ("I'm sorry if I say, I need you", 0.08),
        ("But I don't care, I'm not scared of love", 0.06),
        ("Cause when I'm not with you, I'm weaker", 0.07),
        ("Is that so wrong? Is it so wrong", 0.08),
        ("That you make me strong?", 0.06),
    ]
    delays = [0.3, 3.7, 7.4, 10.2, 13.7]
    
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
