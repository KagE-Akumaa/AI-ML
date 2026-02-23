# Hard: Write a single-line list comprehension filtering firewall alert dictionaries by ports 22 or 3389.

firewall_alerts = [
    {"src_ip": "10.0.0.5", "dst_port": 22, "action": "BLOCKED"},
    {"src_ip": "192.168.1.44", "dst_port": 443, "action": "ALLOWED"},
    {"src_ip": "203.0.113.77", "dst_port": 3389, "action": "BLOCKED"},
    {"src_ip": "8.8.8.8", "dst_port": 53, "action": "ALLOWED"},
    {"src_ip": "172.16.5.66", "dst_port": 80, "action": "ALLOWED"},
    {"src_ip": "52.23.14.7", "dst_port": 22, "action": "BLOCKED"},
]

imp_alerts = [x for x in firewall_alerts if x["dst_port"] in [22, 3389]]

print(imp_alerts)
