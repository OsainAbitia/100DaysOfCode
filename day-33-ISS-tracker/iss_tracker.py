"""Track and compare International Space Station location and compare with user's location."""
import requests
from datetime import datetime

class ISSTracker():
    """Initialize ISSTracker class."""
    
    def __init__(self) -> None:
        """Initialize current time and location."""
        self.my_lat = 24.023161
        self.my_long = -104.671242
        self.current_time = datetime.now()

    def get_location(self) -> dict:
        """Get location from ISS API address."""
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        location = {
            "latitude": float(data["iss_position"]["latitude"]),
            "longitude": float(data["iss_position"]["longitude"])
        }
        return location
    
    def is_above_me(self) -> bool:
        """Check if ISS is above user's location."""
        iss_location = self.get_location()
        min_lat, max_lat = self.my_lat - 5, self.my_lat + 5
        min_long, max_long = self.my_long - 5, self.my_long + 5

        if iss_location["latitude"] < max_lat and iss_location["latitude"] > min_lat  \
        and iss_location["longitude"] < max_long and iss_location["longitude"] > min_long:
            return True
        else:
            return False
        
    def is_visible(self) -> bool:
        """Check if current user's location is night time."""
        parameters = {
            "lat": self.my_lat,
            "lon": self.my_long,
            "formatted": 0
        }
        response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        if self.current_time.hour < sunrise or self.current_time.hour > sunset:
            return True
        else:
            return False

