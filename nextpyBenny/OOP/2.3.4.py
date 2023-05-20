class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = int((self._green + self._red + self._blue) / 3)
        self._green = avg
        self._blue = avg
        self._red = avg

    def print_pixel_info(self):
        color = ""
        if self._red == 0 and self._blue == 0 and self._green > 50:
            color = "Green"
        if self._red == 0 and self._green == 0 and self._blue > 50:
            color = "Blue"
        if self._green == 0 and self._blue == 0 and self._red > 50:
            color = "Red"

        print(f"X: {self._x}, Y: {self._y}, "
              f"Color: ({self._red}, {self._green}, {self._blue}) {color}")


def main():
    my_pixel = Pixel(5, 6, 250, 0, 0)
    my_pixel.print_pixel_info()
    my_pixel.set_grayscale()
    my_pixel.print_pixel_info()


if __name__ == '__main__':
    main()
