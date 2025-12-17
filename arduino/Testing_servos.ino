#include <Servo.h>

const uint8_t SERVO_PIN = 7;   // servo signal
const uint8_t VRX_PIN   = A2;  // joystick X (VRx)

Servo s;

// Optional: tweak these if your joystick doesn't reach full 0..1023
const int RAW_MIN = 0;         // set to ~100–150 if needed
const int RAW_MAX = 1023;      // set to ~900–950 if needed

// Smoothing (EMA): 0 = no smoothing, 0.7 is pretty smooth
const float ALPHA = 0.7;

float filt = 512.0;  // start near center

void setup() {
  s.attach(SERVO_PIN);   // servo power should be external 5–6 V, GND common with Arduino
  s.write(90);           // start centered
  pinMode(VRX_PIN, INPUT);
}

void loop() {
  // Read joystick
  int raw = analogRead(VRX_PIN);            // 0..1023

  // Clamp to expected range (handles imperfect pots)
  raw = constrain(raw, RAW_MIN, RAW_MAX);

  // Normalize to 0..1023 after clamping
  long norm = map(raw, RAW_MIN, RAW_MAX, 0, 1023);

  // Smooth to reduce jitter
  filt = ALPHA * filt + (1.0 - ALPHA) * (float)norm;

  // Map to servo angle 0..180
  int angle = map((int)filt, 0, 1023, 0, 180);

  // Optional tiny deadband (prevents buzzing)
  static int lastAngle = 90;
  if (abs(angle - lastAngle) >= 1) {
    s.write(angle);
    lastAngle = angle;
  }

  delay(10);  // ~100 Hz update
}
