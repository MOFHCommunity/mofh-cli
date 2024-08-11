#!/usr/bin/env python3

import argparse
import configparser
import mofh

# Load the configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Extract API credentials
api_username = config['default']['api_username']
api_password = config['default']['api_password']

# Initialize the MOFH client
client = mofh.Client(username=api_username, password=api_password)

# Define account management functions
def create_account(username, password, email, plan, domain):
    try:
        response = client.create(username=username, password=password, contactemail=email, domain=domain, plan=plan)
        print(f"Account creation successful: {response}")
    except Exception as e:
        print(f"Failed to create account: {e}")

def suspend_account(username, reason):
    try:
        response = client.suspend(username=username, reason=reason)
        print(f"Account suspended successfully: {response}")
    except Exception as e:
        print(f"Failed to suspend account: {e}")

def unsuspend_account(username):
    try:
        response = client.unsuspend(username=username)
        print(f"Account unsuspended successfully: {response}")
    except Exception as e:
        print(f"Failed to unsuspend account: {e}")

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Manage MyOwnFreeHost accounts")
    subparsers = parser.add_subparsers(dest="command")
    
    # Parser for creating accounts
    create_parser = subparsers.add_parser("create", help="Create a new hosting account")
    create_parser.add_argument("username", type=str, help="Username for the new account")
    create_parser.add_argument("password", type=str, help="Password for the new account")
    create_parser.add_argument("email", type=str, help="Email address for the new account")
    create_parser.add_argument("plan", type=str, help="Package for the new account")
    create_parser.add_argument("domain", type=str, help="Domain for the new account")
    
    # Parser for suspending accounts
    suspend_parser = subparsers.add_parser("suspend", help="Suspend an existing account")
    suspend_parser.add_argument("username", type=str, help="Username of the account to suspend")
    suspend_parser.add_argument("reason", type=str, help="Reason for suspension")
    
    # Parser for unsuspending accounts
    unsuspend_parser = subparsers.add_parser("unsuspend", help="Unsuspend a suspended account")
    unsuspend_parser.add_argument("username", type=str, help="Username of the account to unsuspend")
    
    # Parse the arguments and call the appropriate function
    args = parser.parse_args()
    
    if args.command == "create":
        create_account(args.username, args.password, args.email, args.plan, args.domain)
    elif args.command == "suspend":
        suspend_account(args.username, args.reason)
    elif args.command == "unsuspend":
        unsuspend_account(args.username)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

