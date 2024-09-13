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
        ("\n""And if you like midnight driving with the windows down", 0.08),
        ("And if you like going places we can't even pronounce", 0.08),
        ("If you like to do whatever you've been dreaming about", 0.08),
        ("Then baby, you're perfect", 0.05),
        ("Baby, you're perfect", 0.05),
        ("So let's start right now""\n", 0.05),
    ]
    
    delays = [0.3, 5.2, 10.0, 15.0, 17.5, 19.5]
    
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