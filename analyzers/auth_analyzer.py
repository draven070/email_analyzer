import re


def analyze_authentication(headers):

    auth_headers = headers.get(
        "authentication_results", []
    )

    combined = " ".join(auth_headers).lower()

    result = {
        "spf": "unknown",
        "dkim": "unknown",
        "dmarc": "unknown"
    }

    for mechanism in ["spf", "dkim", "dmarc"]:

        match = re.search(
            rf"\b{mechanism}=(pass|fail|softfail|neutral|none|temperror|permerror)\b",
            combined
        )

        if match:
            result[mechanism] = match.group(1)

    return result