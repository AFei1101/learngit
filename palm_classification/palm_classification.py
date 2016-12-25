#! python3
# -*- coding:utf-8 -*--

class Tool:
	def perison(self,R,C):
		RO,C0 = R,C
		average_r = sum(R)/len(R)	
		R0 = map(lambda x: x-average_r,R)
		C0 = map(lambda x: x-average_r,C)
		#print R0,C0

		xxr = sum(map(lambda x:x*x,R0))
		xxc = sum(map(lambda x:x*x,C0))
		xx = 0
		for i in range(len(R0)):
			xx += R0[i]*C0[i]
		ps = xx/pow(xxc*xxr,0.5)
		return ps
	
class main():
	def __init__(self,R,C):
		#print R[0][0]-C[0][0]
		#ind = 0
		self.R = R
		self.C = C
		self.inds = []
		self.match_number = 0
		self.raw_int = 0
		self.tool = Tool()
		
		
	def match1(self):
		for ci in range(len(self.C)):
			#print 'c'+str(ci)+str(average_c)
			self.inds.append(self.raw_int)
			for ri in range(len(self.R)):
				ind = 0
				#average_r = sum(self.R[ri])/len(self.R[ri])
				#print 'r'+str(ri)+str(average_r)
				#print (C[ci][j]-R[ri][j])
				ps = self.tool.perison (R[ri],C[ci])
				#print ps
				
				if ps > self.inds[ci]:
					self.inds[ci] = ps
					self.match_number = ri
				#inds[ci].append(ind) 

			print ('C'+str(ci)+u'矢量为R'+str(self.match_number)+
			u'模型，二者之间的皮尔逊相关度最大，为'+str(self.inds[ci])+u'。')
	
	def match2(self):
		for ci in range(len(self.C)):
			self.inds.append(self.raw_int)
			for ri in range(len(self.R)):
				ind = 0
				for j in range(len(self.C[ci])):
					#print (C[ci][j]-R[ri][j])
					ind += pow((self.C[ci][j]-self.R[ri][j])/self.R[ri][j],2)
				
				if ind < self.inds[ci]:
					self.inds[ci] = ind
					self.match_number = ri
				#inds[ci].append(ind) 

			print ('C'+str(ci)+u'矢量为R'+str(self.match_number)+
			u'模型，二者之间的欧几里得距离最小，为'+str(self.inds[ci])+u'。')
				#inds.append(ind)
			#print inds
			#[ci]	


R = [[8.305,7.320,7.685,5.633,5.750,8.555,1.700,1.645],
[7.607,6.969,7.059,5.011,5.071,8.684,1.754,1.557],
[7.045,6.226,6.555,4.217,4.715,7.820,1.715,1.470],
[7.596,6.852,7.440,5.362,5.666,8.302,1.774,1.660],
[8.080,7.080,7.645,5.437,5.570,8.650,1.765,1.640],
[8.910,7.590,8.385,5.825,5.945,9.195,1.888,1.660]
]

C = [[8.318,7.229,7.683,5.808,5.687,8.469,1.694,1.694],
[7.108,6.356,6.594,4.416,4.719,7.864,1.694,1.452],
[7.621,6.774,7.251,4.895,5.081,8.574,1.826,1.720]
]


a = main(R,C)
a.match1()
a.match2()
