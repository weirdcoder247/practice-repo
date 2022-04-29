class Solution():
    def mergeSort(self, array: list) -> None:
        # Break recursion when array length is 1
        if len(array) > 1:
            middle_index = len(array)//2
            left_array = array[:middle_index]
            right_array = array[middle_index:]
            
            self.mergeSort(left_array)
            self.mergeSort(right_array)
            
            i = j = k = 0
            
            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    array[k] = left_array[i]
                    i += 1
                else:
                    array[k] = right_array[j]
                    j += 1
                k += 1
            
            while i < len(left_array):
                array[k] = left_array[i]
                i += 1
                k += 1
            
            while j < len(right_array):
                array[k] = right_array[j]
                j += 1
                k += 1
        

def main():
    array = [5,4,3,2,1]
    obj = Solution()
    obj.mergeSort(array)
    return array


if __name__ == "__main__":
    print(main())

