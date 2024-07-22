class Solution(object):
    def sortPeople(self, names, heights):
        n=len(names)
        temp={}
        result=[]

        for h,n in zip(heights,names):
            temp[h] =n
        
        myKeys=sorted(temp.keys(),reverse=True)
        
        for i in myKeys:
            result.append(temp[i])

        return result
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """