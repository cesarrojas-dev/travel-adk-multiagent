"""Tool de búsqueda web usada por el WebSearchAgent cuando Google Search no está disponible."""

from ddgs import DDGS


def search_web(query: str, max_results: int = 5) -> dict:
    """Search the web and return a short list of results.

    Args:
        query: Search text, for example "Cusco clima julio turismo".
        max_results: Maximum number of results to return (1 to 10).

    Returns:
        Dictionary with the status and a list of results (title, url, snippet).
    """
    if not query or not query.strip():
        return {"status": "error", "message": "The search query cannot be empty."}

    max_results = max(1, min(int(max_results), 10))

    try:
        raw_results = DDGS().text(query.strip(), max_results=max_results)
    except Exception as error:  # noqa: BLE001 - la red puede fallar de muchas formas
        return {"status": "error", "message": f"Web search failed: {error}"}

    results = [
        {
            "title": item.get("title", ""),
            "url": item.get("href", ""),
            "snippet": item.get("body", ""),
        }
        for item in raw_results
    ]

    if not results:
        return {"status": "not_found", "query": query, "results": []}

    return {"status": "success", "query": query, "results": results}
