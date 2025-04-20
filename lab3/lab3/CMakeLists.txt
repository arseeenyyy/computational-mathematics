cmake_minimum_required(VERSION 3.10)
project(IntegralSolver)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

file(GLOB_RECURSE SOURCES "src/*.cpp")  
file(GLOB_RECURSE HEADERS "src/*.h") 

add_executable(IntegralSolver ${SOURCES} ${HEADERS})

