import heapq


def max_sliding_window(arr, k):
    ans = []
    heap = []

    # Initialize the heap with the first k elements
    for i in range(k):
        heapq.heappush(heap, (-arr[i], i))

    # The maximum element in the first window
    ans.append(-heap[0][0])

    # Process the remaining elements
    for i in range(k, len(arr)):
        heapq.heappush(heap, (-arr[i], i))

        # Remove elements that are outside the current window
        while heap[0][1] <= i - k:
            heapq.heappop(heap)

        # The maximum element in the current window
        ans.append(-heap[0][0])

    return ans


arr = [2, 3, 7, 9, 5, 1, 6, 4, 3]
k = 3

# Find the maximum element in each sliding window of size k
result = max_sliding_window(arr, k)

# Print the results
for num in result:
    print(num, end=" ")
