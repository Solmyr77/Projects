int incoming = 0;

void setup() {
  
  pinMode (2, OUTPUT);
  pinMode (3, OUTPUT);
  pinMode (4, OUTPUT);
  pinMode (5, OUTPUT);
  pinMode (A0, INPUT);

  Serial.begin (9600);
  
}

void loop() {

  if (Serial.available() > 0) {
    incoming = Serial.read();
  }
  
  Serial.println("loop complete");

}
