# Write a function is_rfc1918(ip) returning True/False based on private IP ranges.
def is_rfc1918(ip):
    if ip.startswith("10.") or ip.startswith("192.") or ip.startswith("172."):
        return True
    return False


ip = "10.0.0.5"

ip_list = [
    "10.0.0.5",
    "10.44.12.99",
    "172.16.0.1",
    "172.31.255.255",
    "192.168.1.100",
    "192.168.56.1",
    "8.8.8.8",
    "1.1.1.1",
    "203.0.113.45",
    "52.23.14.7",
    "91.198.174.192",
]
print(is_rfc1918(ip))


for x in ip_list:
    print(f"{x} - {is_rfc1918(x)}")
