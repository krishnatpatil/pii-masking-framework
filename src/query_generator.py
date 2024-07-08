class QueryGenerator:
    def __init__(self, config):
        self.config = config

    def generate_update_query(self, table_config, masking_rules):
        query = f"UPDATE {table_config['name']} SET "
        updates = []

        for column, mask_type in masking_rules.items():
            if column in table_config['columns']:
                col_name = table_config['columns'][column]
                if mask_type == 'Z' * len(table_config['columns'][column]):
                    updates.append(f"{col_name} = '{'Z' * len(table_config['columns'][column])}'")
                elif mask_type == 'nullify city_state':
                    updates.append(f"{col_name} = NULL")
                elif mask_type == '999-999-9999':
                    updates.append(f"{col_name} = '999-999-9999'")
                elif mask_type == '999-99-9999':
                    updates.append(f"{col_name} = '999-99-9999'")
                elif mask_type == 'nullify':
                    updates.append(f"{col_name} = NULL")
                elif mask_type == '01/01/1099':
                    updates.append(f"{col_name} = '01/01/1099'")

        query += ", ".join(updates)
        query += " WHERE date_of_birth < DATEADD(year, -20, CURRENT_DATE)"
        return query