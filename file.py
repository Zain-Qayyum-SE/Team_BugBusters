#include <iostream>
#include <string>
#include <iomanip> // Essential for setw() and alignment

using namespace std;

// ---------------- ROOM DATA (Using Parallel Arrays) ----------------

// Room IDs (1, 2, 3) are derived from the array index + 1
const int NUM_ROOMS = 3;

string roomNames[NUM_ROOMS] = {
    "Standard",
    "Executive",
    "Suite"
};

int pricesPerNight[NUM_ROOMS] = {
    10000,
    17000,
    40000
};

string amenitiesList[NUM_ROOMS] = {
    "1 Bed, Study Table, Fridge, Attached Bathroom",
    "2 Beds, Sofa-cum-Bed, Mini Bar, Complimentary Breakfast, Attached Bathroom",
    "Fresh Fruit Basket, Hot Tub, 2 Rooms, TV, Library, Table Tennis"
};

// ---------------- HELPER FUNCTION TO PRINT DOUBLE LINE SEPARATOR ----------------
void printDoubleSeparator() {
    // Prints a line long enough to span the columns (95 characters wide)
    cout << "==================================================================================================" << endl;
}

// ---------------- HELPER FUNCTION TO PRINT SINGLE LINE SEPARATOR ----------------
void printSingleSeparator() {
    // Prints a line long enough to span the columns (95 characters wide)
    cout << "--------------------------------------------------------------------------------------------------" << endl;
}

// ---------------- SHOW ROOMS FUNCTION (Table Display without Structs) ----------------
void showRooms() {

    cout << "\n";
    printDoubleSeparator();

    // Title Row
    cout << "|| " << left << setw(92) << "         *** AVAILABLE ROOMS FOR SELECTION ***" << "||" << endl;

    printDoubleSeparator();

    // Header Row: ID | ROOM TYPE | PRICE (PKR) | AMENITIES
    cout << "|| " << left << setw(5) << "ID"
         << "| " << left << setw(14) << "ROOM TYPE"
         << "| " << left << setw(14) << "PRICE (PKR)"
         << "| " << left << setw(57) << "AMENITIES" << "||" << endl;

    printSingleSeparator();

    // Data Rows: Loop through the arrays
    for(int i = 0; i < NUM_ROOMS; i++) {
        cout << "|| " << left << setw(5) << (i + 1) // ID is array index + 1
             << "| " << left << setw(14) << roomNames[i]
             // Right-align price for numeric clarity
             << "| " << right << setw(10) << pricesPerNight[i] << " " << left << setw(3) << ""
             << "| " << left << setw(57) << amenitiesList[i] << "||" << endl;
    }

    printDoubleSeparator();
}

// ---------------- EXAMPLE MAIN FUNCTION ----------------
int main() {
    showRooms();
    return 0;
}
