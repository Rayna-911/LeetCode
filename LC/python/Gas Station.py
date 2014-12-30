class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost):
            return -1
        curr = 0
        res = 0
        for i in range(len(gas)):
            curr = gas[i]-cost[i]+curr
            if curr < 0:
                curr = 0
                res = i+1
        return res
