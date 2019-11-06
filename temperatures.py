from serial import Serial
import json
from datetime import datetime


class Temperature():
    """ Temperature given by a sensor
    """

    sensor_id = None
    temperature = None

    def __init__(self,
                 sensor_id: int,
                 temperature: int,
                 timestamp: datetime = None):
        self.sensor_id = sensor_id
        self.temperature = temperature
        self.timestamp = timestamp if timestamp is not None else datetime.now()

    @classmethod
    def from_serial(cls, device: str = '/dev/ttyACM1', baudrate: int = 9600):
        """ reads json data from serial

        :param device: device on which to read
        :param baudrate: speed of reading
        """

        # TODO: device auto-detection
        with Serial(device, baudrate) as serial:
            print(serial.name)
            json_msg = None
            while json_msg is None:
                message = serial.readline()
                print(message)
                try:
                    json_msg = json.loads(message)
                    # TODO: verify that sensor_id and temp are in json
                except ValueError:
                    print("Non-json")


            sensor_id = (int(json_msg['sensor_id'])
                         if 'sensor_id' in json_msg
                         else None)
            temperature = (int(json_msg['temperature'])
                           if 'temperature' in json_msg
                           else None)

            return cls(sensor_id, temperature)

    def to_json(self):
        return {'temperature': self.temperature,
                'sensor_id': self.sensor_id,
                'timestamp': self.timestamp.isoformat()}

    def __str__(self):
        return "sensor: {}, {}°C, {}".format(self.sensor_id, self.temperature,
                self.timestamp)

    def __repr__(self):
        return "Temperature({})".format(str(self))
