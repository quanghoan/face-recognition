import pandas as pd
import os, errno

train_csv = pd.read_csv('/home/harry/python/aivivn/data/train.csv')
grouped = train_csv.groupby('label')

for image,group in grouped:
	try:
		os.makedirs('/home/harry/python/aivivn/sorted_images/'+str(image))
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
	print(image)
	print(group)