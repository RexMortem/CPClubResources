#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);



int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));
    
    // Write your code here

    switch (n){
        case 1:
            printf("%s", "one");
            break;
        case 2:
            printf("%s", "two");
            break;
        case 3:
            printf("%s", "three");
            break;
        case 4:
            printf("%s", "four");
            break;
        case 5:
            printf("%s", "five");
            break;
        case 6:
            printf("%s", "six");
            break;
        case 7:
            printf("%s", "seven");
            break;
        case 8:
            printf("%s", "eight");
            break;
        case 9:
            printf("%s", "nine");
            break;
        default:
            printf("%s", "Greater than 9");
    }
    
    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
