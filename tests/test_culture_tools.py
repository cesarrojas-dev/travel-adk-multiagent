from travel_assistant.tools.culture_tools import get_local_culture_info


def test_culture_info_for_cusco():
    result = get_local_culture_info("Cusco")

    assert result["status"] == "success"
    assert "Cuy chactado" in result["typical_dishes"]
    assert len(result["local_customs"]) >= 1
    assert "Sulpayki" in result["useful_phrases"]


def test_culture_info_accepts_accent_and_case():
    result = get_local_culture_info("  PARÍS ")

    assert result["status"] == "success"
    assert "Bonjour" in result["useful_phrases"]


def test_culture_info_unknown_destination():
    result = get_local_culture_info("Tokio")

    assert result["status"] == "not_found"


def test_culture_info_empty_destination():
    result = get_local_culture_info("   ")

    assert result["status"] == "error"
