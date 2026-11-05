class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = defaultdict(list)

        for word in strs:

            freq_array = [0] * 26

            for char in word:
                freq_array[ord(char) - ord('a')] += 1
            
            hashMap[tuple(freq_array)].append(word)
        
        return list(hashMap.values())




