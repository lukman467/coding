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
        ("\nNow, you're the inspiration of this precious song", 0.08),
        ("And I just wanna see your face light up since you put me on", 0.06),
        ("So now, I say goodbye to the old me its already gone", 0.08),
        ("And I can't wait wait wait wait wait to get you home", 0.07),
        ("Just to let you know, you are\n", 0.08)
    ]
    delays = [0.3, 6.5, 12.6, 19.1, 23.7]

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
