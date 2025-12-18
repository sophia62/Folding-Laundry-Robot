# 🧺 Folding Laundry Robot

A multi-phase robotics and software engineering project exploring autonomous garment manipulation, robotic motion control, and system-level design through the construction of two different robotic systems capable of folding clothes. This project integrates mechanical design, electronics, embedded systems, Python automation, and software architecture, and was developed as part of my interdisciplinary work in Software Engineering, Data Analytics, and Intercultural Studies.

My Intercultural Studies background directly informed the project’s problem selection and design perspective. Clothing care and laundry practices vary widely across cultures in terms of garment types, folding norms, space constraints, and daily routines. Rather than treating folding as a purely mechanical task, I approached it as a human-centered, culturally situated problem, emphasizing adaptability, consistency, and accessibility. This lens guided decisions such as focusing on flexible garments, prioritizing repeatable and gentle folding motions, and framing the project around real-world usability rather than idealized lab conditions. The result is a robotics system that not only demonstrates technical capability, but also reflects an awareness of how automation intersects with everyday life across diverse cultural contexts.

---

## 📌 Project Overview

The Folding Laundry Robot is an experimental robotics project designed to explore how autonomous systems can interact with **soft, deformable objects** such as clothing a problem that remains challenging even in industry. While many robots excel at rigid object manipulation, garments introduce variability in shape, friction, and placement.

This project tackles that challenge through:

* Iterative hardware prototypes
* Multiple control architectures
* Careful motion sequencing
* Safety‑aware servo control
* Modular, extensible software design

The result is a robot that can **consistently fold small garments** while demonstrating strong software design principles and engineering rigor.

---

## 🤖 Robots Used (Two Distinct Systems)

### **Robot 1: Arduino‑Based Servo Arm (Early Prototype)**

**Purpose:**

* Proof of concept
* Understanding servo kinematics
* Manual pose sequencing
* Learning torque limits and mechanical constraints

**Hardware:**

* Arduino UNO R3
* 6× MG996R high‑torque servo motors
* Aluminum servo brackets
* Bearings and mounting plates
* Breadboard + jumper wires
* External power supply (high‑current)
* Basic gripper mechanism
* Linear rail stage with NEMA stepper motor
* A4988 stepper driver

**Key Learnings:**

* Torque requirements for folding motions
* Servo jitter and power isolation issues
* Importance of safe angle limits
* Timing and synchronization challenges

**Programming Language:**

* C++ (Arduino)

**Programming Approach:**

* Direct PWM control
* Predefined pose sequences
* Hard‑coded angle transitions
* Safety clamping to prevent over‑rotation

---

### **Robot 2: Advanced 6‑DOF Robotic Arm (Final System)**

**Purpose:**

* Precision motion control
* Scalable architecture
* Software‑first robotics pipeline
* Reliable garment folding demonstrations

**Hardware:**

* 6‑DOF robotic arm
* MG996 / Dynamixel‑class servo motors
* U2D2 communication interface
* External 24V power supply
* Reinforced aluminum structure

**Control Platforms:**

* macOS (primary development)
* Raspberry Pi (experimentation and deployment)

**Programming Languages:**

* **Python** (primary control)
* C++ (supporting components)

**Key Capabilities:**

* Precise angle control in degrees
* Velocity and acceleration limits
* Multi‑pose choreography
* Safe torque and compliance handling

---

## 🧠 Software Architecture

### **Languages & Technologies**

| Area               | Technology             |
| ------------------ | ---------------------- |
| Embedded Control   | Arduino C++            |
| High‑Level Control | Python                 |
| Robotics SDK       | Dynamixel SDK          |
| Motion Planning    | Custom pose sequencing |
| OS                 | macOS, Raspberry Pi OS |
| Version Control    | Git + GitHub           |

---

### **Programming Strategy**

The system is programmed using a **pose‑based motion architecture**:

1. Each pose defines exact joint angles
2. Poses are executed sequentially
3. Safety checks are enforced before movement
4. Timing is controlled to avoid torque spikes
5. Motions are designed to account for fabric behavior

This approach ensures **repeatability, safety, and clarity**, while allowing future extensions such as:

* Vision‑based correction
* Dynamic pose adjustment
* Machine learning integration

---

## 🧩 Key Features

* ✅ Multi‑robot iterative development
* ✅ Safety‑bounded servo motion
* ✅ Modular pose definitions
* ✅ Cross‑platform control (Mac + Pi)
* ✅ Real‑world garment manipulation
* ✅ Professional robotics documentation

---

## 🔁 Development Process

### **1. Research & Inspiration**

Garment folding is a known challenge in robotics. Major companies including Amazon have invested heavily in solving similar problems due to the enormous logistical value of automated textile handling.

This project was motivated by:

* Cultural relevance (everyone folds laundry)
* Real‑world difficulty
* Clear industry applications

---

### **2. Mechanical Iteration**

* Tested multiple gripper designs
* Adjusted joint spacing and lever arms
* Tuned servo torque limits
* Reinforced stress points

---

### **3. Software Iteration**

* Began with direct servo control
* Transitioned to structured pose execution
* Introduced safety abstraction layers
* Refactored code for readability and extensibility

---

### **4. Testing & Validation**

* Incremental motion testing
* Emergency stop logic
* Servo temperature monitoring
* Repeated folding trials

---

## 📂 Repository Structure

```
folding-laundry-robot/
├── arduino/
│   └── early_prototype.ino
├── python/
│   ├── robot_arm.py
│   ├── poses.py
│   └── safety.py
├── docs/
│   ├── diagrams
│   └── notes.md
├── videos/
│   └── demo_links.md
└── README.md
```

---

## 🎥 Demo Video

▶️ **Final Folding Demonstration:**

* *[Link her](https://youtu.be/dMsEmocv1UU)e*

---

## 🔗 Code Links

* **Dinamixel Download:**

  * *GitHub link here*

* **Python Robot Control:**

  * *GitHub link here*


---

## 🚀 Future Work

* Vision‑based garment detection
* Reinforcement learning for fold optimization
* ROS2 integration
* Automated garment classification
* Industrial‑scale folding adaptations

---

## 🧠 Skills Demonstrated

* Robotics systems engineering
* Software architecture & design patterns
* Embedded systems programming
* Hardware‑software integration
* Iterative prototyping
* Safety‑critical control logic
* 

---


## ⭐ Acknowledgements

Special thanks to mentors, faculty, and peers who supported this project through feedback, technical discussions, and encouragement.

---

