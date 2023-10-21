import json
import glob
from pathlib import Path


def get_logs(logdir):
    logfiles = glob.glob(str(Path(logdir) / "access*.log"))
    print("Logs found:", logfiles)
    return logfiles


def json_dump(obj: list[dict], filename: str) -> None:
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)


def print_dict(data, indent=0):
    for key, value in data.items():
        if isinstance(value, dict):
            print(" " * indent + f"{key}:")
            print_dict(value, indent + 2)
        elif isinstance(value, list):
            print(" " * indent + f"{key}:")
            for item in value:
                print(" " * (indent + 2) + str(item))
        else:
            print(" " * indent + f"{key}: {value}")
