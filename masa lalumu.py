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
        ("\nKAU KAU KAU tak pernah katakan", 0.08),
        ("Apa kurangnya ku untukmu", 0.07),
        ("Namun ku tak sebanding", 0.07),
        ("Meskipun aku di sampingmu", 0.07),
        ("Dan kau masih cinta yang lalu", 0.06),
        ("Dia pergi, kau menunggu", 0.06),
        ("Baik kau pergi berhenti bebani diriku", 0.08),
    ]
    delays = [0.3, 2.5, 4.7, 6.2, 8.1, 10.4, 12.2]
    
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