import os, sys, shutil

def main():
    # get the name from input
    if len(sys.argv) < 2:
        print ("Please enter a name")
        print ("Example 'python setup.py my_project'")
        return None
    if len(sys.argv) > 2:
    	print ("Please enter a one word long name")
        print ("Example 'python setup.py my_project'")
        return None
    name = sys.argv[1]
    # print("setting project name to \"%s\"" % name)
    sys.stdout.write("setting project name to \"%s\"..." % name)

    # string replace files files
    recursiveReplace('core', '[*projectName*]', name)
    recursiveReplace('[*projectName*]', '[*projectName*]', name)
    fileReplace('Procfile', '[*projectName*]', name)
    fileReplace('manage.py', '[*projectName*]', name)

    # rename the project directory
    os.rename("[*projectName*]", name)

    # delete this file and .git
    os.remove('setName.py')
    shutil.rmtree('.git')

    print ("done!")

def recursiveReplace(dir, oldStr, newStr):
    for dirName, subdirList, fileList in os.walk(dir):
        for fname in fileList:
            fullName = os.path.join(dirName, fname)
            fileReplace(fullName, oldStr, newStr)


def fileReplace(fileName, oldStr, newStr):
    with open(fileName) as f:
        file = f.read()
        newfile = file.replace(oldStr,newStr)
        open(fileName,"w").write(newfile)


main()