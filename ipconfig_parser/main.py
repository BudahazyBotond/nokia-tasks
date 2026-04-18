from pathlib import Path

def get_adapters(path:list):
    adapters = []
    in_same_adapter = True
    how_many_adapters = int(get_adapters_count(path))
    j=0
    for i in range(how_many_adapters):
        
        while in_same_adapter:
            adapter = []
            for j in range(len(path)):
                line = path[j]
                if line.split(" ")[:3] == ["Ethernet", "adapter", "Ethernet"]:
                    in_same_adapter = False
                    break
                adapter.append(line)
            adapters.append(adapter)
    return adapters

def get_adapters_count(path:list):
    path = path[::-1]
    for line in path:
        if line.split(" ")[:3] == ["Ethernet", "adapter", "Ethernet"]:
            return line.split(" ")[3:][0].split(":")[0]

def find_line_in_file(path:list, to_find:str):
    return
    
def dump_list(path:list):
    for line in path:
        print(line)

def main():
    paths = []
    for path in sorted(Path(".").glob("*.txt")):
        paths.append(path.name)
    a_path = Path(paths[0]).read_text(encoding="utf-8").splitlines()
    b_path = Path(paths[1]).read_text(encoding="utf-8").splitlines()    
    dump_list(get_adapters(a_path))
    #dump_list(a_path)
    #dump_list(b_path)


if __name__ == "__main__":
    main()
    