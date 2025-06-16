# 💼 Bank Account System & OOP Practice Arena

A complete Object-Oriented Programming (OOP) learning project built from scratch in Python. This repository reflects a **step-by-step progression from foundational OOP concepts to applied practice** in two different settings:

- A **Banking System** with persistent JSON storage and encapsulated logic
- A **Turn-based Game Simulation** demonstrating clean inheritance and polymorphism

---

## 🧩 What's Inside

| File         | Purpose                                                                 |
|--------------|-------------------------------------------------------------------------|
| `bank.py`    | Bank account simulation implementing real-world banking logic           |
| `class.py`   | A simple OOP-based turn-based game (Hero vs Enemy)                      |
| `accounts.json` | Stores persistent bank account data                                   |
| `README.md`  | You’re reading it 😉                                                     |

---

## 🚀 What We Set Out to Learn

This project wasn’t just about coding — it was about deeply **understanding and implementing**:

- ✅ Encapsulation
- ✅ Abstraction
- ✅ Inheritance
- ✅ Polymorphism
- ✅ File handling & data persistence
- ✅ Modular design with class-based structure

---

## 🔐 Bank System (bank.py)

### 💡 Highlights:
- Each account has a unique ID like `CHAB3736123` generated with regex
- Deposits, withdrawals, and balance checks via simple CLI
- Persistent account storage in `accounts.json`
- Ability to **switch between accounts** during runtime
- Admins can access all data via JSON inspection

### 🔧 Key Concepts Used:
- **Encapsulation**: Protected attributes like `__balance` and `__account_number`
- **Abstraction**: Users interact with public methods without touching internal logic
- **Data Persistence**: Real-time saving/loading of accounts using the `json` module
- **Error Handling**: Prevented crashes from invalid user inputs and JSON issues

---

## ⚔️ OOP Game Simulation (class.py)

Built as an extension to apply **Inheritance and Polymorphism** through a fun and simple turn-based combat game.

### 🎮 Setup:
- A base `Character` class with core attributes (`name`, `health`, `attack`)
- Two subclasses: `Hero` and `Enemy`
- Overridden `attack()` method to demonstrate **polymorphic behavior**
- Game loop to simulate real-time decisions and health deduction

### 👇 Why It Mattered:
- Gave a **practical grip** over polymorphism by overriding behaviors dynamically
- Reinforced **inheritance structure** in a use-case outside finance

---

## ⚔️ Problems We Faced (and How We Solved Them)

| Issue | What Went Wrong | Our Solution |
|-------|------------------|---------------|
| JSONDecodeError | Empty JSON file caused crashes on load | Handled empty read using `.strip()` and fallback to `[]` |
| Account switch failed | `switch_account` wasn’t being *called* (missing `()`) | Fixed with proper function call syntax |
| Redundant Account Creation | Code forced new account even if JSON had data | Implemented account switching + admin view |
| No Polymorphism in Bank | Realized too late | Covered this via `class.py` game simulation |

---

## 🧠 Final Takeaways

This project wasn’t built in one go — it was **debugged, broken, redesigned**, and finally **brought together** with intention and understanding.

What started as just an attempt to learn OOP became a **personal hands-on OOP bootcamp**.

- 📘 We *didn’t just read* about polymorphism — we implemented it in combat logic
- 🔐 We *didn’t just hear* about encapsulation — we protected every attribute
- 🔄 We *iterated through bugs and confusion* — and emerged clearer

---

## 💡 Future Improvements (Optional Ideas)

- GUI interface with Tkinter or PyQt
- Full transaction history for each account
- Role-based access for Admin vs User
- Save game results in `class.py` to JSON

---

## 📚 To Run the Project

```bash
# Install the rstr package if not already installed
pip install rstr

# Run the bank system
python bank.py

# Run the OOP game (optional)
python class.py

