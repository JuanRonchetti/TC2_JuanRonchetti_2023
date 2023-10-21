/*
===============================================================================
 Name        : filter.c
 Authors     : Israel Pavelek, Cesar Fuoco
 Version     : 1.0
 Copyright   : $(copyright)
 Description : main definition
===============================================================================
*/

#include "filter.h"
#include <stdint.h>

// ************ FIR Equirriple ************
int32_t fir_taps[FIR_TAP_NUM] = {0};
float float_fir_taps[FIR_TAP_NUM] = {
		-0.0516038426863699,	-0.007634315704683342,	-0.006788611900933189,	-0.004873327093108144,
		-0.0018349926008721202,	0.002330954717100911,	0.007574850808482849,	0.01379050733003701,
		0.020816491713683247,	0.028440796724530065,	0.03640907774635375,	0.0444355904023601,
		0.052216634226004775,	0.05944559238719488,	0.0658285357830471,		0.07109969831742727,
		0.07503570077699821,	0.07746758787834511,	0.07829012297251628,	0.07746758787834511,
		0.07503570077699821,	0.07109969831742727,	0.0658285357830471,		0.05944559238719488,
		0.052216634226004775,	0.0444355904023601,		0.03640907774635375,	0.028440796724530065,
		0.020816491713683247,	0.01379050733003701,	0.007574850808482849,	0.002330954717100911,
		-0.0018349926008721202,	-0.004873327093108144,	-0.006788611900933189,	-0.007634315704683342,
		-0.0516038426863699
};

// ********** FIR Least Squares ***********
/*

int32_t fir_taps[FIR_TAP_NUM] = {0};
float float_fir_taps[FIR_TAP_NUM] = {
-0.0001709565280916023  -0.0005703876216335467  -0.00090067539029671
-0.000664339442453209    0.00026967600140912086  0.0012750588785842639
 0.0014521438568201924   0.0007211193468302557   0.00021537218155155122
 0.0010773446156862488   0.0026797828836463136   0.002581546645077922
-0.0009349970882621784  -0.006145774904619687   -0.008582135398567944
-0.005485632291899778    0.0004902637801327739   0.0033254788081690657
 0.0004843517406661728  -0.0029005106635890767   0.0012466952821684684
 0.013743538322120118    0.023974672190035837    0.018942726572470377
-0.0018656907040149524  -0.02250767110300779    -0.025229064010471286
-0.010639590322499008   -0.000253473106037819   -0.01374670499214893
-0.041873510555710404   -0.046747797663802354    0.0025831755169481267
 0.08992998228133772     0.15068566241386827     0.12098649407683912
-0.0015978067809712913  -0.14322748519730083     0.9165495879953738
-0.14322748519730083    -0.0015978067809712913   0.12098649407683912
 0.15068566241386827     0.08992998228133772     0.0025831755169481267
-0.046747797663802354   -0.041873510555710404   -0.01374670499214893
-0.000253473106037819   -0.010639590322499008   -0.025229064010471286
-0.02250767110300779    -0.0018656907040149524   0.018942726572470377
 0.023974672190035837    0.013743538322120118    0.0012466952821684684
-0.0029005106635890767   0.0004843517406661728   0.0033254788081690657
 0.0004902637801327739  -0.005485632291899778   -0.008582135398567944
-0.006145774904619687   -0.0009349970882621784   0.002581546645077922
 0.0026797828836463136   0.0010773446156862488   0.00021537218155155122
 0.0007211193468302557   0.0014521438568201924   0.0012750588785842639
 0.00026967600140912086 -0.000664339442453209   -0.00090067539029671
-0.0005703876216335467  -0.0001709565280916023
};

*/

// ************ IIR Butterworth ***********
int32_t iir_taps[IIR_TAP_NUM] = {0};
float float_iir_taps[IIR_TAP_NUM] = {
		0.010419890902565022,	0.020839781805130044,	0.010419890902565022,
		1.6911935001269052,		-0.7328730637371653}; // Los coeficientes a con signo cambiado






