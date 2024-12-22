
import re
import json


class ValidateValue:

    allowed_values_for_month = ['1','2','3','4','5','6','7','8','9','10','11','12','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    allowed_values_for_week = ['0','1','2','3','4','5','6','SUN','MON','TUE','WED','THU','FRI','SAT','L']


    def __init__(self):
        pass

    def starts_with_alphabet(self,value):
        if value[0].isalpha():
            return True
        else:
            return False
        
    def has_space(self,value):
        if ' ' in value:
            return True
        else:
            return False
        
    def has_special_characters(self,value):
        if re.search(r'[^a-zA-Z0-9]',value):
            return True
        else:
            return False
    
    def is_enclosed_in_double_quotes(self,value):
        if value[0] == '"' and value[-1] == '"':
            return True
        else:
            return False
        
    def is_string(self,value):
        if isinstance(value,str):
            return True
        
    def is_json(self,value):
        try:
            if json.loads(value):
                return True
        except json.JSONDecodeError:
            return False
        
    def is_bool(self,value):
        if value not in ['TRUE','FALSE']:
            return False
        
    def is_positive_number(self,value):
        try:
            num = float(value)
            return True
        except ValueError:
            return False

    def is_valid_cron(self,value):
        if 'MINUTE' not in value:
            if len(value) != 5:
                return False
            elif not 0 <= int(value[0]) <= 59:
                return False
            elif not 0 <= int(value[1]) <= 23:
                raise False
            elif not (0 <= int(value[2]) <= 31 or value[2] == 'L'):
                raise False
            elif value[3] not in ValidateCron.allowed_values_for_month:
                raise False
            elif value[4] not in ValidateCron.allowed_values_for_week:
                raise False


