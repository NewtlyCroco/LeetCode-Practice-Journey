class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        length = len(arr)
        for i in range(0,length):
            for j in range(0,length):
                if i != j:
                    if arr[i] == (arr[j] * 2):
                        return True

        return False
        