with open("/Users/liyuanchao/Desktop/emo_name_text_trans.txt", "w") as f:
	with open("/Users/liyuanchao/Desktop/name_trans_iem.txt", "r") as f1:
		with open("/Users/liyuanchao/Desktop/emo_name_trans.txt", "r") as f2:
			data1 = f1.readlines()
			data2 = f2.readlines()

			name_trans = {}

			for line1 in data1:
				new1 = line1.split(",")
				trans = []
				for i in new1[1:]:
					trans.append(i)
				trans = ",".join(trans)
				name_trans[new1[0]] = trans

			for line2 in data2:
				line2 = line2[:-1]
				new2 = line2.split(",")
				new_line = ",".join(new2) + "," + name_trans[new2[1]]
				f.write(new_line)