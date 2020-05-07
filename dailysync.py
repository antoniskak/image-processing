#!/usr/bin/env python3.7

from multiprocessing import Pool
import subprocess
import os
import re
import time

start = time.perf_counter()
src = "/home/antonis/Desktop/Python/multi-proc/images/image-processing"
dest = "/home/antonis/Desktop/Python/multi-proc/backup"

def run(file):
    print(f"Handling {file}")
    time.sleep(1)
    subprocess.call(["rsync", "-arq", file, dest])

if __name__ == "__main__":
    file_list = []
    for root, dirs, files in os.walk(src, topdown = False):
        for name in files:
            if re.match(".*(.jpg)$",name):
                file_list.append(name)
    #Create a pool of specific number of cpus
    p = Pool(len(file_list))
    p.map(run, file_list)

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)")
