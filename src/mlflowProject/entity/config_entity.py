from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConifg:
    root_dir: Path
    source_url: Path
    local_data_file: Path
    unzip_dir: Path