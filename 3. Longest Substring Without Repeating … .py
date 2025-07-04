class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num_max = 0
        current_num = 0

        substring_list: list[str] = []
        for char in s:
            if char not in substring_list:
                current_num += 1
            else:
                num_max = max(num_max, current_num)
                substring_list = substring_list[substring_list.index(char)+1:]
                current_num = len(substring_list) + 1
            substring_list.append(char)
        return max(num_max, current_num)
