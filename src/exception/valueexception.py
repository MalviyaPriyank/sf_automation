class AttributeValidationError(Exception):
    """Base class for attribute validation exceptions."""
    def __init__(self, attr_name, object_type, message):
        self.attr_name = attr_name
        self.object_type = object_type
        self.message = message
    
    def __str__(self):
        return f"Attribute {self.attr_name} of object type {self.object_type} {self.message}."

class MustStartWithAlphabet(AttributeValidationError):
    def __init__(self, attr_name, object_type):
        super().__init__(attr_name, object_type, "must start with an alphabet")

class MustNotHaveSpace(AttributeValidationError):
    def __init__(self, attr_name, object_type):
        super().__init__(attr_name, object_type, "cannot have spaces")

class MustNotHaveSpecialCharacters(AttributeValidationError):
    def __init__(self, attr_name, object_type):
        super().__init__(attr_name, object_type, "must not contain special characters")

class MustBeEnclosedInQuotes(AttributeValidationError):
    def __init__(self, attr_name, object_type):
        super().__init__(attr_name, object_type, "must be enclosed in quotes")

class MustBeBool(AttributeValidationError):
    def __init__(self, attr_name, object_type):
        super().__init__(attr_name, object_type, "must be either True or False.")

class MustBePositiveNumber(AttributeValidationError):
    def __init__(self, attr_name, object_type):
        super().__init__(attr_name, object_type, "must be a positive number")

class MustBeBetween(AttributeValidationError):
    def __init__(self, attr_name, object_type , val1, val2):
        super().__init__(attr_name, object_type, f"must be between {val1} and {val2}")

class MustBeBetween(AttributeValidationError):
    def __init__(self, attr_name, object_type , val1, val2):
        super().__init__(attr_name, object_type, f"must be between {val1} and {val2}")

class IsARequiredAttribute(Exception):
    def __init__(self, *args):
        super().__init__(*args)
    
