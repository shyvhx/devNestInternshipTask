from string import ascii_lowercase as alc

def removeDuplicatesFromList(x):
  return list(dict.fromkeys(x))


def customerSort(file,outputFile):

    f = open(file, "r")

    #Remove header
    f.readline()


    # Create a list of 26 empty lists (one for each letter from the alphabet a-z)
    list = []
    for i in alc:
        list.append([])

    #Loop through the file line by line
    for line in f:
        firstLetter = line[0]
        # ASCII code of first letter minus 65 will result in indexing as such: A - 0 / B - 1 / C -2 and so on
        list[ord(firstLetter)-65].append(line)

    f.close()



    f = open(outputFile, "w")
    #f.write(list)

    for l in list:
        if len(l)==0:
            break
        else:
            l = removeDuplicatesFromList(l)
            f.write('\n'+l[0][0]+':\n')
            for i in range(len(l)):
                f.write(l[i])

    f.close()






if __name__ == '__main__':

    print(customerSort('input_example.txt','output.txt'))


