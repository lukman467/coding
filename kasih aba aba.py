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


def sing_lyric_part(lyric_part, delay, speed, add_newline=False):
    time.sleep(delay)
    with lock:
        for char in lyric_part:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        if add_newline:
            print()  

def sing_song():
    lyrics = [
        ("\nKu merasakan apa yang kau rasakan", 0.10),
        ("Tanpa ragu ku bilang kamu yang paling paham aku", 0.07),
        # ("Dua jadi satu, belah hati aku", 0.10),
        ("Aku mau maju tapi tinggal tunggu waktu", 0.08)
    ]
    delays = [0.3, 4.3, 12.1]

    threads = []
    for i in range(0):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    t_0 = Thread(target=sing_lyric_part, args=("Dua jadi satu ", 8.4, 0.09, False))
    t_1 = Thread(target=sing_lyric_part, args=("belah hati aku", 10.2, 0.10, True))
    threads.extend([t_0, t_1])
    t_0.start()
    t_1.start()
    
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
    