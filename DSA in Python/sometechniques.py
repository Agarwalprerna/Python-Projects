
#2 pointer technique

'''
def find_2_num(numbers , target):
    left =0
    right = len(numbers)-1

    while left < right:
        sum = numbers[left] + numbers[right]


        if sum == target:
            return [ numbers[left] , numbers[right]]

        elif sum > target:
            right -= 1

        else:
            left += 1
    return []        


numbers = [4,5,6,7,8,9]    
print(find_2_num(numbers , 12))

'''

# sliding window technique

def slidingwindow( arr , window_size):

    current_sum =0 

    for i in range(0,window_size):
        current_sum += arr[i]

    best_sum = current_sum    

    print(f"window 1: {arr[0:window_size]} = sum: {current_sum}")    

    
    for i in range(window_size , len(arr)):
        left_value = arr[i-window_size]
        right_value = arr[i]

        current_sum = current_sum -left_value + right_value
        print(f"window {i-window_size + 2}: {arr[i-window_size + 1: i+1]} = sum: {current_sum}")

        if current_sum >best_sum:
            best_sum = current_sum

    return best_sum   


arr = [3,8,2,5,7,6,12]
print("best sum = ",slidingwindow(arr,4))
