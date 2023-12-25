class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # - Mapping value to index
        num_map = {}
        two_sum_list = []
        for i, num in enumerate(nums):
            target_diff = target - num
            if target_diff in num_map.values():
                two_sum_list.append(i)
                two_sum_list.append(list(num_map.keys())[list(num_map.values()).index(target_diff)])
                num_map[i] = num
            else:
                num_map[i] = num

        return two_sum_list