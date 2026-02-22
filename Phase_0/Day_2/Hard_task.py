# Hard: Parse a multiline string of raw HTTP headers into a Python dictionary.
headers = """Host: suspicious-domain.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml
Referer: http://malicious-site.biz/phish
Connection: keep-alive
X-Forwarded-For: 192.168.1.100"""


new_header = headers.split("\n")

header_dict = {}

# using strip on y[1] to get the leading whitespace
for x in new_header:
    y = x.split(":", maxsplit=1)
    key = y[0].strip()
    value = y[1].strip()
    header_dict[key] = value

print(header_dict.items())
