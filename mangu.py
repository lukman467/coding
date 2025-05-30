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
        # ("\nJangan salahkan faham ku kini tertuju oh", 0.10),
        ("Siapa yang tau", 0.11),
        ("Siapa yang mau", 0.11),
        ("Kau di sana", 0.10),
        ("Aku diseberangmu\n", 0.11),
        # ("Cerita kita sulit dicerna", 0.10),
        ("Tak lagi sama", 0.10),
        ("Cara berdoa\n", 0.10),
        # ("Cerita kita sulit diterka", 0.10),
        ("Tak lagi sama", 0.10),
        ("Arah kiblatnya", 0.10),
    ]
    
    delays = [9.6, 12.3, 15.5, 17.0, 25.2, 28.0, 35.7, 38.2]
    
    threads = []
    for i in range(0):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    t_0 = Thread(target=sing_lyric_part, args=("\nJangan salahkan faham ku kini ", 0.3, 0.13, False))
    t_1 = Thread(target=sing_lyric_part, args=("tertuju oh", 5.8, 0.13, True))
    threads.extend([t_0, t_1])
    t_0.start()
    t_1.start()

    t_2 = Thread(target=sing_lyric_part, args=("Cerita kita ", 20.2, 0.13, False))
    t_3 = Thread(target=sing_lyric_part, args=("sulit dicerna", 22.7, 0.13, True))
    threads.extend([t_2, t_3])
    t_2.start()
    t_3.start()

    t_4 = Thread(target=sing_lyric_part, args=("Cerita kita ", 30.2, 0.13, False))
    t_5 = Thread(target=sing_lyric_part, args=("sulit diterka", 32.7, 0.13, True))
    threads.extend([t_4, t_5])
    t_4.start()
    t_5.start()

    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
