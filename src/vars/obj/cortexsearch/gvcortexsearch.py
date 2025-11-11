import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseMethod,BaseTag

class CortexSearchTag(BaseTag,BaseMethod):
    ATTRIBUTES="ATTRIBUTES"
    WAREHOUSE="WAREHOUSE"
    ON="ON"
    TARGET_LAG="TARGET_LAG"
    TARGET_LAG_UNIT="TARGET_LAG_UNIT"
    EMBEDDING_MODEL="EMBEDDING_MODEL"
    INITIALIZE="INITIALIZE"
    SERVICE_QUERY="SERVICE_QUERY"
    BASE_TABLE="BASE_TABLE"

    @classmethod
    def get_attributes_with_description(cls):
        attr_dict=super().get_attributes_with_description()
        attr_dict["ATTRIBUTES"]="user provided value that specifies comma-separated list of columns in the base table that you wish to filter on when issuing queries to the service. Attribute columns must be included in the source query. This value has to be taken from the user. Pass this as a list : [val1, val2]"
        attr_dict["WAREHOUSE"]="user provided value that specifies the warehouse to use for running the source query, building the search index, and keeping it refreshed per the TARGET_LAG target."
        attr_dict["ON"]="user provided value that specifies the text column in the base table that user wish to search on. This column must be a text value."
        attr_dict["TARGET_LAG"]="user provided value that specifies the maximum amount of time that the Cortex Search service content should lag behind updates to the base tables specified in the source query."
        attr_dict["TARGET_LAG_UNIT"]="value that specifies if the lag is in SECONDS, MINUTES,HOURS or DAYS."
        attr_dict["EMBEDDING_MODEL"]="user provided optional parameter that specifies the embedding model to use in the Cortex Search Service. This property cannot be altered after you create the Cortex Search Service. To modify the property, recreate the Cortex Search Service with a CREATE OR REPLACE CORTEX SEARCH SERVICE command.If the EMBEDDING_MODEL is not specified, the default model is used. The default model is snowflake-arctic-embed-m-v1.5"
        attr_dict["INITIALIZE"]="user provided value that specifies the behavior of the initial refresh of the Cortex Search Service."
        attr_dict["SERVICE_QUERY"]="""Specifies a query defining the base table from which the service is created eg: SELECT
        transcript_text (search column),
        region (filter_column),
        agent_id (filter_column)
        FROM support_transcripts"""
        attr_dict["BASE_TABLE"]="user provided value for base table on which the search service will be created."
        return attr_dict

    @classmethod
    def allowed_value_list(cls):
        return {
            "EMBEDDING_MODEL":["snowflake-arctic-embed-m-v1.5","snowflake-arctic-embed-l-v2.0","snowflake-arctic-embed-l-v2.0-8k","voyage-multilingual-2"],
            "INITIALIZE":["ON_CREATE","ON_SCHEDULE"],
            "TARGET_LAG_UNIT":["seconds","minutes","hours","days"]   
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass