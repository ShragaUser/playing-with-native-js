def compile(rootFileUrl):
    print("compiling")
    rootFile = getFileStringByUrl(rootFileUrl)
    nextRequire = rootFile.find("require")
    
    while(nextRequire != -1):
        anonFunc = replaceRequire(rootFile[rootFile.find("(",nextRequire)+2:rootFile.find(")",nextRequire)-1])
        rootFile = rootFile.replace(rootFile[nextRequire:rootFile.find(")",nextRequire)+1], anonFunc)
        nextRequire = rootFile.find("require")
    
    compiledFile = cleanUp(rootFile)
    
    return compiledFile

def cleanUp(fileCode):
    # find all variable assingment and see if variable is used - if not delete it
    return fileCode

def getFileStringByUrl(url):
    if url.find(".js") == -1:
        url += ".js"
    # read file with python
    data = ""
    with open(url, 'r') as file:
        data = file.read()
    return data

def replaceRequire(url):
    file = getFileStringByUrl(url)
    currentRootFolder = url[:url.rfind("/")]
    file = "(function(){" + file + "})()"
    moduleExportsIndex = file.find("module.exports")
    file = file.replace("module.exports", "return")
    file = file[:file.find("=",moduleExportsIndex)] + file[file.find("=",moduleExportsIndex)+1:]
    file = fixRealtiveRequirePaths(file, currentRootFolder)
    return file

def fixRealtiveRequirePaths(file, rootFolder):
    nextRequire = file.find("require")
    all_urls = []
    while(nextRequire != -1):
        url = file[file.find("(",nextRequire)+2:file.find(")",nextRequire)-1]
        all_urls.append(url)
        nextRequire = file.find("require",nextRequire+1)
    for url in all_urls:
        file = file.replace(url, fixRelativePath(url, rootFolder))
    return file

def fixRelativePath(url, rootFolder):
    # check if url is relative
    if url[:1] == ".":
        currentRootFolder = url[:url.rfind("/")]
        last2DotIndex = url.rfind("..")
        while(last2DotIndex != -1):
            url = url[:last2DotIndex] + url[last2DotIndex+1:]
            rootFolder = rootFolder[:rootFolder.rfind("/")]
            last2DotIndex = url.rfind("..")
        return rootFolder + url[1:]
    return url

def writetoFile(fileData):
    with open("./compiled.js", "w") as compiled_file:
        compiled_file.write(fileData)
    
def main():
    compiledFile = compile("./script.js")
    writetoFile(compiledFile)

if __name__ == "__main__":
    main()