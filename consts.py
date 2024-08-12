import car_consts
import numpy as np

#  hyper-parameters
LF_K = 0.05  # look forward gain
LFC = 1.2  # [m] look-ahead distance
V_KP = 1.0  # speed proportional gain
DELTA_T = 0.1  # [s] time tick
TARGETED_SPEED = 1.0  # [m/s]
T = 100.0  # max simulation time
WB = car_consts.wheelbase 
MAX_STEER = car_consts.max_steering_angle_rad  # maximum steering angle [rad]
MAX_DSTEER = car_consts.max_dt_steering_angle  # maximum steering speed [rad/s]
MAX_SPEED = car_consts.max_linear_velocity  # maximum speed [m/s]
MIN_SPEED = car_consts.min_linear_velocity  # minimum speed [m/s]
MAX_ACCEL = 1.0  # maximum accel [m/ss]
SENSE_CONE_RADIUS = 20
SENSE_CONE_ANGLE = np.pi/4

# Kino RRT params
KINORRT_TRIES           = 4
KINORRT_ITER            = 320
KINORRT_MAX_STEP_SIZE   = 25


NEXT_IDX = 10

RESOLUTION = 0.05000000074505806
INFLATION = 0.2/RESOLUTION