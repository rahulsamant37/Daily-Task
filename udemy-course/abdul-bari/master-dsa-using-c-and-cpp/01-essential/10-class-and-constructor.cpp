#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

class rectangle {
private:
    int length;
    int breadth;

public:
    rectangle(int l, int b) {
        length = l;
        breadth = b;
    }

    int area () {
        return length*breadth;
    }

    void changeLength(int l) {
        length = l;
    }
};

int main() {
    rectangle rec(5, 10);
    rec.changeLength(20);
    cout << rec.area() << endl;
    return 0;
}
