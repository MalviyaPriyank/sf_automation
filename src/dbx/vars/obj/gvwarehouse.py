from dataclasses import dataclass

@dataclass(frozen=True)
class WarehouseTags:
    AUTO_STOP_MINS="AUTO_STOP_MINS"
    CHANNEL_DBSQL_VERSION="CHANNEL_DBSQL_VERSION"
    CHANNEL_NAME="CHANNEL_NAME"
    CLUSTER_SIZE="CLUSTER_SIZE"
