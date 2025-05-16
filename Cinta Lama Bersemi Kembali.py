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
        ("\nMau tak mau ku harus menolakmu", 0.06),
        ("Karna ku sudah ada pengganti dirimu", 0.06),
        ("Aku yang sekarang bukanlah yang dulu", 0.06),
        ("Maafkan mantan aku tak mau\n", 0.09),
        ("Cintaku padamu bersemi kembali", 0.11),
        ("Maukah kau menjadi pacarku lagi", 0.11),
    ]
    delays = [0.3, 2.4, 4.7, 6.6, 10.6, 15.2]
    
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
