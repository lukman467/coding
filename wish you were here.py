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
        ("\n""If a picture is all that I have", 0.09),
        ("I can picture the times that we won't get back", 0.08),
        ("If I picture it now, it don't seem so bad", 0.09),
        ("Either way, I still wish you were here", 0.08),
        ("Don't say everything's meant to be", 0.09),
        ("Cause you know it's not what I believe", 0.08),
        ("Can't help but think that it should've been me", 0.08),
        ("Either way, I still wish you were here", 0.08),
    ]
    delays = [0.3, 4.7, 9.2, 13.9, 18.3, 22.9, 26.9, 31.9]

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
