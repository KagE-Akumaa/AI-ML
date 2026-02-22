# Take a messy syslog string and use .strip() and .split() to extract just the attacker's IP.
log = "May 2 09:12:45 webserver ALERT!! Unauthorized access attempt -- src=45.67.89.10 "

data = log.split()

print(data)

messy_ip = data[-1]

clean_ip = messy_ip.replace("src=", "")

print(f"Attacker Ip address: {clean_ip}")
