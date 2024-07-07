import pyray as pr
import config
from rubik import Rubik
from utils import generate_random_movements

pr.init_window(config.window_w, config.window_h, "Building a Rubik's cube")
rubik_cube = Rubik()
rotation_queue = generate_random_movements(5)
pr.set_target_fps(config.fps)

while not pr.window_should_close():
    rotation_queue, _ = rubik_cube.handle_rotation(rotation_queue)
    pr.update_camera(config.camera, pr.CAMERA_THIRD_PERSON)

    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)
    pr.begin_mode_3d(config.camera)
    pr.draw_grid(20, 1.0)

    for cube in rubik_cube.cubes:
        for part in cube:
            position = pr.Vector3(part.center[0], part.center[1], part.center[2])
            pr.draw_model(part.model, position, 1.0, part.face_color)

    pr.end_mode_3d()
    pr.end_drawing()

pr.close_window()
