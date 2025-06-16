# 🏦 Bank Account Management System (Python, OOP)

This project is a simple **Bank Account Management System** implemented in **Python** using key principles of **Object-Oriented Programming (OOP)**. It simulates the operations of a real-world bank, with a focus on clean design, encapsulation, and data persistence.

---

## 📚 Features

- 🔐 Create a new account with a unique bank-style account number (`CHXX3736###`)
- 💰 Deposit and withdraw funds
- 📊 View balance and account info
- 🔄 Switch between existing accounts
- 📁 Save all account data persistently in a `JSON` file
- 👨‍💼 Admin access via `accounts.json` to view all customer records

---

## 🧠 Concepts Implemented

### ✅ Object-Oriented Programming
- **Encapsulation** – All attributes are private and accessed via methods.
- **Abstraction** – The internal logic is hidden behind simple functions like `create_account()`.
- **Modularity & Reusability** – Clean class structure and helper functions make the code extensible.

### 📄 JSON-based Persistence
- All accounts are stored in a file called `accounts.json`, allowing data persistence across program executions.

### 🔢 Unique Account Number Generator
- Used `rstr` (regular expression string generator) to simulate real-world bank-style account numbers.
- Pattern: `CH[A-Z]{2}3736\d{3}`

---

## 🛠️ Tech Stack

- **Python 3.12+**
- `rstr` library for regex-based string generation
- Standard Python libraries: `json`, `os`

---

## 🧪 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/bank-oop-system.git
   cd bank-oop-system
