# Simple project to demostrate conan integration

* Note this project defines a decontainer configuration. So no need for any pre-installations.
* It also defines a task configuration to configure and build using cmake
* Note that CMake tools and its commands to configure and build CMake projects does not support conan install steps directly, resulting in manual execution of the conan installations.
* Therefore this project incorporates all the steps in the configure_build.sh script file.
* Note that due to the installation of conan as a python package, and due to the fact that python packages cannot be installed globally, we first have to active the venv before doing anything

<pre>
source /opt/venv/bin/activate

if [ -d "build" ]; then
  rm -rf "build";
fi

mkdir build
cd build
conan install .. --profile:host=pvdefault --profile:build=pvdefault --build=missing -of .
cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake
cmake --build . --config Release
</pre>
