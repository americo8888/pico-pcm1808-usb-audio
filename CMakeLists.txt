cmake_minimum_required(VERSION 3.20)

include(${CMAKE_CURRENT_SOURCE_DIR}/../../../hw/bsp/family_support.cmake)

# Override family_add_linkermap to a no-op to avoid missing linkermap.py error
function(family_add_linkermap TARGET)
endfunction()

project(audio_4_channel_mic C CXX ASM)

# Checks this example is valid for the family and initializes the project
family_initialize_project(${PROJECT_NAME} ${CMAKE_CURRENT_LIST_DIR})

# Espressif has its own cmake build system
if(FAMILY STREQUAL "espressif")
  return()
endif()

add_executable(${PROJECT_NAME})

# Example source
target_sources(${PROJECT_NAME} PUBLIC
  ${CMAKE_CURRENT_SOURCE_DIR}/src/main.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/usb_descriptors.c
  )

# Add PIO generation
pico_generate_pio_header(${PROJECT_NAME} ${CMAKE_CURRENT_SOURCE_DIR}/src/i2s_slave.pio)

# Example include
target_include_directories(${PROJECT_NAME} PUBLIC
  ${CMAKE_CURRENT_SOURCE_DIR}/src
  )

# Add libm for GCC
if (CMAKE_C_COMPILER_ID STREQUAL "GNU")
  target_link_libraries(${PROJECT_NAME} PUBLIC m)
endif()

# Add Pico SDK libraries
target_link_libraries(${PROJECT_NAME} PUBLIC
  hardware_pio
  hardware_dma
  )

# Configure compilation flags and libraries for the example without RTOS.
# See the corresponding function in hw/bsp/FAMILY/family.cmake for details.
family_configure_device_example(${PROJECT_NAME} noos)
