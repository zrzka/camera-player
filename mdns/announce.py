import time
import os

from avahi.service import AvahiService

SERVICE_NAME = os.getenv("SERVICE_NAME", "Camera Player")
SERVICE_TYPE = os.getenv("SERVICE_TYPE", "_cameraplayer._udp")
SERVICE_PORT = int(os.getenv("SERVICE_PORT", 5000))

if __name__ == "__main__":
    print("Registering service {}".format(SERVICE_NAME))
    print(" - type: {}".format(SERVICE_TYPE))
    print(" - port: {}".format(SERVICE_PORT))
    avahiservice = AvahiService(SERVICE_NAME, SERVICE_TYPE, SERVICE_PORT)
    print("Service registered ...")
    print("Infinite loop to avoid container restart & keep alive...")
    while True:
        time.sleep(1)
