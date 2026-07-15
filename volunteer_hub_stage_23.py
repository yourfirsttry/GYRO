# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: VolunteerHub
def print_table(headers, rows):
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row or []):
            col_widths[i] = max(col_widths[i], len(str(val)))
    widths = [max(w, 6) for w in col_widths]
    sep = '+'.join('-' * (w + 2) for w in widths)
    print(sep)
    header_line = '| ' + ' | '.join(str(h).center(widths[i]) for i, h in enumerate(headers)) + ' |'
    print(header_line)
    print(sep)
    for row in rows:
        line = '| ' + ' | '.join(str(row[i] if i < len(row) else '').ljust(widths[i]) for i in range(len(headers))) + ' |'
        print(line)
    print(sep)

def format_volunteer(vol):
    return [vol['name'], str(vol.get('phone', '')), vol['role']]

def format_shift(shift):
    return [shift['event_name'], shift['time_slot'], str(len(shift['volunteers']))]
