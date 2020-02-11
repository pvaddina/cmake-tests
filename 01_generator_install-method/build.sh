cmakeInstallPrefix="../../../gen/"

rm -rf ../gen/calc_lib
rm -rf calc_lib/build
mkdir calc_lib/build
cd calc_lib/build
cmake -DCMAKE_INSTALL_PREFIX=$cmakeInstallPrefix ..
make
make install
cd ../../
