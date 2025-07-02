def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """Return Body Mass Index given weight and height.

    Parameters
    ----------
    weight_kg : float
        Weight in kilograms.
    height_cm : float
        Height in centimeters.

    Returns
    -------
    float
        The calculated BMI.
    """
    return weight_kg / (height_cm / 100) ** 2
