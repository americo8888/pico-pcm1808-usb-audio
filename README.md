# Raspberry Pi Pico - PCM1808 Stereo 24-bit I2S Slave Microphone

This project is a modified TinyUSB USB audio microphone example for the Raspberry Pi Pico (RP2040). It has been adapted to capture stereo (2-channel) audio from a **PCM1808** module configured as an **I2S Master**.

The Pico operates in **I2S Slave mode**, listening for external bit clock (BCLK) and word select (LRCK) signals from the PCM1808 and sampling data on each rising edge.

## Key Features

- **Format**: 2 Channels (Stereo), 24-bit resolution, 48 kHz sample rate.
- **I2S Configuration**: Pico as Slave, PCM1808 as Master.
- **USB Class**: USB Audio Class 2.0 (UAC2) compatible.
- **Implementation**:
  - PIO-based I2S input engine for precise clock synchronization.
  - DMA ring buffering for low-latency, glitch-free capture.
  - Custom UAC2 descriptors for improved host compatibility (tested with Audacity).

## Hardware Connections

| PCM1808 Pin | Pico GPIO | Description |
| :--- | :--- | :--- |
| **DATA** | **GPIO 10** | I2S Serial Data Output from PCM1808 |
| **BCLK** | **GPIO 11** | I2S Bit Clock (Output from PCM1808) |
| **LRCK** | **GPIO 12** | I2S Word Select / Left-Right Clock (Output from PCM1808) |
| **VDD** | **VBUS (5V)** | Power (5V from USB) |
| **GND** | **GND** | Common Ground |

*Note: A short is applied to **OP2** for the PCM1808 module's 48 kHz master-mode configuration.*

## Build Instructions (Ubuntu 24.04 LTS)

### 1. Install System Dependencies
Open a terminal and install the required packages:
```bash
sudo apt update
sudo apt install -y git cmake python3 build-essential \
    gcc-arm-none-eabi libnewlib-arm-none-eabi libstdc++-arm-none-eabi-newlib
```

### 2. Setup Pico SDK
If you haven't already installed the SDK, clone it and its submodules:
```bash
mkdir -p ~/pico
cd ~/pico
git clone -b master https://github.com/raspberrypi/pico-sdk.git
cd pico-sdk
git submodule update --init
```

### 3. Set Environment Variables
The build system needs to know where the Pico SDK is located. You can add this to your `~/.bashrc` to make it permanent:
```bash
export PICO_SDK_PATH=~/pico/pico-sdk
```
*(Apply to current session: `source ~/.bashrc` or `export PICO_SDK_PATH=~/pico/pico-sdk`)*

### 4. Build the Project
Navigate to the project directory and run the following:
```bash
# From the project root (where CMakeLists.txt is located)
mkdir -p build
cd build

# Run CMake
cmake ..

# Compile (using all available CPU cores)
make -j$(nproc)
```

## Flashing the Pico

1.  Hold the **BOOTSEL** button on your Raspberry Pi Pico.
2.  Plug the Pico into your USB port.
3.  The Pico will appear as a mass storage device named `RPI-RP2`.
4.  Drag and drop the `pcm1808_stereo_mic.uf2` file (found in the `build` folder) onto the `RPI-RP2` drive.
5.  The Pico will reboot automatically and be recognized as **"MicNode_Stereo"**.
