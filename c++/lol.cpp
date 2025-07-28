#include <iostream>

using namespace std;

void even_indecator(int num){
if(num%2 == 0){
    cout<< "Even"<< endl;
}else{
  cout<< "Odd"<<endl;
}

}

int main(){

    int x;
    cout <<"enter your num: ";
    cin >> x;

    even_indecator(x);

    return 0;
}