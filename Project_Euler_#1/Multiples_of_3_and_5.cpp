#include <iostream>
using namespace std;

int main() {

    long int divisibility_3, divisibility_5, divisibility_15, test_cases, N;
    
    cin >> test_cases;
    
    for (test_cases; test_cases > 0; test_cases--) {
        cin >> N;

        //Finds number of terms divisibly by 3, 5, and 15
        divisibility_3 = (N - 1) / 3;
        divisibility_5 = (N - 1) / 5;
        divisibility_15 = (N - 1) / 15;

        //Output uses sum of consecutive integers formula and removes multiples of 15
        cout << (3*divisibility_3*(divisibility_3 + 1) + 5*divisibility_5*(divisibility_5 + 1) - 15*divisibility_15*(divisibility_15 + 1)) / 2 << endl;
    }

    return 0;
}