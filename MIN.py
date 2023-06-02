# MIN algorithm
# Scheme
#   -> Replace the page that will not be used for the longest period of time
# Tie-breaking rule
#   -> Page with smallest page number

def MINalgorithm(n, m, k, array):
    # MIN algorithm
    memory_state = []
    page_fault = 0
    page_fault_list = [None] * k
    
    
    for i in range(k):
        replace_page = []
        if len(memory_state) < m:
            if array[i] not in memory_state:
                memory_state.append(array[i])
                page_fault_list[i] = bool(True)
                page_fault += 1
        else:
            if array[i] not in memory_state:
                for j in range(i+1, k):
                    if array[j] in memory_state and array[j] not in replace_page:
                        replace_page.append(array[j])
                # replace_page 리스트에 모두 들어있는 경우
                if len(replace_page) == m:
                    memory_state[memory_state.index(replace_page[-1])] = array[i]
                # replace_page 리스트에 일부 page만 들어온 경우
                else:
                    replace = min([x for x in memory_state if x not in replace_page])
                    memory_state[memory_state.index(replace)] = array[i]
                
                page_fault_list[i] = bool(True)
                page_fault += 1
        
        if i==0:
            print("메모리 상태 변화 과정 (page fault 발생 위치 표시)")
            print()
        print("{}번째".format(i))
        print("Memory_state: {}".format(memory_state))
        print("page fault: {}".format(page_fault_list[i]))
        print()
    
    return print("총 page fault 횟수: {}".format(page_fault))