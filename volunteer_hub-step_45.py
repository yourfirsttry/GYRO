# === Stage 45: Добавь восстановление из резервной копии ===
# Project: VolunteerHub
import os
import json
from datetime import datetime

BACKUP_DIR = "backups"
BACKUP_FILE = os.path.join(BACKUP_DIR, "volunteerhub_backup.json")

def save_backup(data):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    with open(BACKUP_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[Backup] Saved to {BACKUP_FILE}")

def restore_backup():
    if not os.path.exists(BACKUP_FILE):
        print("[Backup] No backup file found.")
        return False
    with open(BACKUP_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"[Backup] Restored {len(data)} items from {BACKUP_FILE}")
    return data

def list_backups():
    if not os.path.exists(BACKUP_DIR):
        print("[Backup] No backups directory.")
        return []
    backups = []
    for f in os.listdir(BACKUP_DIR):
        if f.endswith(".json"):
            backups.append((f, os.path.getsize(os.path.join(BACKUP_DIR, f))))
    return sorted(backups, key=lambda x: x[1], reverse=True)
