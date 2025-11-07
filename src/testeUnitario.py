import time
from typing import Any

def get_time_taken() -> Any:
    initial_time = time.perf_counter()
    end_time = time.perf_counter()
    teste = end_time - initial_time