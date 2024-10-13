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
        ("\n""We don't talk enough", 0.12),
        ("We should open up", 0.14),
        ("Before it's all too much", 0.12),
        ("Will we ever learn?", 0.12),
        ("We've been here before", 0.12),
        ("It's just what we know", 0.12),
        ("\n""Stop your crying, baby", 0.07),
        ("It's a sign of the times", 0.06),
        ("We gotta get away", 0.08),
        ("We got to get away""\n", 0.08)
    ]
    
    delays = [0, 4.0, 8.0, 16.0, 20.0, 24.0, 32.0, 34.0, 38.0, 42.5]
    
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
