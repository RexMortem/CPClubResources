#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a,b;
    
    cin >> a >> b;
    cout << a.size() << " " << b.size() << endl;
    
    string c = a + b;
    
    cout << c << endl;
    
    char swap = a[0];
    a[0] = b[0];
    b[0] = swap;
    
    cout << a << " " << b;
    return 0;
}
