import random
import string

class MaskingRule:
    @staticmethod
    def mask_value(value, data_type):
        if data_type == 'STRING':
            return ''.join(random.choices(string.ascii_letters, k=len(value)))
        elif data_type == 'NUMBER':
            return '9' * len(str(value))
        elif data_type == 'DATE':
            return '1900-01-01'
        else:
            return value
