def find_peak_index(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        # If the element to the right is greater, a peak must exist on the right
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            # Otherwise, the peak is on the left (including mid)
            right = mid
            
    return left

# Example usage:
arr = [3, 4, 6, 7, 5]
print(f"Index of peak: {find_peak_index(arr)}") 
# Output: 3 (which is the value 7)