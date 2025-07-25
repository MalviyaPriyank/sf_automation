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