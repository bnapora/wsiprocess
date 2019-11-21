import wsiprocess as wp
from pathlib import Path
import urllib.request


def download_test_file():
    url = "http://openslide.cs.cmu.edu/download/openslide-testdata/Hamamatsu/"
    filename = "CMU-1.ndpi"
    data = urllib.request.urlopen(url+filename).read()
    with open(filename, "wb") as f:
        f.write(data.content)


def test_slide():
    slide = wp.Slide("CMU-1.ndpi")
    print(slide.width)


def test_annotation():
    annotation = wp.Annotation("CMU-1.xml")
    annotation.export_thumb_mask(cls="foreground", save_to=".")
    annotation.export_thumb_masks(".")


def test_inclusion():
    inclusion = wp.Inclusion("CMU-1.txt")
    print(inclusion)


def test_none():
    """
    [Arguments for Patcher]
    slide, method, annotation=False, save_to=".", patch_width=256, patch_height=256,
    overlap_width=1, overlap_height=1, on_foreground=1., on_annotation=1.,
    start_sample=True, finished_sample=True, extract_patches=True
    """
    slide = wp.Slide("CMU-1.ndpi")

    # no annotation file
    patcher = wp.Patcher(slide, "none", start_sample=False, finished_sample=False, on_foreground=False, on_annotation=False)
    patcher.get_patch_parallel()

    # with annotation file
    annotation = wp.Annotation("CMU-1.xml")
    annotation.make_masks(slide)
    patcher = wp.Patcher(slide, "none", annotation, start_sample=False, finished_sample=False, on_foreground=False, on_annotation=False)
    patcher.get_patch_parallel(annotation.classes[0])

    # with annotation file and inclusion file
    inclusion = wp.Inclusion("CMU-1.txt")
    annotation.make_masks(slide, inclusion, foreground=True)
    patcher = wp.Patcher(slide, "none", annotation, start_sample=False, finished_sample=False, on_foreground=False, on_annotation=False)
    patcher.get_patch_parallel(annotation.classes[0])


def test_classification():
    slide = wp.Slide("CMU-1.ndpi")

    # no annotation file
    patcher = wp.Patcher(slide, "classification", start_sample=False, finished_sample=False, on_foreground=False, on_annotation=False)
    patcher.get_patch_parallel()

    # with annotation file
    annotation = wp.Annotation("CMU-1.xml")
    annotation.make_masks(slide)
    patcher = wp.Patcher(slide, "classification", annotation, start_sample=False, finished_sample=False, on_foreground=False, on_annotation=False)
    patcher.get_patch_parallel(annotation.classes[0])

    # with annotation file and inclusion file
    inclusion = wp.Inclusion("CMU-1.txt")
    annotation.make_masks(slide, inclusion, foreground=True)
    patcher = wp.Patcher(slide, "classification", annotation, start_sample=False, finished_sample=False, on_foreground=False, on_annotation=False)
    patcher.get_patch_parallel(annotation.classes[0])


def test_detection():
    slide = wp.Slide("CMU-1.ndpi")

    # no annotation file
    patcher = wp.Patcher(slide, "detection", start_sample=False, finished_sample=False, on_foreground=False, on_annotation=False)
    patcher.get_patch_parallel()

    # with annotation file
    annotation = wp.Annotation("CMU-1.xml")
    annotation.make_masks(slide)
    patcher = wp.Patcher(slide, "detection", annotation, start_sample=False, finished_sample=False, on_foreground=False, on_annotation=False)
    patcher.get_patch_parallel(annotation.classes[0])

    # with annotation file and inclusion file
    inclusion = wp.Inclusion("CMU-1.txt")
    annotation.make_masks(slide, inclusion, foreground=True)
    patcher = wp.Patcher(slide, "detection", annotation, start_sample=False, finished_sample=False, on_foreground=False, on_annotation=False)
    patcher.get_patch_parallel(annotation.classes[0])


def test_segmentation():
    slide = wp.Slide("CMU-1.ndpi")

    # no annotation file
    patcher = wp.Patcher(slide, "segmentation", start_sample=False, finished_sample=False, on_foreground=False, on_annotation=False)
    patcher.get_patch_parallel()

    # with annotation file
    annotation = wp.Annotation("CMU-1.xml")
    annotation.make_masks(slide)
    patcher = wp.Patcher(slide, "segmentation", annotation, start_sample=False, finished_sample=False, on_foreground=False, on_annotation=False)
    patcher.get_patch_parallel(annotation.classes[0])

    # with annotation file and inclusion file
    inclusion = wp.Inclusion("CMU-1.txt")
    annotation.make_masks(slide, inclusion, foreground=True)
    patcher = wp.Patcher(slide, "segmentation", annotation, start_sample=False, finished_sample=False, on_foreground=False, on_annotation=False)
    patcher.get_patch_parallel(annotation.classes[0])
