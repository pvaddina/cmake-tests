rm -rf gen
rm -rf calc_lib/build
mkdir calc_lib/build
cd calc_lib/build
cmake -DCMAKE_INSTALL_PREFIX=../../ ..
make
make install
cd ../..
