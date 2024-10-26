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
        ("\n""Bradley's on the microphone with Ras MG", 0.06),
        ("All the people in the dance will agree", 0.07),
        ("That we're well-qualified to represent the L.B.C", 0.08),
        ("Me, me and Louie, we gonna run to the party", 0.08),
        ("And dance to the rhythm, it gets harder""\n", 0.07)
    ]
    delays = [0.3, 3.3, 5.8, 10.2, 14.0]
    
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
