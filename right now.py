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
        ("Right now", 0.11),
        ("I wish you were here with me", 0.07),
        ("Cause right now", 0.09),
        ("Everything is new to me", 0.09),
        ("You know I can't fight the feeling", 0.10),
        ("And every night I feel it", 0.09),
        ("Right now", 0.11),
        ("I wish you were here with me", 0.07),
    ]
    delays = [0.3, 2.2, 7.5, 10.0, 16.2, 20.5, 24.0, 26.0]
    
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
