# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: VolunteerHub
def backup_data(data_path, backup_dir=".backups"):
    import shutil, os
    if not os.path.exists(data_path):
        return
    os.makedirs(backup_dir, exist_ok=True)
    filename = f"backup_{os.path.basename(data_path)}_{int(time.time())}.dat"
    backup_path = os.path.join(backup_dir, filename)
    shutil.copy2(data_path, backup_path)
    return backup_path
