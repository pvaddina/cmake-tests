cmakeModPath="../../../gen/"

rm -rf calculator/build
mkdir calculator/build
cd calculator/build
cmake -DCMAKE_MODULE_PATH=$cmakeModPath ..
make
