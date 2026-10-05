import os


def folder_summary(folder, ext: str = ".txt") -> int:
    files = []
    width = 0

    for name in sorted(os.listdir(folder)):
        path = os.path.join(folder, name)

        if name == "summary.txt":
            continue

        if not os.path.isfile(path):
            continue

        if not name.endswith(ext):
            continue

        lines = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                lines += 1

        size = os.path.getsize(path)
        files.append((name, lines, size))

        if len(name) > width:
            width = len(name)

    summary_path = os.path.join(folder, "summary.txt")

    with open(summary_path, "w", encoding="utf-8") as summary:
        for name, lines, size in files:
            summary.write(f"{name:<{width}} {lines:>7} {size:>7}\n")

    return len(files)