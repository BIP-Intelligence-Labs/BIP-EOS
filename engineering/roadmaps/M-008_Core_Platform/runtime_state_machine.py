from enum import Enum

class RuntimeState(Enum):
    CREATED='created'
    BOOTING='booting'
    RUNNING='running'
    STOPPING='stopping'
    STOPPED='stopped'
