/*
 * Folding Laundry Robot - Early Prototype
 * Arduino control code for robotic arm servo motors
 */

#include <Servo.h>

// Servo motor definitions
Servo baseServo;      // Base rotation
Servo shoulderServo;  // Shoulder joint
Servo elbowServo;     // Elbow joint
Servo wristServo;     // Wrist rotation
Servo gripperServo;   // Gripper control

// Pin assignments
const int BASE_PIN = 9;
const int SHOULDER_PIN = 10;
const int ELBOW_PIN = 11;
const int WRIST_PIN = 6;
const int GRIPPER_PIN = 5;

// Safety limits (degrees)
const int BASE_MIN = 0;
const int BASE_MAX = 180;
const int SHOULDER_MIN = 15;
const int SHOULDER_MAX = 165;
const int ELBOW_MIN = 0;
const int ELBOW_MAX = 180;
const int WRIST_MIN = 0;
const int WRIST_MAX = 180;
const int GRIPPER_MIN = 10;  // Open
const int GRIPPER_MAX = 90;  // Closed

// Current positions
int currentBase = 90;
int currentShoulder = 90;
int currentElbow = 90;
int currentWrist = 90;
int currentGripper = 10;

void setup() {
  Serial.begin(9600);
  
  // Attach servos to pins
  baseServo.attach(BASE_PIN);
  shoulderServo.attach(SHOULDER_PIN);
  elbowServo.attach(ELBOW_PIN);
  wristServo.attach(WRIST_PIN);
  gripperServo.attach(GRIPPER_PIN);
  
  // Move to home position
  moveToHome();
  
  Serial.println("Folding Laundry Robot - Ready");
  Serial.println("Commands: h=home, o=open gripper, c=close gripper, m=manual mode");
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    switch(command) {
      case 'h':
        moveToHome();
        Serial.println("Moved to home position");
        break;
        
      case 'o':
        openGripper();
        Serial.println("Gripper opened");
        break;
        
      case 'c':
        closeGripper();
        Serial.println("Gripper closed");
        break;
        
      case 'm':
        manualMode();
        break;
        
      default:
        Serial.println("Unknown command");
        break;
    }
  }
}

void moveToHome() {
  moveServo(baseServo, currentBase, 90, BASE_MIN, BASE_MAX);
  currentBase = 90;
  
  moveServo(shoulderServo, currentShoulder, 90, SHOULDER_MIN, SHOULDER_MAX);
  currentShoulder = 90;
  
  moveServo(elbowServo, currentElbow, 90, ELBOW_MIN, ELBOW_MAX);
  currentElbow = 90;
  
  moveServo(wristServo, currentWrist, 90, WRIST_MIN, WRIST_MAX);
  currentWrist = 90;
  
  openGripper();
}

void openGripper() {
  moveServo(gripperServo, currentGripper, GRIPPER_MIN, GRIPPER_MIN, GRIPPER_MAX);
  currentGripper = GRIPPER_MIN;
}

void closeGripper() {
  moveServo(gripperServo, currentGripper, GRIPPER_MAX, GRIPPER_MIN, GRIPPER_MAX);
  currentGripper = GRIPPER_MAX;
}

void moveServo(Servo &servo, int currentPos, int targetPos, int minLimit, int maxLimit) {
  // Check safety limits
  if (targetPos < minLimit || targetPos > maxLimit) {
    Serial.print("ERROR: Target position out of range: ");
    Serial.println(targetPos);
    return;
  }
  
  // Smooth movement
  int step = (currentPos < targetPos) ? 1 : -1;
  
  for (int pos = currentPos; pos != targetPos; pos += step) {
    servo.write(pos);
    delay(15);  // Smooth motion delay
  }
  
  servo.write(targetPos);
}

void manualMode() {
  Serial.println("Manual mode - Enter servo angles (b,s,e,w,g followed by angle)");
  Serial.println("Example: 'b90' sets base to 90 degrees. 'x' to exit.");
  
  while (true) {
    if (Serial.available() > 0) {
      char servoId = Serial.read();
      
      if (servoId == 'x') {
        Serial.println("Exiting manual mode");
        break;
      }
      
      int angle = Serial.parseInt();
      
      switch(servoId) {
        case 'b':
          if (angle >= BASE_MIN && angle <= BASE_MAX) {
            moveServo(baseServo, currentBase, angle, BASE_MIN, BASE_MAX);
            currentBase = angle;
            Serial.print("Base: ");
            Serial.println(angle);
          }
          break;
          
        case 's':
          if (angle >= SHOULDER_MIN && angle <= SHOULDER_MAX) {
            moveServo(shoulderServo, currentShoulder, angle, SHOULDER_MIN, SHOULDER_MAX);
            currentShoulder = angle;
            Serial.print("Shoulder: ");
            Serial.println(angle);
          }
          break;
          
        case 'e':
          if (angle >= ELBOW_MIN && angle <= ELBOW_MAX) {
            moveServo(elbowServo, currentElbow, angle, ELBOW_MIN, ELBOW_MAX);
            currentElbow = angle;
            Serial.print("Elbow: ");
            Serial.println(angle);
          }
          break;
          
        case 'w':
          if (angle >= WRIST_MIN && angle <= WRIST_MAX) {
            moveServo(wristServo, currentWrist, angle, WRIST_MIN, WRIST_MAX);
            currentWrist = angle;
            Serial.print("Wrist: ");
            Serial.println(angle);
          }
          break;
          
        case 'g':
          if (angle >= GRIPPER_MIN && angle <= GRIPPER_MAX) {
            moveServo(gripperServo, currentGripper, angle, GRIPPER_MIN, GRIPPER_MAX);
            currentGripper = angle;
            Serial.print("Gripper: ");
            Serial.println(angle);
          }
          break;
      }
    }
  }
}
