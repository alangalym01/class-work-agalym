def cm_squared_to_m_squared(cm_squared):
    """
    Convert centimeters squared to meters squared

    Parameters:
        (float) value in cm^2
    
    Output
        (float) value in m^2
    """
    return cm_squared * 0.0001

def m_squared_to_cm_squared(m_squared):
    """
    Convert meters squared to centimeters squared

    Parameters:
        (float) value in m^2
    
    Output
        (float) value in cm^2
    """
    return m_squared * 10000

def compare_areas(shape1, shape2):
    """
    Compare areas of two shapes

    Parameters:
        (float) area of shape 1
        (float) area of shape 2
    
    Output
        "Shape __ is bigger"
    """
    return "Shape 1 is bigger" if shape1 > shape2 else "Shape 2 is bigger"