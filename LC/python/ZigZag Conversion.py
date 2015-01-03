class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        res = [[] for i in range(nRows)]
        position = 0
        ditect = 1
        for i in s:
            res[position].append(i)
            if position == nRows-1:
                direct = -1
            elif position == 0:
                direct = 1
            position += direct
        return ''.join([''.join(rows) for rows in res])

                
            
        
