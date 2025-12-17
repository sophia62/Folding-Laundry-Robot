"""
Pose Definitions Module
Defines standard poses for the folding laundry robot
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Pose:
    """
    Represents a robot arm pose with joint angles.
    All angles are in degrees.
    """
    name: str
    base: int        # Base rotation (0-180)
    shoulder: int    # Shoulder joint (15-165)
    elbow: int       # Elbow joint (0-180)
    wrist: int       # Wrist rotation (0-180)
    gripper: int     # Gripper (10=open, 90=closed)
    
    def __str__(self) -> str:
        return (f"Pose({self.name}): "
                f"base={self.base}, shoulder={self.shoulder}, "
                f"elbow={self.elbow}, wrist={self.wrist}, "
                f"gripper={self.gripper}")


# Standard poses for folding operations
POSE_HOME = Pose(
    name="home",
    base=90,
    shoulder=90,
    elbow=90,
    wrist=90,
    gripper=10  # Open
)

POSE_PICKUP = Pose(
    name="pickup",
    base=90,
    shoulder=45,
    elbow=135,
    wrist=90,
    gripper=10  # Open
)

POSE_GRIP = Pose(
    name="grip",
    base=90,
    shoulder=45,
    elbow=135,
    wrist=90,
    gripper=90  # Closed
)

POSE_LIFT = Pose(
    name="lift",
    base=90,
    shoulder=75,
    elbow=90,
    wrist=90,
    gripper=90  # Closed
)

POSE_FOLD_START = Pose(
    name="fold_start",
    base=60,
    shoulder=60,
    elbow=120,
    wrist=45,
    gripper=90  # Closed
)

POSE_FOLD_MIDDLE = Pose(
    name="fold_middle",
    base=90,
    shoulder=90,
    elbow=90,
    wrist=90,
    gripper=70  # Partially closed
)

POSE_FOLD_END = Pose(
    name="fold_end",
    base=120,
    shoulder=60,
    elbow=120,
    wrist=135,
    gripper=50  # Partially open
)

POSE_PLACE = Pose(
    name="place",
    base=90,
    shoulder=45,
    elbow=120,
    wrist=90,
    gripper=10  # Open
)

POSE_REST = Pose(
    name="rest",
    base=90,
    shoulder=120,
    elbow=60,
    wrist=90,
    gripper=10  # Open
)


# Dictionary of all available poses
ALL_POSES: Dict[str, Pose] = {
    "home": POSE_HOME,
    "pickup": POSE_PICKUP,
    "grip": POSE_GRIP,
    "lift": POSE_LIFT,
    "fold_start": POSE_FOLD_START,
    "fold_middle": POSE_FOLD_MIDDLE,
    "fold_end": POSE_FOLD_END,
    "place": POSE_PLACE,
    "rest": POSE_REST,
}


def get_pose(name: str) -> Pose:
    """
    Get a pose by name.
    
    Args:
        name: Name of the pose
        
    Returns:
        Pose object
        
    Raises:
        KeyError: If pose name not found
    """
    if name not in ALL_POSES:
        raise KeyError(f"Pose '{name}' not found. Available poses: {list(ALL_POSES.keys())}")
    return ALL_POSES[name]


def list_poses() -> list:
    """
    Get list of all available pose names.
    
    Returns:
        List of pose names
    """
    return list(ALL_POSES.keys())


# Predefined folding sequences
SEQUENCE_TOWEL_FOLD = [
    POSE_HOME,
    POSE_PICKUP,
    POSE_GRIP,
    POSE_LIFT,
    POSE_FOLD_START,
    POSE_FOLD_MIDDLE,
    POSE_FOLD_END,
    POSE_PLACE,
    POSE_HOME,
]

SEQUENCE_SHIRT_FOLD = [
    POSE_HOME,
    POSE_PICKUP,
    POSE_GRIP,
    POSE_LIFT,
    POSE_FOLD_START,
    POSE_REST,
    POSE_FOLD_MIDDLE,
    POSE_FOLD_END,
    POSE_PLACE,
    POSE_HOME,
]


if __name__ == "__main__":
    # Display all poses
    print("Available Poses:")
    print("=" * 50)
    for pose_name in list_poses():
        pose = get_pose(pose_name)
        print(pose)
    
    print("\n" + "=" * 50)
    print(f"Total poses defined: {len(ALL_POSES)}")
