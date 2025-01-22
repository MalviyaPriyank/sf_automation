class PrivilegeException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"ERROR : {self.message}"

class InvalidObject(PrivilegeException):
    def __init__(self, object_type):
        super().__init__(f"Snowflake does not allow granting privilege to {object_type} object type")

class InvalidPrivilege(PrivilegeException):
    def __init__(self, privilege_type,object_type):
        super().__init__(f"Snowflake does not allow setting {privilege_type} on object of type {object_type}")

    