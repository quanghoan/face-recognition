import pandas as pd
import os, errno, glob, shutil

train_csv = pd.read_csv('../aivivn/data/train.csv')
grouped = train_csv.groupby('label')

for name,group in grouped:
	try:
		os.makedirs('../aivivn/sorted_images/'+str(name))
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
	for image in glob.glob('../aivivn/data/train/*.png'):
	    basename = os.path.basename(image)
	    if basename in group.values:
	    	shutil.copy(image, '../aivivn/sorted_images/'+str(name))
	print(name)
	print(group)



