class Solution {
public:
    bool isPrime(int n)
    {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i = i + 6)
        if (n % i == 0 || n % (i + 2) == 0) return false;
        return true;
    }
    vector<int> closestPrimes(int left, int right) {
        int c=0,mindiff=9999;
        int p1=-1,p2=-1,num1,num2;
        for(int i=left;i<=right;i++)
        {
            if (isPrime(i) && p1==-1) {p1=i;c++;}
            else if(isPrime(i) && p1!=-1){p2=i;c++;}
            if(p1!=-1 && p2!=-1)
            {
                //cout<<p1<<" "<<p2<<endl;
                if(p2-p1 < mindiff) 
                {
                    mindiff=p2-p1;
                    num1=p1,num2=p2;
                    //cout<<"!!"<<p1<<" "<<p2<<endl;
                }
                p1=p2;p2=-1;
            }

        }
        if (c>=2){vector<int>arr = {num1,num2};return arr;}
        else {vector<int>arr = {-1,-1};return arr;}
    }
};
