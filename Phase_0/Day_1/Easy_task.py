"""
Easy: Create a list of 5 internal IP addresses. Append a new IP to the list, then
print the list.

"""

ip_list = ["192.168.1.10", "192.168.1.11", "10.0.0.5", "10.0.0.6", "172.16.0.8"]

# Step 2. append new IP
ip_list.append("192.168.1.12")

# Step 3. Print Full list
print("Full IP-List:", ip_list)

# Step 4. Print using loop
print("\nIp List using loop")
for index, value in enumerate(ip_list):
    print(index, value)
