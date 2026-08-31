# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: VolunteerHub
ANSI = {
    'RESET': '\033[0m',
    'BOLD': '\033[1m',
    'DIM': '\033[2m',
    'UNDERLINE': '\033[4m',
    'BLINK': '\033[5m',
    'REVERSE': '\033[7m',
    'BLACK': '\033[30m',
    'RED': '\033[31m',
    'GREEN': '\033[32m',
    'YELLOW': '\033[33m',
    'BLUE': '\033[34m',
    'MAGENTA': '\033[35m',
    'CYAN': '\033[36m',
    'WHITE': '\033[37m',
    'LIGHT_GRAY': '\033[37m',
}

def color(text, code, enable=True):
    if enable:
        return f'{ANSI[code]}{text}{ANSI["RESET"]}'
    return text

def bold(text):
    return f'{ANSI["BOLD"]}{text}{ANSI["RESET"]}'

def dim(text):
    return f'{ANSI["DIM"]}{text}{ANSI["RESET"]}'

def green(text):
    return color(text, 'GREEN')

def red(text):
    return color(text, 'RED')

def yellow(text):
    return color(text, 'YELLOW')

def blue(text):
    return color(text, 'BLUE')

def cyan(text):
    return color(text, 'CYAN')

def magenta(text):
    return color(text, 'MAGENTA')

def white(text):
    return color(text, 'WHITE')

def header(title):
    return f'\n{bold(white(title))}\n'

def success(msg):
    return green(msg)

def error(msg):
    return red(msg)

def warn(msg):
    return yellow(msg)

def info(msg):
    return blue(msg)

def section_title(title):
    return f'\n{cyan(bold(title))}\n'

def print_status(status, label='Статус'):
    if status == 'ACTIVE':
        print(f'{green("●")} {label}: {status}')
    elif status == 'INACTIVE':
        print(f'{red("●")} {label}: {status}')
    else:
        print(f'{yellow("●")} {label}: {status}')

def print_member(name, role, level):
    print(f'  {cyan(name)} [{role}] - {dim(level)}')

def print_event_schedule(events):
    print(f'{cyan("⏰ Расписание событий:")}')
    for e in events:
        print(f'  {green("✓")} {e["title"]} ({e["date"]})')
