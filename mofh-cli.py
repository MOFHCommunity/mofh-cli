#!/usr/bin/env python3

import argparse
import configparser
import requests
from requests.auth import HTTPBasicAuth

# Load the configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Extract API credentials
api_username = config['default']['api_username']
api_password = config['default']['api_password']

# Define functions for API operations
def get_version():
    try:
        url = "https://panel.myownfreehost.net/json-api/version.php"
        response = requests.post(url, auth=HTTPBasicAuth(api_username, api_password))
        print(f"API Version: {response.text}")
    except Exception as e:
        print(f"Failed to get API version: {e}")

def list_packages():
    try:
        url = "https://panel.myownfreehost.net/json-api/listpkgs.php"
        response = requests.post(url, auth=HTTPBasicAuth(api_username, api_password))
        print(f"Available packages: {response.text}")
    except Exception as e:
        print(f"Failed to list packages: {e}")

def check_available(domain):
    try:
        url = f"https://panel.myownfreehost.net/json-api/checkavailable.php"
        data = {'domain': domain}
        response = requests.post(url, params=data, auth=HTTPBasicAuth(api_username, api_password))
        print(f"Domain availability: {response.text}")
    except Exception as e:
        print(f"Failed to check domain availability: {e}")

def get_user_domains(username):
    try:
        url = f"https://panel.myownfreehost.net/json-api/getuserdomains.php"
        data = {'username': username}
        response = requests.post(url, params=data, auth=HTTPBasicAuth(api_username, api_password))
        print(f"Domains for user {username}: {response.text}")
    except Exception as e:
        print(f"Failed to get user domains: {e}")

def get_domain_user(domain):
    try:
        url = f"https://panel.myownfreehost.net/json-api/getdomainuser.php"
        data = {'domain': domain}
        response = requests.post(url, params=data, auth=HTTPBasicAuth(api_username, api_password))
        print(f"User for domain {domain}: {response.text}")
    except Exception as e:
        print(f"Failed to get domain user: {e}")

def get_cname(domain):
    try:
        url = f"https://panel.myownfreehost.net/json-api/getcname.php"
        data = {'domain_name': domain}
        response = requests.post(url, params=data, auth=HTTPBasicAuth(api_username, api_password))
        print(f"CNAME for domain {domain}: {response.text}")
    except Exception as e:
        print(f"Failed to get CNAME: {e}")

def create_support_ticket(username, subject, comments, ip):
    try:
        url = "https://panel.myownfreehost.net/json-api/supportnewticket.php"
        data = {
            'clientusername': username,
            'subject': subject,
            'comments': comments,
            'ipaddress': ip
        }
        response = requests.post(url, params=data, auth=HTTPBasicAuth(api_username, api_password))
        print(f"Support ticket created: {response.text}")
    except Exception as e:
        print(f"Failed to create support ticket: {e}")

def reply_to_ticket(username, ticket_id, comments, ip):
    try:
        url = "https://panel.myownfreehost.net/json-api/supportreplyticket.php"
        data = {
            'ticket_id': ticket_id,
            'clientusername': username,
            'comments': comments,
            'ipaddress': ip
        }
        response = requests.post(url, params=data, auth=HTTPBasicAuth(api_username, api_password))
        print(f"Replied to ticket {ticket_id}: {response.text}")
    except Exception as e:
        print(f"Failed to reply to support ticket: {e}")

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Manage MyOwnFreeHost accounts and API operations")
    subparsers = parser.add_subparsers(dest="command")
    
    # General API functions
    subparsers.add_parser("version", help="Get API version")
    subparsers.add_parser("listpkgs", help="List available packages")
    
    check_available_parser = subparsers.add_parser("check_available", help="Check domain availability")
    check_available_parser.add_argument("domain", type=str, help="Domain to check")
    
    get_user_domains_parser = subparsers.add_parser("get_user_domains", help="Get user domains")
    get_user_domains_parser.add_argument("username", type=str, help="Username to get domains for")
    
    get_domain_user_parser = subparsers.add_parser("get_domain_user", help="Get user associated with a domain")
    get_domain_user_parser.add_argument("domain", type=str, help="Domain to query")

    get_cname_parser = subparsers.add_parser("get_cname", help="Get CNAME record for a domain")
    get_cname_parser.add_argument("domain", type=str, help="Domain to get CNAME for")
    
    # Support ticket operations
    create_ticket_parser = subparsers.add_parser("create_ticket", help="Create a support ticket")
    create_ticket_parser.add_argument("username", type=str, help="Username for the support ticket")
    create_ticket_parser.add_argument("subject", type=str, help="Subject of the support ticket")
    create_ticket_parser.add_argument("comments", type=str, help="Comments for the support ticket")
    create_ticket_parser.add_argument("ip", type=str, help="IP address for the support ticket")

    reply_ticket_parser = subparsers.add_parser("reply_ticket", help="Reply to a support ticket")
    reply_ticket_parser.add_argument("username", type=str, help="Username for the ticket reply")
    reply_ticket_parser.add_argument("ticket_id", type=str, help="Ticket ID to reply to")
    reply_ticket_parser.add_argument("comments", type=str, help="Comments for the reply")
    reply_ticket_parser.add_argument("ip", type=str, help="IP address for the ticket reply")
    
    # Parse the arguments and call the appropriate function
    args = parser.parse_args()
    
    if args.command == "version":
        get_version()
    elif args.command == "listpkgs":
        list_packages()
    elif args.command == "check_available":
        check_available(args.domain)
    elif args.command == "get_user_domains":
        get_user_domains(args.username)
    elif args.command == "get_domain_user":
        get_domain_user(args.domain)
    elif args.command == "get_cname":
        get_cname(args.domain)
    elif args.command == "create_ticket":
        create_support_ticket(args.username, args.subject, args.comments, args.ip)
    elif args.command == "reply_ticket":
        reply_to_ticket(args.username, args.ticket_id, args.comments, args.ip)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
