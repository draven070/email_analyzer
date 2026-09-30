def calculate_risk(
    auth,
    header,
    urls,
    attachments,
    reputation,
    ml_probability
):

    score = 0

    # Authentication
    if auth.get("spf") == "fail":
        score += 10

    if auth.get("dkim") == "fail":
        score += 10

    if auth.get("dmarc") == "fail":
        score += 15

    # Header
    if header.get("domain_mismatch"):
        score += 10

    # URLs
    for url in urls:

        if url.get("hostname_is_ip"):
            score += 15

        if url.get("suspicious_keyword"):
            score += 10

        if not url.get("https"):
            score += 5

    # Attachments
    risky_extensions = {
        ".exe",
        ".scr",
        ".js",
        ".vbs",
        ".ps1",
        ".bat",
        ".cmd",
        ".lnk"
    }

    for attachment in attachments:

        filename = attachment[
            "filename"
        ].lower()

        for ext in risky_extensions:

            if filename.endswith(ext):
                score += 20

    # ML
    score += round(
        ml_probability * 30
    )

    # Reputation
    if reputation.get("malicious"):
        score += 30

    return min(score, 100)