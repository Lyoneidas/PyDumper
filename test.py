#generate test files
with open('DumpData.dmp', "r") as f:
    i = 0
    w = open('test_data.dmp', "w")
    while i<5000:
        line = f.readline()
        w.write(line)
        i+=1
    w.close()
f.close()
