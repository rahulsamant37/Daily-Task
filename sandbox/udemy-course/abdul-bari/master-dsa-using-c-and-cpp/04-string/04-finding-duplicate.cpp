#include <bits/stdc++.h>
using namespace std;

#define endl '\n'


bool check_duplicate(string str) {
    unordered_set<char> s;
    for (char ch: str) {
        if (s.count(ch)) {
            return false;
        }
        s.insert(ch);
    }
    return true;
}

int main() {
    string str1 = "RAHUL";
    string str2 = "SAMANT";
    if (check_duplicate(str1)) {
        cout << "str1 contains no duplicate" << endl;
    } else {
        cout << "str1 contains duplicate" << endl;
    }
    if (check_duplicate(str2)) {
        cout << "str2 contains no duplicate" << endl;
    } else {
        cout << "str2 contains duplicate" << endl;
    }
    return 0;
}
