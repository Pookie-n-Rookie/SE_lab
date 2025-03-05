
void f1(int x,int y)
{
    printf("The numbers are : ");
    printf("< %d, %d> \n",x,y);
}
void f2(int*p ,int *q)
{
    *p = (*p) + (*q);
    *q = (*p) -(*q);
    *p = (*p) - (*q);
}
