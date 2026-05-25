class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_hashmap = {};

        for i, n in enumerate(nums):
            diff = target-n
            if diff in nums_hashmap:
                return[nums_hashmap[diff], i]
            else:
                nums_hashmap[n] = i;

        
        



        