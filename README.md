

# **MOFH-CLI Documentation**

## **Overview**
`mofh-cli` is a command-line tool that simplifies the management of MyOwnFreeHost (MOFH) accounts. This tool allows administrators to create, suspend, unsuspend, delete accounts, reset passwords, change packages, check domain availability, retrieve user domains, query CNAME records, and manage support tickets via the MOFH API.

---

## **Installation**

### **Prerequisites**
- Python 3.6 or higher.
- MOFH Python package (`mofh`).
- A valid MOFH API account with a username and password.

---

### **Setup**

1. **Install Required Packages**  
   Before using `mofh-cli`, ensure that the necessary Python packages are installed:
   ```bash
   pip install mofh
   ```

2. **Configuration File**  
   The tool relies on a configuration file named `config.ini` to store API credentials. Create this file in the same directory as `mofh-cli` with the following content:
   ```ini
   [default]
   api_username = your_api_username
   api_password = your_api_password
   ```

3. **Run the Script**  
   The script can be run directly from the command line:
   ```bash
   ./mofh-cli.py [command] [options]
   ```

---

## **Usage**

### **Commands**

#### **1. Create a New Account**
Creates a new hosting account.

**Syntax:**
```bash
./mofh-cli.py create <username> <password> <email> <plan> <domain>
```

**Example:**
```bash
./mofh-cli.py create johndoe pass123 john@example.com basic_plan example.com
```

---

#### **2. Suspend an Account**
Suspends an existing account by username.

**Syntax:**
```bash
./mofh-cli.py suspend <username> <reason>
```

**Example:**
```bash
./mofh-cli.py suspend johndoe "Violation of terms"
```

---

#### **3. Unsuspend an Account**
Unsuspends a previously suspended account.

**Syntax:**
```bash
./mofh-cli.py unsuspend <username>
```

**Example:**
```bash
./mofh-cli.py unsuspend johndoe
```

---

#### **4. Delete an Account**
Deletes an account by username.

**Syntax:**
```bash
./mofh-cli.py delete <username>
```

**Example:**
```bash
./mofh-cli.py delete johndoe
```

---

#### **5. Change Account Password**
Resets the password for an account.

**Syntax:**
```bash
./mofh-cli.py change_password <username> <new_password>
```

**Example:**
```bash
./mofh-cli.py change_password johndoe newpass123
```

---

#### **6. Change Hosting Plan**
Changes the hosting plan/package for an account.

**Syntax:**
```bash
./mofh-cli.py change_package <username> <new_plan>
```

**Example:**
```bash
./mofh-cli.py change_package johndoe premium_plan
```

---

#### **7. Check Domain Availability**
Checks if a domain is available for registration.

**Syntax:**
```bash
./mofh-cli.py check_available <domain>
```

**Example:**
```bash
./mofh-cli.py check_available example.com
```

---

#### **8. Retrieve User Domains**
Lists all domains associated with a username.

**Syntax:**
```bash
./mofh-cli.py get_user_domains <username>
```

**Example:**
```bash
./mofh-cli.py get_user_domains johndoe
```

---

#### **9. Get User for Domain**
Retrieves the username associated with a domain.

**Syntax:**
```bash
./mofh-cli.py get_domain_user <domain>
```

**Example:**
```bash
./mofh-cli.py get_domain_user example.com
```

---

#### **10. Retrieve CNAME Record**
Gets the CNAME record for a domain.

**Syntax:**
```bash
./mofh-cli.py get_cname <domain>
```

**Example:**
```bash
./mofh-cli.py get_cname example.com
```

---

#### **11. Create Support Ticket**
Creates a new support ticket.

**Syntax:**
```bash
./mofh-cli.py create_ticket <username> <subject> <comments> <ip>
```

**Example:**
```bash
./mofh-cli.py create_ticket johndoe "Account Issue" "My account is not accessible" 192.168.0.1
```

---

#### **12. Reply to a Support Ticket**
Replies to an existing support ticket.

**Syntax:**
```bash
./mofh-cli.py reply_ticket <username> <ticket_id> <comments> <ip>
```

**Example:**
```bash
./mofh-cli.py reply_ticket johndoe 123456 "Issue resolved" 192.168.0.1
```

---

### **Options**

- `username`: Username associated with the account.
- `password`: Account password (required for account creation).
- `email`: Contact email (required for account creation).
- `plan`: Hosting plan/package (required for account creation or change).
- `domain`: Domain name (used for account creation and domain queries).
- `reason`: Reason for account suspension.
- `new_password`: New password for account.
- `new_plan`: New hosting plan/package.
- `subject`: Subject for support tickets.
- `comments`: Description or comments for support tickets.
- `ip`: IP address for support tickets.

---

## **Error Handling**

The tool includes error handling to ensure a clear response is provided if something goes wrong.

**Example:**
```
Failed to create account: <Error Message>
```

---

## **Configuration File Example**

```ini
[default]
api_username = your_mofh_api_username
api_password = your_mofh_api_password
```

Place this file in the same directory as `mofh-cli.py`.

---

## **Contributing**

We welcome contributions to `mofh-cli`. Whether you're fixing bugs, adding new features, or enhancing documentation, your input is appreciated. Fork the project, make changes, and submit a pull request.
