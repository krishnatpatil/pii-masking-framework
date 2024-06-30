import re

class PIIDetector:
    def __init__(self):
        # Define regex patterns for PII detection
        self.email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        self.phone_number_pattern = re.compile(r'\b(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\b')

    def detect_pii(self, text):
        # Detect PII types in the text
        pii_types = []
        if self.email_pattern.search(text):
            pii_types.append('Email')
        if self.phone_number_pattern.search(text):
            pii_types.append('Phone Number')
        # Add more PII types as needed
        return pii_types