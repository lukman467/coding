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
        ("\n""You'd be mineeeeee", 0.08),
        ("would you mind if I took your hand tonight?", 0.10),
        ("Know you're all that I want this life", 0.10),
        ("\n""I'll imagine we fell in love", 0.07),
        ("I'll nap under moonlight skies with you", 0.07),
        ("I think I'll picture us, you with the waves", 0.07),
        ("The ocean's colors on your face", 0.08),
        ("I'll leave my heart with your air", 0.08),
        ("So let me fly with you", 0.08),
        ("Will you be forever with me?", 0.11),
    ]

    delays = [0.2, 2.4, 8.0, 15.7, 18.6, 22.4, 26.0, 29.8, 34.1, 37.3]

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