#include <iostream>
#include <string>
#include <iomanip> // Essential for setw() and alignment

using namespace std;

// ---------------- ROOM STRUCTURE (Needed for function signature) ----------------
struct Room {
    int id;
    string name;
    int pricePerNight;
    string amenities;
};

// ---------------- ROOM DATA (Needed for function content) ----------------
Room rooms[3] = {
    {1, "Standard", 10000,
     "1 Bed, Study Table, Fridge, Attached Bathroom"},

    {2, "Executive", 17000,
     "2 Beds, Sofa-cum-Bed, Mini Bar, Complimentary Breakfast, Attached Bathroom"},

    {3, "Suite", 40000,
     "Fresh Fruit Basket, Hot Tub, 2 Rooms, TV, Library, Table Tennis"}
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

// ---------------- SHOW ROOMS FUNCTION (Table Display with ==) ----------------
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

    // Data Rows
    for(int i = 0; i < 3; i++) {
        cout << "|| " << left << setw(5) << rooms[i].id
             << "| " << left << setw(14) << rooms[i].name
             // Right-align price for numeric clarity
             << "| " << right << setw(10) << rooms[i].pricePerNight << " " << left << setw(3) << ""
             << "| " << left << setw(57) << rooms[i].amenities << "||" << endl;
    }

    printDoubleSeparator();
}

