from pathlib import Path

def get_adapters(original_path: list):
    adapters = []
    current_adapter = []
    for line in original_path:
        if line.startswith("Ethernet adapter Ethernet"):
            if current_adapter:
                adapters.append(current_adapter)
            current_adapter = [line]
        elif current_adapter:
            current_adapter.append(line)
    if current_adapter:
        adapters.append(current_adapter)
    return adapters

def get_last_adapter(path:list):
    path = path[::-1]
    for line in path:
        if line.split(" ")[:3] == ["Ethernet", "adapter", "Ethernet"]:
            return line.split(" ")[3:][0].split(":")[0]

def find_line_in_file(path:list, to_find:str):
    return
    
def dump_list(path:list):
    for line in path:
        print(line)

def del_empty_lines(path:list):
    new_path = []
    for line in path:
        if not len(line) == 0 and not line == len(line)*" ":
            new_path.append(line)
    return new_path

def main():
    paths = []
    for path in sorted(Path(".").glob("*.txt")):
        paths.append(path.name)
    a_path = del_empty_lines(Path(paths[0]).read_text(encoding="utf-8").splitlines())
    b_path = del_empty_lines(Path(paths[1]).read_text(encoding="utf-8").splitlines())
    dump_list(get_adapterss(a_path)[0])
    #dump_list(a_path)
    #dump_list(b_path)


if __name__ == "__main__":
    main()
    