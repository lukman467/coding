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
        ("Janganlah kau tinggalkan diri ku", 0.1),
        ("Tak kan mampu menghadapi semua", 0.12),
        ("Hanya bersamamu ku akan bisa", 0.11),
        ("Kau adalah darah ku", 0.10),
        ("Kau adalah jantung ku", 0.10),
        ("Kau adalah hidup ku lengkapi diri ku", 0.10),
        ("Oh sayangku kau begitu", 0.1),
        ("Sempurnaaaaaaaaaaaaaaaaa", 0.1)
    ]
    delays = [0.3, 4.5, 9.3, 14.1, 18.8, 23.0, 28.0, 34.5]
    
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
