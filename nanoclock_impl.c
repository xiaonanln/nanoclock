#include <time.h>
#include <stdint.h>

uint64_t clock_impl(void)
{
	struct timespec ts;
	clock_gettime(CLOCK_REALTIME, &ts);
	return (uint64_t)ts.tv_sec * 1000000000UL + ts.tv_nsec;
}

