# https://psd-tools.readthedocs.io/en/latest/index.html

import json
from psd_tools import PSDImage

psd = PSDImage.open('example.psd')
psd.composite().save('--finalResultImage.png')
uiAssetsFolder = './ui-assets/'

UIJson = []

for layer in psd:
    
    print()
    fname = "".join(x for x in layer.name if x.isalnum())
    print('😲', fname, psd.index(layer),'left:',layer.left, 'top:',layer.top, 'width:',layer.width, 'height:',layer.height )
    print()
    
    if layer.kind == 'type': # Layer that has text and styling information for fonts or paragraphs.
        print('--type--',layer.text)
        layer.composite().save(uiAssetsFolder + fname + '.png')
        UIJson.append({"layerIndex":psd.index(layer),"path":uiAssetsFolder + fname + '.png', "left":layer.left, "top":layer.top, "width":layer.width, "height":layer.height})
    elif layer.kind == 'pixel': # Layer that has rasterized image in pixels.
        print('--pixel--',layer)
        layer.composite().save(uiAssetsFolder + fname + '.png')
        UIJson.append({"layerIndex":psd.index(layer),"path":uiAssetsFolder + fname + '.png', "left":layer.left, "top":layer.top, "width":layer.width, "height":layer.height})
    elif layer.kind == 'group': # Group of layers.
        print('--group--',layer)
    elif layer.kind == 'shape': # Layer that has drawing in vector mask.
        print('--shape--',layer)
        layer.composite().save(uiAssetsFolder + fname + '.png')
        UIJson.append({"layerIndex":psd.index(layer),"path":uiAssetsFolder + fname + '.png', "left":layer.left, "top":layer.top, "width":layer.width, "height":layer.height})
    elif layer.kind == 'smartobject': # Layer that inserts external data.
        print('--smartobject--',layer)
        layer.composite().save(uiAssetsFolder + fname + '.png')
        UIJson.append({"layerIndex":psd.index(layer),"path":uiAssetsFolder + fname + '.png', "left":layer.left, "top":layer.top, "width":layer.width, "height":layer.height})
    else: # group, pixel, shape, type, smartobject, or psdimage
        print('--other--',layer)
            
    print()
    
layout = json.dumps(UIJson)
f = open("UIlayout.js", "w")
f.write("export let UILayout="+layout)
f.close()