#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// ---------------- ROOM STRUCTURE ----------------
struct Room {
    int id;
    string name;
    int pricePerNight;
    string amenities;
};

// ---------------- CUSTOMER STRUCTURE ----------------
struct Customer {
    string cnic;
    string name;
    string phone;
    string password;
};

// ---------------- BOOKING STRUCTURE ----------------
struct Booking {
    string cnic;
    string roomName;
    int pricePerNight;
    int inDay, inMonth;
    int outDay, outMonth;
    int nights;
    int totalBill;
    string paymentMethod;
    string paymentDetail;
};

// ---------------- ROOM DATA (CENTRALIZED) ----------------
Room rooms[3] = {
    {1, "Standard", 10000,
     "1 Bed, Study Table, Fridge, Attached Bathroom"},

    {2, "Executive", 17000,
     "2 Beds, Sofa-cum-Bed, Mini Bar, Complimentary Breakfast, Attached Bathroom"},

    {3, "Suite", 40000,
     "Fresh Fruit Basket, Hot Tub, 2 Rooms, TV, Library, Table Tennis"}
};

// ---------------- CHECK IF CUSTOMER EXISTS ----------------
bool customerExists(string cnic) {
    ifstream file("customers.txt");
    Customer c;
    while(file >> c.cnic >> c.name >> c.phone >> c.password) {
        if(c.cnic == cnic) {
            file.close();
            return true;
        }
    }
    file.close();
    return false;
}

// ---------------- REGISTER CUSTOMER ----------------
void registerCustomer() {
    Customer c;
    cout << "Enter CNIC: ";
    cin >> c.cnic;

    if(customerExists(c.cnic)) {
        cout << "CNIC already registered\n";
        return;
    }

    cout << "Enter Name: ";
    cin >> c.name;

    cout << "Enter Phone Number: ";
    cin >> c.phone;

    cout << "Create Password: ";
    cin >> c.password;

    ofstream file("customers.txt", ios::app);
    file << c.cnic << " " << c.name << " "
         << c.phone << " " << c.password << endl;
    file.close();

    cout << "Registration successful\n";
}

// ---------------- LOGIN CUSTOMER ----------------
bool loginCustomer(string &cnic) {
    string pass;
    cout << "Enter CNIC: ";
    cin >> cnic;
    cout << "Enter Password: ";
    cin >> pass;

    ifstream file("customers.txt");
    Customer c;

    while(file >> c.cnic >> c.name >> c.phone >> c.password) {
        if(c.cnic == cnic && c.password == pass) {
            file.close();
            cout << "Login successful\n";
            return true;
        }
    }
    file.close();

    cout << "Invalid CNIC or password\n";
    return false;
}

// ---------------- SHOW ROOMS WITH AMENITIES ----------------
void showRooms() {
    cout << "\n--- AVAILABLE ROOMS ---\n\n";
    for(int i = 0; i < 3; i++) {
        cout << rooms[i].id << ". " << rooms[i].name << endl;
        cout << "Price: " << rooms[i].pricePerNight << " PKR per night\n";
        cout << "Amenities: " << rooms[i].amenities << "\n\n";
    }
}

// ---------------- BOOK ROOM ----------------
void bookRoom(string cnic) {
    Booking b;
    int choice;

    b.cnic = cnic;

    showRooms();
    cout << "Choose room (1-3): ";
    cin >> choice;

    if(choice < 1 || choice > 3) {
        cout << "Invalid choice\n";
        return;
    }

    b.roomName = rooms[choice - 1].name;
    b.pricePerNight = rooms[choice - 1].pricePerNight;

    cout << "Enter Check-in Day: ";
    cin >> b.inDay;
    cout << "Enter Check-in Month: ";
    cin >> b.inMonth;

    cout << "Enter Check-out Day: ";
    cin >> b.outDay;
    cout << "Enter Check-out Month: ";
    cin >> b.outMonth;

    int inTotal = (b.inMonth * 30) + b.inDay;
    int outTotal = (b.outMonth * 30) + b.outDay;

    if(outTotal <= inTotal) {
        cout << "Invalid dates\n";
        return;
    }

    b.nights = outTotal - inTotal;
    b.totalBill = b.nights * b.pricePerNight;

    cout << "Total Nights: " << b.nights << endl;
    cout << "Total Bill: " << b.totalBill << " PKR\n";

    cout << "\nPayment Options\n";
    cout << "1. Cash\n2. EasyPaisa\n3. Visa/MasterCard\nChoice: ";
    int pay;
    cin >> pay;

    if(pay == 1) {
        b.paymentMethod = "Cash";
        b.paymentDetail = "Paid at desk";
    }
    else if(pay == 2) {
        b.paymentMethod = "EasyPaisa";
        cout << "Enter EasyPaisa Number: ";
        cin >> b.paymentDetail;
    }
    else if(pay == 3) {
        b.paymentMethod = "Visa/MasterCard";
        cout << "Enter last 4 digits of card: ";
        cin >> b.paymentDetail;
    }
    else {
        cout << "Invalid payment option\n";
        return;
    }

    ofstream file("bookings.txt", ios::app);
    file << b.cnic << " " << b.roomName << " "
         << b.pricePerNight << " "
         << b.inDay << " " << b.inMonth << " "
         << b.outDay << " " << b.outMonth << " "
         << b.nights << " " << b.totalBill << " "
         << b.paymentMethod << " " << b.paymentDetail << endl;
    file.close();

    cout << "Booking confirmed successfully\n";
}

// ---------------- ADMIN PANEL ----------------
void adminPanel() {
    ifstream file("bookings.txt");
    Booking b;

    cout << "\n--- ADMIN PANEL ---\n\n";

    while(file >> b.cnic >> b.roomName >> b.pricePerNight
          >> b.inDay >> b.inMonth
          >> b.outDay >> b.outMonth
          >> b.nights >> b.totalBill
          >> b.paymentMethod >> b.paymentDetail) {

        cout << "CNIC: " << b.cnic << endl;
        cout << "Room: " << b.roomName << endl;
        cout << "Stay: " << b.inDay << "/" << b.inMonth
             << " to " << b.outDay << "/" << b.outMonth << endl;
        cout << "Nights: " << b.nights << endl;
        cout << "Bill: " << b.totalBill << " PKR\n";
        cout << "Payment: " << b.paymentMethod << "\n\n";
    }

    file.close();
}

// ---------------- MAIN MENU ----------------
int main() {
    int choice;
    string cnic;

    while(true) {
        cout << "\n1. Register\n2. Login\n3. Admin Panel\n4. Exit\nChoice: ";
        cin >> choice;

        if(choice == 1)
            registerCustomer();
        else if(choice == 2 && loginCustomer(cnic))
            bookRoom(cnic);
        else if(choice == 3)
            adminPanel();
        else if(choice == 4)
            break;
        else
            cout << "Invalid option\n";
    }

    return 0;
}
