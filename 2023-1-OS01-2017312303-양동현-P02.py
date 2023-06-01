from MIN import MINalgorithm
from FIFO import FIFOalgorithm
from LRU import LRUalgorithm
from LFU import LFUalgorithm
from WS import WSalgorithm

with open('input.txt', 'r') as f:
    lines = f.readlines()
    
    # =======================================================
    # 요구 명세서에 주어진 입력 포맷
    #
    #   N: process가 갖는 page 개수 (최대 100)
    #   M: 할당 page frame 개수 (최대 20, WS 기법에서는 비사용)
    #   W: window size (최대 100, WS 기법에서만 사용)
    #   K: page reference string 길이 (최대 1,000)
    # =======================================================

    n, m, w, k = [int(l) for l in lines[0].split(' ')]
    array = [int(l) for l in lines[1].split(' ')]
    
    # 입력값 범위를 벗어난 경우 예외 처리 수행
    
    if n > 100 or n < 0:
        print("입력값 n={}가 범위를 벗어났습니다. 다시 입력해주세요".format(n))
    elif m > 20 or m < 0:
        print("입력값 m={}가 범위를 벗어났습니다. 다시 입력해주세요".format(m))
    elif k > 10000 or k < 0:
        print("입력값 k={}가 범위를 벗어났습니다. 다시 입력해주세요".format(k))
    else:
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
        if w > 100 or w < 0:
            print("입력값 w={}가 범위를 벗어났습니다. 다시 입력해주세요".format(w))
        else:
            print("WS")
            WSalgorithm(n, w, k, array)
    

