class PIIDetector:
    PII_PATTERNS = {
        'name': ['name', 'full_name'],
        'phone': ['phone', 'phone_number'],
        'email': ['email', 'email_address'],
        'ssn': ['ssn', 'social_security_number'],
        'address': ['address', 'street_address']
    }

    @classmethod
    def detect_pii_columns(cls, metadata):
        pii_columns = {}
        for table, columns in metadata.items():
            pii_columns[table] = [col['name'] for col in columns if any(pattern in col['name'] for pattern in cls.PII_PATTERNS.values())]
        return pii_columns
