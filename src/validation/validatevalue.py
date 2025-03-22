
import re
import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
from datetime import datetime
from croniter import croniter

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
    MustNotBeASubString,
    InvalidProtocol,
    InvalidAzureUrl,
    UrlMustStartWith,
    ArnNotRequired,
    InvalidParentAttribute,
    AttributeNotRequired,
    MustBeSingleByteCharacter,
    StringMustBeOfAllowedLength,
    BaseValueMustBeLessThanOrEqualReferenceValue,
    CannotSetBothParameters,
    MustBeOfLength,
    MustBeATuple,
    InvalidTimestamp,
    InvalidSchedule,
    InvalidCron,
    CustomErrorMessage,
    InvalidDataType
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
        if value.upper() not in allowed_list:
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
        if value.upper() not in allowed_list:
            raise ValueNotAllowed(object_type,attr_name,allowed_list)

        
    @staticmethod
    def required_attribute_check(value,object_type,attr_name,*largs):
        if value == "NONE":
            raise IsARequiredAttribute(object_type,attr_name,largs)
        
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
        if value.upper() not in ["TRUE","FALSE"]:
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
    def is_between(value,num1,num2,object_type,attr_name,**kwargs):
        try:
            num = float(value)
            if num1 <= num <= num2:
                return True
            else:
                if len(kwargs)!=0:
                    raise MustBeBetween(object_type,attr_name,num1,num2)
                else:
                    raise CustomErrorMessage(object_type,attr_name,value,kwargs)
                        
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
    def is_list(value,object_type,attr_name,*largs,**kwargs):
        if isinstance(value,list):
            if len(largs) != 0:
                list_len = len(value)
                if list_len < largs[0]: 
                    return True 
                else:
                    raise MustBeWithinLimit(object_type,attr_name,largs[0])
            elif len(largs) == 0:
                return True
            
            if len(kwargs)!=0:
                if "MUST_BE_OF_LENGTH" in kwargs.keys():
                    if len(value) == kwargs["MUST_BE_OF_LENGTH"]:
                        return True
                    else:
                        raise MustBeOfLength(object_type,attr_name,kwargs['MUST_BE_OF_LENGTH'])

        else:
            raise MustBeAList(object_type,attr_name)
        
    @staticmethod
    def is_tuple(value,object_type,object_name):
        if isinstance(value,tuple):
            return True
        else:
            raise MustBeATuple(object_type,object_name)

    @staticmethod
    def is_valid_collation_specifier(value,object_type,attr_name,valid_specifiers):
        specifier_list=value.split('-')
        for specifier in specifier_list:
            if specifier not in valid_specifiers:
                raise MustBeAValidCollationSpecifier(object_type,attr_name,specifier,valid_specifiers)
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
            raise MustNotBeASubString(src_attr_name,ref_attr_name,object_type)
        else:
            return False
        
    @staticmethod
    def is_single_byte_characetr(value,object_type,attr_name):
        if len(value)==1:
            return True
        else:
            raise MustBeSingleByteCharacter(object_type,attr_namej)
    @staticmethod
    def is_valid_url(value,allowed_protocols,object_type,attr_name):
        protocol=value.split(':')[0]
        url=value.split(':')[1]
        #check for protocol
        if protocol not in allowed_protocols:
            raise InvalidProtocol(object_type,attr_name,allowed_protocols)
        #check for URL after protocol
        if url.startswith("//"):
            if 'azure' in protocol:
                azure_url=url.removeprefix("//")
                account=azure_url.split('/')[0]
                account_chunks=account.split('.')
                if (len(account_chunks) != 5
                    or account_chunks[1] != 'blob'
                    or account_chunks[2] != 'core'
                    or account_chunks[3] != 'windows'
                    or account_chunks[4] != 'net'):
                    raise InvalidAzureUrl(object_type,attr_name)
        else:
            raise UrlMustStartWith(object_type,attr_name)
        
    @staticmethod
    def is_s3_alias(object_type,attr_name,url):
        if url.endswith('s3alias'):
            return True
        else:
            raise ArnNotRequired(object_type,attr_name)
        
    @staticmethod
    def is_parent_attribute_compatible(value,object_type,attr_name,parent_attribute,compatible_value_lst_parent_attribute):
        if value not in compatible_value_lst_parent_attribute:
            raise InvalidParentAttribute(object_type,attr_name,parent_attribute,compatible_value_lst_parent_attribute)
        elif value in compatible_value_lst_parent_attribute:
            return True
    
    @staticmethod
    def not_required(object_type,attr_name,condition):
        raise AttributeNotRequired(object_type,attr_name,condition)
    
    @staticmethod
    def is_string_of_allowed_length(value,object_type,attr_name,allowed_length):
        if len(value)<=allowed_length:
            return True
        else:
            raise StringMustBeOfAllowedLength(object_type,attr_name,allowed_length)
    
    @staticmethod
    def is_less_than_or_equal_to(value_base,value_ref,object_type,attr_name):
        if value_base<=value_ref:
            return True
        else:
            raise BaseValueMustBeLessThanOrEqualReferenceValue(object_type,attr_name,value_ref)
        
    @staticmethod
    def is_conflicting_parameter_null(original_parameter_val,conflicting_parameter_val,original_parameter,conflicting_parameter,object_type):
        if conflicting_parameter_val !="NONE":
            raise CannotSetBothParameters(original_parameter,conflicting_parameter,object_type)
        elif conflicting_parameter_val=="NONE":
            return True
        
    @staticmethod
    def is_valid_timestamp(object_name,attribute_name,value):
        formats = [
            "%Y-%m-%d %H:%M:%S.%f",       # Without timezone
            "%Y-%m-%d %H:%M:%S.%f %z"     # With timezone
        ]
        
        for fmt in formats:
            try:
                datetime.strptime(value, fmt)
                return True
            except ValueError:
                raise InvalidTimestamp(object_name,attribute_name,value)
            
    @staticmethod
    def is_valid_schedule(schedule,object_name,attribute_name):
        split_schedule=schedule.split(' ')
        if split_schedule[0] == 'USING' and split_schedule[1] == 'CRON':
            return True,'CRON','NA'
        elif (split_schedule[-1] == 'M' 
              or split_schedule[-1]=='MINUTES'
              or split_schedule[-1]=='MINUTE'):
            return True,'MINUTE',split_schedule[0]
        elif (split_schedule[-1] == 'H' 
              or split_schedule[-1]=='HOURS'
              or split_schedule[-1]=='HOUR'):
            return True,'HOUR',split_schedule[0]
        elif (split_schedule[-1] == 'S' 
              or split_schedule[-1]=='SECONDS'
              or split_schedule[-1]=='SECOND'):
            return True,'SECOND',split_schedule[0]
        else:
            raise InvalidSchedule(object_name,attribute_name,['CRON','HOUR','MINUTE','SECOND'])
    
    @staticmethod
    def is_valid_cron(value,object_name,attr_name):
        try:
            croniter(value, datetime.now())  
            return True
        except:
            raise InvalidCron(object_name,attr_name)
        
    @staticmethod
    def is_valid_column_types(object_name,attribute_name,tbl_data_typ_lst,allowed_data_type_lst):
        invalid_data_typ_lst=list(set(tbl_data_typ_lst) - set(allowed_data_type_lst))
        if len(invalid_data_typ_lst) !=0:
            raise InvalidDataType(object_name,attribute_name,invalid_data_typ_lst)
        else:
            return True
        


        

        
    
