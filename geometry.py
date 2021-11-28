import open3d as o3d
import numpy as np


def create_cylinder(cylinder_coefficients, height=5, step=0.5, vis=False):
    """

    Args:
        cylinder_coefficients: A dictionary containing cylindrical coefficients:
                                (r,x0,y0,z0,a,b,c
                                r the radius of the cylinder
                                x0,y0,z0 the Starting center of the cylinder
                                a, b, c: axis coefficient of the cylinder)
        height: height_ of the cylinder
        step: Density of cylinder point cloud
        vis: whether to visualize the cylinder

    Returns:
        numpy form of the cylinder point cloud: n x 3
    References:
        https://blog.csdn.net/inerterYang/article/details/111998278
        https://blog.csdn.net/inerterYang/article/details/111304307

    @Author: Carlos_Lee 202111

    """
    r = cylinder_coefficients['r']
    x0 = cylinder_coefficients['x0']
    y0 = cylinder_coefficients['y0']
    z0 = cylinder_coefficients['z0']
    a = cylinder_coefficients['a']
    b = cylinder_coefficients['b']
    c = cylinder_coefficients['c']

    angle_ = np.arange(0, 2 * np.pi, step / 10).reshape(-1, 1)

    v = np.arange(0, height, step)
    npy = []
    for i in v:
        x = x0 + r * b / np.power(a * a + b * b, 0.5) * np.cos(angle_) + \
            r * a * c / np.power(a * a + b * b, 0.5) / np.power(a * a + b * b + c * c, 0.5) * \
            np.sin(angle_) + a / np.power(a * a + b * b + c * c, 0.5) * i

        y = y0 - r * a / np.power(a * a + b * b, 0.5) * np.cos(angle_) + \
            r * b * c / np.power(a * a + b * b, 0.5) / np.power(a * a + b * b + c * c, 0.5) * \
            np.sin(angle_) + b / np.power(a * a + b * b + c * c, 0.5) * i

        z = z0 - r * np.power(a * a + b * b, 0.5) / np.power(a * a + b * b + c * c, 0.5) * np.sin(angle_) + \
            c / np.power(a * a + b * b + c * c, 0.5) * i

        npy.append(np.concatenate([x, y, z], axis=-1))

    npy = np.concatenate(npy, axis=0)
    if vis:
        coordinate_ = o3d.geometry.TriangleMesh.create_coordinate_frame(size=height / 2., origin=[0.0, 0.0, 0.0])
        pcd_ = o3d.geometry.PointCloud()
        pcd_.points = o3d.utility.Vector3dVector(npy)
        o3d.visualization.draw_geometries([coordinate_, pcd_], window_name="generate cylinder",
                                          width=960, height=900, left=960, top=100)
    return npy


def create_line(line_coefficients, height=5, step=0.5, vis=False):
    """

    Args:
        line_coefficients: A dictionary containing cylindrical coefficients:
                                (r, x0, y0, z0_, a, b, c
                                r not used: to keep the same form between cylinder coefficients and line coefficients,
                                so that a same group of coefficients can generate a cylinder and a line, then the line is
                                the Central axis of the cylinder
                                x0,y0,z0 the Starting center of the cylinder
                                a, b, c the axis coefficient of the cylinder)
        height: length of the line
        step: Density of line point cloud
        vis: whether to visualize the cylinder

    Returns:
        numpy form of the line point cloud: n x 3

    @Author: Carlos_Lee 202111
    """
    x0 = line_coefficients['x0']
    y0 = line_coefficients['y0']
    z0 = line_coefficients['z0']
    a = line_coefficients['a']
    b = line_coefficients['b']
    c = line_coefficients['c']

    v = np.arange(0, height, step)
    npy = np.zeros((len(v), 3))

    for idx_, i in enumerate(v):
        x = x0 + a / np.power(a * a + b * b + c * c, 0.5) * i
        y = y0 + b / np.power(a * a + b * b + c * c, 0.5) * i
        z = z0 + c / np.power(a * a + b * b + c * c, 0.5) * i

        npy[idx_] = [x, y, z]
    if vis:
        coordinate_ = o3d.geometry.TriangleMesh.create_coordinate_frame(size=height / 2., origin=[0.0, 0.0, 0.0])
        pcd_ = o3d.geometry.PointCloud()
        pcd_.points = o3d.utility.Vector3dVector(npy)
        o3d.visualization.draw_geometries([coordinate_, pcd_], window_name="generate line",
                                          width=960, height=900, left=960, top=100)

    return npy

