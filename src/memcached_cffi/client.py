from .utils import ensure_bytes
from ._memcached import lib, ffi

class Client(object):
	def __init__(self, servers):
		args = ['--BINARY-PROTOCOL', '--HASH=crc']
		args += ['--SERVER=' + s for s in sorted(servers)]

		options = ensure_bytes(' '.join(args))

		success, err = self.check_config(options)
		if not success:
			raise ValueError(err)

		self.memcached = lib.memcached(options, len(options))

	def check_config(self, options):
		err = ffi.new("char[1000]")
		res = lib.libmemcached_check_configuration(options, len(options), err, 1000)
		return res == 0, ffi.string(err)

	def get(self, key):
		value_length = ffi.new("size_t *")
		flags = ffi.new("uint32_t *")
		error = ffi.new("memcached_return_t *")
		key_b = ensure_bytes(key)
		val = lib.memcached_get(self.memcached, key_b, len(key_b),
			value_length, flags, error)

		if val == ffi.NULL:
			return None
		else:
			return ffi.unpack(val, value_length[0])

	def set(self, key, value, ttl=0):
		key_b = ensure_bytes(key)
		value_b = ensure_bytes(value)
		ret = lib.memcached_set(self.memcached, key_b, len(key), value_b, len(value_b), ttl, 0)
		return ret == 0


