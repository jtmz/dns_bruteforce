import dns.resolver
import sys

try:
    domain = sys.argv[1]
    name_file = sys.argv[2]

except:
    print "Invalid Args"
    print "Usege: dnsbrute.py <domain> <wordlist>"
    sys.exit(1)

try:
    file = open(name_file)
    subdomain = file.read().splitlines()
except:
    print "file not found"
    sys.exit()

for line in subdomain:

    try:
        hostname = line + '.' + domain
        sucess = dns.resolver.query(hostname, 'a' )
        for ip in sucess:
            print hostname, ip

    except:
        pass
