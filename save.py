import os


def createDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def changeDirectory(path):
    os.chdir(path)


def saveFile(fileName, fileType, fileContent):
    f = open(fileName + fileType, 'w', encoding='utf-8', errors='ignore')
    f.write(fileContent)
    f.close()
    return True


def dictToSave(savedPages):
    i = 1
    savedPagesStr = ''
    for key in savedPages:
            savedPagesStr += (str(i) + ': ' + key + ' - ' + savedPages[key] + '\n')
            i += 1
    return savedPagesStr