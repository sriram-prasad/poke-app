import unittest
from unittest.mock import patch, Mock
from app.services import PokemonService


class TestPokemonService(unittest.TestCase):
    """
    Unit tests for the PokemonService class
    """

    @patch("app.services.requests.get")
    def test_get_pokemon_by_id_success(self, mock_get):
        """
        Test get_pokemon_by_id when the API call is successful.

        This test verifies that the service correctly processes and returns
        Pokémon data when the API returns a valid response.

        Args:
            mock_get (Mock): The mocked requests.get function.

        Mock Behavior:
            - The API returns a JSON response with Pokémon details (name, sprites, types).

        Asserts:
            - The returned Pokémon name is capitalised correctly.
            - The image URL matches the mock response.
            - The Pokémon's type list contains the correct types.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "pikachu",
            "sprites": {"front_default": "image_url"},
            "types": [{"type": {"name": "electric"}}],
            "ndex": "#0025",
        }
        mock_get.return_value = mock_response

        service = PokemonService()
        result = service.get_pokemon_by_id(25)

        self.assertEqual(result["name"], "Pikachu")
        self.assertEqual(result["image"], "image_url")
        self.assertIn("Electric", result["types"])
        self.assertEqual(result["ndex"], "#0025")

    @patch("app.services.requests.get")
    def test_get_pokemon_by_id_failure(self, mock_get):
        """
        Test get_pokemon_by_id when the API call fails.

        This test verifies that the service handles API errors gracefully
        by returning a structured error message.

        Args:
            mock_get (Mock): The mocked requests.get function.

        Mock Behavior:
            - The API raises a RuntimeError due to a failed request.

        Asserts:
            - The returned response contains an 'error' key.
        """
        mock_get.side_effect = RuntimeError("API request failed: 404 Not Found")

        service = PokemonService()
        result = service.get_pokemon_by_id(9999)  # Invalid ID

        self.assertIn("error", result)

    @patch("app.services.requests.get")
    def test_get_random_pokemon(self, mock_get):
        """
        Test get_random_pokemon to fetch and process a random Pokémon.

        This test verifies that the service fetches and processes a random
        Pokémon's data correctly using the mocked API.

        Args:
            mock_get (Mock): The mocked requests.get function.

        Mock Behavior:
            - The API returns a JSON response with Pokémon details (name, sprites, types).

        Asserts:
            - The returned Pokémon name is capitalised correctly.
            - The image URL matches the mock response.
            - The Pokémon's type list contains all expected types.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "bulbasaur",
            "sprites": {"front_default": "image_url"},
            "types": [{"type": {"name": "grass"}}, {"type": {"name": "poison"}}],
            "ndex": "#0001",
        }
        mock_get.return_value = mock_response

        service = PokemonService()
        result = service.get_random_pokemon()

        self.assertEqual(result["name"], "Bulbasaur")
        self.assertEqual(result["image"], "image_url")
        self.assertIn("Grass", result["types"])
        self.assertIn("Poison", result["types"])
        self.assertEqual(result["ndex"], "#0001")
