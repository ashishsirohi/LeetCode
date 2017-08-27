import math

def maxSubArray(arr, low, high):
    if high == low:
        return [low, high, arr[low]]
    else:
        mid = int(math.floor((low+high)/2))
        left_low, left_high, left_sum = maxSubArray(arr, low, mid)
        right_low, right_high, right_sum = maxSubArray(arr, mid+1, high)
        cross_low, cross_high, cross_sum = maxCrossingSubArray(arr, low, mid, high)
        if left_sum > right_sum and left_sum > cross_sum:
            return [left_low, left_high, left_sum]
        elif right_sum > left_sum and right_sum > cross_sum:
            return [right_low, right_high, right_sum]
        else:
            return [cross_low, cross_high, cross_sum]


def maxCrossingSubArray(arr, low, mid, high):
    left_sum = 0
    left_index = 0
    sum = arr[mid]
    i = mid - 1
    if mid == low:
        left_index = low
        left_sum = arr[low]
    else:
        while i >= low:
            sum = sum + arr[i]
            if sum > left_sum:
                left_sum = sum
                left_index = i
            i = i - 1


    right_index = 0
    right_sum = 0
    sum = arr[mid+1]
    i = mid + 2
    if mid + 1 == high:
        right_index = high
        right_sum = arr[high]
    else:
        while i <= high:
            sum = sum + arr[i]
            if sum > right_sum:
                right_sum = sum
                right_index = i
            i = i + 1

    return [left_index, right_index, left_sum+right_sum]

#print maxCrossingSubArray([2, -3, 22, -1, 10, 3, 6, -8, 10, -23, 15], 0, 5, 10)
#print maxCrossingSubArray([2, -3], 0, 0, 1)
left_index, right_index, sum = maxSubArray([2, -3, 22, -1, -10, -30, 6, -8, 10, -23, 15], 0, 10)
print left_index
print right_index
print sum
