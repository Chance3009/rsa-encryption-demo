# Secret Notes with RSA Encryption – SWE4356 Group Assignment

A simple demonstration of RSA encryption using Python. This application allows users to create, store, and retrieve encrypted notes using RSA encryption.

---

## Group Member - Group 1

| Name             | Matric Number |
|------------------|---------------|
| Chan Ci En       | 215035        |
| Khoo Boo Jing    | 215382        |
| Loo Huai Yuan    | 215516        |
| Chu Xing En      | 215090        |
| Loh Joe Ying     | 215507        |
| Tan Yong Jin     | 217086        |

---

## Features

- RSA encryption/decryption of notes
- Secure storage in SQLite database
- Simple command-line interface

---

## How It Works

### Encryption Process
- Uses RSA algorithm for encryption
- Generates new key pair for each session
- Stores only encrypted data in database

### Database Storage
- SQLite database for persistence
- Stores encrypted notes with timestamps
- No original text is saved

### Security Notes
- Keys are generated fresh each session
- Original text is never stored in database
- Uses SQLite with parameterized queries for safety

---

## Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/Chance3009/rsa-encryption-demo.git
cd rsa-encryption-demo
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Tool
```bash
python app.py
```

---

## Available Commands

1. **Save Note**: Add a new encrypted note
2. **Get Note**: Retrieve and decrypt a note by ID
3. **List Notes**: View all stored notes
4. **Exit**: Close the application
