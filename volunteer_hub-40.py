# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: VolunteerHub
def add_cli_parser():
    parser = argparse.ArgumentParser(description="VolunteerHub CLI")
    sub = parser.add_subparsers(dest="command")
    for cmd in ["register", "login", "logout", "list_tasks",
                 "add_volunteer", "add_event", "add_shift",
                 "add_report", "generate_report"]:
        p = sub.add_parser(cmd, help=f"Execute {cmd}")
        p.add_argument("--file", default="volunteerhub.db", help="DB path")
    return parser
