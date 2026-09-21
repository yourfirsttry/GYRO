# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: VolunteerHub
def mass_delete_with_confirm(items, target, confirm_prompt):
    """Массовое удаление элементов с подтверждением через параметр."""
    if confirm_prompt is None:
        confirm_prompt = "Вы уверены, что хотите удалить {} элементов?"
    if confirm_prompt.lower() in ("y", "yes", "true", "1"):
        for i in range(len(items)):
            target.remove(items[i])
        return len(items)
    return 0
