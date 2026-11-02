from unittest.mock import patch

from travel_assistant.tools.search_tools import search_web


def test_search_web_empty_query():
    result = search_web("   ")

    assert result["status"] == "error"


def test_search_web_success():
    fake = [{"title": "Cusco", "href": "https://example.com", "body": "Info de Cusco"}]

    with patch("travel_assistant.tools.search_tools.DDGS") as mock_ddgs:
        mock_ddgs.return_value.text.return_value = fake
        result = search_web("Cusco turismo")

    assert result["status"] == "success"
    assert result["results"][0]["url"] == "https://example.com"


def test_search_web_no_results():
    with patch("travel_assistant.tools.search_tools.DDGS") as mock_ddgs:
        mock_ddgs.return_value.text.return_value = []
        result = search_web("consulta sin resultados")

    assert result["status"] == "not_found"


def test_search_web_network_error():
    with patch("travel_assistant.tools.search_tools.DDGS") as mock_ddgs:
        mock_ddgs.return_value.text.side_effect = RuntimeError("sin red")
        result = search_web("Cusco")

    assert result["status"] == "error"
    assert "failed" in result["message"].lower()
