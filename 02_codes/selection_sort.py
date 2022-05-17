class Solution():
    def selectionSort(self, array: list) -> None:
        n = len(array)
        for i in range(n):
            min_elem = i
            for j in range(i + 1, n):
                if array[j] < array[min_elem]:
                    min_elem = j
            array[i], array[min_elem] = array[min_elem], array[i]

        
def main():
    array = [5,4,3,2,1]
    obj = Solution()
    obj.selectionSort(array)
    return array


if __name__ == "__main__":
    print(main())

