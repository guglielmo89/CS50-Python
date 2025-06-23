def main():
    name = input("File name: ").strip().lower()
    if name.endswith("gif") or name.endswith("png"):
        print("image/gif")
    elif name.endswith("jpg") or name.endswith("jpeg"):
        print("image/jpeg")
    elif name.endswith("pdf") or name.endswith("zip"):

    elif name.endswith("txt"):
        print("text/plain")
    else:
        print("application/octet-stream")

main()
