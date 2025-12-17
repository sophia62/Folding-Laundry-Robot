"""
Safety Module
Implements safety checks and constraints for robot arm operations
"""

from typing import Tuple, Optional
import math


class SafetyChecker:
    """
    Safety checker for robot arm operations.
    Validates poses and movements to prevent damage or unsafe conditions.
    """
    
    # Joint angle limits (degrees)
    BASE_MIN = 0
    BASE_MAX = 180
    SHOULDER_MIN = 15
    SHOULDER_MAX = 165
    ELBOW_MIN = 0
    ELBOW_MAX = 180
    WRIST_MIN = 0
    WRIST_MAX = 180
    GRIPPER_MIN = 10   # Open
    GRIPPER_MAX = 90   # Closed
    
    # Maximum allowed change per transition (degrees)
    MAX_JOINT_CHANGE = 90
    
    # Kinematic link lengths (arbitrary units)
    SHOULDER_LENGTH = 10.0
    ELBOW_LENGTH = 8.0
    WRIST_LENGTH = 5.0
    
    # Collision zones (combinations to avoid)
    COLLISION_ZONES = [
        # (shoulder_min, shoulder_max, elbow_min, elbow_max)
        # Avoid positions where arm might hit base
        (15, 40, 0, 30),
    ]
    
    def __init__(self):
        """Initialize safety checker."""
        self.collision_count = 0
        self.safety_violation_count = 0
    
    def is_angle_in_range(self, angle: float, min_val: float, max_val: float) -> bool:
        """
        Check if angle is within allowed range.
        
        Args:
            angle: Angle to check
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            
        Returns:
            True if angle is safe, False otherwise
        """
        return min_val <= angle <= max_val
    
    def is_pose_safe(self, pose) -> bool:
        """
        Check if a pose is safe.
        
        Args:
            pose: Pose object to validate
            
        Returns:
            True if pose is safe, False otherwise
        """
        # Check each joint is within limits
        if not self.is_angle_in_range(pose.base, self.BASE_MIN, self.BASE_MAX):
            print(f"Safety violation: Base angle {pose.base} out of range "
                  f"[{self.BASE_MIN}, {self.BASE_MAX}]")
            self.safety_violation_count += 1
            return False
        
        if not self.is_angle_in_range(pose.shoulder, self.SHOULDER_MIN, self.SHOULDER_MAX):
            print(f"Safety violation: Shoulder angle {pose.shoulder} out of range "
                  f"[{self.SHOULDER_MIN}, {self.SHOULDER_MAX}]")
            self.safety_violation_count += 1
            return False
        
        if not self.is_angle_in_range(pose.elbow, self.ELBOW_MIN, self.ELBOW_MAX):
            print(f"Safety violation: Elbow angle {pose.elbow} out of range "
                  f"[{self.ELBOW_MIN}, {self.ELBOW_MAX}]")
            self.safety_violation_count += 1
            return False
        
        if not self.is_angle_in_range(pose.wrist, self.WRIST_MIN, self.WRIST_MAX):
            print(f"Safety violation: Wrist angle {pose.wrist} out of range "
                  f"[{self.WRIST_MIN}, {self.WRIST_MAX}]")
            self.safety_violation_count += 1
            return False
        
        if not self.is_angle_in_range(pose.gripper, self.GRIPPER_MIN, self.GRIPPER_MAX):
            print(f"Safety violation: Gripper position {pose.gripper} out of range "
                  f"[{self.GRIPPER_MIN}, {self.GRIPPER_MAX}]")
            self.safety_violation_count += 1
            return False
        
        # Check for collision zones
        if self.is_in_collision_zone(pose):
            print(f"Safety violation: Pose {pose.name} is in collision zone")
            self.collision_count += 1
            return False
        
        return True
    
    def is_in_collision_zone(self, pose) -> bool:
        """
        Check if pose is in a known collision zone.
        
        Args:
            pose: Pose to check
            
        Returns:
            True if pose is in collision zone, False otherwise
        """
        for zone in self.COLLISION_ZONES:
            shoulder_min, shoulder_max, elbow_min, elbow_max = zone
            if (shoulder_min <= pose.shoulder <= shoulder_max and
                elbow_min <= pose.elbow <= elbow_max):
                return True
        return False
    
    def is_transition_safe(self, current_pose, target_pose) -> bool:
        """
        Check if transition between two poses is safe.
        
        Args:
            current_pose: Current pose
            target_pose: Target pose
            
        Returns:
            True if transition is safe, False otherwise
        """
        # Calculate change in each joint
        base_change = abs(target_pose.base - current_pose.base)
        shoulder_change = abs(target_pose.shoulder - current_pose.shoulder)
        elbow_change = abs(target_pose.elbow - current_pose.elbow)
        wrist_change = abs(target_pose.wrist - current_pose.wrist)
        gripper_change = abs(target_pose.gripper - current_pose.gripper)
        
        # Check if any single joint change is too large
        if base_change > self.MAX_JOINT_CHANGE:
            print(f"Unsafe transition: Base change of {base_change}° exceeds max {self.MAX_JOINT_CHANGE}°")
            return False
        
        if shoulder_change > self.MAX_JOINT_CHANGE:
            print(f"Unsafe transition: Shoulder change of {shoulder_change}° exceeds max {self.MAX_JOINT_CHANGE}°")
            return False
        
        if elbow_change > self.MAX_JOINT_CHANGE:
            print(f"Unsafe transition: Elbow change of {elbow_change}° exceeds max {self.MAX_JOINT_CHANGE}°")
            return False
        
        if wrist_change > self.MAX_JOINT_CHANGE:
            print(f"Unsafe transition: Wrist change of {wrist_change}° exceeds max {self.MAX_JOINT_CHANGE}°")
            return False
        
        return True
    
    def calculate_reach(self, pose) -> float:
        """
        Calculate approximate reach distance from base.
        Simplified calculation assuming fixed link lengths.
        
        Args:
            pose: Pose to calculate reach for
            
        Returns:
            Approximate reach distance in arbitrary units
        """
        # Simplified kinematic calculation using class constants
        shoulder_rad = math.radians(pose.shoulder)
        elbow_rad = math.radians(pose.elbow)
        
        # Simple 2D reach calculation
        x = (self.SHOULDER_LENGTH * math.cos(shoulder_rad) +
             self.ELBOW_LENGTH * math.cos(shoulder_rad + elbow_rad) +
             self.WRIST_LENGTH)
        
        y = (self.SHOULDER_LENGTH * math.sin(shoulder_rad) +
             self.ELBOW_LENGTH * math.sin(shoulder_rad + elbow_rad))
        
        reach = math.sqrt(x**2 + y**2)
        return reach
    
    def get_safety_stats(self) -> dict:
        """
        Get safety statistics.
        
        Returns:
            Dictionary with safety statistics
        """
        return {
            "collision_count": self.collision_count,
            "safety_violation_count": self.safety_violation_count,
        }
    
    def reset_stats(self):
        """Reset safety statistics."""
        self.collision_count = 0
        self.safety_violation_count = 0


# Emergency safety limits for critical scenarios
EMERGENCY_LIMITS = {
    "max_speed": 50,  # Maximum speed in degrees/second
    "min_clearance": 5,  # Minimum clearance from obstacles in cm
    "max_force": 10,  # Maximum force in Newtons
}


def check_emergency_conditions(sensor_data: dict) -> Tuple[bool, Optional[str]]:
    """
    Check for emergency conditions based on sensor data.
    
    Args:
        sensor_data: Dictionary with sensor readings
        
    Returns:
        Tuple of (is_safe, error_message)
    """
    # Check for obstacle detection
    if "distance" in sensor_data:
        if sensor_data["distance"] < EMERGENCY_LIMITS["min_clearance"]:
            return False, f"Obstacle detected at {sensor_data['distance']}cm"
    
    # Check for excessive force
    if "force" in sensor_data:
        if sensor_data["force"] > EMERGENCY_LIMITS["max_force"]:
            return False, f"Excessive force detected: {sensor_data['force']}N"
    
    # Check for over-temperature
    if "temperature" in sensor_data:
        if sensor_data["temperature"] > 70:  # Celsius
            return False, f"Motor overheating: {sensor_data['temperature']}°C"
    
    return True, None


if __name__ == "__main__":
    from poses import POSE_HOME, POSE_PICKUP, POSE_FOLD_START
    
    checker = SafetyChecker()
    
    print("Testing Safety Checker")
    print("=" * 50)
    
    # Test pose validation
    print(f"\nChecking home pose: {checker.is_pose_safe(POSE_HOME)}")
    print(f"Checking pickup pose: {checker.is_pose_safe(POSE_PICKUP)}")
    print(f"Checking fold_start pose: {checker.is_pose_safe(POSE_FOLD_START)}")
    
    # Test transition validation
    print(f"\nChecking transition home -> pickup: {checker.is_transition_safe(POSE_HOME, POSE_PICKUP)}")
    print(f"Checking transition pickup -> fold_start: {checker.is_transition_safe(POSE_PICKUP, POSE_FOLD_START)}")
    
    # Display statistics
    print(f"\nSafety Statistics: {checker.get_safety_stats()}")
