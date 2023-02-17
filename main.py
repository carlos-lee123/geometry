import open3d as o3d
import geometry

if __name__ == "__main__":
    cylinder_coefficients = {'r': 2.0, 'x0': 0, 'y0': 0, 'z0': 0, 'a': 1, 'b': 1, 'c': 0}
    cylinder_npy = geometry.create_cylinder(cylinder_coefficients=cylinder_coefficients, height=5, step=0.05, vis=False)
    pcd_cylinder = o3d.geometry.PointCloud()
    pcd_cylinder.points = o3d.utility.Vector3dVector(cylinder_npy)
    pcd_cylinder.paint_uniform_color([1, 0, 0])

    cylinder_vertical_coefficients = {'r': 5.0, 'x0': 0, 'y0': 0, 'z0': 0}
    cylinder_npy_vertical = geometry.create_cylinder_vertical(cylinder_coefficients=cylinder_vertical_coefficients, height=5, step=0.05, vis=False)
    pcd_cylinder_vertical = o3d.geometry.PointCloud()
    pcd_cylinder_vertical.points = o3d.utility.Vector3dVector(cylinder_npy_vertical)
    pcd_cylinder_vertical.paint_uniform_color([0, 1, 0])


    line_coefficients = {'r': 2.0, 'x0': -2, 'y0': -2, 'z0': 0, 'a': 1, 'b': 1, 'c': 0}
    line_npy = geometry.create_line(line_coefficients=line_coefficients, height=10, step=0.05, vis=False)
    pcd_line = o3d.geometry.PointCloud()
    pcd_line.points = o3d.utility.Vector3dVector(line_npy)
    pcd_line.paint_uniform_color([0, 0, 0])

    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=4, origin=[0.0, 0.0, 0.0])
    o3d.visualization.draw_geometries(
        [coordinate, pcd_line, pcd_cylinder,pcd_cylinder_vertical],
        window_name="cylinder line",
        width=960, height=900, left=960, top=100)

    # You can modify the cylinder_coefficients to generate any spatial cylinder, for example:
    cylinder_coefficients2 = {'r': 2.0, 'x0': -2, 'y0': -2, 'z0': 0, 'a': 1, 'b': -3, 'c': 0}
    cylinder_npy2 = geometry.create_cylinder(cylinder_coefficients=cylinder_coefficients2, height=5, step=0.05,
                                             vis=False)
    pcd_cylinder2 = o3d.geometry.PointCloud()
    pcd_cylinder2.points = o3d.utility.Vector3dVector(cylinder_npy2)
    pcd_cylinder2.paint_uniform_color([1, 1, 0])

    # pcd_cylinder2 is the yellow one,pcd_cylinder is the red one
    o3d.visualization.draw_geometries(
        [coordinate, pcd_cylinder, pcd_cylinder2],
        window_name="cylinder",
        width=960, height=900, left=960, top=100)
