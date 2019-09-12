from .entity import Entity


class Image(Entity):
    def __init__(self, **attributes):
        self.id = attributes.get('id', '')
        self.namespace = attributes.get('namespace', '')
        self.reference = attributes.get('reference', '')
        self.extension = attributes.get('extension', 'jpg')
        self.uri = attributes.get('uri', '')
