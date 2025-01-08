class StringValidationError(Exception):
    """Base class for attribute validation exceptions."""
    def __init__(self, attr_name, object_type, message):
        self.attr_name = type(attr_name).__name__
        self.object_type = object_type
        self.message = message
    
    def __str__(self):
        return f"Attribute {self.attr_name} of object type {self.object_name} {self.message}."

class MustStartWithAlphabet(StringValidationError):
    def __init__(self, attr_name, object_type):
        super().__init__(attr_name, object_type, "must start with an alphabet")

class MustNotHaveSpace(StringValidationError):
    def __init__(self, attr_name, object_type):
        super().__init__(attr_name, object_type, "cannot have spaces")

class MustNotHaveSpecialCharacters(StringValidationError):
    def __init__(self, attr_name, object_type):
        super().__init__(attr_name, object_type, "must not contain special characters")

class MustBeEnclosedInQuotes(StringValidationError):
    def __init__(self, attr_name, object_type):
        super().__init__(attr_name, object_type, "must be enclosed in quotes")
