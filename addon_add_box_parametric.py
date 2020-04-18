bl_info = {
    "name": "Add Box Parametric",
    "author": "Ludvig Ström",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > Box Parametric",
    "description": "Adds a box that is independently scalable in x,y,z with origin at 0,0,0",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}


import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector


def add_object(self, context):
    scale_x = self.scale.x
    scale_y = self.scale.y
    scale_z = self.scale.z

    verts = [
        Vector((0 * scale_x, 0 * scale_y, 0 * scale_z)),
        Vector((0 * scale_x, 1 * scale_y, 0 * scale_z)),
        Vector((1 * scale_x, 1 * scale_y, 0 * scale_z)),
        Vector((1 * scale_x, 0 * scale_y, 0 * scale_z)),
        Vector((0 * scale_x, 0 * scale_y, 1 * scale_z)),
        Vector((0 * scale_x, 1 * scale_y, 1 * scale_z)),
        Vector((1 * scale_x, 1 * scale_y, 1 * scale_z)),
        Vector((1 * scale_x, 0 * scale_y, 1 * scale_z)),
    ]

    edges = []
    faces = [[0, 1, 2, 3],[4, 5, 6, 7],[0, 4, 7, 3],[1, 5, 6, 2],[0, 1, 5, 4],[3, 2, 6, 7]]

    mesh = bpy.data.meshes.new(name="Box Parametric")
    mesh.from_pydata(verts, edges, faces)
    object_data_add(context, mesh, operator=self)


class OBJECT_OT_add_object(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_box_parametric"
    bl_label = "Add Box Paramatric"
    bl_options = {'REGISTER', 'UNDO'}

    scale: FloatVectorProperty(
        name="scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )

    def execute(self, context):

        add_object(self, context)

        return {'FINISHED'}


# Registration

def add_object_button(self, context):
    self.layout.operator(
        OBJECT_OT_add_object.bl_idname,
        text="Box Parametric",
        icon='CUBE')


# This allows you to right click on a button and link to documentation
def add_object_manual_map():
    url_manual_prefix = "https://github.com/ludvigStrom/Parametric-Box---blender-extension/blob/master/README.md"
    return url_manual_prefix


def register():
    bpy.utils.register_class(OBJECT_OT_add_object)
    bpy.utils.register_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_button)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_object)
    bpy.utils.unregister_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_button)


if __name__ == "__main__":
    register()
