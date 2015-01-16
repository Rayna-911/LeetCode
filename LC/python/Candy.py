class Solution:
    # @param ratings, a list of integer
    # @return an integer
    #dp
    def candy(self, ratings):
        res = [1] * len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                res[i] = res[i-1]+1
        for i in range(len(ratings)-1,0,-1):
           if ratings[i]<ratings[i-1]:
               if res[i] >= res[i-1]:
                   res[i-1] = res[i]+1
        return sum(res)

        
