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
        ("I have loved you since we were 18", 0.08),
        ("Long before we both thought the same thing", 0.07),
        ("To be loved and to be in love", 0.07),
        ("And all I could do is say that these arms were made for holding you oh oh oh whoa", 0.07),
        ("I wanna love like you made me feel", 0.09),
        ("When we were 18", 0.1)
    ]
    delays = [0.3, 6.9, 11.0, 14.0, 20.8, 24.8]
    
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
