import random
import time
import math
import copy

def insertion_sort(input):
    output = [input[0]]
    for i in input[1:]:
        index = 0
        for j in output:
            if i < j:
                output.insert(index, i)
                break
            index +=1

    return output

def selection_sort(input):
    # the subset of input that is sorted, initally 0
    sorted = 0
    # the minimum value at the current iteration, for now the first element
    min = input[sorted]
    min_idx = 0

    
    #when the sorted elements are equal to length of the input, exit
    while sorted < len(input) -1:
        #used to track the current index
        #iterate over the unsorted subset looking for the minimum value
        for i, val in enumerate(input[sorted:]):
            if val < min:
                #update the minimum value, take note of its index
                min = val
                min_idx = i + sorted
            

        # swap the min with the end of the sorted line after each index of the 
        # iteration
        temp = input[sorted]
        input[sorted] = min
        input[min_idx] = temp

        sorted += 1
        min = input[sorted]
    
    return input
        
def merge_sort(input):
    working_list = copy.deepcopy(input)

    def top_down_merge(a, begin, middle, end, b):
        i = k = begin
        j = middle

        for _ in a[begin: end]:
            if i < middle and (j >= end or a[i] < a[j]):
                b[k] = a[i]
                i +=1
            else:
                b[k] = a[j]
                j += 1
            
            k += 1 

    def top_down_split_merge(b, begin, end,a):
        if end - begin < 2:
            return
        middle = int((end + begin) / 2)
        top_down_split_merge(a, begin, middle, b)
        top_down_split_merge(a, middle, end, b)
        top_down_merge(b, begin, middle, end, a)

    top_down_split_merge(working_list, 0, len(input), input)



def bubble_sort(input):
    swap_count = 0
    input_length = len(input)
    while True:
        for i, val in enumerate(input):
            if i + 1 == input_length:
                continue
            next = input[i + 1]
            if val > next:
                input[i] = next
                input[i + 1] = val
                swap_count += 1
        if swap_count == 0:
            break
        swap_count = 0
    return input


if __name__ == '__main__':
    l = []
    for i in range(1000):
        l.append(random.randint(1,1000))

    start = time.time()
    
    # insertion_sort(l)
    # selection_sort(l)
    # bubble_sort(l)
    # comb_sort(l)
    merge_sort(l)
    # print(l)
    print(f"Sort time is {time.time() - start}ms")