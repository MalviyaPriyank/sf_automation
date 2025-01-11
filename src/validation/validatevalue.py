
import re
import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
from valueexception import ( 
    MustStartWithAlphabet,
    MustNotHaveSpace,
    MustNotHaveSpecialCharacters,
    MustBeEnclosedInQuotes,
    MustBeString,
    MustBeJSON,
    MustBeBool,
    MustBePositiveNumber,
    MustBeBetween,
    MustBeValidNumber,
    MustBeValidCRON
)

class ValidateValue:

    allowed_values_for_month = ['1','2','3','4','5','6','7','8','9','10','11','12','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    allowed_values_for_week = ['0','1','2','3','4','5','6','SUN','MON','TUE','WED','THU','FRI','SAT','L']


    def __init__(self):
        pass

    @staticmethod
    def starts_with_alphabet(value,object_type,attr_name):
        if value[0].isalpha():
            return True
        else:
            raise MustStartWithAlphabet(object_type,attr_name)
        
    @staticmethod
    def has_space(value,object_type,attr_name):
        if ' ' in value:
            raise MustNotHaveSpace(object_type, attr_name)
        else:
            return False

    @staticmethod    
    def has_special_characters(value):
        if re.search(r'[^a-zA-Z0-9]',value):
            return True
        else:
            return False

    @staticmethod
    def has_special_characters_except_underscore(value,object_type,attr_name):
        if re.search(r'[^a-zA-Z0-9_]',value):
            raise MustNotHaveSpecialCharacters(object_type,attr_name)
        else:
            return False

    @staticmethod
    def is_enclosed_in_double_quotes(value,object_type,attr_name):
        if value[0] == '"' and value[-1] == '"':
            return True
        else:
            raise MustBeEnclosedInQuotes(object_type,attr_name)
        
    @staticmethod
    def is_enclosed_in_single_quotes(value,object_type,attr_name):
        if value[0] == "'" and value[-1] == "'":
            return True
        else:
            raise MustBeEnclosedInQuotes(object_type,attr_name)
        
    @staticmethod
    def is_string(value,object_type,attr_name):
        if isinstance(value,str):
            return True
        else:
            raise MustBeString(object_type,attr_name)
        
    @staticmethod
    def is_json(value,object_type,attr_name):
        try:
            if json.loads(value):
                return True
        except json.JSONDecodeError:
            raise MustBeJSON(object_type,attr_name)
        
    @staticmethod
    def is_bool(value,object_type,attr_name):
        if value not in ["TRUE","FALSE"]:
            raise MustBeBool(object_type,attr_name)
        else:
            return True
        
    @staticmethod
    def is_positive_number(value,object_type,attr_name):
        try:
            num = float(value)
            return True
        except ValueError:
            raise MustBePositiveNumber(object_type,attr_name)
        
    @staticmethod
    def is_between(value,num1,num2,object_type,attr_name):
        try:
            num = float(value)
            if num1 <= num <= num2:
                return True
            else:
                raise MustBeBetween(object_type,attr_name,num1,num2)
        except ValueError:
            raise MustBeValidNumber(object_type,attr_name)

    @staticmethod
    def is_valid_cron(value,object_type,attr_name):
        if 'MINUTE' not in value:
            if len(value) != 5:
                raise MustBeValidCRON(object_type,attr_name)
            elif not 0 <= int(value[0]) <= 59:
                raise MustBeValidCRON(object_type,attr_name)
            elif not 0 <= int(value[1]) <= 23:
                raise MustBeValidCRON(object_type,attr_name)
            elif not (0 <= int(value[2]) <= 31 or value[2] == 'L'):
                raise MustBeValidCRON(object_type,attr_name)
            elif value[3] not in ValidateCron.allowed_values_for_month:
                raise MustBeValidCRON(object_type,attr_name)
            elif value[4] not in ValidateCron.allowed_values_for_week:
                raise MustBeValidCRON(object_type,attr_name)


