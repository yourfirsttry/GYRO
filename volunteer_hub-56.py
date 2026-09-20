# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: VolunteerHub
def mass_update_selected(self):
    """Массовое обновление выбранных записей (участники/смены/события/отчёты)."""
    if not self.selected_rows:
        return
    new_values = self._get_bulk_values()
    if new_values is None:
        return
    for row_idx, entity_type in self.selected_rows:
        entity = self._fetch_entity(row_idx)
        if entity is None:
            continue
        for field, value in new_values.items():
            if field not in entity:
                continue
            if hasattr(entity[field], 'set'):
                entity[field].set(value)
            else:
                entity[field] = value
        self._save_entity(entity)
        self._refresh_table()
        self._update_statusbar(f'Обновлено {len(self.selected_rows)} записей')
