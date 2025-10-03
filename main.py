#! /usr/bin/env python3

from numpy import sin
from NI_DAQ.GenericMqtteLogger import initialize_logging
from NI_DAQ.DAQ import DAQ
from Constants import DAQConfig, LoggerConfig, MQTTConfig
import logging
import sys, signal

import subprocess
from multiprocessing import Event


add_cmd = ["nidaqmxconfig", "--add-net-dev", "cDAQ9185-2304EC6.local"]
reserve_cmd = ["nidaqmxconfig", "--reserve", "cDAQ9185-2304EC6"] 
unreserve_cmd = ["nidaqmxconfig", "--unreserve" "cDAQ9185-2304EC6"]

stop_event = Event()

def handle_signal(*args):
    logging.debug("Exiting")
    stop_event.set()
    res = subprocess.run(unreserve_cmd)


if __name__ == "__main__":

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGHUP, handle_signal)

    mqtt_config = MQTTConfig()

    # do the nidaqmx config and reserve
    initialize_logging(
        process_name="Main", broker=mqtt_config.host_name, port=mqtt_config.host_port
    )
    
    logging.debug(f"[Main] Main initialized. ")

    res = subprocess.run(add_cmd)

    if not res.returncode:
        logging.debug(f"[MAIN] added daq")

    else: 
        logging.error(f"Could not add DAQ")
        exit(1)

    res = subprocess.run(reserve_cmd)

    if not res.returncode:
        logging.debug(f"[Main] reserved DAQ")
    else :
        logging.error(f"[Main] could not reserve daq")
        exit(1)


    logging.debug(f"[Main] Starting DAQ Process")
    daq_logger = LoggerConfig(log_name="DAQ", mqtt_config=mqtt_config)
    DAQ.run(daq_logger, stop_event)
