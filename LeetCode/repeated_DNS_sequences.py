class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        setval = set()
        set2 = set()
        for i in range(len(s)-9):
            string = s[i:i+10]
            print(string)
            if string in setval:
                set2.add(string)
            setval.add(string)
        return list(set2)
                
                
            