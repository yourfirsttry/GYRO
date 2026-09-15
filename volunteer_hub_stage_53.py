# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: VolunteerHub
def import_records_from_file(filepath):
    """Import volunteer records from a simple text file.
    
    Expected format:
        name;role;hours;event;date
        Alice;Coordinator;10;TechFair;2024-01-15
        Bob;Volunteer;5;TechFair;2024-01-15
    
    Returns list of dicts.
    """
    records = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split(';')
                if len(parts) == 5:
                    records.append({
                        'name': parts[0].strip(),
                        'role': parts[1].strip(),
                        'hours': float(parts[2].strip()),
                        'event': parts[3].strip(),
                        'date': parts[4].strip(),
                    })
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"Error importing records: {e}")
    return records
