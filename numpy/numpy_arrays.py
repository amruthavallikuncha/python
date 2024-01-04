
import numpy as np

# Creating NumPy arrays
array_a = np.array([1, 2, 3, 4, 5])
array_b = np.array([[1, 2, 3], [4, 5, 6]])

# Basic NumPy Array Operations
shape_of_array_a = array_a.shape
element_at_index_two = array_a[2]
subset_of_array_a = array_a[1:4]

# Reshaping arrays
reshaped_array_b = array_b.reshape((3, 2))

# Basic mathematical operations
sum_of_arrays = array_a + array_b
elementwise_product = np.multiply(array_a, array_b)

# Aggregation functions
mean_value = np.mean(array_a)
max_value = np.max(array_b)
min_value = np.min(array_a)

# Array broadcasting
broadcasted_sum = array_a + 10

# Advanced NumPy Array Operations
# Creating arrays with arange and linspace
aranged_array = np.arange(1, 10, 2)
linspace_array = np.linspace(0, 1, 5)

# Random number generation
random_array = np.random.rand(3, 3)

# Indexing and slicing
row_slice = array_b[1, :]
column_slice = array_b[:, 2]

# Transposing arrays
transposed_array_b = array_b.T

# Matrix multiplication
matrix_product = np.dot(array_b, reshaped_array_b)

# Universal functions (ufunc)
square_root = np.sqrt(array_a)
exponential = np.exp(array_a)

# Statistical operations
mean_along_axis_1 = np.mean(array_b, axis=1)
std_deviation_along_axis_0 = np.std(array_b, axis=0)

# Stacking arrays
vertical_stack = np.vstack((array_a, array_a))
horizontal_stack = np.hstack((array_b, reshaped_array_b))

# Splitting arrays
split_arrays = np.split(array_a, [2, 4])

# Boolean indexing
even_numbers = array_a[array_a % 2 == 0]

# Broadcasting with different shapes
broadcasted_sum_diff_shapes = array_a[:, np.newaxis] + reshaped_array_b

# Saving and loading arrays
np.save('array_a.npy', array_a)
loaded_array_a = np.load('array_a.npy')

# Creating an identity matrix
identity_matrix = np.eye(3)

# Creating a diagonal matrix
diagonal_matrix = np.diag([1, 2, 3])

# Applying functions element-wise
sin_values = np.sin(array_a)

# Using np.where for conditional operations
conditional_array = np.where(array_a > 3, array_a, 0)
