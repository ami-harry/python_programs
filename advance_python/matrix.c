#include <stdio.h>
int main()
{
    int arr[5], sum = 0, avg = 0;
    printf("Enter the values:\n ");
    for (int i = 1; i <= 5; i++)
    {
        scanf("%d", &arr[i]);
    }

    // printing the sum
    for (int i = 1; i <= 5; i++)
    {

        sum += arr[i];
    }
    printf("the sum is %d \n", sum);
    avg = sum / 5;
    printf("the average is %d\n ", avg);
    return 0;
}