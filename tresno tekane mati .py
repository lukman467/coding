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
        ("\nNganti tok duake aku lilo", 0.11),
        ("Wis kulino bab ngampet loro", 0.10),
        ("Pokoke kowe liyane aku wegah", 0.11),
        ("Raono kata pisah percoyo endinge indah\n", 0.09),
        ("Kelangan kowe aku jelas ngamuk", 0.10),
        ("Mlaku tanpo kowe ati remuk", 0.11),
        ("Tak pasrahke gusti kabeh takdirku", 0.10),
        ("Dongaku ora pedot yo mung dinggo sliramu\n", 0.08),
    ]
    
    delays = [0.3, 4.3, 7.9, 11.6, 16.0, 19.3, 23.3, 27.0]
    
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
