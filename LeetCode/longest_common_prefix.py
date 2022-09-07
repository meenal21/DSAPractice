class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # get the max length and iterate over all the elements:
        # binary search -
        val = list(zip(*strs))
        counter = ""
        for i in val:
            if len(set(i)) == 1:
                counter += set(i).pop()
            else:
                break
        return counter
        