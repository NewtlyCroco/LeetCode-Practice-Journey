class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        #ok for reference I deleted my last solution, and have been weirdly stumped by this problem, reapproaching with hashmaps
        #makes so much sense, as if we have a value in our hashmap, we can just add to the weight, and if not add a new value with eight to the map
        #I did look at the solution for this problem to get the hashmap solution, feeling dumb lol, but concieded this one!

        values = {}

        for valuepairs in items1:
            valueinsert = valuepairs[0]
            values[valueinsert] = values.get(valuepairs[0],0) + valuepairs[1]

        for valuepairs in items2:
            valueinsert = valuepairs[0]
            values[valueinsert] = values.get(valuepairs[0],0) + valuepairs[1]


        results = []
        for key, value in values.items():
            results.append((key, value))
        results.sort()
        return results

            

        




        