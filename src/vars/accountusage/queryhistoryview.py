import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.baseaccountusage import AccountUsageViews

class QueryHistoryColumnList:
    _view=AccountUsageViews._query_history_view
    _reader_account_name="reader_account_name"
    _query_id="query_id"
    _query_text="query_text"
    _database_id="database_id"
    _database_name="database_name"
    _schema_id="schema_id"
    _schema_name="schema_name"
    _query_type="query_type"
    _session_id="session_id"
    _user_name="user_name"
    _role_name="role_name"
    _warehouse_id="warehouse_id"
    _warehouse_name="warehouse_name"
    _warehouse_size="warehouse_size"
    _warehouse_type="warehouse_type"
    _cluster_number="cluster_number"
    _query_tag="query_tag"
    _execution_status="execution_status"
    _error_code="error_code"
    _error_message="error_message"
    _start_time="start_time"
    _end_time="end_time"
    _total_elapsed_time="total_elapsed_time"
    _bytes_scanned="bytes_scanned"
    _percentage_scanned_from_cache="percentage_scanned_from_cache"
    _bytes_written="bytes_written"
    _bytes_written_to_result="bytes_written_to_result"
    _bytes_read_from_result="bytes_read_from_result"
    _rows_produced="rows_produced"
    _rows_inserted="rows_inserted"
    _rows_updated="rows_updated"
    _rows_deleted="rows_deleted"
    _rows_unloaded="rows_unloaded"
    _bytes_deleted="bytes_deleted"
    _partitions_scanned="partitions_scanned"
    _partitions_total="partitions_total"
    _bytes_spilled_to_local_storage="bytes_spilled_to_local_storage"
    _bytes_spilled_to_remote_storage="bytes_spilled_to_remote_storage"
    _bytes_sent_over_the_network="bytes_sent_over_the_network"
    _compilation_time="compilation_time"
    _execution_time="execution_time"
    _queued_provisioning_time="queued_provisioning_time"
    _queued_repair_time="queued_repair_time"
    _queued_overload_time="queued_overload_time"
    _transaction_blocked_time="transaction_blocked_time"
    _outbound_data_transfer_cloud="outbound_data_transfer_cloud"
    _outbound_data_transfer_region="outbound_data_transfer_region"
    _outbound_data_transfer_bytes="outbound_data_transfer_bytes"
    _inbound_data_transfer_cloud="inbound_data_transfer_cloud"
    _inbound_data_transfer_region="inbound_data_transfer_region"
    _inbound_data_transfer_bytes="inbound_data_transfer_bytes"
    _list_external_files_time="list_external_files_time"
    _credits_used_cloud_services="credits_used_cloud_services"
    _reader_account_deleted_on="reader_account_deleted_on"
    _release_version="release_version"
    _external_function_total_invocations="external_function_total_invocations"
    _external_function_total_sent_rows="external_function_total_sent_rows"
    _external_function_total_received_rows="external_function_total_received_rows"
    _external_function_total_sent_bytes="external_function_total_sent_bytes"
    _external_function_total_received_bytes="external_function_total_received_bytes"
    _query_load_percent="query_load_percent"
    _is_client_generated_statement="is_client_generated_statement"
    _query_acceleration_bytes_scanned="query_acceleration_bytes_scanned"
    _query_acceleration_partitions_scanned="query_acceleration_partitions_scanned"
    _query_acceleration_upper_limit_scale_factor="query_acceleration_upper_limit_scale_factor"
    _transaction_id="transaction_id"
    _child_queries_wait_time="child_queries_wait_time"
    _role_type="role_type"
    _query_hash="query_hash"
    _query_hash_version="query_hash_version"
    _query_parameterized_hash="query_parameterized_hash"
    _query_parameterized_hash_version="query_parameterized_hash_version"
    _secondary_role_stats="secondary_role_stats"
    _rows_written_to_result="rows_written_to_result"
    _query_retry_time="query_retry_time"
    _query_retry_cause="query_retry_cause"
    _fault_handling_time="fault_handling_time"
    _user_type="user_type"
    _user_database_name="user_database_name"
    _user_database_id="user_database_id"
    _user_schema_name="user_schema_name"
    _user_schema_id="user_schema_id"
    _binds_values="binds_values"
    


class QueryHistoryView:
    def __init__(self):
        self.attr=QueryHistoryColumnList()

    def get_col_and_definitions(self):
        semantic_dic={
            self.attr._reader_account_name:"Name of the reader account in which the SQL statement was executed.",
            self.attr._query_id:"Internal/system-generated identifier for the SQL statement.",
            self.attr._query_text:"Text of the SQL statement. The limit is 100K characters. Longer SQL statements are truncated.",
            self.attr._database_id:"internal/system-generated identifier for the database that was in use.",
            self.attr._database_name:"atabase that was specified in the context of the query at compilation.",
            self.attr._schema_id:"Internal/system-generated identifier for the schema that was in use.",
            self.attr._schema_name:"Schema that was specified in the context of the query at compilation.",
            self.attr._query_type:"DML, query, etc. If the query failed, then the query type may be UNKNOWN.",
            self.attr._session_id:"Session that executed the statement.",
            self.attr._user_name:"User who issued the query.",
            self.attr._role_name:"Role that was active in the session at the time of the query.",
            self.attr._warehouse_id:"Internal/system-generated identifier for the warehouse that was used.",
            self.attr._warehouse_name:"Warehouse that the query executed on, if any.",
            self.attr._warehouse_size:"Size of the warehouse when this statement executed.",
            self.attr._warehouse_type:"Type of the warehouse when this statement executed.",
            self.attr._cluster_number:"The cluster (in a multi-cluster warehouse) that this statement executed on.",
            self.attr._query_tag:"Query tag set for this statement through the QUERY_TAG session parameter.",
            self.attr._execution_status:"Execution status for the query. Valid values: success, fail, incident.",
            self.attr._error_code:"Error code, if the query returned an error",
            self.attr._error_message:"Error message, if the query returned an error. The limit is 5K characters. Longer error messages are truncated.",
            self.attr._start_time:"Statement start time (in the local time zone)",
            self.attr._end_time:"Statement end time (in the local time zone)",
            self.attr._total_elapsed_time:"Elapsed time (in milliseconds).",
            self.attr._bytes_scanned:"Number of bytes scanned by this statement.",
            self.attr._percentage_scanned_from_cache:"Percentage of data scanned from the local disk cache. The value ranges from 0.0 to 1.0. Multiply by 100 to get a true percentage.",
            self.attr._bytes_written:"Number of bytes written (e.g. when loading into a table).",
            self.attr._bytes_written_to_result:"Number of bytes written to a result object. For example, select * from . . . would produce a set of results in tabular format representing each field in the selection. In general, the results object represents whatever is produced as a result of the query, and bytes_written_to_result represents the size of the returned result.",
            self.attr._rows_produced:"The number of rows produced by this statement. The ROWS_PRODUCED column will be deprecated in a future release. The value in the ROWS_PRODUCED column doesn’t always reflect the logical number of rows affected by a query. Snowflake recommends using the ROWS_INSERTED, ROWS_UPDATED, ROWS_WRITTEN_TO RESULT, or ROWS_DELETED columns instead.",
            self.attr._rows_inserted:"Number of rows inserted by the query.",
            self.attr._rows_updated:"Number of rows updated by the query.",
            self.attr._rows_deleted:"Number of rows deleted by the query.",
            self.attr._rows_unloaded:"Number of rows unloaded during data export.",
            self.attr._bytes_deleted:"Number of bytes deleted by the query.",
            self.attr._partitions_scanned:"Number of micro-partitions scanned.",
            self.attr._partitions_total:"Total micro-partitions of all tables included in this query.",
            self.attr._bytes_spilled_to_local_storage:"Volume of data spilled to local disk.",
            self.attr._bytes_spilled_to_remote_storage:"Volume of data spilled to remote disk.",
            self.attr._bytes_sent_over_the_network:"Volume of data sent over the network.",
            self.attr._compilation_time:"Compilation time (in milliseconds)",
            self.attr._execution_time:"Execution time (in milliseconds)",
            self.attr._queued_provisioning_time:"Time (in milliseconds) spent in the warehouse queue, waiting for the warehouse compute resources to provision, due to warehouse creation, resume, or resize.",
            self.attr._queued_repair_time:"Time (in milliseconds) spent in the warehouse queue, waiting for compute resources in the warehouse to be repaired.",
            self.attr._queued_overload_time:"Time (in milliseconds) spent in the warehouse queue, due to the warehouse being overloaded by the current query workload.",
            self.attr._transaction_blocked_time:"Time (in milliseconds) spent blocked by a concurrent DML.",
            self.attr._outbound_data_transfer_cloud:"Target cloud provider for statements that unload data to another region and/or cloud.",
            self.attr._outbound_data_transfer_region:"Target region for statements that unload data to another region and/or cloud.",
            self.attr._outbound_data_transfer_bytes:"Number of bytes transferred in statements that unload data from Snowflake tables.",
            self.attr._inbound_data_transfer_cloud:""
        }