class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        min_index = 0
        min_ones_count = -1

        for rows in range(0, len(mat)):
            temp_count = 0
            for numbers in mat[rows]:
                temp_count += numbers
            if temp_count > min_ones_count:
                min_ones_count = temp_count
                min_index = rows
        
        return [min_index, min_ones_count]


        