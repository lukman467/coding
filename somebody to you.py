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
        ("\nAll I wanna be, yeah, all I ever wanna be, yeah, yeah", 0.05),
        ("Is somebody to you", 0.05),
        ("All I wanna be, yeah, all I ever wanna be, yeah, yeah", 0.05),
        ("Is somebody to you", 0.05),
        ("Everybody's tryna be a billionaire", 0.06),
        ("But every time I look at you, I just don't care", 0.05),
        ("Cause all I wanna be, yeah, all I ever wanna be, yeah, yeah", 0.06),
        ("Is somebody to youuuuu", 0.05)
    ]
    delays = [0.3, 3.5, 5.3, 8.5, 10.0, 12.5, 14.7, 18.5]
    
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
