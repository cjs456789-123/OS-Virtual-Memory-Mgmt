# LRU
# Scheme
#   -> Replace the page that has not been used for the longest period of time
# Requirements
#   -> Timestamping

def LRUalgorithm(n, m, k, array):
    # LRUalgorithm
    memory_state = []
    page_fault = 0
    page_fault_list = [0] * k
    timestamp = []
    
    for i in range(k):
        replace_page = []
        if len(memory_state) < m:
            if array[i] not in memory_state:
                memory_state.append(array[i])
                page_fault_list[i] = 1
                page_fault += 1
        else:
            if array[i] not in memory_state:
                # page frame 순서를 유지하면서 먼저 들어온 page 교체하기(timestamping)
                for time in timestamp:
                    if time in memory_state:
                        replace = time
                        break
                memory_state[memory_state.index(replace)] = array[i]
                page_fault_list[i] = 1
                page_fault += 1
        
        if array[i] in timestamp:
            timestamp.remove(array[i])    
        timestamp.append(array[i])
    return print("총 page fault 횟수: {}\n메모리 상태 변화 과정: {}".format(page_fault, page_fault_list))