#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

string endec(string data, int key, bool mode) // 0 - dec, 1 - enc
{
    string result;
    for(auto s : data){
        result += s + (mode ? key : -key); 
    }
    return result;
}

int main(int argc, char const *argv[])
{
    string input;
    int enc_or_dec = 0, key = 0;
    cout << "1. Шифрувати, 2. Розшифрувати\n";
    cin >> enc_or_dec;
    cout << "Введіть ключ: ";
    cin >> key;
    
    fstream f("text.txt");
    stringstream ss;
    ss << f.rdbuf();
    f.seekg(0);
    f << endec(ss.str(), key, enc_or_dec == 2);
    f.close();
    return 0;
}
