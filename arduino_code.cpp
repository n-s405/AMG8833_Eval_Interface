#include <Wire.h>
#include <GridEye.h>

GridEye sensor;

void setup(void)
{
  Wire.begin();
  sensor.setFramerate(10);
  Serial.begin(115200);
  while (!Serial) {
    ; 
  }
}

int pixel[64];
void loop(void)
{
  delay(100);
  sensor.pixelOut(pixel);

  Serial.write(0x55);
  Serial.write(0xaa);
  for (int i = 0; i < 64; i++) {
    Serial.write((pixel[i]     ) & 0xff);
    Serial.write((pixel[i] >> 8) & 0xff);
  }
}
