# LFU
# Scheme
#   -> Replace the page with the smallest reference counts
# Tie-breaking
#   -> LRU
# Requirements
#   -> Accumulated page reference count


def LFUalgorithm(n, m, k, array):
    memory_state = []
    page_fault = 0
    page_fault_list = [None] * k
    timestamp = []      # reference 순서 저장
    # frequency = [0] * n # reference count (인덱스=페이지 번호, 원소값=빈도수)
    frequency = {}      # 리스트 대신 딕셔너리 사용
    # for i in range(1, n+1):
    #     frequency[i] = 0
    
    for i in range(k):
        replace = 0
        if len(memory_state) < m:
            if array[i] not in memory_state:
                memory_state.append(array[i])
                page_fault_list[i] = bool(True)
                page_fault += 1
        else:
            if array[i] not in memory_state:
                freq_of_memory_state = {}
                # memory_state 원소 중 frequency가 가장 작은 page 찾기
                for key, value in frequency.items():
                    if key in memory_state:
                        freq_of_memory_state[key] = value
                
                min_freq = min(freq_of_memory_state.values())
                min_freq_key = [key for key in freq_of_memory_state.keys() if freq_of_memory_state[key] == min_freq]
                
                if len(min_freq_key) == 1:
                    replace = min_freq_key[0]   # min_freq_key = [1] 리스트 형태로 저장되어 슬라이싱 해줌
                else:
                    # Tie-breaking: LRU strategies
                    # min_freq_key 에서 timestamp 순서가 가장 빠른 key 선택
                    for j in timestamp:
                        if j in min_freq_key:
                            replace = j
                            break
                memory_state[memory_state.index(replace)] = array[i]
                page_fault_list[i] = bool(True)
                page_fault += 1
                
        if array[i] in timestamp:
            timestamp.remove(array[i])
        timestamp.append(array[i])
        # print("timestamp: ", timestamp)
        
        if array[i] not in frequency:
            frequency[array[i]] = 1
        else:
            frequency[array[i]] += 1
        # print("frequency: ", frequency)
        # print('\n')
    
        if i==0:
            print("메모리 상태 변화 과정 (page fault 발생 위치 표시)")
            print()
        print("{}번째".format(i))
        print("Memory_state: {}".format(memory_state))
        print("page fault: {}".format(page_fault_list[i]))
        print()
    
    return print("총 page fault 횟수: {}".format(page_fault))