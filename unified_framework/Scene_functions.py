
import numpy as np
import cv2


Dir = '/home/omari/Desktop/Python/language/Simultaneous_learning_and_ground/images/'
Dir2 = '/home/omari/Desktop/Python/language/Simultaneous_learning_and_ground/images2/'

object_radius = 20 	#used in Scene_functions and QSR_functions
map_size = 500
object_number_max = 4
frames = 1
H_std = 5
S_std = .05
V_std = .05
color_number_max = 16
name_window = 150
th = 40


def scene_descreption(o_loc,o_color,o_qsr):

	initial2 = ['','this is a ','a ','the ']
	initial = ['','the ']
	iss = ['','is ','is ','is ']

	obj_number = len(o_loc)
	#------ generating sentences ---------#
	ss = []
	if obj_number==1:
		r1 = int(np.random.rand(1)*4)
		ss.append(initial2[r1]+o_color['name'][0])

	counter = 0			
	for j in range(obj_number):
		for k in range(j+1,obj_number):
			r1 = int(np.random.rand(1)*2)
			r2 = int(np.random.rand(1)*4)
			ss.append(initial[r1]+o_color['name'][j]+' '+iss[r2]+o_qsr[str(j)+'-'+str(k)+'-dir']+' and '+o_qsr[str(j)+'-'+str(k)+'-spa']+' '+o_color['name'][k])
			counter+=1
	k = ''
	if len(ss)==1:
		sentence = ss[0]
	else:
		for j in range(len(ss)-1):
			k = k+ss[j]+' and '
		k = k+ss[len(ss)-1]
		sentence = k

	return sentence
#-------------------------------------------------------------------------------------#
def scene_gnerator(object_number_max):
	obj_number = int(np.random.rand(1)*object_number_max)+1

	#------ object locations ---------#
	# randomly place objects in a map of area 500*500 with object radius being 20
	object_locations = []

	obj_2 = np.abs(np.random.rand(2)*(map_size-2*object_radius))
	object_locations.append([obj_2])	# first object

	for j in range(1,obj_number):
		#while 1:
		obj_2 = np.abs(np.random.rand(2)*(map_size-2*object_radius))
		object_locations.append([obj_2])

	#------ object colours ---------#
	o_color = {}
	object_colors_names = []
	object_colors = []
	H_value = []
	S_value = []
	V_value = []

	HSV,color1,name1 = colourr(int(np.random.rand(1)*color_number_max))
	object_colors.append(color1)
	object_colors_names.append(name1)
	H_value.append(HSV[0])
	S_value.append(HSV[1])
	V_value.append(HSV[2])

	for j in range(1,obj_number):
		while 1:
			num = int(np.random.rand(1)*color_number_max)
			HSV,color1,name1 = colourr(num)
			if name1 not in object_colors_names:
				break
		object_colors.append(color1)
		object_colors_names.append(name1)
		H_value.append(HSV[0])
		S_value.append(HSV[1])
		V_value.append(HSV[2])

	o_color['H'] = H_value	
	o_color['S'] = S_value	
	o_color['V'] = V_value	
	o_color['color'] = object_colors	
	o_color['name'] = object_colors_names

	#------ plot object locations ---------#
	#img = np.zeros(shape=(map_size, map_size, 3), dtype=np.uint8)+255 
	img = cv2.imread('table.jpg')
	for j in range(len(object_locations)):
		c = object_colors[j]
		l = object_locations[j][0]
		cv2.circle(img,(int(l[0])+object_radius,int(l[1])+object_radius),object_radius+2,(0,0,0),-1)
		cv2.circle(img,(int(l[0])+object_radius,int(l[1])+object_radius),object_radius,(c[2],c[1],c[0]),-1)


	# draw borders
	img[0:1,:,:] = 0
	img[:,0:1,:] = 0
	img[map_size-1:map_size,:,:] = 0
	img[:,map_size-1:map_size,:] = 0

	return object_locations,o_color,img



#-------------------------------------------------------------------------------------#
def HSV_to_RGB(H,S,V):
	#http://www.rapidtables.com/convert/color/hsv-to-rgb.htm
	C = V * S
	X = C * (1 - np.abs(np.mod((H / 60.0),2.0) - 1))
	m = V - C
	if H>=0 and H<60:
		R=C
		G=X
		B=0
	elif H>=60 and H<120:
		R=X
		G=C
		B=0
	elif H>=120 and H<180:
		R=0
		G=C
		B=X
	elif H>=180 and H<240:
		R=0
		G=X
		B=C
	elif H>=240 and H<300:
		R=X
		G=0
		B=C
	elif H>=300 and H<=360:
		R=C
		G=0
		B=X
	return int((R+m)*255),int((G+m)*255),int((B+m)*255)


#-------------------------------------------------------------------------------------#
def colourr(num):

	if num == 0: #white
		H = np.random.normal(0, H_std, 1)
		S = np.random.normal(0, S_std, 1)
		V = np.random.normal(1, V_std, 1)
		name = 'white object'
	if num == 1: #black
		H = np.random.normal(0, H_std, 1)
		S = np.random.normal(0, S_std, 1)
		V = np.random.normal(0, V_std, 1)
		name = 'black object'
	if num == 2: #green
		H = np.random.normal(120, H_std, 1)
		S = np.random.normal(1, S_std, 1)
		V = np.random.normal(.5, V_std, 1)
		name = 'green object'
	if num == 3: #blue
		H = np.random.normal(240, H_std, 1)
		S = np.random.normal(1, S_std, 1)
		V = np.random.normal(1, V_std, 1)
		name = 'blue object'
	if num == 4: #red
		H = np.random.normal(0, H_std, 1)
		S = np.random.normal(1, S_std, 1)
		V = np.random.normal(1, V_std, 1)
		name = 'red object'
	if num == 5: #maroon
		H = np.random.normal(0, H_std, 1)
		S = np.random.normal(1, S_std, 1)
		V = np.random.normal(.5, V_std, 1)
		name = 'maroon object'
	if num == 6: #yellow
		H = np.random.normal(60, H_std, 1)
		S = np.random.normal(1, S_std, 1)
		V = np.random.normal(1, V_std, 1)
		name = 'yellow object'
	if num == 7: #olive
		H = np.random.normal(60, H_std, 1)
		S = np.random.normal(1, S_std, 1)
		V = np.random.normal(.5, V_std, 1)
		name = 'olive object'
	if num == 8: #Lime
		H = np.random.normal(120, H_std, 1)
		S = np.random.normal(1, S_std, 1)
		V = np.random.normal(1, V_std, 1)
		name = 'lime object'
	if num == 9: #silver
		H = np.random.normal(0, H_std, 1)
		S = np.random.normal(0, S_std, 1)
		V = np.random.normal(.75, V_std, 1)
		name = 'silver object'
	if num == 10: #aqua
		H = np.random.normal(180, H_std, 1)
		S = np.random.normal(1, S_std, 1)
		V = np.random.normal(1, V_std, 1)
		name = 'aqua object'
	if num == 11: #teal
		H = np.random.normal(180, H_std, 1)
		S = np.random.normal(1, S_std, 1)
		V = np.random.normal(.5, V_std, 1)
		name = 'teal object'
	if num == 12: #navy
		H = np.random.normal(240, H_std, 1)
		S = np.random.normal(1, S_std, 1)
		V = np.random.normal(.5, V_std, 1)
		name = 'navy object'
	if num == 13: #Fuchsia
		H = np.random.normal(300, H_std, 1)
		S = np.random.normal(1, S_std, 1)
		V = np.random.normal(1, V_std, 1)
		name = 'Fuchsia object'
	if num == 14: #Purple
		H = np.random.normal(300, H_std, 1)
		S = np.random.normal(1, S_std, 1)
		V = np.random.normal(.5, V_std, 1)
		name = 'Purple object'
	if num == 15: #Gray
		H = np.random.normal(0, H_std, 1)
		S = np.random.normal(0, S_std, 1)
		V = np.random.normal(.5, V_std, 1)
		name = 'gray object'


	if S>1:
		S=np.zeros(1)+1
	if S<0:
		S=-S
	if V>1:
		V=np.zeros(1)+1
	if V<0:
		V=-V
	if H<0:
		H = H+360
	if H>360:
		H = H-360

	H = int(H)
	S = S[0]
	V = V[0]

	R,G,B = HSV_to_RGB(H,S,V)
	n = [R,G,B]
	return [H,S,V],n,name



