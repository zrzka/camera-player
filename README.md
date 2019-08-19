# Camera player

* Announces `_cameraplayer._udp` service (port `5000` by default)
* Utilizes `omxplayer` to play video stream from the `raspivid` on another device
  * Check the [camera streamer](https://github.com/zrzka/camera-streamer) project

The mDNS/Avahi/Bonjour part (`mdns/avahi` folder) is copy & paste of the same folder
from the [balena-avahi-dbus](https://github.com/balena-io-playground/balena-avahi-dbus)
repository.

## Deployment

This project is ready to be deployed to the [balenaCloud](https://www.balena.io/cloud).

```sh
balena push $YOUR_APP_NAME
```

## Hardware

* Raspberry Pi 3 B+
* Official Pi 7" display

## Fleet configuration variables

* `BALENA_HOST_CONFIG_gpu_mem_1024=448`
* `BALENA_HOST_CONFIG_gpu_mem_256=192`
* `BALENA_HOST_CONFIG_gpu_mem_512=256`
* `BALENA_HOST_CONFIG_start_x=1`
