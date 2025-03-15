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
        ("\nDon't listen to them", 0.07),
        ("Cause what do they know", 0.05),
        ("We need each other", 0.07),
        ("to have, to hold", 0.07),
        ("They'll see in time", 0.08),
        ("I know\n", 0.07),
        ("When destiny calls you", 0.07),
        ("you must be strong", 0.07),
        ("I may not be with you", 0.07),
        ("But you've got to hold on", 0.07),
        ("They'll see in time", 0.08),
        ("I know", 0.07),
    ]
    delays = [0.3, 3.2, 5.8, 8.3, 10.6, 15.5, 20.8, 23.4, 26.0, 28.5, 31.2, 36.0]
    
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