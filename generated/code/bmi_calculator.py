def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """Return Body Mass Index given weight and height."""
    return weight_kg / (height_cm / 100) ** 2
