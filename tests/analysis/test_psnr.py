import os

import pytest
import cv2

from analysis.compression_analysis import psnr

def test_psnr_on_known_images():
    """Integration test that psnr returns expected values for predefined images"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    original = cv2.imread(os.path.join(dir_path, 'original_image.png'))
    contrast = cv2.imread(os.path.join(dir_path, 'compressed_image.png'), 1)
    original2 = cv2.imread(os.path.join(dir_path, 'PSNR-example-base.png'))
    contrast2 = cv2.imread(os.path.join(dir_path, 'PSNR-example-comp-10.jpg'), 1)
    
    assert psnr.psnr(original, contrast) == pytest.approx(29.735, abs=0.005)
    assert psnr.psnr(original2, contrast2) == pytest.approx(31.535, abs=0.005)
