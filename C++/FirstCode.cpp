#include<iostream>
#include<string>
using namespace std;
double power(double num, double ex){
    double tt = num;
    for(int i=1;i < ex;i++){
        num = num*tt;

    }
        return num;
}
int main()
{
    int num;
    int ex;
    std:string name;
    std:: cout << "Hello USER, tell me your name" << std::endl;
    std::getline(std::cin,name);
    std::cout << "Nice to meet you " << name << ", please inform a number and a exponential" << std::endl;
    std::cin >> num >> ex;
    std:: cout << "The result is " << power(num,ex) << std::endl;
    return 0;
}