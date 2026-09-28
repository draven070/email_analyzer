from email import policy
from email.parser import BytesParser
from pathlib import Path


class EmailParser:

    def __init__(self, filepath):
        self.filepath = Path(filepath)

    def parse(self):
        with open(self.filepath, "rb") as f:
            msg = BytesParser(policy=policy.default).parse(f)

        return msg

    def get_headers(self, msg):
        return {
            "from": msg.get("From"),
            "to": msg.get("To"),
            "cc": msg.get("Cc"),
            "subject": msg.get("Subject"),
            "date": msg.get("Date"),
            "reply_to": msg.get("Reply-To"),
            "return_path": msg.get("Return-Path"),
            "message_id": msg.get("Message-ID"),
            "received": msg.get_all("Received", []),
            "authentication_results":
                msg.get_all("Authentication-Results", [])
        }

    def get_body(self, msg):

        plain = []
        html = []

        if msg.is_multipart():

            for part in msg.walk():

                content_type = part.get_content_type()

                if content_type == "text/plain":
                    try:
                        plain.append(part.get_content())
                    except Exception:
                        pass

                elif content_type == "text/html":
                    try:
                        html.append(part.get_content())
                    except Exception:
                        pass

        else:

            content_type = msg.get_content_type()

            if content_type == "text/plain":
                plain.append(msg.get_content())

            elif content_type == "text/html":
                html.append(msg.get_content())

        return {
            "plain": "\n".join(plain),
            "html": "\n".join(html)
        }