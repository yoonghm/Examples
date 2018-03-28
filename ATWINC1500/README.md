# Microschip's ATWIND1500 IEEE 802.11 b/g/n Wi-Fi Module

## Overview

**ATWINC15x0-MR210xB** is a low power WiFi (IEEE 802.11 b/g/n) module in QFN package.

It integrates Power Amplifier (PA), Low-Noise Amplifier (LNA), Switch, Power Management, and a printed antenna or a micro co-ax (u.FL) connector for an external antenna resulting in a 28-pins, small form factor (21.7 x 14.7 x 2.1 mm) design.

It provides SPI slave interface with a slave master (another microcontroller).

It provides UART interface with a host controller (another micontroller or PC).

It support WPA/WPA2 personal, WPA Enterpeise, TLS and SSL security protocols. it provides DHCP, DNS, TCP/IP (IPv4), UDP, HTTP and HTTPS network protocols.

The references to the ATWINC15x0-MR210xB module include the module devices listed in the following:

- ATWINC1500-MR210PB (4 MB flash, OTA, PCB antenna)
- ATWINC1500-MR210UB (4 MB flash, OTA, uFL connector)
- ATWINC1510-MR210PB (8 MB flash, OTA, PCB antenna)
- ATWINC1510-MR210UB (8 MB flash, OTA, uFL connector)

<img align="lect" src="./ATWINC15x0-MR210xB_Block_Diagram.jpg" alt="ATWINC1500 Block Diagram" />

*Figure:* **ATWINC1500 Block Diagram**

<img align="lect" src="./ATWINC15x0-MR210xB_Pins.jpg" alt="ATWINC1500 Pins" />

*Figure:* **ATWINC1500 Pins**

## SPI Slave Inteface

ATWINC15x0-MR210xB provides a full-duplex slave Serial Peripheral Interface (SPI) to host (microcontroller) that can be used for control and for serial I/O of IEEE 802.11 data.  The pin 10 `SPI_CFG` must be tied to VDDIO via a 1 MΩ resistor.

| Pin No. | Name       | Description                                                         |
|:-------:|:----------:|:--------------------------------------------------------------------|
|    10   | `SPI_CFG`  | Tie to `VDDIO` through a 1-MΩ resistor to enable the SPI interface  |
|    15   | `SPI_RXD`  | SPI MOSI (Master Output, Slave In) pin                              |
|    16   | `SPI_SSN`  | SPI Slave Select, active low                                        |
|    17   | `SPI_TXD`  | SPI MISO (Master In, Slave Out)                                     |
|    18   | `SPI_CLK`  | SPI Clock                                                           |

When the SPI is not selected (`SPI_SSN` is high), the SPI will not interfere with data transfers between master (host) and other SPI slave device in the same SPI bus.

ATWINC15x0-MR210xB supports four standard SPI modes determined by Clock Priority (CPOL) and Clock Phase (CPHA) settings.

## UART Interface

ATWINC15x0-MR210xB support Universal Asynchronous Receiver/Transmitter (UART) interface. This interface should be used for **debug purpose** only.

| Pin No. | Name       | Description                                                         |
|:-------:|:----------:|:--------------------------------------------------------------------|
|    14   | `UART_TXD` | UART transmit output from ATWINC15x0-MR210xB                        |
|    19   | `UART_RXD` | UART receive input to ATWINC15x0-MR210xB                            |

