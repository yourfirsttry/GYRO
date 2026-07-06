# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: VolunteerHub
class Tag:
    def __init__(self, name, color=None):
        self.name = name
        self.color = color or '#' + ''.join(random.choices('0123456789ABCDEF', k=6))

    @property
    def is_valid(self):
        return bool(re.match(r'^[a-zA-Z][a-zA-Z0-9_]{2,}$', self.name))

    def __repr__(self):
        return f'<Tag {self.name}>'


class TagManager:
    def __init__(self):
        self._tags = {}

    @property
    def tags(self):
        return list(self._tags.values())

    def add_tag(self, name, color=None):
        if not Tag.is_valid(name) or name in self._tags:
            raise ValueError(f'Invalid tag name "{name}"')
        tag = Tag(name, color=color)
        self._tags[name] = tag
        return tag

    def remove_tag(self, name):
        if name not in self._tags:
            raise KeyError(f'Tag "{name}" does not exist')
        del self._tags[name]
        return True

    @property
    def count(self):
        return len(self._tags)


TAG_MANAGER = TagManager()
