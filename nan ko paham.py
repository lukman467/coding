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
        ("\nSu jauh sa tanam hati tapi tra hasil", 0.08),
        ("Cobalah dewasa ko su bukan anak kecil", 0.09),
        ("Sa coba imbangi namun hati tra kuat", 0.09),
        ("Tersiksa makan hati dan itu sa su muak\n", 0.09),
        # ("Nanti pasti ko mengerti", 0.13), 
        ("Stelah sa hilang dan sa jauh untuk pergi", 0.12),
        ("Ko akan tau bagaimana sa sayang ko tapi", 0.11),
        ("Sa rasa percuma ko terus ungkit", 0.10),
        # ("Ungkit luka lama yang buat sa trauma", 0.13),
    ]
    
    delays = [0.3, 4.0, 7.7, 11.3, 14.6, 17.3, 21.9, 29.3, 34.7, 39.6, 42.9]
    
    threads = []
    for i in range(4):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    t_nanti = Thread(target=sing_lyric_part, args=("Nanti ", delays[4], 0.13, False))
    threads.append(t_nanti)
    t_nanti.start()

    t_pasti = Thread(target=sing_lyric_part, args=("pasti ko mengerti", delays[5], 0.13, True))
    threads.append(t_pasti)
    t_pasti.start()

    t_ungkit = Thread(target=sing_lyric_part, args=("Ungkit luka lama ", delays[9], 0.12, False))
    threads.append(t_ungkit)
    t_ungkit.start()

    t_trauma = Thread(target=sing_lyric_part, args=("yang buat sa trauma", delays[10], 0.12, True))
    threads.append(t_trauma)
    t_trauma.start()
    
    for i in range(4, len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i+2], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()