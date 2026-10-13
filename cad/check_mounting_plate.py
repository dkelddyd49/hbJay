"""만들어진 STEP 파일의 크기, 부피, 구멍을 검사한다."""

from pathlib import Path

from cadgen import build123d as bd
from cadgen import read_step

shape = read_step(Path(__file__).parent / "STEP" / "mounting_plate.step")
box = shape.bounding_box()
holes = [f for f in shape.faces() if f.geom_type == bd.GeomType.CYLINDER and f.radius < 5]

print(f"외곽 크기: {box.size.X:.1f} x {box.size.Y:.1f} x {box.size.Z:.1f} mm")
print(f"부피: {shape.volume:.0f} mm^3")
print(f"구멍 개수: {len(holes)}, 지름: {sorted({round(f.radius * 2, 2) for f in holes})} mm")
