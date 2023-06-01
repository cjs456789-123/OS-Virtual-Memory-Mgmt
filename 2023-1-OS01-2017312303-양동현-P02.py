from MIN import MINalgorithm
from FIFO import FIFOalgorithm
from LRU import LRUalgorithm
from LFU import LFUalgorithm
# from WS import WSalgorithm

### +++ input 예외사항 체크하기 +++


with open('input.txt', 'r') as f:
    lines = f.readlines()
    
    # ===============================
    # N: process가 갖는 page 개수 (최대 100)
    # M: 할당 page frame 개수 (최대 20, WS 기법에서는 비사용)
    # W: window size (최대 100, WS 기법에서만 사용)
    # K: page reference string 길이 (최대 1,000)
    # ===============================
    n, m, w, k = [int(l) for l in lines[0].split(' ')]
    array = [int(l) for l in lines[1].split(' ')]
    
    print("MIN")
    MINalgorithm(n, m, k, array)
    print()
    print("FIFO")
    FIFOalgorithm(n, m, k, array)
    print()
    print("LRU")
    LRUalgorithm(n, m, k, array)
    print()
    print("LFU")
    LFUalgorithm(n, m, k, array)
    print()
    # print("WS")
    # WSalgorithm(n, w, k, array)
    

    