import numpy as np
import matplotlib.pyplot as plt
import webbrowser










def numpy_basics():
    # np.array()
    # np.shape
    # np.dtype
    # np.zeros()
    # np.ones()
    # np.eye()
    # np.range()
    array1 = np.array([2, 3, 4, 5])
    print(f"array: {array1}  shape: {array1.shape}  type: {array1.dtype}\n")

    array2 = np.zeros(5)
    print(f"array: {array2}  type:{array2.dtype}\n")

    array3 = np.ones([5, 5])
    print(f"array of ones given shape: {array3}\n")

    # identity matrix
    array4 = np.eye(5)
    print(f"identity matrix: {array4}\n")

    # range
    array5 = np.arange(5)
    array6 = np.arange(5, 50, 2)  # (start, stop, step)
    print(f"range: {array5}\n start/stop range: {array6}")
    return

def numpy_arrays_scalars():
    array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(array1 * array1)
    print()
    print(1 / array1)
    print()
    print(array1 ** 3)
    return

def numpy_array_indexing():
    array1 = np.arange(0, 11)
    print(array1)
    print(array1[1:5])
    array1[0:5] = 100
    print(array1)
    array1 = np.arange(0,11)
    print(array1)
    slice1 = array1[0:6]
    print(slice1)
    slice1[:] = 99 # changing slice of an array changes original array values too
    print(slice1)
    print(array1)
    array_copy = array1.copy()
    print(array_copy)

    array_2d = np.array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))
    print(array_2d)
    print(array_2d[:2, 1:])

    array_2d = np.zeros((10, 10))
    print(array_2d)
    length = array_2d.shape[0]
    print(length)
    for i in range(length):
        array_2d[i] = i
    print(array_2d)
    print(array_2d[[6, 4, 2, 7]])
    return

def numpy_array_transposition():
    arr = np.arange(50).reshape((10, 5))
    print(arr)
    print("Transposed")
    print(arr.T)
    print("product of transposed arrays")
    print(np.dot(arr.T, arr))

    arr3d = np.arange(50).reshape((5, 5, 2))
    print(arr3d)
    print(arr3d.transpose(1, 0, 2))
    return

    arr = np.array([[1, 2, 3]])
    print(arr)
    arr.swapaxes(0, 1)
    print(arr)

def universal_array_functions():
    # np.random.randn()
    # np.add()
    # np.sqrt()
    # np.exp()
    # np.maximum()
    arr = np.arange(11)
    print(np.sqrt(arr))
    print(np.exp(arr))
    arr1 = np.random.randn(10)
    print(arr)
    arr2 = np.random.randn(10)
    print(np.add(arr1, arr2))
    return

def open_web_url():
    website = "https://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs"
    webbrowser.open(website)
    return

def main():
    # open_web_url()
    # numpy_basics()
    # numpy_arrays_scalars()
    # numpy_array_indexing()
    # numpy_array_transposition()
    # universal_array_functions()
    array_processing
    return



if __name__ == "__main__":
    main()
