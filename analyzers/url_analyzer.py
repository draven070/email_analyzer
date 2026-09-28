from urllib.parse import urlparse


SUSPICIOUS_WORDS = [
    "login",
    "signin",
    "verify",
    "verification",
    "account",
    "secure",
    "update",
    "password",
    "bank",
    "confirm"
]


def analyze_url(url):

    parsed = urlparse(url)

    hostname = parsed.hostname or ""

    features = {
        "url": url,
        "length": len(url),
        "hostname_length": len(hostname),
        "https": parsed.scheme == "https",
        "hostname_is_ip": False,
        "subdomain_count": hostname.count("."),
        "hyphen_count": hostname.count("-"),
        "suspicious_keyword": False,
        "query_present": bool(parsed.query)
    }

    if any(
        word in url.lower()
        for word in SUSPICIOUS_WORDS
    ):
        features["suspicious_keyword"] = True

    try:
        import ipaddress
        ipaddress.ip_address(hostname)
        features["hostname_is_ip"] = True
    except ValueError:
        pass

    return features