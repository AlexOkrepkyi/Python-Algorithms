class Solution:

    def longest_common_prefix(self, strs: List[str]) -> str:

        common_prefix = []

        for letter in zip(*strs):                # create a series of tuples with corresponding items from each word
            if len(set(letter)) == 1:            # if tuple has only 1 unique letter
                common_prefix.append(letter[0])  # append it to the "common_prefix" list
            else:
                break                            # else break

        return "".join(common_prefix)


"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
