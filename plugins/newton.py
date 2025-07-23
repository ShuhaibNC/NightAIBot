import json
import urllib.parse
import urllib.request

BASE_URL = 'https://newton.vercel.app/api/v2/'

def math_request(operation: str, expression: str):
    """
    Sends a request to Newton API v2 with given operation and expression.
    
    :param operation: One of the supported operations like 'simplify', 'derive'
    :param expression: The math expression as a string
    :return: Result from the API or error message
    """
    url = f"{BASE_URL}{operation}/{urllib.parse.quote(expression)}"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())

            # Return the 'result' field
            return data.get("result", "No result found.")
    except Exception as e:
        return f"Error: {e}"
