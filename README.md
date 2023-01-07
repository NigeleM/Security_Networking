# Security_Networking
Cyber Security and Networking Scripts

# CISA CVEs associated Nessus Plugins
1. Script is used to pull Nessus plugins from tenable
2. Correlate plugins to the CISA CVEs
3. must download the known_exploited_vulnerabilities.csv
4. from https://www.cisa.gov/known-exploited-vulnerabilities-catalog

ipParser.py
- Given a list of ips in string format, group the consecutive ips together and add the nonconsecutive
- example Give ['1.1.1.1','1.1.1.2','1.1.1.4','1.1.1.5','1.1.1.6']
_ Output 1.1.1.1-1.1.1.2,1.1.1.4-1.1.1.6
