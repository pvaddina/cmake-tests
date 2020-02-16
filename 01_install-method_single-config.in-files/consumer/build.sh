cmakeDependencyPath="../../gen/calc_lib/cmake"  # Relative to the 
cmakeInstallPath="../../../gen" # Relative to the CMakeLists.txt location

rm -rf ../gen/calculator
rm -rf calculator/build
mkdir calculator/build
cd calculator/build
# CMAKE_PREFIX_PATH    --> to point to the install location of the dependencies
# CMAKE_INSTALL_PREFIX --> to point to a location where the install commands will 
# copy the generated targets/export configurations
cmake -DCMAKE_PREFIX_PATH=$cmakeDependencyPath -DCMAKE_INSTALL_PREFIX=$cmakeInstallPath ..
make
make install
