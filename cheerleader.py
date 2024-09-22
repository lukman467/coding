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
        ("\n""Hmm, she gives me love and affection", 0.08),
        ("Baby, did I mention?", 0.09),
        ("You're the only girl for me", 0.08),
        ("No, I don't need the next one", 0.08),
        ("Mama loves you too", 0.08),
        ("She thinks I made the right selection", 0.09),
        ("Now all that's left to do", 0.09),
        ("Is just for me to pop the question""\n", 0.07)
    ]
    delays = [0.3, 3.5, 5.8, 8.0, 10.4, 12.0, 15.0, 16.0]
    
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
