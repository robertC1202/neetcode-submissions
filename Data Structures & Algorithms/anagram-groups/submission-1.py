class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            counting = [0] * 26

            for c in word:
                counting[ord(c) - ord('a')] += 1
            
            hashMap[tuple(counting)].append(word)
        
        return list(hashMap.values())