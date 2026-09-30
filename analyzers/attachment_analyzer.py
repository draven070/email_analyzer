import hashlib


def calculate_hash(data):

    return {
        "md5": hashlib.md5(data).hexdigest(),
        "sha1": hashlib.sha1(data).hexdigest(),
        "sha256": hashlib.sha256(data).hexdigest()
    }


def analyze_attachment(part):

    filename = part.get_filename()

    if not filename:
        return None

    data = part.get_payload(decode=True)

    if not data:
        return None

    hashes = calculate_hash(data)

    return {
        "filename": filename,
        "content_type": part.get_content_type(),
        "size": len(data),
        **hashes
    }