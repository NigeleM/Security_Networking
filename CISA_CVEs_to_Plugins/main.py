
import requests
from bs4 import BeautifulSoup as bs

# Script is used to pull Nessus plugins from tenable
# Correlate plugins to the CISA CVEs
# must download the known_exploited_vulnerabilities.csv
# from https://www.cisa.gov/known-exploited-vulnerabilities-catalog
def main():
    # https://www.tenable.com/plugins/search?q=%22CVE-2021-27104%22&sort=&page=1
    CVElist = []
    CVEdict = {}
    with open('known_exploited_vulnerabilities.csv','r+') as CISA_CVE_file:
        for line in CISA_CVE_file:
            CVElist.append(line.split(',')[0].replace("\"",''))

    CVElist.remove('cveID')
    print(CVElist)
    for CVE in CVElist:
        link = f'https://www.tenable.com/plugins/search?q=%22{CVE}%22&sort=&page=1'
        r = requests.get(link)
        url = r.content
        soup = bs(url,'html.parser')
        table = soup.find('table',{'class':'results-table table'})
        CVEdict[CVE] = ''
        if table == None:
            pass
        else:
            tableRows = table.find_all_next('tr')
            for tr in tableRows:
                td = tr.find_all_next('td')
                row = [i.text for i in td]
                if len(row) == 0:
                    continue
                else:
                    CVEdict[CVE] = CVEdict[CVE] + row[0] + ','
        with open('CISA_exploited_CVEs_to_plugins.csv','a+') as CISA_plugins:
            CISA_plugins.write(CVE+','+CVEdict[CVE]+',\n')

main()