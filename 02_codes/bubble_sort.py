class Solution():
    def bubbleSort(self, array: list) -> list:
        n = len(array)
        for i in range(n):
            # works without this flag but will be unoptimized
            swapped = False
            for j in range(n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    swapped = True
            if not swapped:
                break


def main():
    array = [5,4,3,2,1]
    obj = Solution()
    obj.bubbleSort(array)
    return array
    
if __name__ == "__main__":
    print(main())

