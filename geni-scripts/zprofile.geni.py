"""
zprofile. Aim for the most configurable profile for simple lab.
"""

#
# NOTE: This code was machine converted. An actual human would not
#       write code like this!
#
import math
# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as rspec #pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal object,
pc = portal.Context()

imageList = [
		('default', 'Default Image'),
		('urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD', 'UBUNTU 18.04'),
		('urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU16-64-STD', 'UBUNTU 16.04'),
		('urn:publicid:IDN+emulab.net+image+emulab-ops//CENTOS7-64-STD',  'CENTOS 7'),
		('urn:publicid:IDN+emulab.net+image+emulab-ops//FBSD112-64-STD', 'FreeBSD 11.2')]

pc.defineParameter("osImage", "Select OS image",
				 portal.ParameterType.IMAGE,
				 imageList[0], imageList,
				 longDescription="Most clusters have this set of images, " +
				 "pick your favorite one.")

pc.defineParameter("customimage", "Override our custom image address", portal.ParameterType.STRING, "",
					longDescription="If you specify this field, we will use the image here.")


pc.defineParameter("nodeCount", "Number of Nodes", portal.ParameterType.INTEGER, 1,
				 longDescription="If you specify more then one node, " +
				 "we will create a lan for you.")

pc.defineParameter("cores", "Number of Cores per machine.", portal.ParameterType.INTEGER, 0,
				 longDescription="The number of cores for each machine.")

pc.defineParameter("memory", "Memory (GB) per node", portal.ParameterType.INTEGER, 0,
				 longDescription="Memory of the node.")

pc.defineParameter("disk", "Disk (GB) per node", portal.ParameterType.INTEGER, 0,
				 longDescription="Disk (GB) per node.")

pc.defineParameter("XenVM", "Virtual Machine", portal.ParameterType.BOOLEAN, False,
				 longDescription="Use XenVM instead of bare metal machine as specified in nodeCount.")

# Optional physical type for all nodes.
pc.defineParameter("phystype",  "Optional physical node type",
				 portal.ParameterType.STRING, "",
				 longDescription="Specify a physical node type (pc3000,d710,etc) " +
				 "instead of letting the resource mapper choose for you.")

# Optional ephemeral blockstore
pc.defineParameter("tempFileSystemSize", "Temporary Filesystem Size",
				 portal.ParameterType.INTEGER, 0, advanced=True,
				 longDescription="The size in GB of a temporary file system to mount on each of your " +
				 "nodes. Temporary means that they are deleted when your experiment is terminated. " +
				 "The images provided by the system have small root partitions, so use this option " +
				 "if you expect you will need more space to build your software packages or store " +
				 "temporary files.")
				 
# Instead of a size, ask for all available space. 
pc.defineParameter("tempFileSystemMax",  "Temp Filesystem Max Space",
					portal.ParameterType.BOOLEAN, False,
					advanced=True,
					longDescription="Instead of specifying a size for your temporary filesystem, " +
					"check this box to allocate all available disk space. Leave the size above as zero.")

pc.defineParameter("tempFileSystemMount", "Temporary Filesystem Mount Point",
				 portal.ParameterType.STRING,"/mydata",advanced=True,
				 longDescription="Mount the temporary file system at this mount point; in general you " +
				 "you do not need to change this, but we provide the option just in case your software " +
				 "is finicky.")


pc.defineParameter("numSite", "Number of Sites",
				 portal.ParameterType.INTEGER, 0, advanced=True,
				 longDescription="Number of sites that the nodes can maximally. allocate to. This is to " +
				 "prevent vm colocation on a single machine without the machine getting enough resources.")

pc.defineParameter("prefixName", "Prefix of each node's name. Default 'node'", portal.ParameterType.STRING, "node", advanced=True)


# Retrieve the values the user specifies during instantiation.
params = pc.bindParameters()

# Check parameter validity.
if params.nodeCount < 1:
	pc.reportError(portal.ParameterError("You must choose at least 1 node.", ["nodeCount"]))


# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

def getNode(name, siteName):
	if params.XenVM:
		node = request.XenVM(name)
	else:
		node = request.RawPC(name)

	node.Site(siteName)
	node.cores = params.cores 
	if params.memory:
		node.ram = params.memory * 1024
	if params.disk:
		node.disk = params.disk

	# Setup temp blob store
	if params.tempFileSystemSize > 0 or params.tempFileSystemMax:
			bs = node.Blockstore(name + "-bs", params.tempFileSystemMount)
			if params.tempFileSystemMax:
				bs.size = "0GB"
			else:
				bs.size = str(params.tempFileSystemSize) + "GB"
			bs.placement = "any"
	
	# Setup image
	if len(params.customimage) > 0:
		node.disk_image = params.customimage
	elif params.osImage and params.osImage != "default":
		node.disk_image = params.osImage
	
	# Setup the physical node type
	if params.phystype != "":
		node.hardware_type = params.phystype
	return node

nodes = []
numSite = params.numSite or 1
nodePerSite = math.ceil(params.nodeCount / numSite)
for i in range(params.nodeCount):
	siteIndex = math.floor(i / nodePerSite)
	siteName = "Site" + str(siteIndex)
	prefix = params.prefixName or "node"
	name = prefix + str(i)
	node = getNode(name, siteName)
	nodes.append(node)

link1 = request.Link(members = nodes)
link1.best_effort = True

# bs = node0.Blockstore("bs", "/test-data")
# bs.dataset = "urn:publicid:IDN+wisc.cloudlab.us:cs744-s19-pg0+imdataset+enwiki-data"
# bs.readonly = True

# # # Special attributes for this link that we must use.
# fslink.best_effort = True
# fslink.vlan_tagging = True

# Print the generated rspec
pc.printRequestRSpec(request)