import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class StreamTag(BaseTag):
    TABLE_NAME="TABLE_NAME"
    AT="AT"
    APPEND_ONLY="APPEND_ONLY"
    INSERT_ONLY="INSERT_ONLY"
    SHOW_INITIAL_ROWS="SHOW_INITIAL_ROWS"
    OBJECT_TYPE="OBJECT_TYPE"
    BEFORE="BEFORE"
    TIMESTAMP="TIMESTAMP"
    OFFSET="OFFSET"
    OBJECT_TYPE="OBJECT_TYPE"
    
    @classmethod
    def get_attributes_with_description(cls):
        attr_dict=super().get_attributes_with_description()
        attr_dict["TABLE_NAME"]="Name of the table on which stream is created. This is required attribute and must always be passed"
        attr_dict["OBJECT_TYPE"]="Specifies what type of object stream is created on."
        attr_dict["AT"]="Creates a stream at a specific time/point in the past. This should be timestamp."
        attr_dict["APPEND_ONLY"]="""
        Specifies whether this is an append-only stream. Append-only streams track row inserts only. Update and delete operations (including table truncates) are not recorded. For example, if 10 rows are inserted into a table and then 5 of those rows are deleted before the offset for an append-only stream is advanced, the stream records 10 rows.
        This type of stream improves query performance over standard streams and is very useful for extract, load, transform (ELT) and similar scenarios that depend exclusively on row inserts.
        """
        attr_dict["INSERT_ONLY"]="""
        Specifies whether this is an insert-only stream. Insert-only streams track row inserts only; 
        they do not record delete operations that remove rows from an inserted set (i.e. no-ops). 
        For example, in-between any two offsets, if File1 is removed from the cloud storage location referenced by 
        the external table, and File2 is added, the stream returns records for the rows in File2 only, 
        regardless of whether File1 was added before or within the requested change interval. 
        Unlike when tracking change data capture (CDC) data for standard tables, access to 
        the historical records for files in cloud storage is not governed by or guaranteed to Snowflake.
        """
        attr_dict["SHOW_INITIAL_ROWS"]="Specifies the records to return the first time the stream is consumed."
        return attr_dict
        
    @classmethod
    def allowed_value_list(cls):
        return {
            "OBJECT_TYPE":["TABLE","EXTERNAL TABLE","STAGE","VIEW"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
