class Solution:

    def encode(self, strs: List[str]) -> str:
        #["hello", "test", "one"], "hellotestone"
        result = ""
        for word in strs:
            result += str(len(word)) + "_" + word

        return result

    def decode(self, s: str) -> List[str]:
        # "hellotestone", ["hello", "test", "one"]
        result = []
        i=0
        while i < len(s):
            j = i
            while s[j] != '_':
                j += 1

            length = int(s[i:j]) 
            i = j + 1
            
            word = s[i:i+length]
            result.append(word)
            
            i += length
        print(result)
        return result