# WS
# Scheme
#   -> VA



def WSalgorithm(n, w, k, array):    
    memory_state = [] # 초기 할당된 page frame들은 모두 비어 있는 것으로 가정 (요구 명세서에서 명시됨)
    page_fault = 0
    page_fault_list = [0] * k
    timestamp = []      # window size에 포함된 reference 저장
    
    for i in range(k):
        p_ws, q_ws = None, None # 들어온 페이지, 나간 페이지
        num_frames_allocated = 0 # 할당된 page frame 개수
        
        print("{}번째:".format(i))
        
        # reference 일단 기록 (중복 허용)
        timestamp.append(array[i])
        
        memory_state = list(set(timestamp[max(0, i-w-1) : i])) # 중복 제거
        
        if array[i] not in memory_state:
            
            
            # 들어온 페이지 추가
            p_ws = array[i]
            memory_state.append(p_ws)
            # page fault 기록           
            page_fault += 1
            page_fault_list[i] = 1
        
        print("Memory_state: {}".format(memory_state))
        
        # 나간 페이지 반영: 이전 reference vs 현재 reference
        previous_ref = timestamp[max(0, i-w-1) : max(0, i-1)]
        if previous_ref != []: 
            previous = previous_ref[0]
            if previous not in timestamp[max(0, i-w) : i]:
                q_ws = previous
                memory_state.remove(previous)
            
            
            
        num_frames_allocated = len(memory_state)
        
        
        print("Memory_state: {}".format(memory_state))
        print("P_ws: {}, Q_ws: {}".format(p_ws, q_ws))
        print("# of frames allocated: {}".format(num_frames_allocated))
        print()
        

        
    return print("총 page fault 횟수: {}\n메모리 상태 변화 과정: {}".format(page_fault, page_fault_list))