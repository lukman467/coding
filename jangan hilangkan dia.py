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
        ("\n""Sungguh sungguh aku tak ingin", 0.14),
        ("Hatiku jadi milik yang lainnya", 0.14),
        ("Ku bersumpah kau sosok yang tak mungkin", 0.14),
        ("Kutemukan lagi""\n", 0.14),
    ]
    
    delays = [0.3, 6.8, 14.7, 21.9]
    
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