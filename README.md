# Gas Detection and Safety System

A simple gas detection and safety system using a Raspberry Pi.

## Idea

The system detects gas leakage using a gas sensor.

When gas is detected, the system:

* Displays the gas status on the LCD.
* Turns on the red LED.
* Activates the buzzer.
* Uses a motor to close the gas source.

When no gas is detected, the system stays in the normal state.

## Components

* Raspberry Pi
* Gas Sensor
* LCD
* Red LED
* Buzzer
* Motor
* Wires

## How It Works

The gas sensor continuously monitors the environment.

If the gas level exceeds the defined threshold, the Raspberry Pi treats it as a possible gas leak and activates the warning system. The motor is also used to close the gas source.

## Simulation

The project was designed and tested using Wokwi.

[Wokwi Project](https://wokwi.com/projects/475578426743096321)
