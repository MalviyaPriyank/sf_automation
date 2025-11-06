import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))

from snowchainexception import SnowchainException

class AttributeValidationError(SnowchainException):
    """Base class for attribute validation exceptions"""
    def __init__(self, object_type, attr_name, message,**kwargs):
        self.object_type = object_type
        self.attr_name = attr_name
        self.message = message
        if len(kwargs)==0:
            self.error_message = f" Attribute {self.attr_name} of {self.object_type} {self.message}. Please provide different value."
        else:
            for key,value in kwargs.items():
                self.error_message=f"Attribute {key} {value}. Please provide different value."
        super().__init__(self.error_message)

class MustStartWithAlphabet(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name,"must start with an alphabet")

class MustBeString(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must be a string")

class MustNotHaveSpace(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "cannot have spaces")

class MustNotHaveSpecialCharacters(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must not contain special characters")

class MustBeEnclosedInQuotes(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must be enclosed in quotes")

class MustBeBool(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name,"must be either True or False")

class MustBePositiveNumber(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must be a positive number")

class MustBeBetween(AttributeValidationError):
    def __init__(self,object_type , attr_name,val1, val2):
        super().__init__(object_type, attr_name,f"must be between {val1} and {val2}")

class IsARequiredAttribute(AttributeValidationError):
    def __init__(self,object_type,attr_name,*largs):
        if len(largs)==0:
            super().__init__(object_type, attr_name,f"is a required attribute and cannot be NULL")
        else:
            for stmt in largs:
                super().__init__(object_type, attr_name,f"is a required attribute and cannot be NULL,{stmt}")

class MustBeJSON(AttributeValidationError):
    def __init__(self, object_type, attr_name, message):
        super().__init__(object_type, attr_name, f"must be a JSON")

class MustBeValidNumber(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must be a valid number")

class MustBeValidCRON(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must be a valid CRON syntax")

class ValueNotAllowed(AttributeValidationError):
    def __init__(self, object_type, attr_name, allowed_values):
        message = f"can only have following values : {allowed_values}"
        super().__init__(object_type, attr_name, message)
    
class InvalidPassword(AttributeValidationError):
    def __init__(self, min_len,other_requirements,object_type, attr_name):
        message = f"must be at least {min_len} in length, and {other_requirements}"
        super().__init__(object_type, attr_name, message)

class InvalidParamForObject(AttributeValidationError):
    def __init__(self, object_type,attr_name,allowed_type):
        message = f"{attr_name} can only be set for {allowed_type} {object_type}"
        super().__init__(object_type, attr_name, message)

class DependentParameterNotSet(AttributeValidationError):
    def __init__(self, object_type, child_attr_name, parent_attr_name):
        message = f"can only be set if {parent_attr_name} is set"
        super().__init__(object_type, child_attr_name, message) 

class MustBeAList(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        message = f"must be a comma separated list like [val1,val2]"
        super().__init__(object_type, attr_name=attr_name, message=message) 

class MustBeWithinLimit(AttributeValidationError):
    def __init__(self, object_type, attr_name, limit_value):
        message=f"can only have maximum of {limit_value} values"
        super().__init__(object_type, attr_name, message)

class MustBeAValidCollationSpecifier(AttributeValidationError):
    def __init__(self, object_type, attr_name, invalid_specifier,specifier_list):
        message=f"can not have {invalid_specifier} as a collation specifier. List of valid specifiers include {specifier_list}"
        super().__init__(object_type, attr_name, message)

class MustBeValidUTF8Character(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        message=f"must be a valid UTF8 character"
        super().__init__(object_type, attr_name, message)

class MustNotBeASubString(AttributeValidationError):
    def __init__(self, src_attr_name,ref_attr_name,object_type):
        message=f"must not be a substring of {ref_attr_name}"
        super().__init__(object_type, src_attr_name, message)

class InvalidProtocol(AttributeValidationError):
    def __init__(self, object_type, attr_name, allowed_protocols):
        message=f"can have only following protocols {allowed_protocols}"
        super().__init__(object_type, attr_name, message)

class InvalidAzureUrl(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        message=f"for Azure must be in the format 'azure://<account>.blob.core.windows.net'"
        super().__init__(object_type, attr_name, message)

class UrlMustStartWith(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        message=f"must be in the format '<protocol>://<url>'.Make sure your url starts wtih '//'"
        super().__init__(object_type, attr_name, message)

class ArnNotRequired(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        message=f"should only be provided if URL is S3 alias"
        super().__init__(object_type, attr_name, message)

class InvalidParentAttribute(AttributeValidationError):
    def __init__(self, object_type, attr_name,parent_attribute,compatible_value_parent_attribute):
        message=f"can only be set if attribute {parent_attribute} is one of the following {compatible_value_parent_attribute}"
        super().__init__(object_type, attr_name, message)

class AttributeNotRequired(AttributeValidationError):
    def __init__(self, object_type, attr_name,condition):
        message=f"is not required for {condition}"
        super().__init__(object_type, attr_name, message)
    
class MustBeSingleByteCharacter(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        message=f"must be a single byte character"
        super().__init__(object_type, attr_name, message)

class StringMustBeOfAllowedLength(AttributeValidationError):
    def __init__(self, object_type, attr_name, allowed_length):
        message=f"can have maximum {allowed_length} characters"
        super().__init__(object_type, attr_name, message)

class BaseValueMustBeLessThanOrEqualReferenceValue(AttributeValidationError):
    def __init__(self, object_type, attr_name,value_ref):
        message=f"should be set to a value less than or equal to {value_ref}"
        super().__init__(object_type, attr_name,message)

class CannotSetBothParameters(AttributeValidationError):
    def __init__(self, original_param, conflicting_param, object_type):
        message=f"cannot be set along with {conflicting_param}. Only one of them can be used"
        super().__init__(object_type, original_param,message)

class MustBeOfLength(AttributeValidationError):
    def __init__(self, object_type, attr_name, length):
        message=f"must be of length {length}"
        super().__init__(object_type, attr_name, message)

class MustBeATuple(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        message="must be a Tuple"
        super().__init__(object_type, attr_name, message)

class InvalidTimestamp(AttributeValidationError):
    def __init__(self, object_type, attr_name, value):
        message=f" is not a valid timestamp. Use TIMESTAMP_TZ('{value}'), or TIMESTAMP_NTZ('{value}') to convert it to a valid timestamp"
        super().__init__(object_type, attr_name, message)

class InvalidSchedule(AttributeValidationError):
    def __init__(self, object_type, attr_name, valid_schedule):
        message=f"must have schedule specified one of the following : {valid_schedule}"
        super().__init__(object_type, attr_name, message)

class InvalidCron(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        message=f"must be a valid CRON syntax"
        super().__init__(object_type, attr_name, message)

class CustomErrorMessage(AttributeValidationError):
    def __init__(self, object_type, attr_name, condition,**kwargs):
        super().__init__(object_type, attr_name, condition,**kwargs)

class InvalidDataType(AttributeValidationError):
    def __init__(self, object_type, attr_name, invalid_data_typ_list):
        message = f" cannot have following invalid data types {invalid_data_typ_list}"
        super().__init__(object_type, attr_name, message)

class DataTypeNotAllowed(SnowchainException):
    def __init__(self,data_type):
        error_message = f" Data type : {data_type} is not valid as per the allowed data types on Snowflake. Please change it to a Snowflake compatible data type."
        super().__init__(error_message)

class InvalidCIDRNotation(SnowchainException):
    def __init__(self, object_type,attr_name,cidr_str):
        error_message = f" Attribute {attr_name} of {object_type} must follow CIDR Notation. Please change {cidr_str} to follow CIDR Notation."
        super().__init__(error_message)

class InvalidVPCEID(SnowchainException):
    def __init__(self, object_type,attr_name):
        error_message=f"Attribute {attr_name} of {object_type} is not a valid VPCE ID."
        super().__init__(error_message)

class InvalidHostName(SnowchainException):
    def __init__(self, object_type,attr_name):
        error_message=f" {attr_name} of {object_type} must be a valid Host Name."
        super().__init__(error_message)

class PortMustBeBetween(SnowchainException):
    def __init__(self, object_type,attr_name,lower_bound,upper_bound):
        error_message=f"Port specified for {attr_name} of {object_type} must be between {lower_bound} and {upper_bound}."
        super().__init__(error_message)

class PortRangeMustBeFromSmallerToBigger(SnowchainException):
    def __init__(self,object_type,attr_name):
        error_message=f"When specifying port range for {attr_name} of {object_type}, it should be smaller first."
        super().__init__(error_message)

class InvalidHostPort(SnowchainException):
    def __init__(self, object_type,attr_name):
        error_message=f"{attr_name} of {object_type} is not in correct format."
        super().__init__(error_message)

class InvalidObjectTypeForAllowedDatabases(SnowchainException):
    def __init__(self, attr_name,object_name):
        error_message=f"Databases needs to be in the list of allowed objects for configuring {attr_name}, while creating {object_name}. Please ask user for the clarification."
        super().__init__(error_message)

class BaseValueMustBeGreaterThanOrEqualReferenceValue(AttributeValidationError):
    def __init__(self, object_type, attr_name,value_ref):
        message=f"should be set to a value greater than or equal to {value_ref}"
        super().__init__(object_type, attr_name,message)
    
