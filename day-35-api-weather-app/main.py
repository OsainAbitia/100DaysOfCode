"""Entrypoint for the application."""
from weather_forecast import Forecaster

if __name__ == "__main__":
    forecaster = Forecaster()
    forecaster.get_hourly_forecast()