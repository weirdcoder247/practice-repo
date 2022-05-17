class Solution:
    def findTriplets(self, nums, target):
        res = []
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == target:
                        res.append([nums[i], nums[j], nums[k]])
        return res


    def mergeDict(self, d1, d2):
        



def main():
    nums = [2,3,4,5,1,7,8,10]
    target = 10
    d1 = {0:'a', 1:'b'}
    d2 = {0:'c', 2:'d'}
    obj = Solution()
#    return obj.findTriplets(nums, target)
    return obj.mergeDict()
    
if __name__ == "__main__":
    print(main())



class A:
    def m():
        print(“A”)

class B(A):
    def m():
        print(“B”)

class C(A):
    def m():
        print(“C”)

class D(B, C):
    pass

