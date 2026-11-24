import os

TEXT = "You want to write the laws for AI, crypto, and the whole internet, but you just emailed your assistant a screenshot of a Word document and asked them to 'make it a PDF again.' Regulate your own recycle bin first, then we'll talk about the future."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
