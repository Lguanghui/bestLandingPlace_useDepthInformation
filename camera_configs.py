import cv2
import numpy as np
# 内参
# 左摄像头参数
D1 = np.array([[-0.4754237348626463,0.2467561418448715,-2.131526018981568e-05,0.0007070057548779761,-0.06929295740943144]]) #畸变参数
K1 = np.array([[437.0781246995733, 0, 312.6535420708854],
               [0, 437.4960550191722, 196.7985132931464],
               [0, 0, 1]])  # 内参矩阵
# 右摄像头参数
D2 = np.array([[-0.479914,0.262544,-0.00163847,-0.00186997,-0.0834569]])
K2 = np.array([[434.3348694698608, 0, 327.2907536067709], 
               [0, 434.6378194914058, 207.9990223436816], 
               [0, 0, 1]])

# 外参
R = np.array([[0.9999712137546342, 0.001262155155282626, -0.007481886556726869], 
              [-0.001303594214553154, 0.9999838248957293, -0.005536297411727022], 
              [0.007474777870112282, 0.005545891386540605, 0.9999566844541423]])       # 旋转矩阵
T = np.array([-79.96929333115614, 0.06211033022079716, -0.8373146527573727])      # 平移矩阵
 
size = (640, 400)  # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(K1, D1, K2, D2, size, R, T)
 
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(K1, D1, R1, P1, size, cv2.CV_32FC1)
right_map1, right_map2 = cv2.initUndistortRectifyMap(K2, D2, R2, P2, size, cv2.CV_32FC1)
