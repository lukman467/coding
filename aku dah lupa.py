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
        ("\nAku dah lupa tak ingat lagi", 0.07),
        ("Nama kau pun hilang dari hati", 0.05),
        ("Aku move on hidup sendiri", 0.06),
        ("Tak perlu kau, aku happy\n", 0.06),
        ("Aku dah lupa tak ingat lagi", 0.06),
        ("Nama kau pun hilang dari hati", 0.05),
        ("Aku move on hidup sendiri", 0.06),
        ("Tak perlu kau, aku happy\n", 0.06),
    ]
    delays = [0.3, 2.8, 4.2, 6.6, 8.1, 10.2, 11.2, 13.7]
    
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