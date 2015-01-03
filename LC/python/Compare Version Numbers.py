class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        if '.' in version1:
            version1 = version1.split('.')
            while int(version1[-1]) == 0:
                del version1[-1]
        else:
            version1 = [str(int(version1,10))]
            
        if '.' in version2:
            version2 = version2.split('.')
            while int(version2[-1]) == 0:
                del version2[-1]
        else:
            version2 = [str(int(version2,10))]
        
        i = 0 
        while i < (min(len(version1),len(version2))):
            if int(version1[i]) < int(version2[i]):
                return -1
            elif int(version1[i]) == int(version2[i]):
                i+=1
            else:
                return 1
        if len(version1)>len(version2):
            return 1
        elif len(version1)<len(version2):
            return -1
        else:
            return 0
