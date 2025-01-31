#!/bin/bash

inp_c=$1

clang -S -target arm-none-eabi -mcpu=cortex-m0 -O0 -mthumb -nostdlib -I$(dirname $0)/../code_c/include ${inp_c}

inp_asm="$(basename "${inp_c}" .c).s"

python ./scripts/parm_assembler.py ${inp_asm} $2

rm ${inp_asm}