def move_to(x, y):
    """
    Start a new contour at position (x, y).\n
    SVG: M x y
    :param x: The x coordinate of the start of the new contour
    :param y: The y coordinate of the start of the new contour
    :return: moveTo(x, y)
    """
    return f'moveTo({x}f, {y}f)'


def move_to_relative(dx, dy):
    """
    Start a new contour at the offset (dx, dy) relative to the last path position.\n
    SVG: m dx dy
    :param dx: The x offset of the start of the new contour, relative to the last path position
    :param dy: The y offset of the start of the new contour, relative to the last path position
    :return: moveToRelative(dx, dy)
    """
    return f'moveToRelative({dx}f, {dy}f)'


def line_to(x, y):
    """
    Add a line from the last point to the position (x, y). If no contour has been created by calling move_to first, the origin of the line is set to (0, 0).\n
    SVG: L x y
    :param x: The x coordinate of the end of the line
    :param y: The y coordinate of the end of the line
    :return: lineTo(x, y)
    """
    return f'lineTo({x}f, {y}f)'


def line_to_relative(dx, dy):
    """
    Add a line from the last point to the offset (dx, dy) relative to the last point. If no contour has been created by calling move_to first, the origin of the line is set to (0, 0).\n
    SVG: l dx dy
    :param dx: The x offset of the end of the line, relative to the last path position
    :param dy: The y offset of the end of the line, relative to the last path position
    :return: lineToRelative(dx, dy)
    """
    return f'lineToRelative({dx}f, {dy}f)'


def horizontal_line_to(x):
    """
    Add a line from the last point to the position (x, oy), where oy is the y coordinate of the last point. If no contour has been created by calling move_to first, the origin of the line is set to (0, 0).\n
    SVG: H x
    :param x: The x coordinate of the end of the line
    :return: horizontalLineTo(x)
    """
    return f'horizontalLineTo({x}f)'


def horizontal_line_to_relative(dx):
    """
    Add a line from the last point to the position (dx + ox, oy), where ox and oy are the x and y coordinates of the last point. If no contour has been created by calling move_to first, the origin of the line is set to (0, 0).\n
    SVG: h dx
    :param dx: The x offset of the end of the line, relative to the last path position
    :return: horizontalLineToRelative(dx)
    """
    return f'horizontalLineToRelative({dx}f)'


def vertical_line_to(y):
    """
    Add a line from the last point to the position (ox, y), where ox is the x coordinate of the last point. If no contour has been created by calling move_to first, the origin of the line is set to (0, 0).\n
    SVG: V y
    :param y: The y coordinate of the end of the line
    :return: verticalLineTo(y)
    """
    return f'verticalLineTo({y}f)'


def vertical_line_to_relative(dy):
    """
    Add a line from the last point to the position (ox, dy + oy), where ox and oy are the x and y coordinates of the last point. If no contour has been created by calling move_to first, the origin of the line is set to (0, 0).\n
    SVG: v dy
    :param dy: The y coordinate of the end of the line, relative to the last path position
    :return: verticalLineToRelative(dy)
    """
    return f'verticalLineToRelative({dy}f)'


def close():
    """
    Closes the current contour.\n
    SVG: Z or z
    :return: close()
    """
    return 'close()'


def curve_to(x1, y1, x2, y2, x, y):
    """
    Add a cubic Bézier from the last point to the position (x3, y3), approaching the control points (x1, y1) and (x2, y2). If no contour has been created by calling move_to first, the origin of the line is set to (0, 0).\n
    SVG: C x1 x2 y1 y2 x y
    :param x1: The x coordinate of the first control point of the cubic curve
    :param y1: The y coordinate of the first control point of the cubic curve
    :param x2: The x coordinate of the second control point of the cubic curve
    :param y2: The y coordinate of the second control point of the cubic curve
    :param x: The x coordinate of the end point of the cubic curve
    :param y: The y coordinate of the end point of the cubic curve
    :return: curveTo(x1, y1, x2, y2, x, y)
    """
    return f'curveTo({x1}f, {y1}f, {x2}f, {y2}f, {x}f, {y}f)'


def curve_to_relative(dx1, dy1, dx2, dy2, dx, dy):
    """
    Add a cubic Bézier. If no contour has been created by calling moveTo first, the origin of the curve is set to (0, 0). The cubic Bézier control and end points are defined by offsets relative to the last point.\n
    SVG: c dx1 dy1 dx2 dy2 dx dy
    :param dx1: The x offset of the first control point of the cubic curve, relative to the last path position
    :param dy1: The y offset of the first control point of the cubic curve, relative to the last path position
    :param dx2: The x offset of the second control point of the cubic curve, relative to the last path position
    :param dy2: The y offset of the second control point of the cubic curve, relative to the last path position
    :param dx: The x offset of the end point of the cubic curve, relative to the last path position
    :param dy: The y offset of the end point of the cubic curve, relative to the last path position
    :return: curveToRelative(dx1, dy1, dx2, dy2, dx, dy)
    """
    return f'curveToRelative({dx1}f, {dy1}f, {dx2}f, {dy2}f, {dx}f, {dy}f)'


def reflective_curve_to(x2, y2, x, y):
    """
    Add a cubic Bézier from the last point to the position (x2, y2). The first control point is the reflection of the second control point of the previous command. If there is no previous command or the previous command is not a cubic Bézier, the first control point is set to the last path position. The second control point is defined by (x1, y1). If no contour has been created by calling move_to first, the origin of the curve is set to (0, 0).\n
    SVG: S x2 y2 x y
    :param x2: The x coordinate of the second control point of the cubic curve
    :param y2: The y coordinate of the second control point of the cubic curve
    :param x: The x coordinate of the end point of the cubic curve
    :param y: The y coordinate of the end point of the cubic curve
    :return: reflectiveCurveTo(x2, y2, x, y)
    """
    return f'reflectiveCurveTo({x2}f, {y2}f, {x}f, {y}f)'


def reflective_curve_to_relative(dx2, dy2, dx, dy):
    """
    Add a cubic Bézier. If no contour has been created by calling move_to first, the origin of the curve is set to (0, 0). The cubic Bézier second control point and end points are defined by offsets relative to the last point. The reflective nature of the curve is described in reflectiveCurveTo.\n
    SVG: s dx2 dy2, dx dy
    :param dx2: The x offset of the second control point of the cubic curve, relative to the last path position
    :param dy2: The y offset of the second control point of the cubic curve, relative to the last path position
    :param dx: The x offset of the end point of the cubic curve, relative to the last path position
    :param dy: The y offset of the end point of the cubic curve, relative to the last path position
    :return: reflectiveCurveToRelative(dx2, dy2, dx, dy)
    """
    return f'reflectiveCurveToRelative({dx2}f, {dy2}f, {dx}f, {dy}f)'


def quadratic_curve_to(x1, y1, x, y):
    """
    Add a quadratic Bézier from the last point to the position (x2, y2), approaching the control point (x1, y1). If no contour has been created by calling move_to first, the origin of the curve is set to (0, 0).\n
    SVG: Q x1 y1, x y
    :param x1: The x coordinate of the control point of the quadratic curve
    :param y1: The y coordinate of the control point of the quadratic curve
    :param x: The x coordinate of the end point of the quadratic curve
    :param y: The y coordinate of the end point of the quadratic curve
    :return: quadTo(x1, y1, x, y)
    """
    return f'quadTo({x1}f, {y1}f, {x}f, {y}f)'


def quadratic_curve_to_relative(dx1, dy1, dx, dy):
    """
    Add a quadratic Bézier. If no contour has been created by calling move_to first, the origin of the curve is set to (0, 0). The control point and end point of the curve are defined by offsets relative to the last point.\n
    SVG: q dx1 dy1, dx dy
    :param dx1: The x offset of the control point of the quadratic curve, relative to the last path position
    :param dy1: The y offset of the control point of the quadratic curve, relative to the last path position
    :param dx: The x offset of the end point of the quadratic curve, relative to the last path position
    :param dy: The y offset of the end point of the quadratic curve, relative to the last path position
    :return: quadToRelative(dx1, dy1, dx, dy)
    """
    return f'quadToRelative({dx1}f, {dy1}f, {dx}f, {dy}f)'


def reflective_quadratic_curve_to(x, y):
    """
    Add a quadratic Bézier from the last point to the position (x1, y1). The control point is the reflection of the control point of the previous command. If there is no previous command or the previous command is not a quadratic Bézier, the control point is set to the last path position. If no contour has been created by calling move_to first, the origin of the curve is set to (0, 0).\n
    SVG: T x y
    :param x: The x coordinate of the end point of the quadratic curve
    :param y: The y coordinate of the end point of the quadratic curve
    :return: reflectiveQuadCurveTo(x, y)
    """
    return f'reflectiveQuadTo({x}f, {y}f)'


def reflective_quadratic_curve_to_relative(dx, dy):
    """
    Add a quadratic Bézier. If no contour has been created by calling move_to first, the origin of the curve is set to (0, 0). The quadratic Bézier end point is defined by an offset relative to the last point. The reflective nature of the curve is described in reflectiveQuadTo.\n
    SVG: t dx dy
    :param dx: The x offset of the end point of the quadratic curve, relative to the last path position
    :param dy: The y offset of the end point of the quadratic curve, relative to the last path position
    :return: reflectiveQuadToRelative(dx, dy)
    """
    return f'reflectiveQuadToRelative({dx}f, {dy}f)'


def arc_to(rx, ry, x_axis_rotation, large_arc_flag, sweep_flag, x, y):
    """
    Add an elliptical arc from the last point to the position (x, y). If no contour has been created by calling move_to first, the origin of the arc is set to (0, 0).\n
    The ellipse is defined by 3 parameters:\n
    - rx and ry to define the size of the ellipse\n
    - x_axis_rotation to define the orientation (as an X-axis rotation) of the ellipse\n
    In most situations, there are four arc candidates that can be drawn from the origin to (x, y). Which of the arcs is used is influenced by large_arc_flag and sweep_flag.\n
    When large_arc_flag is set to true, the added arc will be chosen amongst the two candidates that represent an arc sweep greater than or equal to 180 degrees.\n
    When sweep_flag is set to true, the added arc will be chosen amongst the two candidates with a positive-angle direction (counter-clockwise)\n
    SVG: A rx ry x-axis-rotation large-arc-flag sweep-flag x y
    :param rx: The horizontal radius of the ellipse
    :param ry: The vertical radius of the ellipse
    :param x_axis_rotation: The rotation of the ellipse around the X-axis, in degrees
    :param large_arc_flag: Defines whether to use an arc candidate with a sweep greater than or equal to 180 degrees
    :param sweep_flag: Defines whether to use an arc candidate that's counter-clockwise or not
    :param x: The x coordinate of the end point of the arc
    :param y: The y coordinate of the end point of the arc
    :return: arcTo(rx, ry, x_axis_rotation, large_arc_flag, sweep_flag, x, y)
    """
    return f'arcTo({rx}f, {ry}f, {x_axis_rotation}f, {large_arc_flag}, {sweep_flag}, {x}f, {y}f)'


def arc_to_relative(rx, ry, x_axis_rotation, large_arc_flag, sweep_flag, dx, dy):
    """
    Add an elliptical arc. If no contour has been created by calling move_to first, the origin of the arc is set to (0, 0). The arc Bézier end point is defined by an offset relative to the last point.\n
    The ellipse is defined by 3 parameters:\n
    - rx and ry to define the size of the ellipse\n
    - x_axis_rotation to define the orientation (as an X-axis rotation) of the ellipse\n
    In most situations, there are four arc candidates that can be drawn from the origin to the end point. Which of the arcs is used is influenced by large_arc_flag and sweep_flag.\n
    When large_arc_flag is set to true, the added arc will be chosen amongst the two candidates that represent an arc sweep greater than or equal to 180 degrees.\n
    When sweep_flag is set to true, the added arc will be chosen amongst the two candidates with a positive-angle direction (counter-clockwise)\n
    SVG: a rx ry x-axis-rotation large-arc-flag sweep-flag dx dy
    :param rx: The horizontal radius of the ellipse
    :param ry: The vertical radius of the ellipse
    :param x_axis_rotation: The rotation of the ellipse around the X-axis, in degrees
    :param large_arc_flag: Defines whether to use an arc candidate with a sweep greater than or equal to 180 degrees
    :param sweep_flag: Defines whether to use an arc candidate that's counter-clockwise or not
    :param dx: The x offset of the end point of the arc, relative to the last path position
    :param dy: The y offset of the end point of the arc, relative to the last path position
    :return: arcToRelative(rx, ry, x_axis_rotation, large_arc_flag, sweep_flag, x, y)
    """
    return f'arcToRelative({rx}f, {ry}f, {x_axis_rotation}f, {large_arc_flag}, {sweep_flag}, {dx}f, {dy}f)'


def get_parameter_count(identifier: str):
    """
    Return the number of parameters of the given identifier.
    :param identifier: SVG identifier
    :return: number of parameters of the given identifier
    """
    if identifier.lower() == 'z':
        return 0
    elif identifier.lower() == 'h' or identifier.lower() == 'v':
        return 1
    elif identifier.lower() == 'm' or identifier.lower() == 'l' or identifier.lower() == 't':
        return 2
    elif identifier.lower() == 's' or identifier.lower() == 'q':
        return 4
    elif identifier.lower() == 'c':
        return 6
    elif identifier.lower() == 'a':
        return 7
    else:
        return -1


def get_svg_component(data: list):
    """
    Maps data list to SVG component.
    :param data: List of data, with identifier at data[0]
    :return: string of SVG component
    """
    if data[0] == 'M':
        return move_to(*data[1:])
    elif data[0] == 'm':
        return move_to_relative(*data[1:])
    elif data[0] == 'L':
        return line_to(*data[1:])
    elif data[0] == 'l':
        return line_to_relative(*data[1:])
    elif data[0] == 'H':
        return horizontal_line_to(*data[1:])
    elif data[0] == 'h':
        return horizontal_line_to_relative(*data[1:])
    elif data[0] == 'V':
        return vertical_line_to(*data[1:])
    elif data[0] == 'v':
        return vertical_line_to_relative(*data[1:])
    elif data[0] == 'Z' or data[0] == 'z':
        return close()
    elif data[0] == 'C':
        return curve_to(*data[1:])
    elif data[0] == 'c':
        return curve_to_relative(*data[1:])
    elif data[0] == 'S':
        return reflective_curve_to(*data[1:])
    elif data[0] == 's':
        return reflective_curve_to_relative(*data[1:])
    elif data[0] == 'Q':
        return quadratic_curve_to(*data[1:])
    elif data[0] == 'q':
        return quadratic_curve_to_relative(*data[1:])
    elif data[0] == 'T':
        return reflective_quadratic_curve_to(*data[1:])
    elif data[0] == 't':
        return reflective_quadratic_curve_to_relative(*data[1:])
    elif data[0] == 'A':
        return arc_to(*data[1:])
    elif data[0] == 'a':
        return arc_to_relative(*data[1:])
    else:
        return ""
