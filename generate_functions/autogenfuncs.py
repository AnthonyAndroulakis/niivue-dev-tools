# for use in ipyniivue

import json
import re

filter_functions = [
	"addMesh", 
	"addMeshFromUrl", 
	"addVolume", 
	"addVolumeFromUrl", 
	#"attachTo", 
	#"attachToCanvas", 
	#"cloneVolume", 
	#"colormap", 
	#"colorMaps", 
	#"createCustomMeshShader", 
	"createEmptyDrawing", 
	"drawGrowCut", 
	"drawMosaic", 
	"drawOtsu", 
	"drawUndo", 
	#"getDescriptives", #need to figure out how to make these getters work
	#"getFrame4D", 
	#"getMediaByUrl", 
	#"getOverlayIndexByID", 
	#"getRadiologicalConvention", 
	#"getVolumeIndexByID", 
	#"isMeshExt", 
	"loadConnectome", 
	#"loadDocument", 
	"loadDocumentFromUrl", 
	"loadDrawingFromUrl", 
	"loadMeshes", 
	"loadVolumes", 
	#"meshShaderNames", 
	"moveCrosshairInVox", 
	"moveVolumeDown", 
	"moveVolumeToBottom", 
	"moveVolumeToTop", 
	"moveVolumeUp", 
	#"off", 
	#"on", 
	"removeHaze", 
	"removeMesh", 
	"removeMeshByUrl", 
	"removeVolume", 
	"removeVolumeByIndex", 
	"removeVolumeByIndex", 
	"removeVolumeByIndex", 
	"removeVolumeByUrl", 
	"reverseFaces", 
	"saveImage", 
	"saveScene", 
	"setClipPlane", 
	"setClipPlaneColor", 
	"setColorMap", 
	"setColorMapNegative", 
	"setCornerOrientationText", 
	"setCrosshairColor", 
	"setCrosshairWidth", 
	"setCustomMeshShader", 
	"setDrawingEnabled", 
	"setDrawOpacity", 
	"setFrame4D", 
	"setHighResolutionCapable", 
	"setInterpolation", 
	"setMeshLayerProperty", 
	"setMeshProperty", 
	"setMeshShader", 
	"setMeshThicknessOn2D", 
	"setModulationImage", 
	"setOpacity", 
	"setPan2Dxyzmm", 
	"setPenValue", 
	"setRadiologicalConvention", 
	"setRenderAzimuthElevation", 
	"setScale", 
	"setSelectionBoxColor", 
	"setSliceMM", 
	"setSliceMosaicString", 
	"setSliceType", 
	"setVolume", 
	#"sph2cartDeg", 
	#"syncWith", 
	"updateGLVolume"
];

def to_snake_case(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('__([A-Z])', r'_\1', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    name = name.lower()
    if name.endswith('_d'):
        fix1D = name.replace('1_d', '_1D')
        fix2D = name.replace('2_d', '_2D')
        fix3D = name.replace('3_d', '_3D')
        fix4D = name.replace('4_d', '_4D')
    else:
        fix1D = name.replace('1_d', '_1D_')
        fix2D = name.replace('2_d', '_2D_')
        fix3D = name.replace('3_d', '_3D_')
        fix4D = name.replace('4_d', '_4D_')
    return fix4D

with open('./found.json') as f:
    funcs = json.load(f)

print('GENERATE TYPESCRIPT CODE:\n______________')
for k,v in funcs.items():
	if k in filter_functions:
		print(f"case '{k}':\n  this.nv.{k}({', '.join('args['+str(i)+']' for i in range(len(v)))});\n  break;")

print('GENERATE PYTHON CODE:\n_______________')
for k,v in funcs.items():
	if k in filter_functions:
		snake_cased_name = to_snake_case(k)
		snake_cased_params = [to_snake_case(i.split(" ")[0]) for i in v]
		print(f'def {snake_cased_name}(self, {", ".join(snake_cased_params)}):\n\tself._send_custom([COMMANDS["{k}"], [{", ".join(snake_cased_params)}]])\n')

print('SUMMARY OF FUNCTIONS:\n_______________')
for k in funcs:
	if k in filter_functions:
		print(k)