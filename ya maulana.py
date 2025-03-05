import time
from threading import Thread, Lock
import sys

Rawrr = Lock()

def animasi_teks(teks, jeda=0.1):
    with Rawrr:
        for karakter in teks:
            sys.stdout.write(karakter)
            sys.stdout.flush()
            time.sleep(jeda)
        print()

def nyanyikan_lirik(lirik, jeda, kecepatan):
    time.sleep(jeda)
    animasi_teks(lirik, kecepatan)

def nyanyikan_lagu():
    lirik_lagu = [
        ("\n""Segala duka hatiku hilang hilangkan", 0.06),
        ("Semua salah dosaku mohon ampunkan", 0.06),
        ("Airmata lukaku hapus hapuskan", 0.07),
        ("Doa hari-hariku harap kabulkan\n", 0.07),
        ("Maulana Maulanaa Yaa Sami' Du'anaa", 0.12),
        ("Birahmatika Yaa Rabbi La Taqtho' Rojanaa", 0.11),
        ("Maulana Maulanaa Yaa Sami' Du'anaa", 0.12),
        ("Birahmatika Yaa Rabbi La Taqtho' Rojanaa""\n", 0.11),
    ]
    
    jeda_lirik = [0.3, 2.7, 4.9, 7.0, 9.6, 14.0, 18.7, 23.3]
    
    threads = []
    for i in range(len(lirik_lagu)):
        lirik, kecepatan = lirik_lagu[i]
        t = Thread(target=nyanyikan_lirik, args=(lirik, jeda_lirik[i], kecepatan))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    nyanyikan_lagu()