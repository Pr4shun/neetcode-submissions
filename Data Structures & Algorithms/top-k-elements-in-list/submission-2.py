class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        array = [[] for i in range(len(nums)+1)]


        for num in nums:
            if num in hashmap:
                hashmap[num] = hashmap[num]+1
            else:
                hashmap.update({num:1})

        for num in hashmap.keys():
            array[hashmap[num]].append(num)

        # returning k elements

        output = []
        for i in range(len(array)-1, 0, -1):
            for num in array[i]:
                output.append(num)
                if len(output) == k:
                    return output

        



        

