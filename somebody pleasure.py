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
        ("\n""Soul try to figure it out", 0.10),
        ("From where I've been escapin", 0.10),
        ("Running to end all the sin", 0.11),
        ("Get away from the pressure", 0.10),
        ("\n""Wondering to get a love that is so pure", 0.14),
        ("Gotta have to always make sure", 0.10),
        ("That I'm not just somebody's pleasure", 0.10)
    ]
    delays = [0.3, 4.6, 9.0, 13.4, 16.4, 25.5, 29.3]
    
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
