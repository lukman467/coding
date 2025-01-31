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
        ("\nCause you're the one that I like", 0.06),
        ("I cant deny", 0.08),
        ("Every night you're on my mind", 0.08),
        ("So if I call you tonight", 0.08),
        ("Will you pick up and give me your time?", 0.08),
        ("Miss you every night", 0.08),
        ("Miss you all the time", 0.07),
        ("No, I don't even know", 0.08),
        ("Where to start", 0.08)
    ]
    delays = [0.3, 2.1, 4.0, 6.0, 8.5, 12.3, 14.5, 16.4, 18.0]
    
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