# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: VolunteerHub
class FavoritesManager:
    def __init__(self, db):
        self.db = db
        self._load()

    def _load(self):
        try:
            self.favorites = self.db.get('favorites', {})
        except Exception:
            self.favorites = {}

    def save(self):
        self.db.set('favorites', self.favorites)

    def toggle_favorite(self, record_id):
        if record_id in self.favorites:
            del self.favorites[record_id]
        else:
            self.favorites[record_id] = True
        self.save()

    def get_favorites(self):
        return list(self.favorites.keys())

    def is_favorite(self, record_id):
        return record_id in self.favorites
