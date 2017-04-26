// Fizz.c is a program that prints the numbers from 1 to 100. 
// But for multiples of three print “Fizz” instead of the number 
// and for the multiples of five print “Buzz”. 
// For numbers which are multiples of both three and five print “FizzBuzz”.
// Problem source: https://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/

#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 100; i++)
    {
        if (i % 3 == 0 && i % 5 == 0)
        {
            printf("FizzBuzz\n");
        }
        
        if (i % 3 == 0)
        {
            printf("Fizz\n");
        }
        
        if (i % 5 == 0)
        {
            printf("Buzz\n");
        }
        
        else 
        {
            printf("%i\n",i);
        }
    }

    return 0;
}
