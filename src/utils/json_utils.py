import dataclasses
import json
from typing import Any


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def json_dumps(object: Any) -> str:
    return json.dumps(object, cls=EnhancedJSONEncoder)
