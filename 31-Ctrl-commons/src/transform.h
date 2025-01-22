/**
 * @file        abc2AB.h
 * @author     
 * @date       01 Jan 2024
 * 
 * @brief      header file for Clarke and Park transformation
 * 
 *      This header file implements the Clarke and Park transformation.
 */ 


#ifndef TRANSFORM_H_
    #define TRANSFORM_H_

#ifdef __cplusplus
extern "C" {
#endif

typedef struct
{
    double     a;
    double     b;
    double     c;
} ABC_t;

typedef struct
{
    double     alpha;
    double     beta;
    double     zero_AB;
} AB0_t;

typedef struct
{
    double     d;
    double     q;
    double     zero_dq;
} DQ0_t;

typedef struct
{
    ABC_t       abc;
    AB0_t       AB0;
    DQ0_t       dq0;
} Transform_Obj_t;


/**
 * @brief      Clarke transformation - amplitude invariant
 *
 * @param      T_inst  The instance of the transformation object
 * @param      numSensors  The number of sensors, 2(phase a,c) or 3(phase a,b,c)
 */
void abc2AB0(Transform_Obj_t *T_inst, int numSensors);

/**
 * @brief      Inverse Clarke transformation - amplitude invariant
 *
 * @param      T_inst  The instance of the transformation object
 * @param      numSensors  The number of sensors, 2(phase a,c) or 3(phase a,b,c)
 */
void AB02abc(Transform_Obj_t *T_inst);

/**
 * @brief      Park transformation
 *
 * @param      T_inst  The instance of the transformation object
 * @param      theta_e  The electrical angle
 */
void AB02dq0(Transform_Obj_t *T_inst, double theta_e);


/**
 * @brief      Inverse Park transformation
 *
 * @param      T_inst  The instance of the transformation object
 * @param      theta_e  The electrical angle
 */
void dq02AB0(Transform_Obj_t *T_inst, double theta_e);



#ifdef __cplusplus
}
#endif

#endif //<- !defined TRANSFORM_H_