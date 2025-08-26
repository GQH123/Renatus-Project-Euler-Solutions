import math

EPS = 1e-6


def get_vector_angle_by_arccos(v1, v2):
    return math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / (math.sqrt(v1[0]**2 + v1[1]**2) * math.sqrt(v2[0]**2 + v2[1]**2)))


def judge_point_in_triangle(p, t):
    v1 = [p[0] - t[0][0], p[1] - t[0][1]]
    v2 = [p[0] - t[1][0], p[1] - t[1][1]]
    v3 = [p[0] - t[2][0], p[1] - t[2][1]]
    angle1 = get_vector_angle_by_arccos(v1, v3)
    angle2 = get_vector_angle_by_arccos(v2, v3)
    angle3 = get_vector_angle_by_arccos(v1, v2)

    if abs(angle1 + angle2 + angle3 - 2 * math.pi) < EPS:
        return True
    else:
        return False


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        triangles = [[float(x) for x in line.split(',')] for line in f.read().split('\n') if line]
        for triangle in triangles:
            assert len(triangle) == 6
        triangles = [[(tri[0], tri[1]), (tri[2], tri[3]), (tri[4], tri[5])] for tri in triangles]
    count = 0
    for triangle in triangles:
        # print(triangle)
        if judge_point_in_triangle([0, 0], triangle):
            count += 1
    print(count)
    pass