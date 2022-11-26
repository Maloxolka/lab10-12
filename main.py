from lab10_1 import get_freq_map
from lab10_2 import split_syllables
from lab10_3 import *
from lab10_4 import *

from lab11 import *

from lab12_1 import *
from lab12_2 import *

if __name__ == '__main__':
    # lab10 task 1 test
    print(get_freq_map([1, 2, 3, 1, 2, 3, 2, 2, [1, 2, 3, [1, 1, 2], [1, 2, 2]], [1, 1, 1, 2]], 1))
    print("\n ------------------ \n")

    # lab10 task 2 test (transcriptions from this: https://www.goethe-verlag.com/book2/RU/RUFA/RUFA010.HTM)
    print(split_syllables("khânevâde"))
    print(split_syllables("dokhtar"))
    print(split_syllables("dâee"))
    print(split_syllables("pâyetakht"))
    print("\n ------------------ \n")

    # lab10 task 3 test
    print(cure_dir("C://Users//Danil//Desktop/lab10_3_test"))
    print("\n ------------------ \n")

    # lab10 task4 test
    pm = PalindromeMaker()
    print(pm.insert_palindrome("sdasdaffg"))
    print(pm.insert_palindrome("zululuz"))
    print(pm.insert_palindrome("toot"))
    print(pm.palindrome)
    print("\n ------------------ \n")

    print(get_anagrams("mash"))
    print("\n ------------------ \n")

    # lab11 test

    data = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        data.append(ele)

    data_quick = data.copy()
    data_bubble = data.copy()
    data_merge = data.copy()
    data_insertion = data.copy()
    data_selection = data.copy()
    data_heap = data.copy()
    data_radix = data.copy()
    data_bucket = data.copy()

    print("Quick Sort")
    quick_sort(data_quick, 0, len(data_quick) - 1)
    print(data_quick)

    print("Bubble Sort")
    bubble_sort(data_bubble)
    print(data_bubble)

    print("Merge Sort")
    merge_sort(data_merge, 0, len(data_merge) - 1)
    print(data_merge)

    print("Insertion Sort")
    insertion_sort(data_insertion)
    print(data_insertion)

    print("Selection Sort")
    selection_sort(data_selection, len(data_selection))
    print(data_selection)

    print("Heap Sort")
    heap_sort(data_heap)
    print(data_heap)

    print("Radix Sort")
    radix_sort(data_radix)
    print(data_radix)

    print("Bucket Sort")
    print(bucket_sort(data_bucket))

    print("\n ------------------ \n")

    # lab12 task 1 test
    assert to_string(56), "56"
    assert repeat_substr("qwe", 3), "qweqweqwe"
    assert get_las("asdfghjkasdfghjkasdfghjkl"), "asdfghjkasdfghjk"

    # lab12 task 2 test
    sudoku = Sudoku()
    sudoku.place(0, 0, 2)
    sudoku.place(7, 7, 3)
    assert sudoku.board, [[2, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 3, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    sudoku.print_board()
