from pathlib import Path


def main():
    paths = []
    for path in sorted(Path(".").glob("*.txt")):
        paths.append(path.name)
    a_path = Path(paths[0]).read_text(encoding="utf-8").splitlines()
    b_path = Path(paths[1]).read_text(encoding="utf-8").splitlines()    
    print(a_path)
    print(b_path)


if __name__ == "__main__":
    main()
    