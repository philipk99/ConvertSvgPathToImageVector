# ConvertSvgPathToImageVector
This is a simple python script to convert a svg path to an android [ImageVector](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/vector/ImageVector).
I use it to create icons programmatically for my Jetpack Compose projects.

Basic Usage:
```
python convert_svg_path_to_image_vector.py -n '<name>' -p '<package>' -t '<type>' -d '<path_data>'
```
With:
- **name**: Name of the icon and file
- **package**: Your app package
- **type**: Type of the icon (Filled, Rounded, ...)
- **path_data**: SVG path data (e.g. "M1,1L2,2z")

## Main Features
- Converts it to a ready to use Kotlin file
- Accepts mutiple data sets per SVG identifier (e.g. "L1,1 2,2z", will be parsed as "L1,1L2,2z")
- Automatically appends a close to the path if no "z" identifier is at the end
