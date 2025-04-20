import argparse
import re
import svg_components as svg


def split_path(path_data: str):
    split = [p for p in re.split(r'([A-Za-z])|\s+|,', path_data) if p is not None]
    split.pop(0)

    out = list()
    key = -1

    for s in split:
        if s.isalpha():
            out.append([s])
            key += 1
        else:
            out[key].append(s)
    return out


def fix_multiple_per_identifier(data_list: list):
    for i, _d in enumerate(data_list):
        id_count = svg.get_parameter_count(_d[0]) + 1
        if len(_d) != id_count:
            data_list[i] = _d[:id_count]
            data_list.insert(i + 1, [_d[0], *_d[id_count:]])

    return data_list


def parse_path(path_data: str):
    data_list = split_path(path_data)
    data_list = fix_multiple_per_identifier(data_list)

    out = list()
    for _d in data_list:
        out.append(svg.get_svg_component(_d))

    if out[-1][0].lower() != 'z':
        out.append(svg.close())
    return out


def lower_first(s: str):
    return s[0].lower() + s[1:]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='convert_svg_path_to_image_vector.py',
        description='Converts a SVG paths to an android image vector.'
    )
    parser.add_argument('-n', '--name', type=str, required=True,
                        help='The name of the icon. Will be used as name for ImageVector.')
    parser.add_argument('-p', '--package', type=str, required=True,
                        help='The name of the package. Will be used as package for icon ImageVector.')
    parser.add_argument('-t', '--type', type=str, required=True,
                        help='The type of the icon. [Filled, Rounded, ...].')
    parser.add_argument('-d', '--data', type=str, required=True, help='The svg path.')

    args = parser.parse_args()

    data = parse_path(args.data)
    with open(args.name + '.kt', 'w') as f:
        f.write(f'package {args.package}\n')
        f.write('\n')
        f.write('import androidx.compose.material.icons.Icons\n')
        f.write('import androidx.compose.material.icons.materialIcon\n')
        f.write('import androidx.compose.material.icons.materialPath\n')
        f.write('import androidx.compose.ui.graphics.vector.ImageVector\n')
        f.write('\n')
        f.write(f'internal val Icons.{args.type}.{args.name}: ImageVector\n')
        f.write('\tget() {\n')
        f.write(f'\t\tif (_{lower_first(args.name)} != null) ''{\n')
        f.write(f'\t\t\treturn _{lower_first(args.name)}!!\n')
        f.write('\t\t}\n')
        f.write(f'\t\t_{lower_first(args.name)} = materialIcon(name = "{args.type}.{args.name}") ''{\n')
        f.write('\t\t\tmaterialPath {\n')
        for d in data:
            f.write(f'\t\t\t\t{d}\n')
        f.write('\t\t\t}\n')
        f.write('\t\t}\n')
        f.write(f'\t\treturn _{lower_first(args.name)}!!\n')
        f.write('\t}\n')
        f.write('\n')
        f.write(f'private var _{lower_first(args.name)}: ImageVector? = null\n')
