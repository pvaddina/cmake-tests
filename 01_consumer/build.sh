cmakeDependencyPath="../../gen/calc_lib/cmake"  # Relative to the current 
cmakeInstallPath="../../../gen" # Relative to the build directory

rm -rf ../gen/calculator
rm -rf calculator/build
mkdir calculator/build
cd calculator/build
#cmake -DCMAKE_PREFIX_PATH=$cmakeDependencyPath -DCMAKE_INSTALL_PREFIX=$cmakeInstallPath ..
cmake -DCMAKE_PREFIX_PATH=$cmakeDependencyPath -DCMAKE_INSTALL_PREFIX=$cmakeInstallPath ..
make
make install
