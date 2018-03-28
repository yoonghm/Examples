# Microschip's ATWIND1500 IEEE 802.11 b/g/n Wi-Fi Module

## Overview

**ATWINC15x0-MR210xB** is a low power consumption IEEE 802.11 b/g/n IoT module, specifically optimized for low-power IoT applications.

The module integrates Power Amplifier (PA), Low-Noise Amplifier (LNA), Switch, Power Management, and a printed antenna or a micro co-ax (u.FL) connector for an external antenna resulting in a 28-pins, small form factor (21.7 x 14.7 x 2.1 mm) design.

It is interoperable with various vendors’ 802.11 b/g/n access points. This module provides SPI ports to interface with a host controller.
The references to the ATWINC15x0-MR210xB module include the module devices listed in the following:

- ATWINC1500-MR210PB (4 MB flash, OTA, PCB antenna)
- ATWINC1500-MR210UB (4 MB flash, OTA, uFL connector)
- ATWINC1510-MR210PB (8 MB flash, OTA, PCB antenna)
- ATWINC1510-MR210UB (8 MB flash, OTA, uFL connector)

<img align="lect" src="./ATWINC15x0-MR210xB_Block_Diagram.jpg" alt="ATWINC1500 Block Diagram" />

**ATWINC1500 Block Diagram**

<img align="lect" src="./ATWINC15x0-MR210xB_Pins.jpg" alt="ATWINC1500 Pins" />

**ATWINC1500 Pins**

## SPI Slave Inteface

ATWINC1500 provides a full-duplex slave Serial Peripheral Interface (SPI) that can be used for control and for serial I/O of IEEE 802.11 data.  The pin 10 `SPI_CFG` must be tied to VDDIO via a 1 MΩ resistor.

| Pin No. | Name       | Description                                                         |
|:-------:|:----------:|:--------------------------------------------------------------------|
|    10   | `SPI_CFG`  | Tie to `VDDIO` through a 1-MΩ resistor to enable the SPI interface  |
|    13   | `SPI_RXD`  | SPI MOSI (Master Output, Slave In) pin                              |
|    16   | `SPI_SSN`  | SPI Slave Select, active low                                        |
|    17   | `SPI_TXD`  | SPI MISO (Master In, Slave Out)                                     |
|    18   | `SPI_CLK`  | SPI Clock                                                           |
