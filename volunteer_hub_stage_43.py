# === Stage 43: Добавь пагинацию длинных списков ===
# Project: VolunteerHub
class Page:
    def __init__(self, items, page_size=20, page=1):
        self.items = items
        self.page_size = page_size
        self.page = page
        self.total_pages = (len(items) + page_size - 1) // page_size if items else 0
        self.start_index = (page - 1) * page_size
        self.end_index = min(start_index + page_size, len(items))
        self.current_items = items[self.start_index:self.end_index]

    def has_next(self):
        return self.start_index + self.page_size < len(self.items)

    def has_prev(self):
        return self.page > 1

    def to_dict(self):
        return {
            'items': self.current_items,
            'page': self.page,
            'page_size': self.page_size,
            'total_pages': self.total_pages,
            'has_next': self.has_next(),
            'has_prev': self.has_prev()
        }

    def __len__(self):
        return len(self.current_items)

    def __getitem__(self, index):
        return self.current_items[index]
