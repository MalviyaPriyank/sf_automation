class AttributeValidationError(Exception):
    """Base class for attribute validation exceptions."""
    def __init__(self, object_type, attr_name, message):
        self.object_type = object_type
        self.attr_name = attr_name
        self.message = message
    
    def __str__(self):
        return f"Attribute {self.attr_name} of object type {self.object_type} {self.message}."

class MustStartWithAlphabet(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name,"must start with an alphabet.")

class MustBeString(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must be a string.")

class MustNotHaveSpace(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "cannot have spaces.")

class MustNotHaveSpecialCharacters(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must not contain special characters.")

class MustBeEnclosedInQuotes(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must be enclosed in quotes.")

class MustBeBool(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name,"must be either True or False.")

class MustBePositiveNumber(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must be a positive number.")

class MustBeBetween(AttributeValidationError):
    def __init__(self,object_type , attr_name,val1, val2):
        super().__init__(object_type, attr_name,f"must be between {val1} and {val2}.")

class IsARequiredAttribute(AttributeValidationError):
    def __init__(self,object_type,attr_name):
        super().__init__(object_type, attr_name,f"is a required attribute and cannot be NULL.")

class MustBeJSON(AttributeValidationError):
    def __init__(self, object_type, attr_name, message):
        super().__init__(object_type, attr_name, f" must be a JSON.")

class MustBeValidNumber(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must be a valid number.")

class MustBeValidCRON(AttributeValidationError):
    def __init__(self, object_type, attr_name):
        super().__init__(object_type, attr_name, "must be a valid CRON syntax.")

class ValueNotAllowed(Exception):
    def __init__(self, object_type, attr_name, allowed_values):
        return f"Attribute {attr_name} of object type {object_type} can only have following values : {allowed_values} "


    
