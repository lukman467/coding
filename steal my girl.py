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
        ("\n""She's been my queen", 0.07),
        ("Since we were sixteen", 0.07),
        ("We want the same things", 0.07),
        ("We dream the same dreams", 0.07),
        ("Alright", 0.07),
        ("Alright", 0.07),
        ("\n""I got it all", 0.07),
        ("Cause she is the one", 0.07),
        ("Her mum calls me love", 0.07),
        ("Her dad calls me son", 0.07),
        ("Alright", 0.07),
        ("Alright", 0.07),
    ]
    delays = [0.3, 1.7, 3.0, 4.5, 6.0, 9.5, 12.9, 13.9, 15.5, 17.0, 18.5, 22.0]
    
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
