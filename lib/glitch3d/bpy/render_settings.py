# Square wall art resolution: 10200x10200 (threadless, society6)
def set_tile(size):
    SCENE.render.tile_x = size
    SCENE.render.tile_y = size

def render_normals():
    SCENE.use_nodes = True
    SCENE.render.layers[0].use_pass_normal = True
    SCENE.render.layers[0].use_pass_z = False
    SCENE.render.layers[0].use_pass_combined = False
    node_tree = bpy.context.scene.node_tree
    enter = node_tree.nodes[1]
    composite = node_tree.nodes['Composite']
    multiply = node_tree.nodes.new('CompositorNodeMixRGB')
    add = node_tree.nodes.new('CompositorNodeMixRGB')
    multiply.blend_type = "MULTIPLY"
    add.blend_type = 'ADD'
    add.inputs[1].default_value = rand_color()
    multiply.inputs[1].default_value = rand_color()
    invert = node_tree.nodes.new('CompositorNodeInvert')
    node_tree.links.new(add.outputs[0], invert.inputs[1])
    node_tree.links.new(multiply.outputs[0], add.inputs[2])
    node_tree.links.new(enter.outputs['Normal'], multiply.inputs[1])
    node_tree.links.new(invert.outputs[0], composite.inputs[0])

def isometric_camera():
    CAMERA.location = (12, -12, 12)
    CAMERA.rotation_euler = (54.8, 0, 45)
    CAMERA.data.type = 'ORTHO'

def render_settings(animate, mode, normals):
    SCENE.render.resolution_x = 2000
    SCENE.render.resolution_y = 2000
    SCENE.render.engine = 'CYCLES'
    SCENE.render.resolution_percentage = 25
    # bpy.SCENE.cycles.device = 'GPU'
    SCENE.render.image_settings.compression = 90
    SCENE.cycles.samples = 20
    SCENE.cycles.max_bounces = 1
    SCENE.cycles.min_bounces = 1
    SCENE.cycles.caustics_reflective = False
    SCENE.cycles.caustics_refractive = False
    SCENE.render.image_settings.color_mode ='RGBA'
    SCENE.render.layers[0].cycles.use_denoising = True
    set_tile(32)
    if normals:
        render_normals()
    if animate:
        SCENE.render.image_settings.file_format='AVI_RAW'
    else:
        SCENE.render.image_settings.file_format='PNG'
    if mode == 'high':
        set_tile(64)
        SCENE.cycles.samples = 100
        SCENE.render.resolution_percentage = 100

