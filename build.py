def solution(list_of_nums):
    even,odd = 0,0
    for i in list_of_nums:
        if(i%2 == 0):
            even += 1
        else:
            odd += 1
    return dict({'ODD':odd,'EVEN':even})

print solution([1,2,3,9,5,6])
