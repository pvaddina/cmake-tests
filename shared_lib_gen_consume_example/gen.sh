rm -rf gen
rm -rf mymath/build
rm -rf calc/build

mkdir mymath/build
cd mymath/build
cmake -DCMAKE_INSTALL_PREFIX="../../gen" ..
make
make install

