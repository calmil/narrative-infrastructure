with open('list.txt') as infile:
  replaced = infile.read().replace("\n","','")
with open('formattedlist.txt', "w") as outfile:
  outfile.write(replaced)