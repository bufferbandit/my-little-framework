import zipfile, platform, shutil, sys, pip

def unstash_flare(file_path, file, location):
    os = platform.system()
    ext = "".join([".exe" if platform.system() == "Windows" else platform.architecture()[0]])
    targeted_file = "flare_" + os + ext
    zip_file   = zipfile.ZipFile(file_path + file + ".zip")
    inzip_file = zip_file.read(targeted_file)
    with open(targeted_file,"wb") as outzip_file:
        outzip_file.write(inzip_file)
    shutil.move(targeted_file, location + targeted_file)
    zip_file.close()
    return file_path + targeted_file

     
def unstash_PyQt(file_path, file, location):
    global targeted_file
    if platform.system() == "Windows":
        version_number = "".join(sys.version.split()[0].split(".")[:-1])
        _platform = "".join(
            ["_amd" if platform.architecture()[0] == "64bit" + platform.architecture()[0][:2]
                    else platform.architecture()[0][:2]]
                          )  
        targeted_file = "PyQt4-4.11.4-cp" + version_number +"-cp" + version_number + "m-win" + _platform + ".whl"
        zip_file = zipfile.ZipFile(file_path + file + ".zip")
        inzip_file = zip_file.read(targeted_file)

        with open(targeted_file,"wb") as outzip_file:
            outzip_file.write(inzip_file)
        shutil.move(targeted_file, location + targeted_file)

        pip.main(["install", location + targeted_file])
        zip_file.close()
        return file_path + targeted_file
    
    elif platform.system() == "Linux":
        #Platform is linux...
        pass

    
#unstash_PyQt( "../../data/","zipp", "../../data/executables/")
#unstash_flare("../../data/","flare_stash","../../data/executables/")
