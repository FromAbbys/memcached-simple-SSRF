import urllib.parse

def get_key():
    key = input("Key name: ")
    cmd = f"get {key}\r\nquit\r\n" 
    print(f"gopher://localhost:11211/_{urllib.parse.quote(urllib.parse.quote(cmd))}")


def retrieve_items():
    cmd = "stats items\r\nquit\r\n\r\n"
    print(f"gopher://localhost:11211/_{urllib.parse.quote(urllib.parse.quote(cmd))}")


def cache_dump():
    slab = input("Slab number: ")
    number_of_itens = input(("Limit to return items: "))
    cmd = f"stats cachedump {slab} {number_of_itens}\r\nquit\r\n"
    print(f"gopher://localhost:11211/_{urllib.parse.quote(urllib.parse.quote(cmd))}")

function_list = ["get_key","retrieve_items","cache_dump"]

print("What function do you want to call:\n")
for x in range(0,len(function_list)):
    print(f"{x} -> {function_list[x]}")

choice = int(input("Choose the number: "))
globals()[function_list[choice]]()
