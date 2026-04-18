from pathlib import Path

def get_adapters(original_path:list):
    path = original_path.copy()
    adapters = []
    in_same_adapter = True
    is_last_adapter = False
    i = 0
    while(is_last_adapter == False):
        if path[i].split(" ")[:3] == ["Ethernet", "adapter", "Ethernet"]:
            print("Found adapter: " + path[i].split(" ")[3:][0].split(":")[0])
            while in_same_adapter:
                adapter = []
                for j in range(len(path)):
                    line = path[j]
                    if line.split(" ")[:3] == ["Ethernet", "adapter", "Ethernet"]:
                        in_same_adapter = False
                        path = path[j:]
                        if line.split(" ")[3:][0].split(":")[0] == get_last_adapter(original_path):
                            print("Found last adapter: " + line.split(" ")[3:][0].split(":")[0])
                            is_last_adapter = True
                        break
                    adapter.append(line)
                adapters.append(adapter)
        in_same_adapter = True
        i+=1
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
        if not len(line) < 0 and not line == len(line)*" ":
            new_path.append(line)
    return new_path

def main():
    paths = []
    for path in sorted(Path(".").glob("*.txt")):
        paths.append(path.name)
    a_path = del_empty_lines(Path(paths[0]).read_text(encoding="utf-8").splitlines())
    b_path = del_empty_lines(Path(paths[1]).read_text(encoding="utf-8").splitlines())
    dump_list(get_adapters(a_path))
    #dump_list(a_path)
    #dump_list(b_path)


if __name__ == "__main__":
    main()
    