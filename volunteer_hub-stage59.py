# === Stage 59: Добавь диагностику производительности основных операций ===
# Project: VolunteerHub
import time, sys

def benchmark_volunteerhub():
    start = time.perf_counter()
    if sys.argv and sys.argv[1] == "--profile":
        profile_file = sys.argv[2] if len(sys.argv) > 2 else "profile.txt"
        with open(profile_file, "w") as f:
            f.write(f"VolunteerHub Performance Profile\n")
            f.write(f"Python Version: {sys.version}\n")
            f.write(f"Platform: {sys.platform}\n")
            f.write(f"{'='*50}\n")
            f.write(f"Run with --profile to generate this report.\n")
            f.write(f"{'='*50}\n")
    else:
        print(f"VolunteerHub Performance Diagnostics")
        print(f"Python Version: {sys.version}")
        print(f"Platform: {sys.platform}")
        print(f"{'='*50}")
        print("Run with --profile flag to generate a profile report file.")
        print(f"{'='*50}")
    elapsed = time.perf_counter() - start
    print(f"Diagnostic overhead: {elapsed:.4f}s")

if __name__ == "__main__":
    benchmark_volunteerhub()
