import evdev
import sys
from pythonosc.udp_client import SimpleUDPClient

usb_name = "USB Gamepad "
carpet = None
code = None
value = None

if len(sys.argv) == 1:
    ip = "localhost"
    port = 8000
elif len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    sys.exit("Please, specify ip and port or use defaults")


client = SimpleUDPClient(ip, port)  # Create client

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for device in devices:
    if device.name == usb_name:
        carpet = device
        break

for event in carpet.read_loop():
    if event.type == evdev.ecodes.EV_KEY or event.type == evdev.ecodes.EV_ABS:
        #print(event.code, event.value)

        if event.code == 290:
            code = "up"
        elif event.code == 288:
            code = "left"
        elif event.code == 291:
            code = "right"
        elif event.code == 289:
            code = "down"
        elif event.code == 294:
            code = "cross"
        elif event.code == 295:
            code = "circle"
        elif event.code == 292:
            code = "triangle"
        elif event.code == 293:
            code = "square"
        elif event.code == 296:
            code = "select"
        elif event.code == 297:
            code = "start"
        elif event.code == 1:
            code = "center"
        
        if event.value == 127:
            value = 0
        elif event.value == 255:
            value = 1
        else:
            value = event.value


        client.send_message(f"/ddr/{code}", value)