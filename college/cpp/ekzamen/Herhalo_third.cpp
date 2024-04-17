#include <iostream>

using namespace std;

string monthName(int monthNumber) {
    switch(monthNumber) {
    case 1: return "Січень";
    case 2: return "лютий";
    case 3: return "березень";
    case 4: return "квітень";
    case 5: return "травень";
    case 6: return "червень";
    case 7: return "липень";
    case 8: return "серпень";
    case 9: return "вересень";
    case 10: return "жовтень";
    case 11: return "листопад";
    case 12: return "грудень";
    default: return "Wrong number of month!";
    }
}

int main() {
    int monthNumber;
    cout << "Введіть номер місяця (1-12)";
    cin >> monthNumber;

    string month = monthName(monthNumber);
    cout << "Назва місяця: " << month << endl;

    return 0;
}
