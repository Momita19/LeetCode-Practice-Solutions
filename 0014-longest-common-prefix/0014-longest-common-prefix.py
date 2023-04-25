class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # algo
        # 1. result
        result = ''
        # 2. zip string in tupple
        for a in zip(*strs):
            print(a)
        # 3. check if not unique, tupple length will be one
            if len(set(a)) == 1:
                result += a[0]
        # 4. if unique then return result
            else:
                return result
        return result