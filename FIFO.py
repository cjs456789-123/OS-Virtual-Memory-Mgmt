# FIFO
# Scheme
#   -> Replace the oldest page
# Requirements
#   -> Timestamping

def FIFOalgorithm(n, m, k, array):
    memory_state = []
    page_fault = 0
    page_fault_list = [None] * k
    j = 0
    
    for i in range(k):
        replace_page = []
        if len(memory_state) < m:
            if array[i] not in memory_state:
                memory_state.append(array[i])
                page_fault_list[i] = bool(True)
                page_fault += 1
        else:
            if array[i] not in memory_state:
                # page frame 순서를 유지하면서 먼저 들어온 page 교체하기(timestamping)
                memory_state[j] = array[i]
                page_fault_list[i] = bool(True)
                page_fault += 1
                if j == m-1:
                    j=0
                else:
                    j+=1
        
        if i==0:
            print("메모리 상태 변화 과정 (page fault 발생 위치 표시)")
            print()
        print("{}번째".format(i))
        print("Memory_state: {}".format(memory_state))
        print("page fault: {}".format(page_fault_list[i]))
        print()
    
    return print("총 page fault 횟수: {}".format(page_fault))