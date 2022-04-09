#define switchPin 3

float current;
float voltage;

void setup() {
  pinMode(switchPin, 1);
  pinMode(A0, 0);
  pinMode(A1, 0);
  pinMode(A2, 0);
  pinMode(A3, 0);

  Serial.begin(115200);
}

void loop() {

  //Drop first five values to increase accuracy
  for (int i = 0; i < 5; i++) {
    analogRead(A1);
  }
  float current_a1 = analogRead(A1);
  for (int i = 0; i < 5; i++) {
    analogRead(A0);
  }
  float current_a0 = analogRead(A0);


  //Calculate current
  current = (current_a1 - current_a0) * 10;


  //Drop first five values to increase accuracy
  for (int i = 0; i < 5; i++) {
    analogRead(A3);
  }
  float voltage_a3 = analogRead(A3);
  for (int i = 0; i < 5; i++) {
    analogRead(A2);
  }
  float voltage_a2 = analogRead(A2);


  //Calculate voltage (change ref value (4.55) to tune)
  voltage = (voltage_a3 - voltage_a2) * 4.55;


  //Switch on mosfet if voltage less than 4.25V
  if (voltage < 4250) {
    digitalWrite(switchPin, 1);
  }
  else {
    digitalWrite(switchPin, 0);
  }


  //Output to serial if charging or measuring cell
  if (current > 10 || voltage > 2500) {
    Serial.print("mA: " + String(current) + "\t");
    Serial.println("mV: " + String(voltage));
  }
}
