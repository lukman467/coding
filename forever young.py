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
        ("\n""Forever young", 0.09),
        ("I want to be forever young", 0.09),
        ("Do you really want to live forever?", 0.08),
        ("Forever, and ever", 0.14),
        ("Forever young", 0.09),
        ("I want to be forever young", 0.1),
        ("Do you really want to live forever?", 0.08),
        ("Forever, and ever", 0.14)
    ]
    delays = [0.3, 2.8, 7.5, 10.9, 14.5, 16.9, 21.6, 24.9]
    
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