import os
from typing import List
from src.base_models import RawContent


def load_raw_content(dir: str) -> List[RawContent]:
    return _get_raw_content(dir)


def _get_raw_content(dir: str) -> List[RawContent]:
    raw_content = []

    for file_name in os.listdir(dir):
        if os.path.isdir(dir+"/"+file_name):
            ret_raw_content = _get_raw_content(dir+"/"+file_name)
            raw_content += ret_raw_content
            continue

        if '.md' not in file_name:
            continue

        with open(dir+"/"+file_name, "+r") as arq:
            content = arq.read()
            raw_content.append(RawContent(
                id=len(raw_content), title=file_name, text=content))

    return raw_content
