// Function to increment a number using pass by pointer
#include <iostream>
using namespace std;

void increment(int *x)
{
    (*x)++;   // Increment the value at the address
}

// Driver Code
int main()
{
    int a = 45;

    cout << "Before Increment\n";
    cout << "a = " << a << "\n";

    increment(&a);

    cout << "After Increment with pass by pointer\n";
    cout << "a = " << a << "\n";
}