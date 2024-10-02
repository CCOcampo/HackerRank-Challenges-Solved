def maxSubarray(arr):
    if all(value < 0 for value in arr):
        max_negative = max(arr)
        return [max_negative, max_negative]

    def subarray_sum(arr):
        current_max = global_max = arr[0]
        
        for value in arr[1:]:
            current_max = max(value, current_max + value)
            global_max = max(global_max, current_max)
        return global_max

    def subsequence_sum(arr):
        total_sum = 0
        for value in arr:
            if value > 0:
                total_sum += value
        return total_sum

    subarray_max = subarray_sum(arr)
    subsequence_max = subsequence_sum(arr)

    return [subarray_max, subsequence_max]

#Example

arr = [-1,-2,-3,-5,-8,1,4,2,5,7,5,1,-1,3]
print(maxSubarray(arr))  

