#!/usr/bin/python3
def list_division(list1, list2, length):
    new = []
    for x in range(length):
        a = 0
        try:
            a = list1[x] / list2[x]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
          new.append(a)
    return new
