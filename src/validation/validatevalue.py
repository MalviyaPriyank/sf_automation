
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
    MustBeValidCRON,
    ValueNotAllowed,
    DependentParameterNotSet,
    InvalidPassword,
    IsARequiredAttribute,
    ValueNotAllowed,
    MustBeAList,
    MustBeWithinLimit,
    MustBeAValidCollationSpecifier,
    MustBeValidUTF8Character,
    MustNotBeASubString
)

class ValidateValue:

    allowed_values_for_month = ['1','2','3','4','5','6','7','8','9','10','11','12','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    allowed_values_for_week = ['0','1','2','3','4','5','6','SUN','MON','TUE','WED','THU','FRI','SAT','L']
    min_len_password = 8
    other_password_requirement = "must conatin at least 1 uppercase and 1 lower case letter, must conatin at least 1 digit"

    def __init__(self):
        pass

    @staticmethod
    def starts_with_alphabet(value,object_type,attr_name):
        if value[0].isalpha():
            return True
        else:
            raise MustStartWithAlphabet(object_type,attr_name)
        
    @staticmethod
    def is_valid_value(value,allowed_list,object_type,attr_name):
        if value not in allowed_list:
            raise ValueNotAllowed(object_type,attr_name,allowed_list)
        else:
            return True
        
    @staticmethod
    def has_space(value,object_type,attr_name):
        if ' ' in value:
            raise MustNotHaveSpace(object_type, attr_name)
        else:
            return False

    @staticmethod
    def is_valid_password(value,object_type,attr_name):
        if len(value) < ValidateValue.min_len_password:
            raise InvalidPassword(ValidateValue.min_len_password,ValidateValue.other_password_requirement,object_type,attr_name)
        else:
            has_upper = any(char.isupper() for char in value)
            has_lower = any(char.islower() for char in value)
            has_digit = any(char.isdigit() for char in value)
            if has_upper and has_lower and has_digit:
                return True
            else:
                raise InvalidPassword(ValidateValue.min_len_password,ValidateValue.other_password_requirement,object_type,attr_name)

    @staticmethod    
    def has_special_characters(value,object_type,attr_name):
        if re.search(r'[^a-zA-Z0-9]',value):
            raise MustNotHaveSpecialCharacters(object_type,attr_name)
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
    def is_allowed_value(value,allowed_list,object_type,attr_name):
        if value not in allowed_list:
            raise ValueNotAllowed(object_type,attr_name,allowed_list)

        
    @staticmethod
    def required_attribute_check(value,object_type,attr_name):
        if value == "NONE":
            raise IsARequiredAttribute(object_type,attr_name)
        
    @staticmethod
    def is_enclosed_in_single_quotes(value,object_type,attr_name):
        if value[0] == "'" and value[-1] == "'":
            return True
        else:
            raise MustBeEnclosedInQuotes(object_type,attr_name)
        
    @staticmethod
    def is_dependent_param_null(value,object_type,child_attr_name,parent_attr_name):
        if value == "NONE":
            raise DependentParameterNotSet(object_type,child_attr_name,parent_attr_name)
        else:
            return False
        
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

    @staticmethod
    def is_list(value,object_type,attr_name,*largs):
        if isinstance(value,list):
            if len(largs) != 0:
                list_len = len(value)
                if list_len < largs[0]:
                    return True 
                else:
                    raise MustBeWithinLimit(object_type,attr_name,largs[0])
            elif len(largs) == 0:
                return True
        else:
            raise MustBeAList(object_type,attr_name)

    @staticmethod
    def is_valid_collation_specifier(value,object_type,attr_name,valid_specifiers):
        specifier_list=value.split('-')
        for specifier in specifier_list:
            if specifier not in valid_specifiers:
                raise MustBeAValidCollationSpecifier(object_type,attr_name,specifier)
        return True
    
    @staticmethod
    def is_valid_utf8(value,object_type,attr_name):
        try:
            value.encode('utf-8')
            return True
        except UnicodeEncodeError:
            raise MustBeValidUTF8Character(object_type,attr_name)
        
    @staticmethod
    def is_a_substring(src_value,ref_value,src_attr_name,ref_attr_name,object_type):
        if src_value in ref_value:
            raise MustNotBeASubString(src_value,ref_value,object_type)
        else:
            return False
