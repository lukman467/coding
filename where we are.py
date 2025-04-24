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
        ("\nDid we ever know?", 0.07),
        ("Did we ever know?", 0.07),
        ("Did we ever know?", 0.12),
        ("\nIs it all inside of my head?", 0.08),
        ("Maybe you still think I don't care", 0.07),
        ("But all I need is you", 0.08),
        ("Yeah, you know it's true", 0.05),
        ("yeah, you know it's true", 0.05),
        ("\nForget about where we are and let go", 0.11),
        ("We're so close\n", 0.09)
    ]
    delays = [0.3, 2.4, 4.1, 8.0, 11.9, 15.9, 18.5, 20.5, 22.7, 28.0]
    
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
