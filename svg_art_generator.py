from typing import IO, NamedTuple
import random
from collections import namedtuple


class HtmlComponent:
    '''HtmlComponent class '''

    TAB = "   " # HTML indentation tab (default: three spaces)

    def __init__(self, file_name: str, window_title: str):
        """Initializes a HtmlComponent"""
        self.__fnam: str = file_name
        self.__windtitle: str = window_title
        self.__fd: IO[str] = self.open_html_file()
    
    def get_fd(self) -> IO[str]:
        """get_fd method"""
        return self.__fd

    def open_html_file(self) -> None:
        """open_html_file method"""
        return open(self.__fnam, "w")
    
    def close_html_file(self) -> None:
        """close_html_file method"""
        self.__fd.close()

    def write_html_comment(self, tab_num: int, comment: str) -> None:
        """write_html_comment method"""
        tabs: str = HtmlComponent.TAB * tab_num
        self.__fd.write(f"{tabs}<!--{comment}-->\n")
    
    def write_html_line(self, tab_num: int, line: str) -> None:
        """write_html_line method"""
        tabs: str = HtmlComponent.TAB * tab_num 
        self.__fd.write(f"{tabs}{line}\n")

    def write_html_head(self) -> None:
        """write_html_header method"""
        self.write_html_line(0,"<!DOCTYPE html>")
        self.write_html_line(0, "<html>")
        self.write_html_line(0,"<head>")
        self.write_html_line(1, f"<title>{self.__windtitle}</title>")
        self.write_html_line(0, "</head>")
        self.write_html_line(0, "<body>")
        
    def write_html_tail(self) -> None:
        """write_html_tail method"""
        self.write_html_line(0, "</body>")
        self.write_html_line(0, "</html>")



class CircleShape(NamedTuple):
    """Circle class"""

    #Define namedtuple for CircleShape
    cx: int # circle center x coordinate
    cy: int # circle center y coordinate
    rad: int # circle radius
    red: int 
    green: int
    blue: int
    opacity: float
        
    def drawCircleLine(self, f: IO[str], tab_num: int, c: tuple) -> None:
        """drawCircle method"""
        tabs: str = "   " * tab_num
        line1: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" '
        line2: str = f'fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.opacity:.1f}"></circle>'
        f.write(f"{tabs}{line1+line2}\n")


class RectangleShape(NamedTuple):
    """Rectangle class"""

    # Defining namedtuple for RectangleShape
    w: int # width
    h: int # height
    x: int # x-pos of top left corner
    y: int # y-pos of top left corner
    rx: int # x corners rounded value
    ry: int # y corners rounded value
    red: int
    green: int
    blue: int
    opacity: float

    def drawRectangle(self, f: IO[str], tab_num: int, r: tuple) -> None:
        """drawRectangle method"""
        tabs: str = "   " * tab_num
        line1: str = f'<rect width="{r.w}" height="{r.h}" x="{r.x}" y="{r.y}" rx="{r.rx}" ry="{r.ry}" '
        line2: str = f'fill="rgb({r.red}, {r.green}, {r.blue})" fill-opacity="{r.opacity:.1f}"></rect>'
        f.write(f"{tabs}{line1+line2}\n")


class EllipseShape(NamedTuple):
    """EllipseShape class"""

    rx: int # ellipse x radius
    ry: int # ellipse y radius
    cx: int # center x-position
    cy: int # center y-position
    red: int 
    green: int
    blue: int
    opacity: int
    

    def drawEllipse(self, f: IO[str], tab_num: int, e: tuple) -> None:
        """drawEllipse method"""
        tabs: str = "   " * tab_num
        line1: str = f'<ellipse rx="{self.rx}" ry="{self.ry}" cx="{self.cx}" cy="{self.cy}" '
        line2: str = f'fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.opacity:.1f}"></ellipse>'
        f.write(f"{tabs}{line1+line2}\n")
    


class PyArtConfig(NamedTuple):
    """PyArtConfig class"""

    # Default Ranges:
    SHAPE_VALUES = [0,1,3] # circle = 0, rect = 1, ellipse = 3
    X_RANGE = (0,1000)
    Y_RANGE = (0,700)
    RAD_RANGE = (0,100)
    RX_RANGE = (10,30)
    RY_RANGE = (10,30)
    W_RANGE = (10,100)
    H_RANGE = (10,100)
    RGB_RANGE = (0,255)
    OP_RANGE = (0.0, 1.0)

    #Defining namedtuple for PyArtConfig
    cnt: int # shape count
    sha: int # shape type, 0 = circle, 1 = rect, 3 = ellipse
    x: int # x coordinate 
    y: int # y coordinate 
    rad: int # circle radius
    rx: int # ellipse x radius or rectangle x rounded edge value
    ry: int # ellipse y radius or rectangle y rounded edge value
    w: int # rectangle width
    h: int # rectangle height
    red: int
    green: int 
    blue: int 
    op: float # shape opacity



class RandomShape:
    """RandomShape class"""

    def __init__(self, py_art_config: PyArtConfig, cnt) -> None:
        """Initializing random shape."""
        self.py_art_config = py_art_config
        self.cnt = cnt
        self.sha = None
        self.make_random_shape()
       
    def make_random_shape(self) -> None:
        """make_random_shape method: generate random shape parameters"""

        # random shape choice
        self.sha = random.choice(self.py_art_config.SHAPE_VALUES)

        # random x-coord of shape
        self.x = random.randint(*self.py_art_config.X_RANGE)

        # random y-coord of shape
        self.y = random.randint(*self.py_art_config.Y_RANGE)

        # generate random radius for circle
        self.rad = random.randint(*self.py_art_config.RAD_RANGE)

        # generate random width and height for rect
        self.w = random.randint(*self.py_art_config.W_RANGE)
        self.h = random.randint(*self.py_art_config.H_RANGE)

        # generate random x and y radii for ellipse
        self.rx = random.randint(*self.py_art_config.RX_RANGE)
        self.ry = random.randint(*self.py_art_config.RY_RANGE)
        
        # random red colour value
        self.red = random.randint(*self.py_art_config.RGB_RANGE)

        # random green colour value
        self.green = random.randint(*self.py_art_config.RGB_RANGE)

        # random blue colour value
        self.blue = random.randint(*self.py_art_config.RGB_RANGE)

        # random opacity value
        self.op = random.random()

    def gen_rand_shape_data(self, num_shapes) -> list:
        """gen_rand_shape_data method: makes a list of random shapes"""

        # initializing list of shape data 
        shape_data = []

        # initialize count value
        cnt = 0

        for i in range(num_shapes):
            
            # generate random shape for each row
            random_shape = RandomShape(self.py_art_config, cnt)

            # add created shape to list of shape_data 
            shape_data.append(random_shape)
            
            # increment count
            cnt +=1

        # return list of shapes' random properties data
        return shape_data


class SvgCanvas(HtmlComponent):
    """SvgCanvas class"""
    
    def __init__(self, file_descriptor: IO[str]) -> None:
        self.__fd = file_descriptor
        self.file_name = file_descriptor.name

    def write_html_comment(self, tab_num: int, comment: str):
        """write_html_comment method"""
        tabs: str = HtmlComponent.TAB * tab_num
        self.__fd.write(f"{tabs}<!--{comment}-->\n")

    def openSVGcanvas(self, tab_num: int, canvas: tuple) -> None:
        """openSVGcanvas method"""
        tabs: str = "   " * tab_num
        
        self.write_html_comment(tab_num,"Define SVG drawing box")
        self.__fd.write(f'{tabs}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

    def genArt(self, tab_num: int)-> None:
        """genArt method"""

        tabs: str = "   "*tab_num
        self.write_html_comment(tab_num,"Generate art here")

        # initializing s with no properties
        s: PyArtConfig = PyArtConfig(cnt=0,sha=0,x=0,y=0,rad=0,rx=0,ry=0,w=0,h=0,red=0,green=0,blue=0,op=0.0)
        random_shape = RandomShape(s, 0)

        # setting num_shapes so each file will have a different number of shapes 
        if self.file_name == "art_piece3.html":
            num_shapes = 500
        elif self.file_name  == "art_piece2.html":
            num_shapes = 300
        elif self.file_name == "art_piece1.html":
            num_shapes = 1000

        # generate list of random shapes for the art
        shape_data = random_shape.gen_rand_shape_data(num_shapes)

        for shape in shape_data:
            # writing to the html file the svg command for each shape in the generated list

            if shape.sha == 0:
                # if shape is a circle, make a circle object and draw the circle

                # create the circle object
                circle = CircleShape(shape.x, shape.y, shape.rad, shape.red, shape.green, shape.blue, shape.op)
                
                # switching up the colours a bit for the different html files
                if self.file_name == "art_piece3.html":
                    circle = CircleShape(shape.x, shape.y, shape.rad, shape.red, 0, shape.blue, shape.op)
                elif self.file_name == "art_piece2.html":
                    circle = CircleShape(shape.x, shape.y, shape.rad, shape.red, shape.green, 0, shape.op)

                # draw the circle to html file
                circle.drawCircleLine(self.__fd, tab_num, circle)

            elif shape.sha == 1:
                # if the shape is a rectangle, make a rectangle object and draw the rectangle

                # create rectangle object
                rectangle = RectangleShape(shape.w, shape.h, shape.x, shape.y, shape.rx, shape.ry, shape.red, shape.green, shape.blue, shape.op)

                # switching up shape and/or colour properties for different output files
                if self.file_name == "art_piece3.html":
                    rectangle = RectangleShape(shape.w, shape.h, shape.x, shape.y, shape.rx, shape.ry, shape.red, 0, shape.blue, shape.op)
                elif self.file_name == "art_piece2.html":
                    rectangle = RectangleShape(shape.w, shape.h, shape.x, shape.y, 0, 0, shape.red, shape.green, 0, shape.op)

                # draw the rectangle to the html file
                rectangle.drawRectangle(self.__fd, tab_num, rectangle)

            elif shape.sha == 3:
                # if shape is an ellipse, make an ellipse object and draw the ellipse

                # create ellipse object
                ellipse = EllipseShape(shape.rx, shape.ry, shape.x, shape.y, shape.red, shape.green, shape.blue, shape.op)

                # switching up the colours a bit for different output files
                if self.file_name == "art_piece3.html":
                    ellipse = EllipseShape(shape.rx, shape.ry, shape.x, shape.y, shape.red, 0, shape.blue, shape.op)
                elif self.file_name == "art_piece2.html":
                    ellipse = EllipseShape(shape.rx, shape.ry, shape.x, shape.y, shape.red, shape.green, 0, shape.op)

                # draw the ellipse to the html file
                ellipse.drawEllipse(self.__fd, tab_num, ellipse)

    
    def closeSVGcanvas(self, tab_num: int) -> None:
        """closeSVGcanvas method"""
        tabs: str = "   " * tab_num
        self.__fd.write(f"{tabs}</svg>\n")


class HtmlDocument(HtmlComponent):
    """HtmlDocument class"""

    def __init__(self, file_name: str, window_title: str) -> None:
        """Initializes an Html Document."""
        super().__init__(file_name, window_title)
        self.svg_canvas = SvgCanvas(self.get_fd())

    def generate_svg_content(self) -> None:
        """generate_svg_content method"""
        self.svg_canvas.openSVGcanvas(1, (1000,700))
        self.svg_canvas.genArt(1)
        self.svg_canvas.closeSVGcanvas(1)

    def generate_html_file(self) -> None:
        """generate_html_file method"""
        self.write_html_head()
        self.generate_svg_content()
        self.write_html_tail()


def main() -> None:
    """main method: creates three html files with randomly generated art"""

    # making art_piece1.html file and its art
    hd1: HtmlDocument = HtmlDocument("art_piece1.html", "Generated-Image-1")
    hd1.generate_html_file()
    hd1.close_html_file()

    # making art_piece2.html file and its art
    hd2: HtmlDocument = HtmlDocument("art_piece2.html", "Generated-Image-2")
    hd2.generate_html_file()
    hd2.close_html_file()

    # making art_piece2.html file and its art
    hd3: HtmlDocument = HtmlDocument("art_piece3.html", "Generated-Image-3")
    hd3.generate_html_file()
    hd3.close_html_file()


if __name__ == "__main__":
    main()