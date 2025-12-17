"""
Robot Arm Control Module
Controls the robotic arm for folding laundry operations
"""

import serial
import time
from typing import Tuple, Optional
from poses import Pose, POSE_HOME, POSE_PICKUP, POSE_FOLD_START
from safety import SafetyChecker


class RobotArm:
    """
    Main robot arm controller class.
    Communicates with Arduino hardware via serial connection.
    """
    
    def __init__(self, port: str = '/dev/ttyUSB0', baudrate: int = 9600):
        """
        Initialize robot arm controller.
        
        Args:
            port: Serial port for Arduino connection
            baudrate: Serial communication baud rate
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_conn: Optional[serial.Serial] = None
        self.safety_checker = SafetyChecker()
        self.current_pose: Optional[Pose] = None
        self.is_connected = False
        
    def connect(self) -> bool:
        """
        Establish serial connection with Arduino.
        
        Returns:
            True if connection successful, False otherwise
        """
        try:
            self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)  # Wait for Arduino to reset
            self.is_connected = True
            print(f"Connected to robot arm on {self.port}")
            
            # Move to home position
            self.move_to_pose(POSE_HOME)
            return True
            
        except serial.SerialException as e:
            print(f"Failed to connect: {e}")
            self.is_connected = False
            return False
    
    def disconnect(self):
        """Close serial connection."""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
            self.is_connected = False
            print("Disconnected from robot arm")
    
    def send_command(self, command: str) -> str:
        """
        Send command to Arduino and read response.
        
        Args:
            command: Single character command
            
        Returns:
            Response from Arduino
        """
        if not self.is_connected or not self.serial_conn:
            raise RuntimeError("Not connected to robot arm")
        
        self.serial_conn.write(command.encode())
        time.sleep(0.1)
        
        response = ""
        while self.serial_conn.in_waiting > 0:
            response += self.serial_conn.read(self.serial_conn.in_waiting).decode()
            time.sleep(0.1)
        
        return response.strip()
    
    def move_to_pose(self, pose: Pose) -> bool:
        """
        Move robot arm to a specific pose.
        
        Args:
            pose: Target pose configuration
            
        Returns:
            True if movement successful, False otherwise
        """
        if not self.is_connected:
            print("Error: Not connected to robot arm")
            return False
        
        # Safety check
        if not self.safety_checker.is_pose_safe(pose):
            print(f"Error: Pose {pose.name} failed safety check")
            return False
        
        # Check if smooth transition is safe
        if self.current_pose:
            if not self.safety_checker.is_transition_safe(self.current_pose, pose):
                print(f"Error: Transition from {self.current_pose.name} to {pose.name} is unsafe")
                return False
        
        # Send manual mode command and set each joint
        try:
            self.send_command('m')
            time.sleep(0.2)
            
            # Set base position
            self.send_command(f'b')
            self.serial_conn.write(str(pose.base).encode())
            self.serial_conn.write(b'\n')
            time.sleep(0.5)
            
            # Set shoulder position
            self.send_command(f's')
            self.serial_conn.write(str(pose.shoulder).encode())
            self.serial_conn.write(b'\n')
            time.sleep(0.5)
            
            # Set elbow position
            self.send_command(f'e')
            self.serial_conn.write(str(pose.elbow).encode())
            self.serial_conn.write(b'\n')
            time.sleep(0.5)
            
            # Set wrist position
            self.send_command(f'w')
            self.serial_conn.write(str(pose.wrist).encode())
            self.serial_conn.write(b'\n')
            time.sleep(0.5)
            
            # Exit manual mode
            self.send_command('x')
            
            self.current_pose = pose
            print(f"Moved to pose: {pose.name}")
            return True
            
        except Exception as e:
            print(f"Error moving to pose: {e}")
            return False
    
    def open_gripper(self) -> bool:
        """
        Open the gripper.
        
        Returns:
            True if successful, False otherwise
        """
        if not self.is_connected:
            print("Error: Not connected to robot arm")
            return False
        
        try:
            response = self.send_command('o')
            print("Gripper opened")
            return True
        except Exception as e:
            print(f"Error opening gripper: {e}")
            return False
    
    def close_gripper(self) -> bool:
        """
        Close the gripper.
        
        Returns:
            True if successful, False otherwise
        """
        if not self.is_connected:
            print("Error: Not connected to robot arm")
            return False
        
        try:
            response = self.send_command('c')
            print("Gripper closed")
            return True
        except Exception as e:
            print(f"Error closing gripper: {e}")
            return False
    
    def home(self) -> bool:
        """
        Move to home position.
        
        Returns:
            True if successful, False otherwise
        """
        return self.move_to_pose(POSE_HOME)
    
    def emergency_stop(self):
        """Emergency stop - immediately halt all movement."""
        if self.is_connected:
            # Send home command to stop all servos
            self.send_command('h')
            print("EMERGENCY STOP ACTIVATED")


if __name__ == "__main__":
    # Example usage
    arm = RobotArm()
    
    if arm.connect():
        print("Robot arm connected successfully")
        
        # Test basic movements
        arm.home()
        time.sleep(1)
        
        arm.open_gripper()
        time.sleep(1)
        
        arm.close_gripper()
        time.sleep(1)
        
        arm.disconnect()
    else:
        print("Failed to connect to robot arm")
