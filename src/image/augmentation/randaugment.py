import random
from PIL import Image, ImageEnhance, ImageOps


class RandAugment:
    def __init__(self, n, m):
        self.n = n  # Number of augmentation transformations to apply
        self.m = m  # Magnitude of the augmentations (0-10)
        self.augment_list = [
            (ImageOps.autocontrast, None),
            (ImageOps.equalize, None),
            (ImageOps.invert, None),
            (ImageOps.mirror, None),
            (ImageOps.flip, None),
            (self._rotate, None),
            (self._shear_x, None),
            (self._shear_y, None),
            (self._translate_x, None),
            (self._translate_y, None),
            (self._posterize, None),
            (self._solarize, None),
            (self._color, None),
            (self._contrast, None),
            (self._brightness, None),
            (self._sharpness, None)
        ]

    def __call__(self, img):
        ops = random.choices(self.augment_list, k=self.n)
        for op, val_range in ops:
            mag = self.m
            if val_range is not None:
                val = (mag / 10) * val_range + 1e-5
            else:
                val = None

            img = op(img) if val is None else op(img, val)
        return img

    def _rotate(self, img, v):
        degrees = v * 45
        if random.random() < 0.5:
            degrees = -degrees
        return img.rotate(degrees)

    def _shear_x(self, img, v):
        range_val = 0.3
        if random.random() > 0.5:
            v = -v
        return img.transform(img.size, Image.AFFINE, (1, v * range_val, 0, 0, 1, 0))

    def _shear_y(self, img, v):
        range_val = 0.3
        if random.random() > 0.5:
            v = -v
        return img.transform(img.size, Image.AFFINE, (1, 0, 0, v * range_val, 1, 0))

    def _translate_x(self, img, v):
        range_val = img.size[0] / 3
        if random.random() > 0.5:
            v = -v
        return img.transform(img.size, Image.AFFINE, (1, 0, v * range_val, 0, 1, 0))

    def _translate_y(self, img, v):
        range_val = img.size[1] / 3
        if random.random() > 0.5:
            v = -v
        return img.transform(img.size, Image.AFFINE, (1, 0, 0, 0, 1, v * range_val))

    def _posterize(self, img, v):
        v = int(v * 4)
        v = max(1, v)
        return ImageOps.posterize(img, v)

    def _solarize(self, img, v):
        v = int(v * 256)
        return ImageOps.solarize(img, v)

    def _color(self, img, v):
        return ImageEnhance.Color(img).enhance(v)

    def _contrast(self, img, v):
        return ImageEnhance.Contrast(img).enhance(v)

    def _brightness(self, img, v):
        return ImageEnhance.Brightness(img).enhance(v)

    def _sharpness(self, img, v):
        return ImageEnhance.Sharpness(img).enhance(v)


if __name__ == '__main__':
    # Example Usage
    try:
        img = Image.open('test.jpg')  # Replace 'test.jpg' with an actual image file
        augment = RandAugment(n=2, m=7)
        augmented_img = augment(img)
        augmented_img.save('augmented_test.jpg')
        print("Image augmented and saved as augmented_test.jpg")
    except FileNotFoundError:
        print("Error: test.jpg not found. Please place a test image in the same directory.")
    except Exception as e:
        print(f"An error occurred: {e}")