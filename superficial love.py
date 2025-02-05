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
        ("\nThis superficial love thing got me going crazy", 0.06),
        ("Baby if you want me, then you better need me", 0.07),
        ("Cause I'm so done, not being your number one", 0.08),
        ("And if you wanna keep me, then you better treat me", 0.07),
        ("Like a damn princess, make that an empress", 0.07),
        ("Cause I'm so done, not being your number one", 0.08),
        ("This superficial love", 0.06)
    ]
    delays = [0.3, 3.7, 6.8, 13.0, 16.5, 19.8, 26.0]
    
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