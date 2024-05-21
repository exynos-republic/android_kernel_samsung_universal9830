#!/bin/bash

# Check device arg
if [ -z "$1" ]; then
  echo "Usage: $0 <device>"
  exit 1
fi

device=$1

mkdir -p out/install

./toolchain/mkdtimg cfg_create out/install/dtb.img dtconfigs/exynos9830.cfg -d out/arch/arm64/boot/dts/exynos
./toolchain/mkdtimg cfg_create out/install/dtbo.img dtconfigs/${device}.cfg -d out/arch/arm64/boot/dts/samsung