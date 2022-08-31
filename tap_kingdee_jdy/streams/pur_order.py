import singer
import json
import time
from datetime import datetime
from singer import metadata

from .base import Base

LOGGER = singer.get_logger()

class PurOrder(Base):
    def __init__(self):
        self._start_date = ""
        self._state = {}

    @property
    def name(self):
        return "pur_order"

    @property
    def state(self):
        return self._state
    
    @property
    def specific_api(self):
        return "/pur/pur_order"