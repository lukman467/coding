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
        ("\n""Take me home, I'm fallin", 0.10),
        ("Love me long, I'm rollin", 0.09),
        ("Losing control, body and soul", 0.09),
        ("Mind too for sure, I'm already yours", 0.10),
        ("Walk you down, I'm all in", 0.10),
        ("Hold you tight, you call and", 0.09),
        ("I'll take control, your body and soul", 0.07),
        ("Mind too for sure, I'm already yours", 0.09),
    ]
    delays = [0.3, 3.9, 7.0, 10.5, 15.0, 18.5, 21.5, 24.9]
    
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
