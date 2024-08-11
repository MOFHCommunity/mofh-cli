
# **MOFH-CLI Documentation**

## **Overview**
`mofh-cli` is a command-line tool that simplifies the management of MyOwnFreeHost (MOFH) accounts. This tool allows administrators to easily create, suspend, and unsuspend hosting accounts by interacting with the MOFH API.

## **Installation**

### **Prerequisites**
- Python 3.6 or higher.
- MOFH Python package (`mofh`).
- A valid MOFH API account with a username and password.

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

## **Usage**

### **Commands**

#### **1. Create a New Account**

Use the `create` command to create a new hosting account. You will need to provide the username, password, email, plan, and domain for the new account.

**Syntax:**
```bash
./mofh-cli.py create <username> <password> <email> <plan> <domain>
```

**Example:**
```bash
./mofh-cli.py create johndoe pass123 john@example.com basic_plan example.com
```

**Output:**
```
Account creation successful: <API Response>
```

#### **2. Suspend an Account**

The `suspend` command suspends an existing account by username. You must provide a reason for the suspension.

**Syntax:**
```bash
./mofh-cli.py suspend <username> <reason>
```

**Example:**
```bash
./mofh-cli.py suspend johndoe "Violation of terms"
```

**Output:**
```
Account suspended successfully: <API Response>
```

#### **3. Unsuspend an Account**

Use the `unsuspend` command to unsuspend a previously suspended account.

**Syntax:**
```bash
./mofh-cli.py unsuspend <username>
```

**Example:**
```bash
./mofh-cli.py unsuspend johndoe
```

**Output:**
```
Account unsuspended successfully: <API Response>
```

### **Options**

- `username`: The username associated with the account.
- `password`: The password for the account (only required for account creation).
- `email`: The contact email for the account (only required for account creation).
- `plan`: The hosting plan/package for the account (only required for account creation).
- `domain`: The domain associated with the account (only required for account creation).
- `reason`: The reason for suspending an account.

## **Error Handling**

The tool includes basic error handling. If an error occurs during the execution of a command, a meaningful error message will be displayed.

**Example:**
```
Failed to create account: <Error Message>
```

## **Configuration File Example**

Here’s an example of the `config.ini` file:

```ini
[default]
api_username = your_mofh_api_username
api_password = your_mofh_api_password
```

This file should be placed in the same directory as `mofh-cli.py`.

## **Contributing**

If you would like to contribute to the development of `mofh-cli`, feel free to fork the project and submit pull requests. We welcome contributions that add new features, improve existing functionality, or enhance the documentation.
