import json


def json_dump(obj: list[dict], filename: str) -> None:
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)
