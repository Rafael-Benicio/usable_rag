import os
from typing import List
from src.base_models import RawContent


def load_raw_content() -> List[RawContent]:
    return _get_raw_content('./My', 0, depth=0)[1]


def _get_raw_content(dir: str, id: int, **kwarg) -> tuple[int, List[RawContent]]:
    raw_content = []

    for file_name in os.listdir(dir):
        if os.path.isdir(dir+"/"+file_name):
            id, ret_raw_content = _get_raw_content(
                dir+"/"+file_name, id, depth=kwarg.get("depth")+1)
            raw_content += ret_raw_content
            continue

        if '.md' not in file_name:
            continue

        with open(dir+"/"+file_name, "+r") as arq:
            content = arq.read()
            raw_content.append(RawContent(id=id, text=content))
            id += 1

    return id, raw_content
