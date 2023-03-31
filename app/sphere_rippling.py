import numpy as np
import pathlib
import sys

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from geometry.sphere import SphereGeometry
from material.material import Material


class Example(Base):
    """
    Render an animated rippling effect on the sphere.
    The color shifts back and forth from the red end of the spectrum.
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0, 0, 7])
        geometry = SphereGeometry(
            radius=3,
            radius_segments=128,
            height_segments=64
        )
        vs_code = """
        uniform mat4 modelMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 projectionMatrix;
        in vec3 vertexPosition;
        in vec3 vertexColor;
        out vec3 color;
        uniform float time;
        void main()
        {
            float offset = 0.2 * sin(8.0 * vertexPosition.x + time);
            vec3 pos = vertexPosition + vec3(0.0, offset, 0.0);
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(pos, 1);
            color = vertexColor;
        }
        """
        fs_code = """
        in vec3 color;
        out vec4 fragColor;
        uniform float time;
        void main()
        {
            float r = abs(sin(time));
            vec4 c = vec4(0.25 * r, -0.1 * r, -0.1 * r, 0.0);
            fragColor = vec4(color, 1.0) + c;
        }
        """
        self._time = 0
        material = Material(vs_code, fs_code)
        material.add_uniform("float", "time", self._time)
        material.locate_uniforms()
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

    def update(self):
        self.time += 1 / 60
        self.mesh.material.uniform_dict["time"].data = self.time
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
