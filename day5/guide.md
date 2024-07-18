1) Intsall esptool

pip inistall esptool

2) Connect ESP32 to your PC and check COM-port number.

3) Go to https://micropython.org/download/ESP32_GENERIC/
,copy ,update and use in terminal next texts:
<N> - COM-port number with your ESP32

python -m esptool --chip esp32 --port COM<N> erase_flash

python -m esptool --chip esp32 --port COM<N> 
--baud 460800 write_flash -z 0x1000 <Your bin file>
 
