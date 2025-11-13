import logging
import io
from pathlib import Path
from datetime import datetime
import sys

class SnowchainLogger:
    def __init__(self):
        pass

    def get_logger(self):
        logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        logging.getLogger(__name__).setLevel(logging.INFO)
        self.logger = logging.getLogger(__name__)
        return self.logger
    

    def configure_local_write(self,directory):
        self.log_stream=io.StringIO()
        log_dir=Path(directory)
        log_dir.mkdir(exist_ok=True)
        self.log_filename = log_dir / f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    def add_handlers(self):
        stream_handler=logging.StreamHandler(self.log_stream)
        console_handler=logging.StreamHandler(sys.stdout)
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(console_handler)
