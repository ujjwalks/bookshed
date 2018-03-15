import json

from neomodel import Property
from neomodel.relationship_manager import RelationshipDefinition


class StructuredNodeSerializer(object):
    def __init__(self, *args, **kwargs):
        self.instance = args[0]

        props = self.instance.defined_properties()
        self.fields = kwargs.get('fields', '__all__')
        self.data = {}
        if self.should_include('id'):
            self.data['id'] = self.instance.id

        self.process_properties(props)
        self.serialized_data = json.dumps(self.data)

    def should_include(self, key):
        return key in self.fields or self.fields == '__all__'

    def process_properties(self, props):
        for prop in props.items():
            self.process_property(prop)

    def process_property(self, prop):
        key, value = prop
        if isinstance(value, Property):
            self.process_neomodel_property(key)
        elif isinstance(value, RelationshipDefinition):
            self.process_relationship_definition(key)

    def process_neomodel_property(self, key):
        if self.should_include(key):
            self.data[key] = getattr(self.instance, key)

    def process_relationship_definition(self, key):
        if self.should_include(key):
            rel = getattr(self.instance, key)
            self.data[key] = []
            for r in rel:
                rel_data = StructuredNodeSerializer(r).data
                self.data[key].append(rel_data)
