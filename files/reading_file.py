#Open text file and read
f_read = open('text.txt','r')
lines = f_read.readlines()
f_read.close()

#Opening the file to write data in it
f_write = open('text_to_write.txt','w')

for line in lines:
    f_write.write(line)

f_write.close()

#opening the file to append data in it
f_append = open('text_to_append.txt','a')
for line in lines:
    f_append.write(line)

f_append.close()