class ObjectDependencyBase:
    _dependency_dict = {}

class DBAndSchemaDependency(ObjectDependencyBase):
    _dependency_dict = {
        1: "Database",
        2: "Schema"
    }

class DBOnlyDependency(ObjectDependencyBase):
    _dependency_dict = {
        1: "Database"
    }

class Table(DBAndSchemaDependency): pass
class Schema(DBOnlyDependency): pass
class Alert(DBAndSchemaDependency): pass
class FileFormat(DBAndSchemaDependency) : pass
class Stage(DBAndSchemaDependency): pass

class CopyInto(DBAndSchemaDependency):
    @staticmethod
    def get_dependency_dict():
        base_dict = dict(DBAndSchemaDependency._dependency_dict)
        base_dict[3] = ["File Format", "Stage", "Table"]
        return base_dict

    _dependency_dict = get_dependency_dict()


class ObjectDependency:
    def __init__(self):
        self.registry = {
            "TABLE": Table,
            "SCHEMA": Schema,
            "ALERT":Alert,
            "STAGE":Stage
        }

    def get_dependencies(self,object_type:str):
        """
        Find all the objects that should be set up in order to setup {object_type}.

        Args:
            object_type(str) : The object to be created on snowflake
            
        Returns:
            dict which contains as values the name of objects that are prerequisite. Keys of the dictionary tells the order in which it should be created.
        
        """
        self.cls = self.registry.get(object_type.upper())
        print(f"inside get dependency for {object_type}")
        print(f"class name {self.cls}")
        if not self.cls:
            raise ValueError(f"No dependencies defined for: {object_type}")
        self._dependency_dict = self.cls._dependency_dict
        return self._dependency_dict
