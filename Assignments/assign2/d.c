#include <stdio.h>


int main()
{
   int i,j,k;
   for ( i= 0 ; i< 10; i++)
    for ( j = 0; j< 200; j++)
        for (k = 0; k< 3000; k++)
        {
            int t1,t2;
            t1=i;
            t2=j;
            if ((k !=0) && (k%1000 == 0))
                printf ("you have reached [%d][%d][%d]-th iteraion \n",t1,t2,k);
        }
}

