class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
            
        path = path.split('/')
        res = '/'
        for i in path:
            if i == '..':
                if res != '/':
                    res = '/'.join(res.split('/')[:-1])
                    if res == '':
                        res = '/'
                        
            elif i != '.' and i != '':
                if res != '/':
                    res = res+'/'+i
                else:
                    res = res + i
        return res
        
