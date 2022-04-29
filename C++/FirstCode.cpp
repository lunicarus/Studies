#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main()
{
    int num;
    int ex;
    string name;
    cout << "Hello USER, tell me your name" << endl;
    getline(cin, name); //&& way to get strings with whitespaces
    cout << "Nice to meet you " << name << ", please inform a number and a exponential" << endl;
    cin >> num >> ex; //&& multiple inputs
    cout << "The result is " << pow(num, ex) << endl;
    return 0;
}