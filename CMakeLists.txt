cmake_minimum_required (VERSION 3.10)
project(concaveman)

set(CMAKE_CXX_STANDARD 14)            # Enable c++14 standard
set(CMAKE_CXX_STANDARD_REQUIRED ON)           
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_BUILD_TYPE Release)

add_library( ${PROJECT_NAME} SHARED ${CMAKE_SOURCE_DIR}/src/main/cpp/concaveman.cpp )

# make the demo/test
set( Sources
        ${CMAKE_SOURCE_DIR}/src/test/cpp/test_concaveman.cpp
        ${CMAKE_SOURCE_DIR}/src/main/cpp/concaveman.h
        )


add_executable( ${PROJECT_NAME}_test ${CMAKE_SOURCE_DIR}/src/test/cpp/test_concaveman.cpp )
include_directories(${CMAKE_SOURCE_DIR}/src/main/cpp)

target_link_libraries( ${PROJECT_NAME}_test LINK_PUBLIC ${PROJECT_NAME} )

# install
install( TARGETS ${PROJECT_NAME} DESTINATION ${CMAKE_SOURCE_DIR}/src/main/python/Concaveman/concaveman )
