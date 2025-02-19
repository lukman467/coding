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
        ("\nAku ga mau jadi mataharimu", 0.08),
        ("Karena itu akan membuatku jauh", 0.08),
        ("Aku ga mau jadi bintang-bintangmu", 0.08),
        ("Walau indah itu juga 'kan jauh", 0.08),
        ("Yang aku mau menjadi udaramu", 0.09),
        ("Selalu setia tiap hela nafasmu\n", 0.1),
        ("Aku ga romantis", 0.08),
        ("Maaf, aku ga romantis", 0.08),
        ("Maaf, aku ga romantis", 0.08),
        ("Maaf, aku ga romantis\n", 0.08)
    ]
    delays = [0.3, 4.0, 7.8, 11.5, 14.9, 18.3, 22.0, 23.7, 25.3, 26.8]
    
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
