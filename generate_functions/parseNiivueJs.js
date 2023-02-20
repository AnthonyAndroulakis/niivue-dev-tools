const fs = require("fs");
const acorn = require("acorn");
const { generate } = require("astring");

var outputFn = "./found.json";

//got these functions from the table of contents on https://niivue.github.io/niivue/devdocs/Niivue.html
const functions = [
	"addMesh", 
	"addMeshFromUrl", 
	"addVolume", 
	"addVolumeFromUrl", 
	"attachTo", 
	"attachToCanvas", 
	"cloneVolume", 
	"colormap", 
	"colorMaps", 
	"createCustomMeshShader", 
	"createEmptyDrawing", 
	"drawGrowCut", 
	"drawMosaic", 
	"drawOtsu", 
	"drawUndo", 
	"getDescriptives", 
	"getFrame4D", 
	"getMediaByUrl", 
	"getOverlayIndexByID", 
	"getRadiologicalConvention", 
	"getVolumeIndexByID", 
	"isMeshExt", 
	"loadConnectome", 
	"loadDocument", 
	"loadDocumentFromUrl", 
	"loadDrawingFromUrl", 
	"loadMeshes", 
	"loadVolumes", 
	"meshShaderNames", 
	"moveCrosshairInVox", 
	"moveVolumeDown", 
	"moveVolumeToBottom", 
	"moveVolumeToTop", 
	"moveVolumeUp", 
	"off", 
	"on", 
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
	"sph2cartDeg", 
	"syncWith", 
	"updateGLVolume"
];

var code = fs.readFileSync('./niivue.js', 'utf-8');
var ast = acorn.parse(code, {
	ecmaVersion: "latest",
	sourceType: "module",
	ranges: true
});

var foundFuncs = {};
for (const b of ast.body) {
	if (b?.expression?.left?.object && generate(b.expression.left.object) == 'Niivue.prototype') {
		var name = b.expression.left.property.name;
		if (functions.includes(name)) {
			var params = b.expression.right.params.map(i => generate(i).replaceAll('"', "'"))
			foundFuncs[name] = params;
		}
	}
}

fs.writeFileSync(outputFn, JSON.stringify(foundFuncs))

