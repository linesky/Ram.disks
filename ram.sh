mkdir /mnt/ramdisk1 2> /dev/null
mount -t tmpfs -o size=80M tmpfs /mnt/ramdisk1
mkdir /mnt/ramdisk1/tmp 2> /dev/null
cp /bin/bash /mnt/ramdisk1
cp /bin/sh /mnt/ramdisk1
cp /bin/gcc /mnt/ramdisk1
cp /bin/nasm /mnt/ramdisk1 
cp /bin/objcopy /mnt/ramdisk1
cp ./* /mnt/ramdisk1
mp=$(pwd)
cd /mnt/ramdisk1
./bash
cd $mp
cp /mnt/ramdisk1/* .
