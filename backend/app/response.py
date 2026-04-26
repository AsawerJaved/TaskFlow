def response(success: int = 0, message: str = "", data: dict = None, trace: str = "") -> dict:
    """
    Generate a standardized API response in dictionary format.

    Args:
        success (int): 1 if task successful else 0
        message (str): Human-readable message about the response.
        data (dict): Payload data to return.
        trace (str): Optional error/debug trace for failure cases.

    Returns:
        dict: A response dict with success, message, and data.
    """
    if data is None:
        data = {}

    return {
        "success": success,
        "message": message,
        "data": data,
        "trace": trace
    }