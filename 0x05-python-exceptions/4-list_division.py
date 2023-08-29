#!/usr/bin/python3
def list_division(list1, list2, length):
    new = []
    for x in range(length):
        try:
            a = list1[x] / list2[x]
        except ZeroDivisionError:
            print("division by 0")
            a = 0
        except TypeError:
            print("wrong type")
            a = 0
        except IndexError:
            print("out of range")
            a = 0
        finally:
          new.append(a)
    return new
