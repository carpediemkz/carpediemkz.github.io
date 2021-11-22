import os

def rewrite_dir(dir):
    path = p_path + "/" + dir
    print(path)
    print(type(path))

    files = os.listdir(path)

    for file_name in files:
        print(file_name)
        with open(path+"/"+file_name, "r+", encoding="utf-8") as f:
            old = f.read()
            f.seek(0)
            f.writelines([
                "---\n",
                "title: {0}\n".format(file_name.replace(".md", "")),
                "---\n"
            ])
            f.writelines(old)
            f.close()
            print(path+"/"+file_name + "rewrite end")

if __name__ == "__main__":

    p_path = os.path.abspath('./source/_posts')

    sub_folders = os.listdir(p_path)
    for sf in sub_folders:
        if sf.endswith(".md"):
            print("continue: {}".format(sf))
            continue
        print("folder: {}".format(sf))
        rewrite_dir(sf)
