import os


ENTRY = "Before lawmakers regulate AI, crypto, and the internet, they should demonstrate they can convert a file to PDF without calling IT, printing the email, and asking their grandchild what a browser is, because rules written by people who fear the any key will only protect us from progress."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
