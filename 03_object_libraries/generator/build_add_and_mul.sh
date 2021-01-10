cmakeInstallPrefix="../../../install_add_mul"

rm -rf ../install_add_mul/add_lib
rm -rf add_lib/build
mkdir add_lib/build
cd add_lib/build
cmake -DCMAKE_INSTALL_PREFIX=$cmakeInstallPrefix ..
cmake --build . --target install
cd ../../


rm -rf ../install_add_mul/mul_lib
rm -rf mul_lib/build
mkdir mul_lib/build
cd mul_lib/build
cmake -DCMAKE_INSTALL_PREFIX=$cmakeInstallPrefix ..
cmake --build . --target install
cd ../../

