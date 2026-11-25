"""Constants for the 4HEAT Lite integration."""

DOMAIN = "4heatlite"
DATA_COORDINATOR = "coordinator"

TCP_PORT = 80
SOCKET_TIMEOUT = 5
SOCKET_BUFFER = 1024

QUERY_SENSORS = '["2WC","1","0310"]'
QUERY_CONFIG = {
    "target_temp": '["2WC","1","0312005a"]',
    "power": '["2WC","1","030e016c"]',
}
QUERY_EXHAUST = '["2WC","1","0312ffff"]'
REGISTER_SENSORS = "10"
REGISTER_EXHAUST = "12ffff"
# Primary air flow, «FL» in the panel's info menu: the board holds it with the
# flue fan and raises Er17/Er41/Er42 when it cannot (Ferlux Iris)
QUERY_AIRFLOW = '["2WC","1","0312ffed"]'
REGISTER_AIRFLOW = "12ffed"
# Fan levels the 4HEAT filemap declares, polled over TCP: data key -> 0e register.
# On a Ferlux the panel's fan setting is not among them (see CONF_FAN_REGISTER).
FAN_REGISTERS = {
    "heating_fan_power": "0e023f",
    "ducted_fan_1": "0e0266",
    "ducted_fan_2": "0e027e",
}

# The module answers ["ERR","1","4"] now and then while busy
QUERY_RETRIES = 2
QUERY_RETRY_DELAY = 1.5
# Failed polls that keep the last data before entities go unavailable
MAX_STALE_POLLS = 2

# Target register max at or below this = whole-degree stove (10-40 vs 100-400)
WHOLE_DEGREE_MAX_RAW = 100

# The module takes one connection at a time and its local server has hung
# (pings fine, port 80 refused until power-cycled): poll gently
DEFAULT_SCAN_INTERVAL = 60
# Fan levels hardly ever change and cost a connection each: read them
# every this many polls
FAN_POLL_EVERY = 10

STATE_NAMES = {
    0: "OFF",
    1: "Check Up",
    2: "Ignition",
    3: "Stabilization",
    4: "Ignition",
    5: "Run",
    6: "Modulation",
    7: "Extinguishing",
    8: "Safety",
    9: "Block",
    10: "Recover Ignition",
    11: "Standby",
    13: "Run M",
    30: "Ignition",
    31: "Ignition",
    32: "Ignition",
    33: "Ignition",
    34: "Ignition",
}

# Alarm codes as the panel shows them (ErNN; 200+ = ELNN, lambda sensor), from the
# board's own table in the 4HEAT cloud model map (Ferlux Iris, SYEVO0000559);
# 1, 2, 7, 8 and 17 worded as the Ferlux manual explains them
ERROR_NAMES = {
    0: "None",
    1: "Safety thermostat",
    2: "Safety pressure switch",
    3: "Low flue temperature",
    4: "Water over-temperature",
    5: "Flue overheating",
    6: "Pellet thermostat",
    7: "Flue fan encoder stopped",
    8: "Flue fan encoder not regulating",
    9: "Minimum water pressure",
    10: "Maximum water pressure",
    11: "Real time clock failure",
    12: "Ignition failed",
    13: "Accidental extinguishing",
    14: "Pressure switch",
    15: "Lack of power supply",
    16: "RS485 communication failure",
    17: "Air flow regulation failed",
    18: "Pellet ended",
    19: "Pellet consent",
    20: "Wood/pellet switch failure",
    21: "Overheating flue probe 2",
    22: "Oxygen regulation failure",
    23: "Probe disconnected",
    24: "Igniter broken",
    25: "Safety engine 1",
    26: "Safety engine 2",
    27: "Safety engine 3",
    28: "Safety engine 4",
    29: "Safety engine 5",
    30: "Overheating air probe",
    31: "Pellet valve closed",
    32: "Water pressure sensor",
    33: "Tube bundle cleaning engine failure",
    34: "Minimum aspiration air",
    35: "Maximum aspiration air",
    36: "Probe reading value out of range",
    37: "Stirrer engine failure",
    38: "Pump failure",
    39: "Air flow sensor failure",
    40: "Service",
    41: "Minimum air flow",
    42: "Maximum air flow",
    43: "Flow switch",
    44: "Door open",
    45: "Limit switch failure",
    46: "Level switch failure",
    47: "Encoder loading engine stopped",
    48: "Encoder loading engine not regulating",
    49: "Combustion alarm",
    50: "Maximum peak alarm",
    51: "Damper position alarm",
    52: "Additional I2C module not communicating",
    53: "Encoder loading engine 2 stopped",
    54: "Encoder loading engine 2 not regulating",
    55: "User maintenance service",
    56: "Plumbing plant changed",
    57: "Forced draught high",
    58: "Overheating oven",
    59: "Condensation",
    60: "Pressureswitch aspiration fan",
    61: "Pressureswitch combustion fan",
    62: "Brazier full",
    63: "Encoder fan 2 broken",
    64: "Encoder fan 2 not regulating",
    65: "Encoder fan 3 broken",
    66: "Encoder fan 3 not regulating",
    68: "Selector",
    79: "Maximum number of pressure switch openings exceeded",
    81: "Motherboard overtemperature",
    200: "Lambda sensor failure",
    201: "Heater sensor shorted to ground",
    202: "Heater sensor disconnected",
    203: "Heater sensor shorted to +12v",
    204: "Lambda sensor shorted to ground",
    205: "Lambda supply voltage low",
    206: "Lambda sensor shorted to +12v",
    207: "Heating sensor timeout",
    208: "Overheated lambda sensor",
}

# Proxy configuration
CONF_DEVICE_ID = "device_id"
CONF_DEVICE_KEY = "device_key"
CONF_MODULE_ADDRESS = "module_address"
CONF_PROXY_MODE = "proxy_mode"
CONF_SCHEDULE_ENABLED = "schedule_enabled"  # v2 migration only
CONF_CACHED_SCHEDULE = "cached_schedule"  # v2 migration only
# The register the panel's fan setting lives in, when it isn't one the filemap
# declares: 0e038c (-7..+7) on a Ferlux SYEVO0000559, whose 0e023f never moves.
# Empty = no fan control.
CONF_FAN_REGISTER = "fan_register"
CONF_ACTIVE_SCHEDULE = "active_schedule"
CONF_CACHED_SCHEDULES = "cached_schedules"
NUM_SCHEDULE_SLOTS = 3
PROXY_MODE_DIRECT = "direct"
PROXY_MODE_LOCAL = "local_only"
PROXY_MODE_KEEPALIVE = "cloud_keepalive"

AZURE_HTTPS_BASE = "https://wifi4heat.azurewebsites.net"
CONF_PROXY_LOG_LEVEL = "proxy_log_level"
CONF_PROXY_DEBUG = "proxy_debug"  # v0.9.92 migration only
LOG_LEVEL_WARNING = "warning"
LOG_LEVEL_INFO = "info"
LOG_LEVEL_DEBUG = "debug"
PROXY_POLL_INTERVAL = 120

STORE_REGISTERS = {
    "12ffff": {"key": "exhaust_temp_store", "group": "12", "scale": 1},
    "12fff7": {"key": "room_temp_store", "group": "12", "temp": True},
    "12ffe0": {"key": "remote_room_temp", "group": "12", "temp": True},
    "12ffe8": {"key": "remote_room_temp_2", "group": "12", "temp": True},
    "12ffed": {"key": "airflow", "group": "12", "scale": 1},
    "12ffde": {"key": "cleaning_counter", "group": "12", "scale": 1},
    "12ffdf": {"key": "service_counter", "group": "12", "scale": 1},
    "12005a": {"key": "target_temp", "group": "12", "temp": True},
    "120058": {"key": "reg_120058", "group": "12", "scale": 1},
    "120059": {"key": "reg_120059", "group": "12", "scale": 1},
    "0e016c": {"key": "power", "group": "0e"},
    "0e023f": {"key": "heating_fan_power", "group": "0e"},
    "0e0266": {"key": "ducted_fan_1", "group": "0e"},
    "0e027e": {"key": "ducted_fan_2", "group": "0e"},
    "0e0231": {"key": "reg_0e0231", "group": "0e"},
    "0c81": {"key": "module_info", "group": "0c"},
}

# Schedule constants
QUERY_SCHEDULE = '["CCG","0"]'
MINUTES_PER_DAY = 1440
DAY_NAMES = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
DAY_OFFSETS = {name: i * MINUTES_PER_DAY for i, name in enumerate(DAY_NAMES)}
BAND_NAMES = ["off", "eco", "comfort", "comfort2"]
TEMP_SCALE = 10
SERVICE_GET_SCHEDULE = "get_schedule"
SERVICE_SET_SCHEDULE = "set_schedule"

# Write command constants
WRITE_FUNCTION = "05"
REGISTER_TEMP = "12005a"
REGISTER_POWER = "0e016c"
TEMP_MIN_RAW = 0x0064
TEMP_MAX_RAW = 0x0190
TEMP_WRITE_SUFFIX = "0001000100"
