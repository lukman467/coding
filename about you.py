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
        ("And if I was a fool for you", 0.2),
        ("I'd wait 500 million hours", 0.2),
        ("On a park bench out on the moon", 0.2),
        ("But in full view of what you are", 0.2),
        ("You're a goddess, you're my rock star", 0.3),
        ("I fell in love with Alexandra", 0.5),
        ("Even though I barely met her", 0.2),
        ("Even though we'd break our hearts", 0.2),
        ("Before we'd even start (Before we'd even start)", 0.5)
    ]
    delays = [0.3, 5.0, 10.0, 15.0, 20.3, 25.0, 27.0, 30.2, 33.3]
    
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
