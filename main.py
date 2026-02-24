"""Matrix Rain Effect - The iconic digital rain in your terminal."""
import random, time, os, sys

def get_size():
    try:
        import shutil
        cols, rows = shutil.get_terminal_size()
        return cols, rows
    except:
        return 80, 24

CHARS = "ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ0123456789ABCDEF"

def rain(duration=20):
    cols, rows = get_size()
    drops = [random.randint(-rows, 0) for _ in range(cols)]
    speeds = [random.randint(1, 3) for _ in range(cols)]
    end = time.time() + duration
    os.system("cls" if sys.platform == "win32" else "clear")
    sys.stdout.write("\033[?25l")  # hide cursor
    sys.stdout.write("\033[32m")   # green color
    try:
        while time.time() < end:
            lines = [[" "] * cols for _ in range(rows)]
            for col in range(cols):
                drop = drops[col]
                for trail in range(12):
                    row = drop - trail
                    if 0 <= row < rows:
                        ch = random.choice(CHARS)
                        if trail == 0:
                            lines[row][col] = f"\033[97m{ch}\033[32m"
                        else:
                            opacity = max(0, 12 - trail)
                            lines[row][col] = ch if opacity > 6 else "."
            sys.stdout.write("\033[H")
            for line in lines:
                sys.stdout.write("".join(line) + "\n")
            for col in range(cols):
                drops[col] += speeds[col]
                if drops[col] - 12 > rows:
                    drops[col] = random.randint(-rows // 2, 0)
                    speeds[col] = random.randint(1, 3)
            sys.stdout.flush()
            time.sleep(0.05)
    finally:
        sys.stdout.write("\033[?25h\033[0m")

if __name__ == "__main__":
    secs = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    print(f"Starting Matrix Rain for {secs}s... (Ctrl+C to stop)")
    time.sleep(1)
    rain(secs)
