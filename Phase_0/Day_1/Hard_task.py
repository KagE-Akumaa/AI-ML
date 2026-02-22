# Task - Hard: You are given a raw list of IPs with duplicates: ["1.1.1.1", "8.8.8.8", "1.1.1.1", "10.0.0.5"]. Convert this to a set to deduplicate it, then create a dictionary that counts how many times each unique IP appeared in the original list.

from collections import Counter

ip_list = [
    "192.168.1.10",
    "192.168.1.11",
    "10.0.0.5",
    "10.0.0.6",
    "172.16.0.8",
    "10.0.0.6",
    "10.0.0.5",
]

ip_set = set(ip_list)

print(ip_set)

ip_dic = {x: 0 for x in ip_list}
ip_dic2 = Counter(ip_list)

for i in ip_list:
    ip_dic[i] += 1

print(ip_dic)
print(ip_dic2)
