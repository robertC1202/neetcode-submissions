class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:

            counting = [0] * 26

            for char in word:
                counting[ord(char) - ord('a')] += 1


            hashMap[tuple(counting)].append(word)

        return list(hashMap.values())