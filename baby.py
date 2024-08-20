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
        ("\n""Oh, for you, I would have done whatever", 0.08),
        ("And I just can't believe we ain't together", 0.07),
        ("And I wanna play it cool, but I'm losing you", 0.07),
        ("I'll buy you anything, I'll buy you any ring", 0.08),
        ("And I'm in pieces, baby fix me", 0.09),
        ("And just shake me 'til you wake me from this bad dream""\n", 0.06),
    ]
    
    delays = [0.3, 4.1, 7.9, 11.5, 14.1, 19.0]
    
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