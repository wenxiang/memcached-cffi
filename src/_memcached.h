typedef struct memcached_st memcached_st;
typedef enum memcached_return_t memcached_return_t;
typedef int... time_t;

memcached_st *memcached(const char *string, size_t string_length);
memcached_return_t libmemcached_check_configuration(const char *option_string, size_t length, char *error_buffer, size_t error_buffer_size);
const char *memcached_strerror(const memcached_st *ptr, memcached_return_t rc);
char * memcached_get(memcached_st *ptr, const char *key, size_t key_length, size_t *value_length, uint32_t *flags, memcached_return_t *error);
memcached_return_t memcached_set(memcached_st *ptr, const char *key, size_t key_length, const char *value, size_t value_length, time_t expiration, uint32_t flags);