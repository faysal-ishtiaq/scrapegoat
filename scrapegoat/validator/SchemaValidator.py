import jsonschema


class SchemaValidator:
    @classmethod
    def validate(cls, data, schema):
        return jsonschema.validate(instance=data, schema=schema)
