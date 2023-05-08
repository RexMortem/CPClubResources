#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    int n,q;
    cin >> n >> q;
    
    vector<int> a[n];
    
    for (int i = 0; i < n; i++){
        int k;
        cin >> k;
        
        vector<int> NewVector;
         
        for (int j = 0; j < k; j++){
            int temp;
            cin >> temp;
            
            NewVector.push_back(temp);
        }
        
        a[i] = NewVector;
    }   

    for (int qi = 0; qi < q; qi++){
        int i, j;
        cin >> i >> j;
        
        vector<int> temp = a[i];
        
        cout << temp[j] << "\n";
    }

    return 0;
}
