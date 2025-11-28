import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseMethod,BaseTag

class CopyIntoTag(BaseTag,BaseMethod):
    TABLE="TABLE"
    STAGE="STAGE"
    FILE_FORMAT="FILE_FORMAT"
    ON_ERROR="ON_ERROR"
    SIZE_LIMIT="SIZE_LIMIT"
    PURGE="PURGE"
    RETURN_FAILED_ONLY="RETURN_FAILED_ONLY"
    MATCH_BY_COLUMN_NAME="MATCH_BY_COLUMN_NAME"
    INCLUDE_METADATA="INCLUDE_METADATA"
    ENFORCE_LENGTH="ENFORCE_LENGTH"
    TRUNCATECOLUMNS="TRUNCATECOLUMNS"
    FORCE="FORCE"
    LOAD_UNCERTAIN_FILES="LOAD_UNCERTAIN_FILES"
    FILE_PROCESSOR="FILE_PROCESSOR"
    SCANNER="SCANNER"
    PROJECT_NAME="PROJECT_NAME"
    MODEL_NAME="MODEL_NAME"
    MODEL_VERSION="MODEL_VERSION"
    LOAD_MODE="LOAD_MODE"

    @classmethod
    def get_attributes_with_description(cls):
        attr_dict = super().get_attributes_with_description()
        attr_dict["TABLE"] = "user provided value for TABLE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["STAGE"] = "user provided value for STAGE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["FILE_FORMAT"] = "user provided value for FILE_FORMAT for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["ON_ERROR"] = "user provided value for ON_ERROR for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["SIZE_LIMIT"] = "user provided value for SIZE_LIMIT for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["PURGE"] = "user provided value for PURGE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["RETURN_FAILED_ONLY"] = "user provided value for RETURN_FAILED_ONLY for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["MATCH_BY_COLUMN_NAME"] = "user provided value for MATCH_BY_COLUMN_NAME for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["INCLUDE_METADATA"] = "user provided value for INCLUDE_METADATA for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["ENFORCE_LENGTH"] = "user provided value for ENFORCE_LENGTH for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["TRUNCATECOLUMNS"] = "user provided value for TRUNCATECOLUMNS for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["FORCE"] = "user provided value for FORCE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["LOAD_UNCERTAIN_FILES"] = "user provided value for LOAD_UNCERTAIN_FILES for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["FILE_PROCESSOR"] = "user provided value for FILE_PROCESSOR for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["SCANNER"] = "user provided value for SCANNER for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["PROJECT_NAME"] = "user provided value for PROJECT_NAME for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["MODEL_NAME"] = "user provided value for MODEL_NAME for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["MODEL_VERSION"] = "user provided value for MODEL_VERSION for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["LOAD_MODE"] = "user provided value for LOAD_MODE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["ONE_TIME_LOAD"]= "this is a flag to signify if the user wants to run one time load or if they are trying to setup a pipeline. Pass this as TRUE if its a one time load other wise FALSE"
        print(f'copy into keys: {attr_dict}')
        return attr_dict


    @classmethod
    def allowed_value_list(cls):
        return {
            "ON_ERROR":["CONTINUE","SKIP_FILE"],
            "MATCH_BY_COLUMN_NAME":["CASE_SENSITIVE","CASE_INSENSITIVE","NONE"],
            "SCANNER":['document_ai'],
            "LOAD_MODE":["FULL_INGEST","ADD_FILES_COPY"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass