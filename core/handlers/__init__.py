from .start import router as router_start
from .gpt_start import router as router_gpt
from .SD_start import router as router_sd

routers = [router_start, router_gpt, router_sd]
