# -*-python-*-
# This file was automatically generated by rpcc.

class Procedure(object):
	__slots__ = [ 'pack_arg', 'unpack_arg', 'pack_res', 'unpack_res' ]

programs = {}

def pack_ptr(p, o, packf):
	if o is None:
		p.pack_uint(0)
	else:
		p.pack_uint(1)
		packf(o)
def unpack_ptr(u, unpackf):
	bit = u.unpack_uint()
	if bit:
		return unpackf()
	else:
		return None

def pack_void(p, o):
	pass
def unpack_void(u):
	return None

def pack_int(p, o):
	p.pack_int(o)
def unpack_int(u):
	return u.unpack_int()

def pack_uint(p, o):
	p.pack_uint(o)
def unpack_uint(u):
	return u.unpack_uint()

def pack_hyper(p, o):
	p.pack_hyper(o)
def unpack_hyper(u):
	return u.unpack_hyper()

def pack_uhyper(p, o):
	p.pack_uhyper(o)
def unpack_uhyper(u):
	return u.unpack_uhyper()

def pack_float(p, o):
	p.pack_float(o)
def unpack_float(u):
	return u.unpack_float()

def pack_double(p, o):
	p.pack_double(o)
def unpack_double(u):
	return u.unpack_double()

def pack_bool(p, o):
	p.pack_bool(o)
def unpack_bool(u):
	return u.unpack_bool()

def pack_u_int32_t(p, o):
	p.pack_uint(o)
def unpack_u_int32_t(u):
	return u.unpack_uint()

def pack_int32_t(p, o):
	p.pack_int(o)
def unpack_int32_t(u):
	return u.unpack_int()

def pack_u_int64_t(p, o):
	p.pack_uhyper(o)
def unpack_u_int64_t(u):
	return u.unpack_uhyper()

def pack_int64_t(p, o):
	p.pack_hyper(o)
def unpack_int64_t(u):
	return u.unpack_hyper()


def pack_rpc_version(p, o):
	p.pack_uint(o)
def unpack_rpc_version(u):
	return u.unpack_uint()

RPC_VERSION = 2

def pack_auth_flavor(p, o):
	p.pack_uint(o)
def unpack_auth_flavor(u):
	return u.unpack_uint()

AUTH_NONE = 0
AUTH_SYS = 1
AUTH_SHORT = 2

class opaque_auth(object):
	__slots__ = [ 'flavor', 'body' ]
	def check(self):
		pass
		assert self.flavor is not None
		assert self.body is not None
	def __eq__(self, other):
		if not self.flavor == other.flavor: return 0
		if not self.body == other.body: return 0
		return 1
	def __ne__(self, other):
		return not self == other
def pack_opaque_auth(p, o):
	o.check()
	pack_auth_flavor(p, o.flavor)
	p.pack_opaque(o.body)
def unpack_opaque_auth(u):
	o = opaque_auth()
	o.flavor = unpack_auth_flavor(u)
	o.body = u.unpack_opaque()
	o.check()
	return o

def pack_msg_type(p, o):
	p.pack_uint(o)
def unpack_msg_type(u):
	return u.unpack_uint()

CALL = 0
REPLY = 1

def pack_reply_stat(p, o):
	p.pack_uint(o)
def unpack_reply_stat(u):
	return u.unpack_uint()

MSG_ACCEPTED = 0
MSG_DENIED = 1

def pack_accept_stat(p, o):
	p.pack_uint(o)
def unpack_accept_stat(u):
	return u.unpack_uint()

SUCCESS = 0
PROG_UNAVAIL = 1
PROG_MISMATCH = 2
PROC_UNAVAIL = 3
GARBAGE_ARGS = 4
SYSTEM_ERR = 5

def pack_reject_stat(p, o):
	p.pack_uint(o)
def unpack_reject_stat(u):
	return u.unpack_uint()

RPC_MISMATCH = 0
AUTH_ERROR = 1

def pack_auth_stat(p, o):
	p.pack_uint(o)
def unpack_auth_stat(u):
	return u.unpack_uint()

AUTH_OK = 0
AUTH_BADCRED = 1
AUTH_REJECTEDCRED = 2
AUTH_BADVERF = 3
AUTH_REJECTEDVERF = 4
AUTH_TOOWEAK = 5
AUTH_INVALIDRESP = 6
AUTH_FAILED = 7

class authsys_parms(object):
	__slots__ = [ 'stamp', 'machinename', 'uid', 'gid', 'gids' ]
	def check(self):
		pass
		assert self.stamp is not None
		assert self.machinename is not None
		assert self.uid is not None
		assert self.gid is not None
		assert self.gids is not None
	def __eq__(self, other):
		if not self.stamp == other.stamp: return 0
		if not self.machinename == other.machinename: return 0
		if not self.uid == other.uid: return 0
		if not self.gid == other.gid: return 0
		if not self.gids == other.gids: return 0
		return 1
	def __ne__(self, other):
		return not self == other
def pack_authsys_parms(p, o):
	o.check()
	pack_u_int32_t(p, o.stamp)
	p.pack_string(o.machinename)
	pack_u_int32_t(p, o.uid)
	pack_u_int32_t(p, o.gid)
	p.pack_array(o.gids, lambda x: pack_u_int32_t(p, x))
def unpack_authsys_parms(u):
	o = authsys_parms()
	o.stamp = unpack_u_int32_t(u)
	o.machinename = u.unpack_string()
	o.uid = unpack_u_int32_t(u)
	o.gid = unpack_u_int32_t(u)
	o.gids = u.unpack_array(lambda : unpack_u_int32_t(u))
	o.check()
	return o

class mismatch_info_t(object):
	__slots__ = [ 'low', 'high' ]
	def check(self):
		pass
		assert self.low is not None
		assert self.high is not None
	def __eq__(self, other):
		if not self.low == other.low: return 0
		if not self.high == other.high: return 0
		return 1
	def __ne__(self, other):
		return not self == other
def pack_mismatch_info_t(p, o):
	o.check()
	pack_u_int32_t(p, o.low)
	pack_u_int32_t(p, o.high)
def unpack_mismatch_info_t(u):
	o = mismatch_info_t()
	o.low = unpack_u_int32_t(u)
	o.high = unpack_u_int32_t(u)
	o.check()
	return o

class reply_data_t(object):
	__slots__ = [ 'stat', 'results', 'mismatch_info' ]
	def check(self):
		pass
		if self.stat == SUCCESS:
			assert self.results is not None
		elif self.stat == PROG_MISMATCH:
			assert self.mismatch_info is not None
	def __eq__(self, other):
		if not self.stat == other.stat: return 0
		if self.stat == SUCCESS:
			if not self.results == other.results: return 0
		elif self.stat == PROG_MISMATCH:
			if not self.mismatch_info == other.mismatch_info: return 0
		return 1
	def __ne__(self, other):
		return not self == other
def pack_reply_data_t(p, o):
	o.check()
	pack_accept_stat(p, o.stat)
	if o.stat == SUCCESS:
		p.pack_fopaque(0, o.results)
	elif o.stat == PROG_MISMATCH:
		pack_mismatch_info_t(p, o.mismatch_info)
def unpack_reply_data_t(u):
	o = reply_data_t()
	o.stat = unpack_accept_stat(u)
	if o.stat == SUCCESS:
		o.results = u.unpack_fopaque(0)
	elif o.stat == PROG_MISMATCH:
		o.mismatch_info = unpack_mismatch_info_t(u)
	o.check()
	return o

class accepted_reply(object):
	__slots__ = [ 'verf', 'reply_data' ]
	def check(self):
		pass
		assert self.verf is not None
		assert self.reply_data is not None
	def __eq__(self, other):
		if not self.verf == other.verf: return 0
		if not self.reply_data == other.reply_data: return 0
		return 1
	def __ne__(self, other):
		return not self == other
def pack_accepted_reply(p, o):
	o.check()
	pack_opaque_auth(p, o.verf)
	pack_reply_data_t(p, o.reply_data)
def unpack_accepted_reply(u):
	o = accepted_reply()
	o.verf = unpack_opaque_auth(u)
	o.reply_data = unpack_reply_data_t(u)
	o.check()
	return o

class rejected_reply(object):
	__slots__ = [ 'stat', 'mismatch_info', 'astat' ]
	def check(self):
		pass
		assert self.stat is not None
		if self.stat == RPC_MISMATCH:
			assert self.mismatch_info is not None
		elif self.stat == AUTH_ERROR:
			assert self.astat is not None
	def __eq__(self, other):
		if not self.stat == other.stat: return 0
		if self.stat == RPC_MISMATCH:
			if not self.mismatch_info == other.mismatch_info: return 0
		elif self.stat == AUTH_ERROR:
			if not self.astat == other.astat: return 0
		return 1
	def __ne__(self, other):
		return not self == other
def pack_rejected_reply(p, o):
	o.check()
	pack_reject_stat(p, o.stat)
	if o.stat == RPC_MISMATCH:
		pack_mismatch_info_t(p, o.mismatch_info)
	elif o.stat == AUTH_ERROR:
		pack_auth_stat(p, o.astat)
def unpack_rejected_reply(u):
	o = rejected_reply()
	o.stat = unpack_reject_stat(u)
	if o.stat == RPC_MISMATCH:
		o.mismatch_info = unpack_mismatch_info_t(u)
	elif o.stat == AUTH_ERROR:
		o.astat = unpack_auth_stat(u)
	o.check()
	return o

class reply_body(object):
	__slots__ = [ 'stat', 'areply', 'rreply' ]
	def check(self):
		pass
		assert self.stat is not None
		if self.stat == MSG_ACCEPTED:
			assert self.areply is not None
		elif self.stat == MSG_DENIED:
			assert self.rreply is not None
	def __eq__(self, other):
		if not self.stat == other.stat: return 0
		if self.stat == MSG_ACCEPTED:
			if not self.areply == other.areply: return 0
		elif self.stat == MSG_DENIED:
			if not self.rreply == other.rreply: return 0
		return 1
	def __ne__(self, other):
		return not self == other
def pack_reply_body(p, o):
	o.check()
	pack_reply_stat(p, o.stat)
	if o.stat == MSG_ACCEPTED:
		pack_accepted_reply(p, o.areply)
	elif o.stat == MSG_DENIED:
		pack_rejected_reply(p, o.rreply)
def unpack_reply_body(u):
	o = reply_body()
	o.stat = unpack_reply_stat(u)
	if o.stat == MSG_ACCEPTED:
		o.areply = unpack_accepted_reply(u)
	elif o.stat == MSG_DENIED:
		o.rreply = unpack_rejected_reply(u)
	o.check()
	return o

class call_body(object):
	__slots__ = [ 'rpcvers', 'prog', 'vers', 'proc', 'cred', 'verf' ]
	def check(self):
		pass
		assert self.rpcvers is not None
		assert self.prog is not None
		assert self.vers is not None
		assert self.proc is not None
		assert self.cred is not None
		assert self.verf is not None
	def __eq__(self, other):
		if not self.rpcvers == other.rpcvers: return 0
		if not self.prog == other.prog: return 0
		if not self.vers == other.vers: return 0
		if not self.proc == other.proc: return 0
		if not self.cred == other.cred: return 0
		if not self.verf == other.verf: return 0
		return 1
	def __ne__(self, other):
		return not self == other
def pack_call_body(p, o):
	o.check()
	pack_u_int32_t(p, o.rpcvers)
	pack_u_int32_t(p, o.prog)
	pack_u_int32_t(p, o.vers)
	pack_u_int32_t(p, o.proc)
	pack_opaque_auth(p, o.cred)
	pack_opaque_auth(p, o.verf)
def unpack_call_body(u):
	o = call_body()
	o.rpcvers = unpack_u_int32_t(u)
	o.prog = unpack_u_int32_t(u)
	o.vers = unpack_u_int32_t(u)
	o.proc = unpack_u_int32_t(u)
	o.cred = unpack_opaque_auth(u)
	o.verf = unpack_opaque_auth(u)
	o.check()
	return o

class body_t(object):
	__slots__ = [ 'mtype', 'cbody', 'rbody' ]
	def check(self):
		pass
		assert self.mtype is not None
		if self.mtype == CALL:
			assert self.cbody is not None
		elif self.mtype == REPLY:
			assert self.rbody is not None
	def __eq__(self, other):
		if not self.mtype == other.mtype: return 0
		if self.mtype == CALL:
			if not self.cbody == other.cbody: return 0
		elif self.mtype == REPLY:
			if not self.rbody == other.rbody: return 0
		return 1
	def __ne__(self, other):
		return not self == other
def pack_body_t(p, o):
	o.check()
	pack_msg_type(p, o.mtype)
	if o.mtype == CALL:
		pack_call_body(p, o.cbody)
	elif o.mtype == REPLY:
		pack_reply_body(p, o.rbody)
def unpack_body_t(u):
	o = body_t()
	o.mtype = unpack_msg_type(u)
	if o.mtype == CALL:
		o.cbody = unpack_call_body(u)
	elif o.mtype == REPLY:
		o.rbody = unpack_reply_body(u)
	o.check()
	return o

class rpc_msg(object):
	__slots__ = [ 'xid', 'body' ]
	def check(self):
		pass
		assert self.xid is not None
		assert self.body is not None
	def __eq__(self, other):
		if not self.xid == other.xid: return 0
		if not self.body == other.body: return 0
		return 1
	def __ne__(self, other):
		return not self == other
def pack_rpc_msg(p, o):
	o.check()
	pack_u_int32_t(p, o.xid)
	pack_body_t(p, o.body)
def unpack_rpc_msg(u):
	o = rpc_msg()
	o.xid = unpack_u_int32_t(u)
	o.body = unpack_body_t(u)
	o.check()
	return o