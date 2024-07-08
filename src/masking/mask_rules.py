class MaskRules:

    @staticmethod
    def mask_name(name: str) -> str:
        return 'Z' * len(name)

    @staticmethod
    def mask_city(city: str) -> None:
        return None

    @staticmethod
    def mask_state(state: str) -> None:
        return None

    @staticmethod
    def mask_phone_number(phone_number: str) -> str:
        return '9' * 10

    @staticmethod
    def mask_ssn(ssn: str) -> str:
        return '9' * 9

    @staticmethod
    def mask_financial_details(financial_details: str) -> None:
        return None

    @staticmethod
    def mask_dob(dob: str) -> str:
        return '1099-01-01'