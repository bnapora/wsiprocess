from PIL import Image, ImageDraw
from pathlib import Path
import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description="Show Bounding Boxes on Extracted Image")
    parser.add_argument("root",
                        help="Root directory of processed result",
                        type=Path)
    args = parser.parse_args()

    color = {"malignant": (255, 0, 0),
             "benign": (0, 128, 0)}

    imgs = (args.root/"patches").glob("*/*.png")
    annot_path = args.root/"results.json"
    with open(annot_path, "r") as f:
        annotation = json.load(f)

    for path in imgs:
        img = Image.open(path)
        stem = path.stem
        x, y = stem.split("_")
        patch = find_patch(annotation, x, y)
        for bb in patch["bbs"]:
            draw = ImageDraw.Draw(img)
            x2 = bb["x"]+bb["w"]
            y2 = bb["y"]+bb["h"]
            outline = color[bb["class"]]
            draw.rectangle((bb["x"], bb["y"], x2, y2),
                           width=2,
                           outline=outline)
        img.save(f"{stem}_with_bb.png")


def find_patch(annotation, x, y):
    for patch in annotation["result"]:
        if int(x) == patch["x"] and int(y) == patch["y"]:
            return patch


if __name__ == '__main__':
    main()