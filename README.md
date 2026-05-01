# ATM Simulation Project

This is a simple ATM Simulation project built using Python and object-oriented programming (OOP).  
The application allows users to perform basic banking operations through a menu-driven interface.

## Features
- Create user account session with basic details
- Display current account balance
- Deposit money
- Withdraw money with insufficient balance check
- View mini statement (transaction history)
- Record each transaction with:
  - Transaction type
  - Amount
  - Updated balance
  - Time

## Technologies Used
- Python 3
- OOP concepts (class, object, methods)
- Built-in `datetime` module

## Project Structure
- `CAP_PROJECT.py` - Main ATM simulation program

## How It Works
1. User enters account details (name, account id, account type, PIN).
2. ATM menu is displayed:
   - Display Balance
   - Withdraw Amount
   - Deposit Money
   - Statement
   - Exit
3. Each operation updates account data.
4. Statement shows complete transaction record in tabular format.

## Learning Outcomes
This project demonstrates:
- Class design and method usage in Python
- Data handling with dictionaries and lists
- Input-driven menu systems
- Basic validation and transaction tracking logic

## Future Improvements
- PIN authentication before transactions
- Save/load transactions from file or database
- Transfer money between accounts
- Interest calculation for savings accounts
- Better exception handling for invalid input
