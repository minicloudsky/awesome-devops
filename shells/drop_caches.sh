#!/bin/bash

# free pagecache
echo 1 > /proc/sys/vm/drop_caches

# free recalimable slab objects (include dentries and inodes)
echo 2 > /proc/sys/vm/drop_caches

# free slab objects and pagecache
echo 3 > /proc/sys/vm/drop_caches

