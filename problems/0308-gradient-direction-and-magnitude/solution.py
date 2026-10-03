import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	grad_arr = np.array(gradient, dtype=float)
	magnitude = float(np.linalg.norm(grad_arr))
	
	if magnitude == 0.0:
		direction = np.zeros_like(grad_arr).tolist()
		descent_direction = np.zeros_like(grad_arr).tolist()
	else:
		direction_arr = grad_arr / magnitude
		direction = direction_arr.tolist()        
		descent_direction = (-direction_arr).tolist()
    
	return {
        'magnitude': magnitude,
        'direction': direction,
        'descent_direction': descent_direction
    }