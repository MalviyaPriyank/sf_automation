from snowflake.core import Root


class Root:
    def __init__(self,session):
        self.session = session
    
    def get_root_object(self):
        root = Root(self.attr.session)
        return root
    