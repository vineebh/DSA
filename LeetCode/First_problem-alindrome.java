class Solution {
    public boolean isPalindrome(int x) {
        boolean result=false;
        int num=x,rem,temp=0;
        while (num>0)
        {
            rem=num%10;
            temp=temp*10+rem;
            num/=10;
        }
        if (temp==x)
            result=true;
        return result;
    }
}