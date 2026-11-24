import os


ENTRY = "Lawmakers who want to regulate AI, crypto, and the entire internet but cannot convert a file to PDF should first pass a basic computer test, because a person who prints every email and calls IT to find the any key probably should not be writing the rules for machines smarter than their printer."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
