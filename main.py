import os

TEXT = "You want to regulate AI, crypto, and the entire internet, yet you just asked your intern to convert a PDF into a PDF, and your password is still 'password123' — maybe start by regulating your own inbox before you legislate the future."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
