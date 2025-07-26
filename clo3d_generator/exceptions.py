
class CLO3DError(Exception):
    """Base exception for CLO3D API errors."""
    pass

class DesignNotFoundError(CLO3DError):
    """Raised when a design ID is not found."""
    pass

class APIError(CLO3DError):
    """Raised when the API returns an error."""
    pass