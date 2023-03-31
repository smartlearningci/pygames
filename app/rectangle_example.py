"""An example of a regular polygon: an rectangle"""

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from geometry.rectangle import RectangleGeometry
from material.surface import SurfaceMaterial
# from material.point import PointMaterial



class Example(Base):
    """ Render a regular hexagon """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0, 0, 4])
        geometry = RectangleGeometry(1, 2)
        material = SurfaceMaterial(property_dict={"useVertexColors": True})
        # material = PointMaterial(property_dict={"baseColor": [1, 1, 0], "pointSize": 5})
        # material = SurfaceMaterial(
        #     property_dict= {
        #         "useVertexColors": True,
        #         "wireframe": True,
        #         "lineWidth": 8
        #     }
        # )
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

    def update(self):
        """Updating scene with movement"""
        self.mesh.rotate_z(0.01337)
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()