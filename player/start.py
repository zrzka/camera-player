import time
import os
import subprocess
import sys

from avahi.service import AvahiService

SERVICE_NAME = os.getenv("SERVICE_NAME", "Camera Player")
SERVICE_TYPE = os.getenv("SERVICE_TYPE", "_cameraplayer._udp")
SERVICE_PORT = int(os.getenv("SERVICE_PORT", 5000))

OMX_PLAYER_CMD = [
    "/usr/bin/omxplayer",
    "--no-osd",
    "--no-keys",
    "--timeout", "0",
    "--win", "0,0,800,480",
    "--display", "4",
    "--fps", "10",
    "--refresh",
    "--threshold", "1",
    "--orientation", "180",
    "udp://@:{}".format(SERVICE_PORT)
]


def announce_player_service():
    print("Registering service {}".format(SERVICE_NAME))
    print(" - type: {}".format(SERVICE_TYPE))
    print(" - port: {}".format(SERVICE_PORT))
    service = AvahiService(SERVICE_NAME, SERVICE_TYPE, SERVICE_PORT)
    print("Service registered ...")
    return service


def launch_omx_player():
    print("Launching omxplayer...")
    player = subprocess.Popen(
        OMX_PLAYER_CMD, stdout=sys.stdout, stderr=sys.stderr)
    print("omxplayer launched ...")
    return player


def main():
    player = launch_omx_player()
    _ = announce_player_service()
    player.wait()

    print("omxplayer did exit with {} return code".format(player.returncode))
    sys.exit(player.returncode)


if __name__ == "__main__":
    main()
