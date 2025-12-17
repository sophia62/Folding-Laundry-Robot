# Folding Laundry Robot - Project Notes

## Overview
This project implements a robotic arm system designed to fold laundry items autonomously. The system consists of Arduino-based hardware control and Python-based high-level control software.

## Hardware Components

### Robot Arm
- **Base Servo**: Rotation of the entire arm (0-180°)
- **Shoulder Servo**: Upper arm movement (15-165°)
- **Elbow Servo**: Forearm movement (0-180°)
- **Wrist Servo**: End effector rotation (0-180°)
- **Gripper Servo**: Gripping mechanism (10° open, 90° closed)

### Pin Configuration
- Base: Pin 9
- Shoulder: Pin 10
- Elbow: Pin 11
- Wrist: Pin 6
- Gripper: Pin 5

## Software Architecture

### Arduino Component (`arduino/early_prototype.ino`)
- Direct servo motor control
- Serial communication interface
- Safety limits enforcement
- Manual and automated control modes

### Python Components

#### `robot_arm.py`
Main control interface for the robot arm:
- Serial communication with Arduino
- High-level movement commands
- Safety integration
- Pose management

#### `poses.py`
Predefined poses for folding operations:
- Standard poses (home, pickup, lift, etc.)
- Folding sequences
- Pose validation

#### `safety.py`
Safety system implementation:
- Joint angle limit checking
- Collision detection
- Transition safety validation
- Emergency stop functionality

## Operation Sequences

### Basic Towel Folding
1. Home position
2. Move to pickup location
3. Close gripper
4. Lift item
5. Execute fold sequence
6. Place folded item
7. Return to home

### Shirt Folding
1. Home position
2. Pickup at shoulder area
3. First fold (sides)
4. Second fold (length)
5. Place in sorted pile
6. Return to home

## Safety Features

### Joint Limits
- All servos have hardware and software limits
- Smooth movement between positions
- Maximum angle change validation

### Collision Avoidance
- Predefined collision zones
- Reach calculation
- Safe transition checking

### Emergency Procedures
- Emergency stop command
- Sensor monitoring (future)
- Force limiting (future)

## Future Enhancements

### Hardware
- [ ] Add force sensors to gripper
- [ ] Implement proximity sensors
- [ ] Add camera for visual feedback
- [ ] Upgrade to stepper motors for precision

### Software
- [ ] Computer vision for item detection
- [ ] Machine learning for fold optimization
- [ ] Multi-item processing queue
- [ ] Web-based control interface

### Capabilities
- [ ] Support for different clothing types
- [ ] Automated sorting by size/type
- [ ] Wrinkle detection and smoothing
- [ ] Integration with washing machine

## Development Notes

### Testing
- Always test new poses in simulation first
- Use manual mode for pose development
- Monitor servo temperatures during extended use
- Keep emergency stop accessible

### Calibration
- Calibrate servo zero positions regularly
- Adjust gripper pressure for different fabrics
- Fine-tune timing delays for smooth operation

### Maintenance
- Check servo connections weekly
- Clean gripper surfaces regularly
- Update firmware as needed
- Document any hardware modifications

## Known Issues
1. Gripper may slip on smooth fabrics (consider adding rubber pads)
2. Large items may exceed reach limits (workspace constraints)
3. Serial communication can be interrupted (add retry logic)

## References
- Arduino Servo Library: https://www.arduino.cc/reference/en/libraries/servo/
- PySerial Documentation: https://pyserial.readthedocs.io/
- Introduction to Robot Kinematics: https://en.wikipedia.org/wiki/Robot_kinematics

## Contributors
- Initial prototype and concept development
- Arduino firmware implementation
- Python control software
- Safety system design

## Version History
- v0.1: Initial prototype with basic movement
- v0.2: Added safety checks and collision detection
- v0.3: Implemented pose sequences for folding

---
Last Updated: 2025-12-17
