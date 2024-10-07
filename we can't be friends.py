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
        ("\n""Know that you made me", 0.09),
        ("I don't like how you paint me, yet I'm still here hanging", 0.07),
        ("Not what you made me", 0.09),
        ("It's something like a daydream", 0.08),
        ("But I feel so seen in the night", 0.09),
        ("So for now, it's only me", 0.08),
        ("And maybe that's all I need""\n", 0.08)
    ]
    delays = [0, 4.0, 8.6, 12.6, 15.0, 19.2, 23.0]
    
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
