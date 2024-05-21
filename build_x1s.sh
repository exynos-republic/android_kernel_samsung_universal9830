make exynos9830-x1sxxx_defconfig \
    O=out \
 	ARCH=arm64 \
	CC=clang \
 	LD=ld.lld \
 	LLVM=1 \
 	LLVM_IAS=1 \
 	CLANG_TRIPLE=aarch64-linux-gnu- \
	CROSS_COMPILE=aarch64-linux-gnu- \ 

# Build Kernel 
./build.sh

# Build Dtb/Dtbo images
./builddt.sh x1s

# Copy Kernel image into install folder
cp out/arch/arm64/boot/Image out/install/Image