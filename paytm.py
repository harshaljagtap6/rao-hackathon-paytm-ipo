list1 = []

def convertor(string1):
    a = string1.split(",")
    a[0] = (a[0].replace("[", ""))
    a[-1] = (a[-1].replace("]", ""))
    for i in range(len(a)):
        a[i] = int(a[i])
    return a


my_file = open("inputpaytm.txt", "r")
out_file = open("outputpaytm.txt", "a")
data = my_file.read()
new_lines = data.split("\n")
count = 1
while(count < 101):
    final_list = []
    list1 = convertor(new_lines[count]).copy()
    print(list1)
    a = list1.index(max(list1))
    print("MAX ->", max(list1))
    print("MIN ->", min(list1))
    final_list.append(max(list1) - min(list1))
    minute = float(9.30)
    init_time = 0.0
    minute = float("{0:.2f}".format(minute))
    for i in range(1, a+1):
        minute = minute + 0.1
        if (float("{0:.2f}".format(minute - int(minute))) == float("{0:.2f}".format(0.6))):
            minute = float("{0:.2f}".format(minute)) + float("{0:.2f}".format(1.0))
            minute = float("{0:.2f}".format(minute)) - float("{0:.2f}".format(0.6))
        if float("{0:.2f}".format(minute)) > 12:
            minute = float("{0:.2f}".format(minute)) - float("{0:.2f}".format(12.0))
    count = count + 1    
    final_list.append(float("{0:.2f}".format(minute)))
    out_file.writelines(str(final_list))
    out_file.writelines("\n")
out_file.close()
my_file.close()


print("-"*100)
print(float("{0:.2f}".format(minute)))
