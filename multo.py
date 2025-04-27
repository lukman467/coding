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
        ("\nDi mo ba ako lilisanin?", 0.13),
        ("Hindi pa ba sapat pagpapahirap sa 'kin?", 0.10),
        ("Hindi na ba ma-mamamayapa?", 0.12),
        ("Hindi na ba ma-mamamayapa?", 0.12),
        ("\nHindi na makalaya...", 0.13)
    ]
    delays = [0.3, 4.8, 9.5, 14.0, 17.3]
    
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
