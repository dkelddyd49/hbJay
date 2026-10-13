"""M8 볼트 구멍 4개가 있는 마운팅 플레이트 (단위: mm)."""

from cadgen import build123d as bd
from cadgen import step, stl

# 플레이트 크기
LENGTH = 100.0  # X 방향 길이
WIDTH = 80.0  # Y 방향 폭
THICKNESS = 10.0  # 두께
CORNER_RADIUS = 5.0  # 모서리 둥글기

# M8 볼트 구멍
M8_CLEARANCE = 9.0  # M8 틈새 구멍 지름 (ISO 273 보통 등급)
HOLE_PITCH_X = 80.0  # 구멍 중심 간 거리 (X)
HOLE_PITCH_Y = 60.0  # 구멍 중심 간 거리 (Y)


@stl(out="../STL/mounting_plate.stl")
@step(out="../STEP/mounting_plate.step")
def mounting_plate():
    # 1) 사각 판을 만들고 세로 모서리를 둥글게 깎는다
    plate = bd.Box(LENGTH, WIDTH, THICKNESS)
    vertical_edges = plate.edges().filter_by(bd.Axis.Z)
    plate = bd.fillet(vertical_edges, CORNER_RADIUS)

    # 2) 네 모서리 위치에 관통 구멍을 뚫는다
    for x in (-HOLE_PITCH_X / 2, HOLE_PITCH_X / 2):
        for y in (-HOLE_PITCH_Y / 2, HOLE_PITCH_Y / 2):
            hole = bd.Pos(x, y, 0) * bd.Cylinder(M8_CLEARANCE / 2, THICKNESS)
            plate = plate - hole

    plate.label = "mounting_plate"
    return plate


if __name__ == "__main__":
    mounting_plate()
