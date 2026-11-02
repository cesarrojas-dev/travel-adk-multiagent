"""Tool del LocalCultureAgent: datos culturales básicos por destino."""

_CULTURE_DATA = {
    "cusco": {
        "dishes": ["Cuy chactado", "Chiri uchu", "Adobo cusqueño", "Sopa de quinua"],
        "customs": [
            "Saludar con un 'buenos días' o 'buenas tardes' al entrar a un lugar.",
            "Pedir permiso antes de fotografiar a las personas en trajes típicos.",
            "Masticar hoja de coca o tomar mate es habitual para la altura.",
        ],
        "phrases": {
            "Allillanchu": "¿Cómo estás? (quechua)",
            "Sulpayki": "Gracias (quechua)",
            "Imaynalla": "Hola, ¿qué tal? (quechua)",
        },
    },
    "arequipa": {
        "dishes": ["Rocoto relleno", "Adobo arequipeño", "Chupe de camarones", "Soltero de queso"],
        "customs": [
            "Los almuerzos son largos y se consideran el momento principal del día.",
            "La gente se enorgullece de su ciudad; preguntar por su historia es bien visto.",
        ],
        "phrases": {
            "Buenas": "Saludo corto y común",
            "Gracias, caserito": "Trato amable al vendedor",
        },
    },
    "buenos aires": {
        "dishes": ["Asado", "Empanadas", "Milanesa", "Dulce de leche"],
        "customs": [
            "Es común saludar con un beso en la mejilla.",
            "Las cenas suelen empezar tarde, después de las 21:00.",
            "La propina habitual en restaurantes es cerca del 10%.",
        ],
        "phrases": {
            "Che": "Forma informal de llamar la atención",
            "¿Me trae la cuenta?": "Para pedir la cuenta",
            "Mate": "Infusión que se comparte en grupo",
        },
    },
    "paris": {
        "dishes": ["Croissant", "Croque-monsieur", "Ratatouille", "Crème brûlée"],
        "customs": [
            "Decir 'Bonjour' al entrar a una tienda es casi obligatorio.",
            "Intentar hablar un poco de francés antes de pasar al inglés.",
            "El servicio suele estar incluido en la cuenta.",
        ],
        "phrases": {
            "Bonjour": "Buenos días",
            "Merci": "Gracias",
            "S'il vous plaît": "Por favor",
            "L'addition, s'il vous plaît": "La cuenta, por favor",
        },
    },
}

_ALIASES = {"parís": "paris", "paris, francia": "paris"}


def get_local_culture_info(destination: str) -> dict:
    """Return typical dishes, local customs and useful phrases for a destination.

    Args:
        destination: Name of the city or place the traveler will visit.

    Returns:
        Dictionary with dishes, customs and phrases, or an error if unknown.
    """
    key = destination.lower().strip()
    key = _ALIASES.get(key, key)

    if not key:
        return {"status": "error", "message": "The destination cannot be empty."}

    for name, data in _CULTURE_DATA.items():
        if name in key:
            return {
                "status": "success",
                "destination": destination,
                "typical_dishes": data["dishes"],
                "local_customs": data["customs"],
                "useful_phrases": data["phrases"],
            }

    return {
        "status": "not_found",
        "destination": destination,
        "message": "No local data for this destination. Use general knowledge and verify it.",
    }
