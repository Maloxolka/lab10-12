import os

def cure_dir(path):
    files = os.listdir(path)

    for file in files:
        with open(path + "//" + file, 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].replace('virus', '')
            with open(path + "//" + file, 'w') as fw:
                for line in lines:
                    fw.write(line)

    return "Done"