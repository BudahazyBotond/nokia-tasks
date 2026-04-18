import json
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

def make_json(path:list):
    
    json = {
        "file_name" : "ipconfig.log",
        "adapters" : [
            
        ]
    }
    adapters = get_adapters(path)
    for i in range(len(adapters)):
        adapter = adapters[i]
        adapter_json = {
                "adapter_name" : find_line_in_file(adapter, "Ethernet adapter Ethernet"),
                "description" : find_line_in_file(adapter, "   Description"),
                "physical_address" : find_line_in_file(adapter, "   Physical Address"),
                "dhcp_enabled" : find_line_in_file(adapter, "   DHCP Enabled"),
                "ipv4_address" : find_line_in_file(adapter, "   IPv4 Address"),
                "subnet_mask" : find_line_in_file(adapter, "   Subnet Mask"),
                "default_gateway" : find_line_in_file(adapter, "   Default Gateway"),
                "dns_servers" : find_line_in_file(adapter, "   DNS Servers")
        }
        json["adapters"].append(adapter_json)
    return json

def find_line_in_file(adapter:list, to_find:str):
    i=0
    for line in adapter:
        if line.startswith(to_find):
            if to_find == "   DNS Servers":
                return ["".join(line.split(":")[1:]).strip(), ":".join(adapter[i+1].split(":")[1:]).strip()]
            if to_find == "Ethernet adapter Ethernet":
                return line.strip(":")
            return ":".join(line.split(":")[1:]).strip("(Preferred)").strip()
        i+=1
    return ""
    
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
    for path in paths:
        with open(path.split(".")[0]+".json", "w") as f:
            json.dump(make_json(del_empty_lines(Path(path).read_text(encoding="utf-8").splitlines())), f, indent=4)
        with open(path.split(".")[0]+".json", 'r') as f:
            data = json.load(f)
            print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
    