import pynvml

pynvml.nvmlInit()


def getFanSpeed(gpu_index: int) -> int:
    """Returns the current fan speed percentage for the specified GPU index."""
    try:
        handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_index)
        fan_speed = pynvml.nvmlDeviceGetFanSpeed(handle)
        return fan_speed  # Already returns as percentage (0-100)
    except pynvml.NVMLError as error:
        print(f"Failed to get fan speed for GPU {gpu_index}: {error}")
        raise  # Re-raise the exception so the caller can handle it


def getTotalDevices() -> int:
    return pynvml.nvmlDeviceGetCount()


def getDeviceName(gpu_index: int) -> str:
    """Retorna o nome da GPU especificada pelo índice."""
    try:
        handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_index)
        name = pynvml.nvmlDeviceGetName(handle)
        return name
    except pynvml.NVMLError as error:
        print(f"Failed to get device name for GPU {gpu_index}: {error}")
        raise  # Re-levanta a exceção para que o chamador possa lidar com ela


def getGpuTemperature(gpu_index: int) -> int:
    """Retorna a temperatura da GPU especificada pelo índice."""
    try:
        handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_index)
        temperature = pynvml.nvmlDeviceGetTemperature(
            handle, pynvml.NVML_TEMPERATURE_GPU
        )
        return temperature
    except pynvml.NVMLError as error:
        print(f"Failed to get temperature for GPU {gpu_index}: {error}")
        raise  # Re-levanta a exceção para que o chamador possa lidar com ela


def setFanDuty(
    currentTemp: int, targetTemps: list[int], targetDuties: list[int]
) -> int:
    if not targetTemps or not targetDuties or len(targetTemps) != len(targetDuties):
        raise ValueError(
            "The targetTemps and targetDuties lists must have the same length and cannot be empty."
        )

    if currentTemp <= targetTemps[0]:
        return targetDuties[0]

    for i in range(1, len(targetTemps)):
        if targetTemps[i - 1] < currentTemp <= targetTemps[i]:
            return targetDuties[i]

    return targetDuties[-1]


if __name__ == "__main__":
    # print(getNvidiaBoardsPresent())
    # print("")
    pass
