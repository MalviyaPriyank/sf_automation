class InvalidObject(Exception):
    def __init__(self, object_type):
        self.object_type = object_type

    def __str__(self):
        return f"Snowflake does not allow granting privilege to {self.object_type} object type"
    