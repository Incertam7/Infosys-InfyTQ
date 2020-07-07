#PF-Exer-30

def find_average(mark_list):
	total = 0
	for i in range(0, len(mark_list)):
		total += mark_list[i]
	marks_avg = total/len(mark_list)
	return marks_avg

try:
    m_list=[15, 26, 34, 24]
    print("Average marks:", find_average(m_list))
except TypeError:
    print("Error: Invalid type")
except ValueError:
    print("Error: Invalid value")
except ZeroDivisionError:
    print("Error: Can't divide by zero")
except IndexError:
    print("List index is out of range")
