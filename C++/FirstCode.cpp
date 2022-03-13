#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main()
{
    int num;
    int ex;
    std::string name;
    std::cout << "Hello USER, tell me your name" << std::endl;
    std::getline(std::cin, name); //&& way to get strings with whitespaces
    std::cout << "Nice to meet you " << name << ", please inform a number and a exponential" << std::endl;
    std::cin >> num >> ex; //&& multiple inputs
    std::cout << "The result is " << pow(num, ex) << std::endl;
    return 0;
}