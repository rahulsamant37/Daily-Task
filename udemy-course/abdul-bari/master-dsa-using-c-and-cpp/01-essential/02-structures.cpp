#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

struct rectangle {
    int length;
    int breadth;
} r2, r3, r4;

struct rectangle r1;

int main() {
    struct rectangle re;
    re.breadth = 10;
    re.length = 12;
    cout << "Area of rectangle is : " << re.breadth*re.length;
    return 0;
}
