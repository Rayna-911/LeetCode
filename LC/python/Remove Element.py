class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if len(A) == 0:
            return 0
        else:
            while elem in A:
                A.remove(elem)
            return len(A)
        
