include <MeMegaPi.h>

// Define motor objects for each motor connected to the MegaPi board
MeMegaPiDCMotor motor1(PORT1B); // motor 1 connected to port 1B
MeMegaPiDCMotor motor2(PORT2B);// motor 2 connected to port 2B

//DC motor for the robotic arm
MeMegaPiDCMotor armMotor3(PORT3B);// Arm motor connected to port 3B

//DC motor for the gripper
MeMegaPiDCMotor gripperMotor1A(PORT1A);//Gripper motor connected to port 1A


// Define the speeds for each motor (adjust as needed)
int motorSpeed1 = 200; // Speed for  motor 1
int motorSpeed2 = 200; // Speed for  motor 2
int armMotorSpeed3 = 80;//Speed for arm motor
int gripperMotorSpeed = 100;//Speed for gripper motor

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // moveForward
  motor1.run(-motorSpeed1);
  motor2.run(motorSpeed2);
  delay(2000);

  //stopMotors
  motor1.stop();
  motor2.stop();
  delay(500);

  // turn right
  motor1.run(motorSpeed1);
  motor2.run(motorSpeed2);
  delay(550);

  //stopMotor
  motor1.stop();
  motor2.stop();
  delay(500);
  
  // moveForward
  motor1.run(-motorSpeed1);
  motor2.run(motorSpeed2);
  delay(2000);

  //stopMotors
  motor1.stop();
  motor2.stop();
  delay(500);

  // turn right
  motor1.run(motorSpeed1);
  motor2.run(motorSpeed2);
  delay(550);

  //stopMotor
  motor1.stop();
  motor2.stop();
  delay(500);

  // moveForward
  motor1.run(-motorSpeed1);
  motor2.run(motorSpeed2);
  delay(2000);

  //stopMotors
  motor1.stop();
  motor2.stop();
  delay(500);

  // turn right
  motor1.run(motorSpeed1);
  motor2.run(motorSpeed2);
  delay(550);

  //stopMotor
  motor1.stop();
  motor2.stop();
  delay(500);

  // moveForward
  motor1.run(-motorSpeed1);
  motor2.run(motorSpeed2);
  delay(2000);

  //stopMotors
  motor1.stop();
  motor2.stop();
  delay(500);

  // turn right
  motor1.run(motorSpeed1);
  motor2.run(motorSpeed2);
  delay(550);

  //stopMotor
  motor1.stop();
  motor2.stop();
  delay(1000);
  
  //lift
  armMotor3.run(-armMotorSpeed3);
  delay(500);

  //lift stop
  armMotor3.stop();
  delay(2000);

  //gripperopen
  gripperMotor1A.run(-gripperMotorSpeed);
  delay(1000);

  // gripper stop
  gripperMotor1A.stop();
  delay(200);

  // gripperclose
  gripperMotor1A.run(gripperMotorSpeed);
  delay(1000);

  // lift down
  armMotor3.run(armMotorSpeed3);
  delay(500);

  //all motor stop
  motor1.stop();
  motor2.stop();
  gripperMotor1A.stop();
  armMotor3.stop();

  

  
}
