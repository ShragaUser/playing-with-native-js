import os, time, glob,subprocess


def getAllFiles():
    dict = {}
    for filename in glob.iglob("./" + '**/*', recursive=True):
        if(filename.find("compiled.js") == -1):
            dict[filename] = os.stat(filename).st_mtime

    return dict
    
def main():
    subprocess.Popen(["python","./server.py"])


    path_to_watch = "."
    before = getAllFiles()
    while 1:
        should_reload = False
        time.sleep(10)
        after = getAllFiles()
        should_reload = len(after) != len(before)
        if (should_reload == False):
            modified = [f for f in before if before[f] < after[f]]
            if modified:
                should_reload = True
                print("A file has been modified")
        else: 
            print("len different")
        
        before = after

        if should_reload:
            print("hot reload in process")
            os.system('compile.py')

if __name__ == "__main__":
    main()

