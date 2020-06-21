from sqlalchemy import types
import json


# Custom data type for handling dictionary based data (Json format)
class JsonDC(types.TypeDecorator):

    impl = types.String

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
            return value
