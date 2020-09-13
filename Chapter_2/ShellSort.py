""" This Module contains an implementation of the shell sort algorithm """


class ShellSort:
    @staticmethod
    def sort(collection):
        n = len(collection)
        gap = n // 2
        # Perform Shell sort using h sort insertion sorts
        while gap > 0:
            for i in range(gap,n):
                tmp = collection[i]
                j = i
                while j >= gap and collection[j-gap] > tmp:
                    collection[j] = collection[j-gap]
                    j -= gap
                collection[j] = tmp
            gap = gap//2


def main():
    test = [12, 34, 54, 2, 3, 44, 5, 11, 1, 19, 10]
    ShellSort.sort(test)
    print(test)

if __name__ == '__main__':
    main()