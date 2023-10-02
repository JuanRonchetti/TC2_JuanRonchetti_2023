################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/Common/Source/math_helper.c 

C_DEPS += \
./src/Common/Source/math_helper.d 

OBJS += \
./src/Common/Source/math_helper.o 


# Each subdirectory must supply rules for building sources it contributes
src/Common/Source/%.o: ../src/Common/Source/%.c src/Common/Source/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DNDEBUG -D__CODE_RED -DARM_MATH_CM4 -D__FPU_PRESENT=1 -I../inc -I../inc_cmsis -O2 -g3 -c -fmessage-length=0 -fno-builtin -ffunction-sections -fdata-sections -fsingle-precision-constant -fno-strict-aliasing -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=softfp -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-src-2f-Common-2f-Source

clean-src-2f-Common-2f-Source:
	-$(RM) ./src/Common/Source/math_helper.d ./src/Common/Source/math_helper.o

.PHONY: clean-src-2f-Common-2f-Source

