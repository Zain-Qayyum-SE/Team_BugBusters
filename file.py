#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    srand(time(0));

    // Room data
    string roomType[3] = {"Single", "Double", "Deluxe"};
    int price[3] = {3000, 5000, 8000};
    int available[3] = {5, 3, 2};

    string facilities[3] = {
        "• Single Bed\n• Free WiFi\n• Attached Bathroom",
        "• Double Bed\n• Free WiFi\n• TV\n• Attached Bathroom",
        "• King Size Bed\n• Free WiFi\n• TV\n• AC\n• Mini Fridge"
    };

    int choice, days;

    // STEP 1: Show facilities only
    cout << "\n========= ROOM FACILITIES =========\n";
    for (int i = 0; i < 3; i++) {
        cout << "\n" << i + 1 << ". " << roomType[i] << " Room";
        cout << "\n   Price per Day : Rs." << price[i];
        cout << "\n   Facilities    :\n   " << facilities[i] << endl;
    }

    // STEP 2: User choice
    cout << "\nSelect Room Type (1-3): ";
    cin >> choice;

    if (choice < 1 || choice > 3) {
        cout << "Invalid choice!";
        return 0;
    }

    int index = choice - 1;

    // STEP 3: Check availability
    if (available[index] <= 0) {
        cout << "\nSorry! No rooms available for this type.";
        return 0;
    }

    cout << "\nRoom is available! (" << available[index] << " left)\n";

    // STEP 4: Days
    cout << "Enter number of days to stay: ";
    cin >> days;

    // STEP 5: Random room number
    int roomNumber = (rand() % 100) + 101;

    // STEP 6: Bill
    int totalBill = price[index] * days;
    available[index]--;

    // STEP 7: Final summary
    cout << "\n========= BOOKING CONFIRMED =========\n";
    cout << "Room Type   : " << roomType[index] << endl;
    cout << "Room Number : " << roomNumber << endl;
    cout << "Days Stayed : " << days << endl;
    cout << "Total Bill  : Rs." << totalBill << endl;

    cout << "\nEnjoy your stay!\n";

    return 0;
}