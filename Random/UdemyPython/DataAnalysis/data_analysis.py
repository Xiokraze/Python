import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import webbrowser

def open_web_url():
    website = "https://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs"
    webbrowser.open(website)
    return

# numpy
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

def array_processing():
    # np.meshgrid
    # np.where()
    # np.unique()
    # np.in1d()
    # plt.imshow()
    # plt.colorbar()
    # plt.title()
    # plt.show()
    # zip()
    # array.sum()
    # array.mean()
    # array.std()
    # array.var()  variance
    # array.any()  true if any value is true
    # array.all()  true only if all values are true
    # array.sort()
    points = np.arange(-5, 5, 0.01)
    dx, dy = np.meshgrid(points, points)
    z = (np.sin(dx) + np.sin(dy))
    plt.imshow(z)
    plt.colorbar()
    plt.title("Plot for sin(x) + sin(y)")
    plt.show()


    A = np.array([1, 2, 3, 4])
    B = np.array([100, 200, 300, 400])
    condition = np.array([True, True, False, False])
    # list comprehension
    answer = [(A_val if cond else B_val) for A_val, B_val, cond in zip(A, B, condition)]
    print(answer)
    # same as above, but replacing comprehension with where
    answer2 = np.where(condition, A, B)
    print(answer2)

    from numpy.random import randn
    arr = randn(5, 5)
    answer3 = np.where(arr<0, 0, arr)
    print(answer3)

    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(arr.sum())
    print(arr.sum(0))
    print(arr.mean())
    print(arr.std())
    print(arr.var())
    bool_arr = np.array([True, False, True])
    print(bool_arr.any())
    print(bool_arr.all())

    arr = randn(5)
    print(arr)
    arr.sort()
    print(arr)

    countries = np.array(["France", "Germany", "USA", "Russia", "USA", "Mexico", "Germany"])
    print(np.unique(countries))
    print(np.in1d(["France", "USA", "Sweden"], countries))
    return

def array_input_output():
    # np.save()
    # np.load() "file.npy"
    # np.savez() "file.npz"
    # np.savetxt()
    # np.loadtxt()
    arr = np.arange(5)
    np.save("myarray", arr)
    arr = np.arange(10)
    print(arr)
    saved_arr = np.load("myarray.npy")
    print(saved_arr)

    # save multiple arrrays to a zip file
    arr1 = np.load("myarray.npy")
    arr2 = arr
    np.savez("ziparray.npz", x=arr1, y=arr2)
    arrays = np.load("ziparray.npz")
    print(arrays["x"])
    print(arrays["y"])

    arr = np.array([[1, 2, 3], [4, 5, 6]])
    np.savetxt("mytextarray.txt", arr, delimiter=',')
    arr = np.loadtxt("mytextarray.txt", delimiter=',')
    print(arr)
    return

def numpy_basics():
    # open_web_url()
    # numpy_basics()
    # numpy_arrays_scalars()
    # numpy_array_indexing()
    # numpy_array_transposition()
    # universal_array_functions()
    # array_processing()
    # array_input_output()
    return

 # pandas
def pandas_series():
    obj = Series([3, 6, 9, 12])
    print(obj)
    print(obj.values)
    print(obj.index)

    ww2_cas = Series([8700000, 4300000, 3000000, 2100000, 400000], index=["USSR", "Germany", "China", "Japan", "USA"])
    print(ww2_cas)
    print(ww2_cas["USA"])
    # countries with casualties > 4 million
    print(ww2_cas[ww2_cas > 4000000])
    print("USSR" in ww2_cas)

    ww2_dict = ww2_cas.to_dict()
    print(ww2_dict)
    ww2_series = Series(ww2_dict)
    print(ww2_series)

    countries = ["China", "Germany", "Japan", "USA", "USSR", "Argentina"]
    obj2 = Series(ww2_dict, index=countries)
    print(obj2)
    print(pd.isnull(obj2))
    print(pd.notnull(obj2))

    print(ww2_series + obj2)

    obj2.name = "World War 2 Casualties"
    print(obj2)
    obj2.index.name = "Countries"
    print(obj2)

    return

def data_frame():
    website = "http://en.wikipedia.org/wiki/NFL_win-loss_records"
    # webbrowser.open(website)
    nfl_frame = pd.read_clipboard()
    print(nfl_frame)
    print(nfl_frame.columns)
    print(nfl_frame.Team)
    print(nfl_frame["First NFL Season"])

    dframe = DataFrame(nfl_frame, columns=["Team", "First NFL Season", "Won"])
    print(dframe)

    print(nfl_frame.head()) # prints first 5, pass a number for specific amount
    print(nfl_frame.tail()) # same as head, but for last 5
    print(nfl_frame.ix[3])	# prints specific row
    nfl_frame["Division"] = "Yay"
    print(nfl_frame)
    nfl_frame["GP"] = np.arange(5)
    print(nfl_frame)


    divisions = Series(["1st", "2nd"], index=[4,0])
    print(divisions)
    nfl_frame["Division"] = divisions
    print(nfl_frame)

    del nfl_frame["Division"]
    print(nfl_frame)

    data = {"City":["SF", "LA", "NYC"], "Population":[83700, 3880000, 8400000]}
    city_frame = DataFrame(data)
    print(city_frame)
    return

def index_objects():
	my_series = Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
	my_index = my_series.index
	print(my_index)
	print(my_index[2])
	print(my_index[2:])
	return

def reindexing():
	ser1 = Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
	print(ser1)
	ser2 = ser1.reindex(['A', 'B', 'C', 'D', 'E', 'F'])
	print(ser2)
	ser2 = ser2.reindex(['A', 'B', 'C', 'D', 'E', 'F', 'G'], fill_value=0)
	print(ser2)

	ser3 = Series(["USA", "Mexico", "Canada"], index=[0, 5, 10])
	print(ser3)
	ranger = range(15)
	print(ser3.reindex(ranger, method="ffill"))

	dframe = DataFrame(np.random.randn(25).reshape((5, 5)), 
		index=['A', 'B', 'D', 'E', 'F'], 
		columns=["col1", "col2", "col3", "col4", "col5"])
	print(dframe)
	dframe2 = dframe.reindex(['A', 'B', 'C', 'D', 'E', 'F'])
	print(dframe2)
	new_cols = ["col1", "col2", "col3", "col4", "col5", "col6"]
	dframe2.reindex(columns=new_cols)
	print(dframe2)

	# print(dframe.ix[['A', 'B', 'C', 'D', 'E', 'F'], new_cols])
	return

def drop_entry():
	ser1 = Series(np.arange(3), index=['a', 'b', 'c'])
	print(ser1)
	print(ser1.drop('b'))
	dframe1 = DataFrame(np.arange(9).reshape((3, 3)), index=["SF", "LA", "NY"], columns=["pop", "pip", "pap"])
	print(dframe1)
	print(dframe1.drop("LA"))
	dframe2 = dframe1.drop("LA")
	print(dframe2)
	print(dframe1.drop("pap", axis=1))
	return

def pandas_basics():
    # pandas_series()
    # data_frame()  # pandas can read clipboard data
    # index_objects()
    # reindexing()
    drop_entry()
    return

def main():
    numpy_basics()
    pandas_basics()


    return



if __name__ == "__main__":
    main()
