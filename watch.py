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
        ("\nWhen you call my name", 0.06),
        ("Do you think I'll come running?", 0.06),
        ("You never did the same", 0.06),
        ("So good at givin' me nothing", 0.07),
        ("When you close your eyes, do you picture me?", 0.07),
        ("When you fantasize, am I your fantasy?", 0.07),
        ("Now you know", 0.10),
        ("Now I'm free", 0.1)
    ]
    delays = [0.3, 3.5, 6.4, 9.5, 12.8, 15.8, 19.6, 22.5]
    
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