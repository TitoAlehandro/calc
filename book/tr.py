def tr():
        import pdb;pdb.set_trace()
def pr(obj):
    for ob in dir(obj):
        print(str(ob) + '           - ' + str(getattr(obj, ob)))

def grep(obj,st):
	for ob in dir(obj):
		if ob.find(st):
			print(str(ob) + '           - ' + str(getattr(obj, ob)))
    
def prm(obj):
    for ob in dir(obj):
        print(str(ob))

