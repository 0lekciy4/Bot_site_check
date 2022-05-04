from asyncio import start_unix_server
import requests
import whois

def get_whois_info(site):
    whois_data = whois.whois(site)
    whois_info  = {
        'domain_name': whois_data.domain_name,
        'expiration_date': whois_data.expiration_date
    }
    return whois_info

def get_site_status(site):
    status_code = requests.get(site).status_code
    return status_code

if __name__ == '__main__':
    site = 'ooo-sbs.ru'
    site_info = get_whois_info(site)
    # site_status = get_site_status()
    print(site_info)
    