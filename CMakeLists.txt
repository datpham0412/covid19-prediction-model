cmake_minimum_required(VERSION 3.10)
project(Covid19_Prediction)

set(CMAKE_CXX_STANDARD 17)

add_subdirectory(SQLiteCpp)

include_directories(include)
include_directories(SQLiteCpp/include)

add_executable(Covid19_Prediction src/main.cpp src/data_processor.cpp)

target_link_libraries(Covid19_Prediction SQLiteCpp sqlite3)