#!/usr/bin/env python3

"""
Structure for message to be exchanged

typedef struct tMsg {
	int    time;    /* 0..3   int(time.time())   */
	int    index;   /* 0..7   Running sequence   */
	float  value;   /* 8..12  random.random()    */
	char   msg[16]; /* 13..28 String             */
} tMsg;
"""

tMsg = 'i i f 16s'
