# NCM_DAQ

- This project serves as reference on connecting an NI-DAQ to a QT application for real-time plotting and logging.
- This project will uses the following packages
    - `nidaqmx`
    - `pyqt5`
    - `pyqtgraphs`
    - `pydantic`
    - `numpy`
    - ``

- Install the requirements with

## Mqtt Topics

| Topic                  | Desc.                            |
| ---------------------- | -------------------------------- |
| NCM/Experiment         | experiment control base function |
| NCM/Experiment/Start   | start experiment                 |
| NCM/Experiment/Stop    | stop experiment                  |
| NCM/Experiment/Rename  | rename experiment                |
| NCM/Experiment/Elapsed | elapsed time of the experiment   |
| NCM/DisplayData        | display data topic               |

### Display Data JSON

```json
{
    "Ultra_Sonic_Distance": { "LL": 0.0, "LQ": 0.0, "RR": 0.0, "RQ": 0.0 },
    "Anemometer": { "LL": 0.0, "LQ": 0.0, "RR": 0.0, "RQ": 0.0 },
    "Standing_Wave": { "Left": 0.0, "Right": 0.0 }
}
```
