import random

class QuickSort:
    def init(self, array):
        self.array = array

    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1

        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]

        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

    def partition_random(self, low, high):
        pivot = random.randint(low, high)
        self.array[pivot], self.array[high] = self.array[high], self.array[pivot]
        return self.partition(low, high)

    def sort(self, low, high, randomized):
        if low < high:
            pivot_func = self.partition_random if randomized else self.partition
            pivot = pivot_func(low, high)
            self.sort(low, pivot - 1, randomized)
            self.sort(pivot + 1, high, randomized)

while True:
    print("Press Ctrl+C to exit...")
    array = [int(i) for i in input("Enter array: ").split()]
    sort_instance = QuickSort(array)
    
    # Sort using the deterministic method
    sort_instance.sort(0, len(array) - 1, randomized=False)
    print("Deterministic variant of sort:", sort_instance.array)
    
    # Sort using the randomized method
    sort_instance.sort(0, len(array) - 1, randomized=True)
    print("Randomized variant of sort:", sort_instance.array)
