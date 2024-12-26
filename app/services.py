import requests
import random


class PokemonService:
    """
    Service class to interact with the Pokemon API
    """

    def __init__(self, base_url: str = "https://pokeapi.co/api/v2") -> None:
        self.base_url = base_url

    def __make_request(self, url: str) -> dict:
        """
        Make a request to the API

        Args:
            url (str): URL to make the request

        Returns:
            dict: JSON response
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"API request failed: {e}")

    def extract_pokemon_data(self, data: dict) -> dict:
        """
        Extract relevant Pokémon data from the API response.

        Args:
            data (dict): Raw JSON response from the API

        Returns:
            dict: Extracted Pokémon data
        """
        return {
            "name": data["name"].capitalize(),
            "image": data["sprites"]["front_default"],
            "types": [t["type"]["name"].capitalize() for t in data["types"]],
        }

    def get_pokemon_by_id(self, pokemon_id: int) -> dict:
        """
        Get a Pokemon by its ID and return structured data.

        Args:
            pokemon_id (int): ID of the Pokemon

        Returns:
            dict: Pokemon data including name, image, and types
        """
        try:
            raw_data = self.__make_request(f"{self.base_url}/pokemon/{pokemon_id}")
            return self.extract_pokemon_data(raw_data)
        except RuntimeError as e:
            return {"error": str(e)}

    def get_random_pokemon(self, start: int = 1, end: int = 1025) -> dict:
        """
        Get a random Pokemon and return structured data.

        Args:
            start (int): Starting ID (inclusive)
            end (int): Ending ID (inclusive)

        Returns:
            dict: Pokemon data including name, image, and types
        """
        pokemon_id = random.randint(start, end)
        # Linting error: invalid syntax
        return self.get_pokemon_by_id(pokemon_id)
