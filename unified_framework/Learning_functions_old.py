
import numpy as np
import math 

#-------------------------------------------------------------------------------------#
def norm_pdf_multivariate(x, mu, sigma):
     size = len(x)
     x_mu = np.matrix(x - mu)
     determ = np.linalg.det(sigma)
     if determ < 0.01:
         new_diag = np.diag(sigma).copy()
         new_diag[new_diag == 0] = 0.05
         new_sigma = np.matrix(np.diag(new_diag))
         determ = np.linalg.det(new_sigma)
         inv = new_sigma.I
     else:
         inv = sigma.I

     norm_const = 1.0/ (math.pow((2*np.pi),float(size)/2) * 
math.pow(determ,1.0/2))
     result = math.pow(math.e, -0.5 * (x_mu * inv * x_mu.T))
     return norm_const * result

#-------------------------------------------------------------------------------------#
def Update_dis_histogram_use_CK(hyp,o_qsr,sentence):

	# Use the consulidated knowledge
	
	flag = 0
	words = []
	o1 = 0
	o2 = 0
	for j in sentence.split(' '):
		if flag == 0:
			if j in hyp['objects_hyp']:
				#print j,hyp['objects_hyp'].index(j),'------------Start'
				o1 = hyp['objects_hyp'].index(j)
				flag = 1
		elif flag == 1:
			if j in hyp['objects_hyp']:
				#print j,hyp['objects_hyp'].index(j),'------------Stop'
				o2 = hyp['objects_hyp'].index(j)
				flag = 0
				if o1 != o2:				#----------- check if o1 and o2 are different
				####################### you can easily learn direction by checking if o1 is < or > o2 and choose which angle
					#print o1,'-',o2,':',words
					if o1>o2:
						k=o2
						o2=o1
						o1=k
					for k in words:
						if k not in hyp['valid_HSV_hyp']:
							hyp['hyp'][k]['counter_dis']+=1
							#A = o_qsr['obj_number']
							#for p in range(A-1):
							#	for k in range(p+1,A):
							d = o_qsr[str(o1)+'-'+str(o2)+'-dis']
							hyp['hyp'][k]['hist_dis'][int(d)] += 1
				words = []
			else:
				words.append(j)
	return hyp

#-------------------------------------------------------------------------------------#
def Update_dis_histogram(hyp,o_qsr):

	for j in hyp['words']:
		if j not in hyp['valid_HSV_hyp']:
			hyp['hyp'][j]['counter_dis']+=1
			A = o_qsr['obj_number']
			"""
			if A==1:
				d = o_qsr[str(0)+'-'+str(1)+'-dis']
				hyp['hyp'][j]['hist_dis'][int(d)] += 1

			else:
			"""
			for p in range(A-1):
				for k in range(p+1,A):
					d = o_qsr[str(p)+'-'+str(k)+'-dis']
					hyp['hyp'][j]['hist_dis'][int(d)] += 1	
	return hyp

#-------------------------------------------------------------------------------------#
def Compute_dis_hypotheses(hyp):
	hyp['valid_dis_hyp'] = []

	for j in hyp['hyp']:
	    if j not in hyp['valid_HSV_hyp'] and hyp['hyp'][j]['counter_dis']!=0:
		hyp['hyp'][j]['score_dis'] = np.zeros(shape=(1000))		# up to 1000 pixel
		flag = 0
		for m in range(20,200,20):
		    for k in range(1000-m):
			if np.sum(hyp['hyp'][j]['hist_dis'][k:m+k])>=hyp['hyp'][j]['counter_dis']*.9:
				hyp['hyp'][j]['score_dis'][k:m+k]=1
				flag=1

		    if flag == 1:	# hypothesis has been found
			hyp['valid_dis_hyp'].append(j)
			break

	for j in hyp['valid_dis_hyp']:
		hyp['hyp'][j]['dis_points_x'] = []
		hyp['hyp'][j]['dis_points_y'] = []
		hyp['hyp'][j]['dis_points_z'] = []
		A = np.nonzero(hyp['hyp'][j]['score_dis'])
		B = np.nonzero(hyp['hyp'][j]['hist_dis'])
		for p in range(len(B[0])):
			if B[0][p] in A[0]:
				d = B[0][p]/700.0
				hyp['hyp'][j]['dis_points_x'].append(d)


		hyp['hyp'][j]['dis_points_x_mean'] = np.mean(hyp['hyp'][j]['dis_points_x'])
		hyp['hyp'][j]['dis_points_y_mean'] = 0
		hyp['hyp'][j]['dis_points_z_mean'] = 0

		hyp['hyp'][j]['dis_points_x_std'] = np.std(hyp['hyp'][j]['dis_points_x'])
		hyp['hyp'][j]['dis_points_y_std'] = 0
		hyp['hyp'][j]['dis_points_z_std'] = 0
								
	return hyp
#-------------------------------------------------------------------------------------#
def Update_dir_histogram_use_CK(hyp,o_qsr,sentence):

	# Use the consulidated knowledge
	
	flag = 0
	words = []
	o1 = 0
	o2 = 0
	for j in sentence.split(' '):
		if flag == 0:
			if j in hyp['objects_hyp']:
				#print j,hyp['objects_hyp'].index(j),'------------Start'
				o1 = hyp['objects_hyp'].index(j)
				flag = 1
		elif flag == 1:
			if j in hyp['objects_hyp']:
				#print j,hyp['objects_hyp'].index(j),'------------Stop'
				o2 = hyp['objects_hyp'].index(j)
				flag = 0
				if o1 != o2:				#----------- check if o1 and o2 are different
				####################### you can easily learn direction by checking if o1 is < or > o2 and choose which angle
					#print o1,'-',o2,':',words
					if o1>o2:
						k=o2
						o2=o1
						o1=k
						o_qsr[str(o1)+'-'+str(o2)+'-ang'] = -o_qsr[str(o1)+'-'+str(o2)+'-ang']	# the other relation

					for k in words:
						if k not in hyp['valid_HSV_hyp']:
							hyp['hyp'][k]['counter_dir']+=1
							#A = o_qsr['obj_number']
							#for p in range(A-1):
							#	for k in range(p+1,A):
							a = o_qsr[str(o1)+'-'+str(o2)+'-ang']*180/np.pi
							if a<0:
								a=a+360
							hyp['hyp'][k]['hist_dir'][int(a)] += 1
				words = []
			else:
				words.append(j)
	return hyp
			

def Update_dir_histogram(hyp,o_qsr):
	for j in hyp['words']:
		if j not in hyp['valid_HSV_hyp']:
			hyp['hyp'][j]['counter_dir']+=1
			A = o_qsr['obj_number']
			for p in range(A-1):
				for k in range(p+1,A):
					a = o_qsr[str(0)+'-'+str(1)+'-ang']*180/np.pi
					if a<0:
						a=a+360
					hyp['hyp'][j]['hist_dir'][int(a)] += 1
	return hyp

#-------------------------------------------------------------------------------------#
def Compute_dir_hypotheses(hyp):
	hyp['valid_dir_hyp'] = []
	window = 361

	for j in hyp['hyp']:
	    if j not in hyp['valid_HSV_hyp'] and hyp['hyp'][j]['counter_dir']!=0:
		hyp['hyp'][j]['score_dir'] = np.zeros(shape=(360))		# up to 1000 pixel
		flag = 0
		for m in range(20,190,20):
		    W=m
		    for k in range(361):
			if W+k-1 < (361):		# to make the circular thing continous
				if np.sum(hyp['hyp'][j]['hist_dir'][k:m+k])>=hyp['hyp'][j]['counter_dir']*.9:
					hyp['hyp'][j]['score_dir'][k:m+k]=1
					flag=1
			else:
				A = np.sum(hyp['hyp'][j]['hist_dir'][0:-(window-1)+k+W])
				B = np.sum(hyp['hyp'][j]['hist_dir'][k:(window-1)])
				if A+B>=hyp['hyp'][j]['counter_dir']*.9:
					hyp['hyp'][j]['score_dir'][0:-(window-1)+k+W] = 1
					hyp['hyp'][j]['score_dir'][k:(window-1)] = 1
					flag = 1

		    if flag == 1:	# hypothesis has been found
			hyp['valid_dir_hyp'].append(j)
			break

	for j in hyp['valid_dir_hyp']:
		hyp['hyp'][j]['dir_points_x'] = []
		hyp['hyp'][j]['dir_points_y'] = []
		hyp['hyp'][j]['dir_points_z'] = []
		A = np.nonzero(hyp['hyp'][j]['score_dir'])
		B = np.nonzero(hyp['hyp'][j]['hist_dir'])
		for p in range(len(B[0])):
			if B[0][p] in A[0]:
				d = B[0][p]
				hyp['hyp'][j]['dir_points_x'].append(d)

		hyp['hyp'][j]['dir_points_x_mean'] = circ_mean(hyp['hyp'][j]['dir_points_x'], low=0, high=360)
		hyp['hyp'][j]['dir_points_x_std'] = circ_std(hyp['hyp'][j]['dir_points_x'], low=0, high=360)
								
	return hyp

#-------------------------------------------------------------------------------------#
def Update_SPA_histogram(hyp,o_qsr,POINTS):

	for j in hyp['words']:
		if j not in hyp['valid_HSV_hyp']:
			hyp['hyp'][j]['counter_SPA']+=1
			
			hyp['hyp'][j]['score_SPA'] = np.zeros(shape=(201,201,101))
			A = o_qsr['obj_number']
			for p in range(A-1):
				for k in range(p+1,A):
					d = o_qsr[str(p)+'-'+str(k)+'-dis']/700.0
					a = o_qsr[str(p)+'-'+str(k)+'-ang']*180/np.pi
					xs,ys,zs = HSV_to_XYZ(a, d, 0.5)		# in this case Z is always to zero
					x = int(xs[0]*100+100)
					y = int(ys[0]*100+100)
					z = int(zs[0]*100)
					hyp['hyp'][j]['hist_SPA'][x,y,z] += 1
					POINTS.append([xs,ys,zs,1.0,1.0,1.0])
				
	return hyp,POINTS

#-------------------------------------------------------------------------------------#
def Compute_SPA_hypotheses(hyp):
	#============== create a set of believes for SPA ===============#
	hyp['valid_SPA_hyp'] = []

	for j in hyp['hyp']:
	    if hyp['hyp'][j]['not_a_hyp_SPA']<10:
		X,Y,Z = np.nonzero(hyp['hyp'][j]['hist_SPA'])	# loop through the histogram values
		flag = 0

		for kk in [12,15,18,20,23,25]:
		    for jj in range(len(X)):
			x1 = X[jj]-kk
			x2 = X[jj]+kk
			y1 = Y[jj]-kk
			y2 = Y[jj]+kk
			z1 = Z[jj]-kk
			z2 = Z[jj]+kk
			x1,x2 = check(x1,x2,0,200)
			y1,y2 = check(y1,y2,0,200)
			z1,z2 = check(z1,z2,0,100)

			# see if a cube in the hitogram can be valid to be a hypothesis
			if  np.sum(hyp['hyp'][j]['hist_SPA'][x1:x2,y1:y2,z1:z2]) >= hyp['hyp'][j]['counter_SPA']*.9:
				hyp['hyp'][j]['score_SPA'][x1:x2,y1:y2,z1:z2] = 1
				flag = 1

		    if flag == 1:	# hypothesis has been found
			hyp['valid_SPA_hyp'].append(j)
			break

		    if kk==25:
			hyp['hyp'][j]['not_a_hyp_SPA']+=1

	for j in hyp['valid_SPA_hyp']:
		hyp['hyp'][j]['SPA_points_x'] = []
		hyp['hyp'][j]['SPA_points_y'] = []
		hyp['hyp'][j]['SPA_points_z'] = []
		A = np.nonzero(hyp['hyp'][j]['score_SPA'])
		B = np.nonzero(hyp['hyp'][j]['hist_SPA'])
		for p in range(len(B[0])):
			if B[0][p] in A[0] and B[1][p] in A[1] and B[2][p] in A[2]:
				hyp['hyp'][j]['SPA_points_x'].append((B[0][p]-100)/100.0)
				hyp['hyp'][j]['SPA_points_y'].append((B[1][p]-100)/100.0)
				hyp['hyp'][j]['SPA_points_z'].append(B[2][p]/100.0)


		hyp['hyp'][j]['SPA_points_x_mean'] = np.mean(hyp['hyp'][j]['SPA_points_x'])
		hyp['hyp'][j]['SPA_points_y_mean'] = np.mean(hyp['hyp'][j]['SPA_points_y'])
		hyp['hyp'][j]['SPA_points_z_mean'] = np.mean(hyp['hyp'][j]['SPA_points_z'])

		hyp['hyp'][j]['SPA_points_x_std'] = np.std(hyp['hyp'][j]['SPA_points_x'])
		hyp['hyp'][j]['SPA_points_y_std'] = np.std(hyp['hyp'][j]['SPA_points_y'])
		hyp['hyp'][j]['SPA_points_z_std'] = np.std(hyp['hyp'][j]['SPA_points_z'])
		
	return hyp

#-------------------------------------------------------------------------------------#
def Test_HSV_Hypotheses(hyp,o_color,sentence):
	hyp['objects'] = {}
	hyp['objects_hyp'] = []
	for i in range(len( o_color['H'])):
		H = o_color['H'][i]
		S = o_color['S'][i]
		V = o_color['V'][i]
		x,y,z = HSV_to_XYZ(H, S, V)
		A = np.matrix([x[0],y[0],z[0]])
		hyp['objects'][i] = ''
		var = 0
		for j in hyp['valid_HSV_hyp']:

			X = hyp['hyp'][j]['HSV_points_x_mean']
			Y = hyp['hyp'][j]['HSV_points_y_mean']
			Z = hyp['hyp'][j]['HSV_points_z_mean']

			Xs= hyp['hyp'][j]['HSV_points_x_std']
			Ys= hyp['hyp'][j]['HSV_points_y_std']
			Zs= hyp['hyp'][j]['HSV_points_z_std']

			B = np.matrix([X,Y,Z])
			result = norm_pdf_multivariate(A, B, np.matrix([[Xs, 0, 0], [0, Ys, 0], [0, 0, Zs]]))

			if var<result:
				hyp['objects'][i] = j
				var = result

		hyp['objects_hyp'].append(hyp['objects'][i])

	return hyp



#-------------------------------------------------------------------------------------#
def Update_HSV_histogram(hyp,o_color,POINTS):

	for j in hyp['words']:
		hyp['hyp'][j]['score_HSV'] = np.zeros(shape=(201,201,101))
		for p in range(len(o_color['H'])):
			H = o_color['H'][p]
			S = o_color['S'][p]
			V = o_color['V'][p]
			xs,ys,zs = HSV_to_XYZ(H, S, V)
			x = int(xs[0]*100+100)
			y = int(ys[0]*100+100)
			z = int(zs[0]*100)
			hyp['hyp'][j]['hist_HSV'][x,y,z] += 1
			c = o_color['color'][p]
			POINTS.append([xs,ys,zs,c[0]/255.0,c[1]/255.0,c[2]/255.0])

	return hyp,POINTS

#-------------------------------------------------------------------------------------#
def Compute_HSV_hypotheses(hyp):

	#============== create a set of believes for HSV ===============#
	hyp['valid_HSV_hyp'] = []

	for j in hyp['hyp']:
	    if hyp['hyp'][j]['not_a_hyp_HSV']<5:
		X,Y,Z = np.nonzero(hyp['hyp'][j]['hist_HSV'])	# loop through the histogram values
		flag = 0
		for kk in [12,15,18,20,23,25]:
		    for jj in range(len(X)):
			x1 = X[jj]-kk
			x2 = X[jj]+kk
			y1 = Y[jj]-kk
			y2 = Y[jj]+kk
			z1 = Z[jj]-kk
			z2 = Z[jj]+kk
			x1,x2 = check(x1,x2,0,200)
			y1,y2 = check(y1,y2,0,200)
			z1,z2 = check(z1,z2,0,100)

			# see if a cube in the hitogram can be valid to be a hypothesis
			if  np.sum(hyp['hyp'][j]['hist_HSV'][x1:x2,y1:y2,z1:z2]) >= hyp['hyp'][j]['counter_HSV']*.9:
				hyp['hyp'][j]['score_HSV'][x1:x2,y1:y2,z1:z2] = 1
				flag = 1

		    if flag == 1:	# hypothesis has been found
			hyp['valid_HSV_hyp'].append(j)
			break

		    if kk==25:
			hyp['hyp'][j]['not_a_hyp_HSV']+=1

	for j in hyp['valid_HSV_hyp']:
		hyp['hyp'][j]['HSV_points_x'] = []
		hyp['hyp'][j]['HSV_points_y'] = []
		hyp['hyp'][j]['HSV_points_z'] = []
		A = np.nonzero(hyp['hyp'][j]['score_HSV'])
		B = np.nonzero(hyp['hyp'][j]['hist_HSV'])
		for p in range(len(B[0])):
			if B[0][p] in A[0] and B[1][p] in A[1] and B[2][p] in A[2]:
				hyp['hyp'][j]['HSV_points_x'].append((B[0][p]-100)/100.0)
				hyp['hyp'][j]['HSV_points_y'].append((B[1][p]-100)/100.0)
				hyp['hyp'][j]['HSV_points_z'].append(B[2][p]/100.0)


		hyp['hyp'][j]['HSV_points_x_mean'] = np.mean(hyp['hyp'][j]['HSV_points_x'])
		hyp['hyp'][j]['HSV_points_y_mean'] = np.mean(hyp['hyp'][j]['HSV_points_y'])
		hyp['hyp'][j]['HSV_points_z_mean'] = np.mean(hyp['hyp'][j]['HSV_points_z'])

		hyp['hyp'][j]['HSV_points_x_std'] = np.std(hyp['hyp'][j]['HSV_points_x'])
		hyp['hyp'][j]['HSV_points_y_std'] = np.std(hyp['hyp'][j]['HSV_points_y'])
		hyp['hyp'][j]['HSV_points_z_std'] = np.std(hyp['hyp'][j]['HSV_points_z'])
		
	return hyp

#-------------------------------------------------------------------------------------#
def sentence_parsing(hyp,sentence):
	#------------- create a list of all words ---------------#
	hyp['words'] = []
	for j in sentence.split(' '):
		if j not in hyp['hyp']:
			hyp['hyp'][j] = {}
			hyp['hyp'][j]['counter_HSV'] = 0	
			hyp['hyp'][j]['hist_HSV'] = np.zeros(shape=(201,201,101))
			hyp['hyp'][j]['score_HSV'] = np.zeros(shape=(201,201,101))
			hyp['hyp'][j]['not_a_hyp_HSV'] = 0
			hyp['hyp'][j]['counter_SPA'] = 0
			hyp['hyp'][j]['hist_SPA'] = np.zeros(shape=(201,201,101))
			hyp['hyp'][j]['score_SPA'] = np.zeros(shape=(201,201,101))
			hyp['hyp'][j]['not_a_hyp_SPA'] = 0

			hyp['hyp'][j]['counter_dis'] = 0	
			hyp['hyp'][j]['hist_dis'] = np.zeros(shape=(1000))		# up to 1000 pixel
			hyp['hyp'][j]['score_dis'] = np.zeros(shape=(1000))		# up to 1000 pixel
			hyp['hyp'][j]['counter_dir'] = 0
			hyp['hyp'][j]['hist_dir'] = np.zeros(shape=(360))		# up to 1000 pixel
			hyp['hyp'][j]['score_dir'] = np.zeros(shape=(360))		# up to 1000 pixel

		if j not in hyp['words']:
			hyp['words'].append(j)	

	# -- add 1 to counter HSV for as many times repeated --#
	for j in hyp['words']:
		hyp['hyp'][j]['counter_HSV']+=1

	return hyp



#-------------------------------------------------------------------------------------#
def HSV_to_XYZ(H, S, V):
	x = [S*np.cos(H*np.pi/180.0)]
	y = [S*np.sin(H*np.pi/180.0)]
	z = [V]
	return x,y,z

#-------------------------------------------------------------------------------------#
def check(b1,b2,a,b):
	if b1<a:
		b1=a
	#if b2>b:
	#	b2=b
	return b1,b2

#-------------------------------------------------------------------------------------#
def circ_mean(samples, low=0, high=2*np.pi):
     """Compute the circular mean for samples assumed to be in the range 
[low to high]
     """
     ang = (np.array(samples) - low)*2*np.pi / (high-low)
     mu = np.angle(np.mean(np.exp(1j*ang)))
     if (mu < 0):
         mu = mu + 2*np.pi
     return mu * (high-low)/(2.0*np.pi) + low

#-------------------------------------------------------------------------------------#
def circ_std(samples, low=0, high=2*np.pi):
     """Compute the circular standard deviation for samples assumed to 
be in the range [low to high]
     """
     ang = (np.array(samples) - low)*2*np.pi / (high-low)
     R = np.mean(np.exp(1j*ang))
     V = 1-abs(R)
     return np.sqrt(V) * (high-low)/(2.0*np.pi)
