def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if not matrix or not matrix[0]:
		return []
	
	if mode == 'row':
		return [sum(row) / len(row) for row in matrix]
	elif mode == 'column':
		return [sum(col) / len(matrix) for col in zip(*matrix)]
	else:
		raise ValueError(f"Невалиден режим: {mode}. Очаква се 'row' или 'column'.")