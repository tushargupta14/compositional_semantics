import json

with open("pos_tag_dictionary.json") as fp:
    for row in fp:
        pos_dict = json.loads(row)

i = 0
fp = open("pos_tag_dictionary.csv", "wb+")

for k,v in pos_dict.iteritems():
    print i
    i += 1
    fp.write(k + "|" + ",".join(v[0]) + "|" + str(v[1]) + "\n")
fp.close()
