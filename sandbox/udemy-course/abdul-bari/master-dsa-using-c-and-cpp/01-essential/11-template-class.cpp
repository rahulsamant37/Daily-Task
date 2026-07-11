#include <bits/stdc++.h>
#include <iomanip>
using namespace std;

#define endl '\n'


class arithmetic {
    private:
    int a;
    int b;
    public:
    arithmetic(int a, int b) {
        this->a = a;
        this->b = b;
    }

    int add() {
        int c = a+b;
        return c;
    }

    int sub() {
        int c = a-b;
        return c;
    }
};

template<class T>
class arithmeticTemplate {
    private:
    T a;
    T b;
    public:
    arithmeticTemplate(T a, T b);
    T add();
    T sub();
};

template<class T>
arithmeticTemplate<T>::arithmeticTemplate(T a, T b) {
    this->a = a;
    this->b = b;
}

template<class T>
T arithmeticTemplate<T>::add() {
    T c = a + b;
    return c;
}

template<class T>
T arithmeticTemplate<T>::sub() {
    T c = a - b;
    return c;
}

int main() {
    arithmetic num(30, 20);
    cout << num.add() << endl;
    arithmeticTemplate<double> num2(10.0, 5.0);
    // it bydefault printing the significant value so we can set it like this
    cout << fixed << setprecision(1); 
    cout << num2.sub() << endl;
    return 0;
}
