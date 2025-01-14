class LoadControl:
    def __init__(self,*args):
        self.table_name = "LOAD_CONTROL"
        self.columns = args

    def create_load_control_table(self):
        qry = "CREATE TABLE LOAD_CONTROL ("

        for i in range(0,len(self.columns)):
            if i != len(self.columns) - 1:
                qry = qry + val + "," 
            else:
                qry = qry + val + ")"

        return qry
