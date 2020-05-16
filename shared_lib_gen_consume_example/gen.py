import platform as pf
import sys
import shutil
import subprocess
import os

detectPlatform = pf.system()

delDirs = []
mkDirs = []
allOpts = {
            "linux":{
                "mymath" : {
                       "delDirs"    : ["gen/linux/mymath", "mymath/build_linux"],
                       "createDirs" : ["mymath/build_linux"],
                       "workingDir" : "mymath/build_linux",
                       "cmakeCmd"   : "cmake -DCMAKE_INSTALL_PREFIX=\"..\/..\/gen\/linux\" ..",
                       "build"      : "make",
                       "install"    : "make install",
                       }
                    },
            "win":  {
                "mymath" : {
                       "delDirs"    : ["gen/win/mymath", "mymath/build_win"],
                       "createDirs" : ["mymath/build_win"],
                       "workingDir" : "mymath/build_win",
                       "cmakeCmd"   : "cmake -DCMAKE_INSTALL_PREFIX=\"..\/..\/gen\/win\" ..",
                       "build"      : "\"c:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\MSBuild\\15.0\\Bin\\msbuild.exe\" mymath.vcxproj",
                       "install"    : "\"c:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\MSBuild\\15.0\\Bin\\msbuild.exe\" install.vcxproj",
                       }
                    }
          }

if detectPlatform == "Linux":
    print("Detected platform - LINUX")
    opt = allOpts["linux"][sys.argv[1]]
    seperator = " ; "
elif detectPlatform == "Windows":
    print("Detected platform - Windows")
    opt = allOpts["win"][sys.argv[1]]
    seperator = " & " 

print("Removing specified directories")
for d in opt["delDirs"]:
    shutil.rmtree(d, ignore_errors=True)

print("Creating empty build directory:", opt["createDirs"])
for d in opt["createDirs"]:
    os.mkdir(d)

print("Running cmake, building and installing")
finalCmd = "cd " + opt["workingDir"] + seperator + opt["cmakeCmd"] + seperator + opt["build"] + seperator + opt["install"]
subprocess.Popen(finalCmd, shell=True) 



