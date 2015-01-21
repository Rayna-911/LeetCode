class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        q1 = [start]
        n = 1
        dict.add(end)
        
        while q1:
            q2 = []
            while q1:
                tmp = q1.pop(0)
                for i in range(len(tmp)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        word = tmp[:i]+j+tmp[i+1:]
                        if word in dict:
                            q2.append(word)
                            dict.remove(word)
            if end in q2:
                return n+1
            else:
                n += 1
            q1 = q2
        return 0
         
