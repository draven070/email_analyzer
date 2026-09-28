import re
import ipaddress


URL_REGEX = re.compile(
    r'https?://[^\s<>"\']+',
    re.IGNORECASE
)

IP_REGEX = re.compile(
    r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
)

EMAIL_REGEX = re.compile(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
)


def extract_iocs(text):

    urls = URL_REGEX.findall(text)
    ips = IP_REGEX.findall(text)
    emails = EMAIL_REGEX.findall(text)

    valid_ips = []

    for ip in ips:
        try:
            ipaddress.ip_address(ip)
            valid_ips.append(ip)
        except ValueError:
            pass

    domains = []

    for url in urls:

        match = re.search(
            r'https?://([^/]+)',
            url
        )

        if match:
            domains.append(match.group(1))

    return {
        "urls": list(set(urls)),
        "domains": list(set(domains)),
        "ips": list(set(valid_ips)),
        "emails": list(set(emails))
    }