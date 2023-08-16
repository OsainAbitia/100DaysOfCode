"""Pixela API Configuration"""
import requests


class Pixela:
    """Main class"""

    def __init__(self) -> None:
        self.pixela_endpoint = "https://pixe.la/v1"

    def create_user(self, username: str, token: str) -> requests.Response:
        """Create a new user.
        
        Inputs:
        
        username: Alphanumeric string value on lowercase
        token: Alphanumeric string value from 8 to 32 characters
        
        Returns:
        
        requests.Response
        """
        user_endpoint = f"{self.pixela_endpoint}/users"
        user_params = {
            "token": token,
            "username": username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }
        
        response = requests.post(url=user_endpoint, json=user_params)
        print(response.text)
        return response

    def create_graph_definition(self, username: str, token: str, graph_id: str) -> requests.Response:
        """Create a new graph definition"""
        graph_definition_endpoint = f"{self.pixela_endpoint}/users/{username}/graphs"
        graph_definition_params = {
            "id": graph_id,
            "name": "Gym attendance",
            "unit": "days",
            "type": "int",
            "color": "sora"
        }

        headers = {
            "X-USER-TOKEN": token
        }

        response = requests.post(url=graph_definition_endpoint, json=graph_definition_params, headers=headers)
        print(response.text)
        return response
    
    def create_pixel(self, username: str, token: str, graph_id: str, date: str) -> requests.Response:
        """Put a pixel"""
        put_pixel_endpoint = f"{self.pixela_endpoint}/users/{username}/graphs/{graph_id}"

        put_pixel_params = {
            "date": date,
            "quantity": "1"
        }

        headers = {
            "X-USER-TOKEN": token
        }

        response = requests.post(url=put_pixel_endpoint, json=put_pixel_params, headers=headers)
        print(response.text)
        return response
    
    def put_pixel(self, username: str, token: str, graph_id: str, date: str, quantity: str) -> requests.Response:
        """Put a pixel"""
        put_pixel_endpoint = f"{self.pixela_endpoint}/users/{username}/graphs/{graph_id}/{date}"

        put_pixel_params = {
            "quantity": quantity
        }

        headers = {
            "X-USER-TOKEN": token
        }

        response = requests.put(url=put_pixel_endpoint, json=put_pixel_params, headers=headers)
        print(response.text)
        return response
    
    def delete_pixel(self, username: str, token: str, graph_id: str, date: str) -> requests.Response:
        """Delete a pixel"""
        delete_pixel_endpoint = f"{self.pixela_endpoint}/users/{username}/graphs/{graph_id}/{date}"

        headers = {
            "X-USER-TOKEN": token
        }

        response = requests.delete(url=delete_pixel_endpoint, headers=headers)
        print(response.text)
        return response
    
    