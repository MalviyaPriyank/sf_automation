
import re
import json


class ValidateValue:

    allowed_values_for_month = ['1','2','3','4','5','6','7','8','9','10','11','12','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    allowed_values_for_week = ['0','1','2','3','4','5','6','SUN','MON','TUE','WED','THU','FRI','SAT','L']


    def __init__(self):
        pass

    @staticmethod
    def starts_with_alphabet(value):
        if value[0].isalpha():
            return True
        else:
            return False
        
    @staticmethod
    def has_space(value):
        if ' ' in value:
            return True
        else:
            return False

    @staticmethod    
    def has_special_characters(value):
        if re.search(r'[^a-zA-Z0-9]',value):
            return True
        else:
            return False

    @staticmethod
    def has_special_characters_except_underscore(value):
        if re.search(r'[^a-zA-Z0-9_]',value):
            return True
        else:
            return False

    @staticmethod
    def is_enclosed_in_double_quotes(value):
        if value[0] == '"' and value[-1] == '"':
            return True
        else:
            return False
        
    @staticmethod
    def is_enclosed_in_single_quotes(value):
        if value[0] == "'" and value[-1] == "'":
            return True
        else:
            return False
        
    @staticmethod
    def is_string(value):
        if isinstance(value,str):
            return True
        
    @staticmethod
    def is_json(value):
        try:
            if json.loads(value):
                return True
        except json.JSONDecodeError:
            return False
        
    @staticmethod
    def is_bool(value):
        if value not in ['TRUE','FALSE']:
            return False
        
    @staticmethod
    def is_positive_number(value):
        try:
            num = float(value)
            return True
        except ValueError:
            return False
        
    @staticmethod
    def is_between(value,num1,num2):
        try:
            num = float(value)
            if num1 <= num <= num2:
                return True
            else:
                return False
        except ValueError:
            return False

    @staticmethod
    def is_valid_cron(value):
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


