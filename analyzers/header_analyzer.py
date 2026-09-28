from email.utils import parseaddr
from urllib.parse import urlparse


def extract_domain(address):

    _, email = parseaddr(address or "")

    if "@" not in email:
        return None

    return email.split("@")[-1].lower()


def analyze_headers(headers):

    result = {
        "from_domain": None,
        "reply_to_domain": None,
        "return_path_domain": None,
        "domain_mismatch": False,
        "received_count": 0,
        "suspicious": []
    }

    result["from_domain"] = extract_domain(headers.get("from"))

    result["reply_to_domain"] = extract_domain(
        headers.get("reply_to")
    )

    result["return_path_domain"] = extract_domain(
        headers.get("return_path")
    )

    result["received_count"] = len(
        headers.get("received", [])
    )

    if (
        result["from_domain"]
        and result["reply_to_domain"]
        and result["from_domain"]
        != result["reply_to_domain"]
    ):
        result["domain_mismatch"] = True
        result["suspicious"].append(
            "From and Reply-To domains differ"
        )

    return result