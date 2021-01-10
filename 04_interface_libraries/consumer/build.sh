cmakeInstallPrefix="../../install_calc"
cmakePrefixPath="../install_add_mul/add_mul_lib"

rm -rf ../install_calc/ctool
rm -rf build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$cmakeInstallPrefix -DCMAKE_PREFIX_PATH=$cmakePrefixPath ..
cmake --build . --target install