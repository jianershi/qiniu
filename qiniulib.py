from credentials import QiNiuACCESS_KEY, QiNiuSECRET_KEY

import qiniu.conf
import qiniu.io
import sys
import qiniu.rs
import qiniu.io
import qiniu.rsf

def uploadToQiNiu(bucketName,fileName):
	'''
	this function support override of existing file
	'''
	
	qiniu.conf.ACCESS_KEY = QiNiuACCESS_KEY
	qiniu.conf.SECRET_KEY = QiNiuSECRET_KEY

	policy = qiniu.rs.PutPolicy(bucketName)
	policy.scope=bucketName+':'+unicode(fileName, "utf-8")
	uptoken = policy.token()


	extra = qiniu.io.PutExtra()
	# extra.mime_type = "image/jpeg"
	f=open(fileName,'r')
	# localfile = "%s" % f.read()
	ret, err = qiniu.io.put(uptoken, fileName, f)
	f.close()
	print ret;
	if err is not None:
		sys.stderr.write('error: %s ' % err)

def list_all(bucketName, rs=None, prefix=None, limit=None):
	'''
	sample code from official api page
	'''

	qiniu.conf.ACCESS_KEY = QiNiuACCESS_KEY
	qiniu.conf.SECRET_KEY = QiNiuSECRET_KEY
	
	if rs is None:
		rs = qiniu.rsf.Client()
	marker = None
	err = None
	while err is None:
		ret, err = rs.list_prefix(bucketName, prefix=prefix, limit=limit, marker=marker)
		marker = ret.get('marker', None)
		# print ret
		return ret['items']
		for item in ret['items']:
			# #do something
			pass
	if err is not qiniu.rsf.EOF:
		#error handling
		pass