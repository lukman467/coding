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
        ("\n""Got the music in you, baby", 0.09),
        ("Tell me why", 0.06),
        ("Got the music in you, baby", 0.09),
        ("Tell me why", 0.06),
        ("You've been locked in here forever", 0.07),
        ("And you just can't say goodbye", 0.09),
    ]
    delays = [0.3, 2.9, 5.5, 7.6, 10.5, 12.4]
    
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