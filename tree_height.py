# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    seen = np.zeros([n],dtype=np.int32)
    maxH = np.zeros([n],dtype=np.int32)
    
    for i in range(n):
        if seen[i] == 0:
            times = 0
            current = i
            while current != -1:
                times = times + 1
                maxH[i] = times
                current = parents[current]
                seen[current] = 1
    return max(maxH)


def main():
    nameFile = input()
    if "I" in nameFile:
        numbers = int(input())
        parents = list(map(int, input().split()))
        computed = compute_height(numbers,parents)
        print(computed)
    elif "F" in nameFile:
        fileName = input()
        if "a" not in fileName:
            file = "test/" + fileName
            with open(file,"r") as fi:
                numbers = int(fi.readline())
                parents = list(map(int, fi.readline().strip().split()))
                compuded = compute_height(numbers, parents)
                print(compuded)

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()