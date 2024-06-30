import random
import string

class MaskingRule:
    def __init__(self):
        pass

    def mask_pii(self, pii_type, value):
        if pii_type == 'Email':
            return self._mask_email(value)
        elif pii_type == 'Phone Number':
            return self._mask_phone_number(value)
        # Add more masking rules as needed
        return value

    def _mask_email(self, email):
        parts = email.split('@')
        username = ''.join(random.choices(string.ascii_lowercase, k=len(parts[0])))
        domain = parts[1]
        return f"{username}@{domain}"

    def _mask_phone_number(self, phone_number):
        return 'xxx-xxx-xxxx'  # Placeholder masking for example