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
        ("Kelak kau kan menjalani hidupmu sendiri", 0.1),
        ("Melukai kenangan yang telah kita lalui", 0.09),
        ("Yang tersisa hanya aku sendiri di sini", 0.09),
        ("Kau akan terbang jauh menembus awan", 0.09),
        ("Memulai kisah baru tanpa diriku", 0.09),
        ("\n""Seandainya kau tau ku tak ingin kau pergi", 0.10),
        ("Meninggalkan ku sendiri bersama bayanganku", 0.10),
        ("Seandainya kau tau aku kan selalu cinta", 0.10),
        ("Jangan kau lupakan kenangan kita selama ini", 0.1)
    ]
    delays = [0.3, 7.0, 14.0, 20.7, 27.5, 35.3, 44.0, 49.0, 57.4]
    
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