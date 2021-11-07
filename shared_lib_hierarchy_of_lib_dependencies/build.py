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
                "addsub" : {
                       "delDirs"    : ["gen/addsub", "addsub/build"],
                       "createDirs" : ["addsub/build"],
                       "workingDir" : "addsub/build",
                       "cmakeCmd"   : "cmake -DCMAKE_INSTALL_PREFIX=\"..\/..\/gen\" ..",
                       "build"      : "make",
                       "install"    : "make install",
                       },
                "muldiv" : {
                       "delDirs"    : ["gen/muldiv", "muldiv/build"],
                       "createDirs" : ["muldiv/build"],
                       "workingDir" : "muldiv/build",
                       "cmakeCmd"   : "cmake -DCMAKE_INSTALL_PREFIX=\"..\/..\/gen\" ..",
                       "build"      : "make",
                       "install"    : "make install",
                       },
                "arithmeticop" : {
                       "delDirs"    : ["gen/arithmeticop", "arithmeticop/build"],
                       "createDirs" : ["arithmeticop/build"],
                       "workingDir" : "arithmeticop/build",
                       "cmakeCmd"   : "cmake -DCMAKE_INSTALL_PREFIX=\"..\/..\/gen\" ..",
                       "build"      : "make",
                       "install"    : "make install",
                       },
                "calc" : {
                       "delDirs"    : ["gen/calc", "calc/build"],
                       "createDirs" : ["calc/build"],
                       "workingDir" : "calc/build",
                       "cmakeCmd"   : "cmake -DCMAKE_INSTALL_PREFIX=\"..\/..\/gen\" ..",
                       "build"      : "make",
                       "install"    : "make install",
                       }
                    },
            "win":  {
                "addsub" : {
                       "delDirs"    : ["gen/addsub", "addsub/build"],
                       "createDirs" : ["addsub/build"],
                       "workingDir" : "addsub/build",
                       "cmakeCmd"   : "cmake -DCMAKE_INSTALL_PREFIX=\"..\/..\/gen\" ..",
                       "build"      : "\"c:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\MSBuild\\15.0\\Bin\\msbuild.exe\" addsub.vcxproj",
                       "install"    : "\"c:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\MSBuild\\15.0\\Bin\\msbuild.exe\" install.vcxproj",
                       },
                "muldiv" : {
                       "delDirs"    : ["gen/muldiv", "muldiv/build"],
                       "createDirs" : ["muldiv/build"],
                       "workingDir" : "muldiv/build",
                       "cmakeCmd"   : "cmake -DCMAKE_INSTALL_PREFIX=\"..\/..\/gen\" ..",
                       "build"      : "\"c:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\MSBuild\\15.0\\Bin\\msbuild.exe\" muldiv.vcxproj",
                       "install"    : "\"c:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\MSBuild\\15.0\\Bin\\msbuild.exe\" install.vcxproj",
                       },
                "arithmeticop" : {
                       "delDirs"    : ["gen/arithmeticop", "arithmeticop/build"],
                       "createDirs" : ["arithmeticop/build"],
                       "workingDir" : "arithmeticop/build",
                       "cmakeCmd"   : "cmake -DCMAKE_INSTALL_PREFIX=\"..\/..\/gen\" ..",
                       "build"      : "\"c:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\MSBuild\\15.0\\Bin\\msbuild.exe\" arithmeticop.vcxproj",
                       "install"    : "\"c:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\MSBuild\\15.0\\Bin\\msbuild.exe\" install.vcxproj",
                       },
                "calc" : {
                       "delDirs"    : ["gen/calc", "calc/build"],
                       "createDirs" : ["calc/build"],
                       "workingDir" : "calc/build",
                       "cmakeCmd"   : "cmake -DCMAKE_INSTALL_PREFIX=\"..\/..\/gen\" ..",
                       "build"      : "\"c:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\MSBuild\\15.0\\Bin\\msbuild.exe\" calc.vcxproj",
                       "install"    : "\"c:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\MSBuild\\15.0\\Bin\\msbuild.exe\" install.vcxproj",
                       }
                    }
          }

if len(sys.argv) <= 1:
    print("Usage:")
    print("python3 build.py <project>")
    print("Example: python3 build.py calc --> Builds the calc project")
    print("Example: python3 build.py addsub --> Builds the addsub project")
else:
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



