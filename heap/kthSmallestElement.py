#max heap
import heapq

def find_kth_smallest(nums, k):
    max_heap = []
    
    # Populate the max heap with the first K elements
    for i in range(k):
        # print(-nums[i])
        heapq.heappush(max_heap, -nums[i])
        
    # For the remaining elements, if an element is smaller than the largest element in the max heap,
    # replace the largest element with the smaller element and adjust the max heap accordingly.
    for i in range(k, len(nums)):
        if nums[i] < -max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -nums[i])
    
    # The negation of the root of the max heap will be the Kth smallest element
    return -max_heap[0]
nums = [3, 1, 7, 2, 9, 5]
k = 3

kth_smallest = find_kth_smallest(nums, k)
print(kth_smallest)  # Output: 3

