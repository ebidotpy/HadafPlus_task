import arabic_reshaper
from bidi.algorithm import get_display

def reshape_persian_text(text: str) -> str:
    """Reshape Persian text for proper display."""
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)
