# Security_Networking
Cyber Security and Networking Scripts

# CISA CVEs associated Nessus Plugins
1. Script is used to pull Nessus plugins from tenable
2. Correlate plugins to the CISA CVEs
3. must download the known_exploited_vulnerabilities.csv
4. from https://www.cisa.gov/known-exploited-vulnerabilities-catalog

# IP list string parser
ipParser.py
- Given a list of ips in string format, group the consecutive ips together and add the nonconsecutive
- example Given ['1.1.1.1','1.1.1.2','1.1.1.4','1.1.1.5','1.1.1.6']
- Output 1.1.1.1-1.1.1.2,1.1.1.4-1.1.1.6
- Very helpful for input for web automations and input.

# Subnet Script and Ip generator
- Generator for IP between a start and end ip
- Get the subnet of IPv6 of a start and end ip


