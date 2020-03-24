#include<stdio.h>
void swap(int *num1, int *num2)
{
    *num1 += *num2;
    *num2 = *num1 - *num2;
    *num1 -= *num2;
}

int main()
{
    int num1, num2;
    printf("Enter two numbers:");
    scanf("%d%d", &num1, &num2);
    printf("Before swapping:\nNum1 = %d\nNum2 = %d", num1, num2);
    swap(&num1, &num2);
    printf("After swapping:\nNum1 = %d\nNum2 = %d", num1, num2);
    return 0;
}
