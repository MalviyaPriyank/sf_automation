import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class SnowpipeTag(BaseTag):
    AUTO_INGEST="AUTO_INGEST"
    ERROR_INTEGRATION="ERROR_INTEGRATION"
    AWS_SNS_TOPIC="AWS_SNS_TOPIC"
    INTEGRATION="INTEGRATION"
    COPYINTO_QUERY="COPYINTO_QUERY"

    @classmethod
    def get_attributes_with_description(cls):
        attr_dict = super().get_attributes_with_description()
        attr_dict["AUTO_INGEST"] = "Specifies whether to automatically load data files from the internal or external stage. DEFAULT value is set to NONE"
        attr_dict["ERROR_INTEGRATION"] ="""
        Required only when configuring Snowpipe to send error notifications to a cloud messaging service.
        Specifies the name of the notification integration used to communicate with the messaging service.
        DEFAULT value is set to NONE"""
        attr_dict["AWS_SNS_TOPIC"] = """
        Required only when configuring AUTO_INGEST for Amazon S3 external stages using SNS.
        Specifies the Amazon Resource Name (ARN) for the SNS topic for your S3 bucket. 
        The CREATE PIPE statement subscribes the Amazon Simple Queue Service (SQS) queue to the specified SNS topic. 
        The pipe copies files to the ingest queue triggered by event notifications via the SNS topic.
        DEFAULT value is set to NONE""",
        attr_dict["INTEGRATION"] = """Required only when configuring AUTO_INGEST for Google Cloud Storage or Microsoft Azure external stages.
        Specifies the existing notification integration used to access the storage queue.
        DEFAULT value is set to NONE""",
        attr_dict["COPYINTO_QUERY"] = """
        The copy into query that is created using copyinto object module. 
        This is a required attribute, this query has to be created before creating snowpipe.
        """
        return attr_dict
    

    @classmethod
    def allowed_value_list(cls):
        pass

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
