
/*
===============================================================================
 Name        : filter.h
 Author      : Israel Pavelek, Cesar Fuoco
 Version     : 1.0
 Copyright   : $(copyright)
 Description : main definition
===============================================================================
*/

#ifndef LOWPASS_H_
#define LOWPASS_H_

#include <stdint.h>

// FIR Equirriple
#define FIR_TAP_NUM 37

// FIR Least Squares
//#define FIR_TAP_NUM 77

// IIR Butterworth
#define IIR_TAP_NUM 5


#define SAMPLES_PER_BLOCK 1000

extern int32_t fir_taps[];
extern int32_t iir_taps[];
extern float float_fir_taps[];
extern float float_iir_taps[];


typedef enum{
	NO_PROCESAR,
	PROCESAR_A,
	PROCESAR_B,

}procesar_type_t;


#endif /* LOWPASS_H_ */
