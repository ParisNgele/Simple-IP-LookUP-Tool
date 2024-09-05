import requests
import sys

def get_ip_info(ip_address, token):
    if token == 'your_token':
        print("Error: API token has not been set. Please replace 'your_token' with a valid API token.")
        return

    url = f"https://ipinfo.io/{ip_address}/json?token={token}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        print("\nIP Lookup Information:")
        print(f"IP Address: {data.get('ip', 'N/A')}")
        print(f"Hostname: {data.get('hostname', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Location: {data.get('loc', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")
        
    except requests.RequestException as e:
        print(f"Error fetching IP information: {e}")

def get_my_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        data = response.json()
        return data.get('ip', 'N/A')
    except requests.RequestException as e:
        print(f"Error fetching your IP address: {e}")
        return None

def main():
    token = 'your_token'  # Replace with your actual token from ipinfo.io

    print("Simple IP LookUp Tool")
    print("1. Enter an IP address")
    print("2. Use my own IP address")

    try:
        choice = input("Choose an option (1 or 2): ").strip()

        if choice == '1':
            ip_address = input("Enter IP address to LookUp: ").strip()
            if ip_address:
                get_ip_info(ip_address, token)
            else:
                print("No IP address entered. Exiting.")
        
        elif choice == '2':
            my_ip = get_my_ip()
            if my_ip:
                print(f"Your public IP address is: {my_ip}")
                get_ip_info(my_ip, token)
            else:
                print("Could not retrieve your IP address. Exiting.")
        
        else:
            print("Invalid choice. Exiting.")
    
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user. Exiting...")
        sys.exit()

if __name__ == "__main__":
    main()
