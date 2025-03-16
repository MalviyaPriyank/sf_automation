from datetime import datetime

class Stage:
    def __init__(self,root,database,schema):
        self.root = root
        self.database = database
        self.schema = schema

    def set_stage(self,value):
        self.stage = value

    def set_stage_reference(self):
        self.stage_reference = self.root.databases[self.database].schemas[self.schema].stages[self.stage]

    def get_list_of_stages_in_schema(self):
        lst_stage = []
        stg_collection = self.root.databases[self.database].schemas[self.schema].stages
        for stage in stg_collection.iter():
            lst_stage.append(stage.name)
        return lst_stage

    def get_list_of_files_from_stage(self):
        lst_stage_files = []
        stage_files = self.stage_reference.list_files()
        for file in stage_files:
            lst_stage_files.append(file.name)

        return lst_stage_files
    
    def remove_stage_name_from_file_path(self,file_path):
        file_path = "/".join(file_path.split("/")[1:])
        return file_path

    
    def download_file_from_stage(self,file_path,destination_path):
        self.stage_reference.get(file_path,destination_path)

    def upload_sql_to_a_file_in_stage(self,qry,file_name,upload_path):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = "./" + file_name + "_" + timestamp + ".txt"        
        #self.stage_reference.put("/sf_automation/" + file_name,'DB', auto_compress=True)


    def upload_file_to_stage(self,file_path,upload_path,auto_compress,overwrite):
        self.stage_reference.put(file_path,upload_path,auto_compress = auto_compress, overwrite = overwrite)






