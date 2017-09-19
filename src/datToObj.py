import numpy
import bpy


#Code from https://wiki.blender.org/index.php/Dev:Py/Scripts/Cookbook/Code_snippets/Materials_and_textures
def makeMaterial(name, diffuse, specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.diffuse_shader = 'LAMBERT' 
    mat.diffuse_intensity = 1.0 
    mat.specular_color = specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.5
    mat.alpha = alpha
    mat.ambient = 1
    return mat
 
def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)
    
def cart2pol(x,y,max_X, max_Y, cx,cy, r):
    newX = cx+numpy.cos(x/max_X * 3.1415928)*r
    newY = cy-numpy.sin(x/max_X * 3.1415928)*r
    #newY = y
    return (newX,newY)
    
    

#Q = numpy.loadtxt("../../Documents/projects/dataview/aframe/src/collada/iris_numClass.csv", delimiter=",",skiprows=1)
#mxX = numpy.max(Q[:,2])
#mxY = numpy.max(Q[:,3])
#mats = [makeMaterial("c1", (1,0,0),(0.1,0.1,0.1),1), makeMaterial("c2", (0,1,0),(0.1,0.1,0.1),1), makeMaterial("c3", (0,0,1),(0.1,0.1,0.1),1)]
#for i in range(0,len(Q)):
#    newLoc = cart2pol(Q[i,2],Q[i,3],mxX,mxY, 0,0,4)
#    bpy.ops.mesh.primitive_cube_add(location=(newLoc[0],newLoc[1],Q[i,3]))
#    setMaterial(bpy.context.object, mats[int(Q[i,4])])
#    bpy.ops.transform.resize(value=(0.03, 0.03, 0.03))

Q = numpy.loadtxt("../../Documents/projects/dataview/aframe/src/collada/wdbc_MDS.csv", delimiter=",")
Q[:,0:3]=(Q[:,0:3]/numpy.max(Q[:,0:3]))*20.0

mxX = numpy.max(Q[:,0])
mxY = numpy.max(Q[:,1])
mxZ = numpy.max(Q[:,2])
mats = [makeMaterial("c1", (1,0,0),(0.1,0.1,0.1),1), makeMaterial("c2", (0,1,0),(0.1,0.1,0.1),1), makeMaterial("c3", (0,0,1),(0.1,0.1,0.1),1)]

for i in range(0,len(Q)):
    #newLoc = cart2pol(Q[i,2],Q[i,3],mxX,mxY, 0,0,4)
    newLoc=(Q[i,0],Q[i,1],Q[i,2])
    bpy.ops.mesh.primitive_cube_add(location=(newLoc[0],newLoc[1],newLoc[2]))
    setMaterial(bpy.context.object, mats[int(Q[i,3])])
    bpy.ops.transform.resize(value=(0.03, 0.03, 0.03))