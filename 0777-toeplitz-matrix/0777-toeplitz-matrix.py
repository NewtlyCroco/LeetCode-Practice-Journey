class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # my approach is quite simple, we dont have to look for any complex pattern
        # but rather just check if the top left value for any given index is either null/invalid, is the same value or is not, and if not, we return false, else if we make it through the whole matrix we can return true
        m = len(matrix)
        n = len(matrix[0]) 
        for collumn in range(0, m):
            for row in range(0, n):
                if topleftvalid(matrix, m, n, row, collumn) is False: #could certainly be done recursively
                    return False
        return True


    

def topleftvalid(matrix, m, n, index_x, index_y) -> bool:
    pos_value = matrix[index_y][index_x]
    topleft_x = index_x-1
    topleft_y = index_y-1
    print(index_y, index_x)
    print("\/")
    print(topleft_y, topleft_x)
    if topleft_x < 0 or topleft_y < 0 or topleft_x >= n or topleft_y >= m:
        return True
    elif pos_value == matrix[topleft_y][topleft_x]:
        return True
    else:
        return False
