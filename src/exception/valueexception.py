class AttributeValidationError(Exception):
    """Base class for attribute validation exceptions"""
    def __init__(self, object_type, attr_name, message):
        self.object_type = object_type
        self.attr_name = attr_name
        self.message = message
    
    def __str__(self):
        return f"ERROR : Attribute {self.attr_name} of {self.object_type} object {self.message}"

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
    def __init__(self,object_type,attr_name):
        super().__init__(object_type, attr_name,f"is a required attribute and cannot be NULL")

class MustBeJSON(AttributeValidationError):
    def __init__(self, object_type, attr_name, message):
        super().__init__(object_type, attr_name, f" must be a JSON")

class MustBeValidNumber(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must be a valid number")

class MustBeValidCRON(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must be a valid CRON syntax")

class ValueNotAllowed(AttributeValidationError):
    def __init__(self, object_type, attr_name, allowed_values):
        message = f" can only have following values : {allowed_values}"
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
        message = f" can only be set if {parent_attr_name} is set"
        super().__init__(object_type, child_attr_name, message)    
        


    
