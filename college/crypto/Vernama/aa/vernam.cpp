#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <fstream>
using namespace std;

vector<int> key(string text)
{
    vector<int> res;
    srand(time(nullptr));
    for (int i = 0; i < text.length(); i++)
    {
        res.push_back((char)(rand() % 10));
    }
    return res;
}
string cipher(string text,const vector<int>& key)
{
    ostringstream res;
    for (int i = 0; i < text.length(); i++)
    {
        res << (char)(text[i] ^ (char)key.at(i));
    }
    return res.str();
}
string decipher(string text,const vector<int>& key)
{
    return cipher(text, key);
}
string keyToString(const vector<int>& k)
{
    ostringstream res;
    for (auto &&i : k) res << i << " ";
    return res.str();
    
}
int main(int argc, char const *argv[])
{
    string text;
    vector<int> ky;
    cout << "Введіть текст: ";
    cin >> text;
    bool choice = 0;
    cout << "0. Шифрувати 1. Дешифрувати:\n";
    cin >> choice;
    if(!choice){
        ky = key(text);
        string res = cipher(text, ky);
        cout <<"Шифротекст: |"<< res <<'|'<<endl;
        cout <<"Ключ: |" << keyToString(ky) << '|' << endl;
        ofstream f("key.txt");
        f << res << '\n' << keyToString(ky) << '\n';
    } else {
        cout << "Введіть ключ: ";
        for (int i = 0; i <= text.length(); i++)
        {
            int buf;
            cin >> buf;
            ky.push_back(buf);
        }
        cout << "Розшифроване: " << decipher(text, ky) << '\n';
    }
}
