import json

with open('/Users/liyuanchao/Desktop/name_trans.txt', 'w') as f1:
	with open('/Users/liyuanchao/Desktop/data.json', 'r') as f:
		data = json.load(f)
		for filename in data["utts"]:
			name_trans = filename + ".wav,"
			for out in data["utts"][filename]:
				if out == "output":
					rec = data["utts"][filename][out]
					for i in rec:
						text = i["rec_text"][1:-5] #去掉_和eos
						text = text.split("▁")
						text = " ".join(text)
						name_trans += text
						name_trans += ","

			f1.write(name_trans[:-1]) #去掉最后的逗号
			f1.write("\n")