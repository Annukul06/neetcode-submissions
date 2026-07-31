class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            goal = target - num
            if goal in map:
                return[map[goal],i]
            map[num] = i


            
             
                
                

                

                    





        

        