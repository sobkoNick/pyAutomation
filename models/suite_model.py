import json
from dataclasses import dataclass, field


@dataclass(init=False, repr=True, eq=True)
class SuiteAttributes:

    title: str
    test_count: int
    # the value is not present when we get all suites.
    description: str = field(default="")


@dataclass(init=False, repr=True, eq=True)
class Suite:

    id: str
    type: str
    attributes: SuiteAttributes

    @staticmethod
    def build(json_str):
        data = json.loads(json_str)
        suite = Suite()
        if 'id' in data.keys():
            suite.id = data['id']
        if 'type' in data.keys():
            suite.type = data['type']

        if 'attributes' in data.keys():
            attributes = SuiteAttributes()
            if 'title' in data['attributes'].keys():
                attributes.title = data['attributes']['title']
            if 'description' in data['attributes'].keys():
                attributes.description = data['attributes']['description']
            if 'test-count' in data['attributes'].keys():
                attributes.test_count = data['attributes']['test-count']
            suite.attributes = attributes
        return suite
