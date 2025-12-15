#include <iostream>
#include <string>
#include <iomanip> 

using namespace std;

// ---------------- ROOM DATA (Using Parallel Arrays) ----------------

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
    // Length: 95 characters
    cout << "==================================================================================================" << endl;
}

// ---------------- HELPER FUNCTION TO PRINT SINGLE LINE SEPARATOR ----------------
void printSingleSeparator() {
    // Length: 95 characters
    cout << "--------------------------------------------------------------------------------------------------" << endl;
}

// ---------------- SHOW ROOMS FUNCTION (Aesthetically Enhanced) ----------------
void showRooms() {

    cout << "\n";
    printDoubleSeparator();

    // Title Row
    cout << "|| " << left << setw(92) << "         *** AVAILABLE ROOMS & FEATURES ***" << "||" << endl;

    printDoubleSeparator();

    // Header Row: Perfectly aligned and centered text is difficult in console, but we align headers to the left for clarity.
    cout << "|| " << left << setw(5) << "ID"
         << "| " << left << setw(14) << "ROOM TYPE"
         << "| " << left << setw(14) << "PRICE (PKR)"
         << "| " << left << setw(57) << "AMENITIES" << "||" << endl;

    printDoubleSeparator(); // Use double line under the header for strong separation

    // Data Rows: Loop through the arrays
    for(int i = 0; i < NUM_ROOMS; i++) {
        // Data row
        cout << "|| " << left << setw(5) << (i + 1)
             << "| " << left << setw(14) << roomNames[i]
             // Right-align price for numeric clarity
             << "| " << right << setw(10) << pricesPerNight[i] << " " << left << setw(3) << ""
             << "| " << left << setw(57) << amenitiesList[i] << "||" << endl;
             
        // Use a single line separator between data entries for better reading flow
        if (i < NUM_ROOMS - 1) {
            printSingleSeparator();
        }
    }

    printDoubleSeparator(); // Close the table with a double line
}

// ---------------- EXAMPLE MAIN FUNCTION ----------------
int main() {
    showRooms();
    return 0;
}
