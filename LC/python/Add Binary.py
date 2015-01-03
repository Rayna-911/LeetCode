class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
#    def addBinary(self, a, b):
#        num1 = int(a,2)
#        num2 = int(b,2)
#        res = bin(num1+num2)
#        return res[2::]
    def addBinary(self, a, b):
        res = []
        v = 0
        for i in range(0,max(len(a),len(b))):
            if i < len(a) and a[len(a)-1-i] == '1':
                v += 1
            if i < len(b) and b[len(b)-1-i] == '1':
                v +=1
            res.insert(0,str(v%2))
            v /= 2
        while v > 0:
            res.insert(0,str(v%2))
            v /= 2
        return (''.join(res))
        
