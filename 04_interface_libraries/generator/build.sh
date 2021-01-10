cmakeInstallPrefix="../../install_add_mul"

rm -rf ../install_add_mul
rm -rf build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$cmakeInstallPrefix ..
cmake --build . --target install
