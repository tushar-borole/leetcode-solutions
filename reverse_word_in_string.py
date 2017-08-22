class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        outputArray=[]
        convertedArray=s.split()
        for m in convertedArray:
            outputArray.append(m[::-1]) #reverse the string and append to the array

        outputString=' '.join(outputArray);

        return outputString


a = Solution()
print(a.reverseWords("Let's take LeetCode contest")) #output : s'teL ekat edoCteeL tsetnoc