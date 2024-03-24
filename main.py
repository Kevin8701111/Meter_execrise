def fetch_voltage(address):
    return 220

def fetch_amperage(address):
    return 32.0

def fetch_active_power(address):
    return 1222.4

def fetch_frequency(address):
    return 59.2

def fetch_power_factor(address):
    return 0.81



class Meter():
    def __init__(self, ip, model, phase, address) -> None:
        self.ip = ip
        self.model = model
        self.phase = phase
        self.address = address

    def get_voltage(self):
        if self.address == 0x1001:
            voltage = fetch_voltage(self.address)
            return voltage

    def get_voltage(self):
        if self.address == 0x1008:
            amperage = fetch_amperage(self.address)
            return amperage

    def get_voltage(self):
        if self.address == 0x1010:
            active_power = fetch_active_power(self.address)
            return active_power

    def get_voltage(self):
        if self.address == 0x101D:
            frequency = fetch_frequency(self.address)
            return frequency

    def get_voltage(self):
        if self.address == 0x101C:
            power_factor = fetch_power_factor(self.address)
            return power_factor



meter_A1 = Meter(ip = '10.0.0.123', model= '123', phase=3, address=0x101C)

meter_A1.get_voltage()
print(meter_A1.get_voltage())
