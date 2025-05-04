source /opt/venv/bin/activate

if [ -d "build" ]; then
  rm -rf "build";
fi

mkdir build
cd build
conan install .. --profile:host=pvdefault --profile:build=pvdefault --build=missing -of .
cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake
cmake --build . --config Release
