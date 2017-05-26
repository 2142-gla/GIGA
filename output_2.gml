Creator "Y"
Version 1.0
graph
[
	label	""
	directed	1
	node
	[
		id 47
		label "YBR001C"
		GO "neutral\ntrehalase"
		graphics
		[
		w	20.0
		h	20.0
		type	"ellipse"
		width	1.00000
		fill	"#E1E1E1"
		outline	"#000000"
		]
	]
	node
	[
		id 48
		label "YDR001C"
		GO "neutral\ntrehalase"
		graphics
		[
		w	20.0
		h	20.0
		type	"ellipse"
		width	1.00000
		fill	"#E1E1E1"
		outline	"#000000"
		]
	]
	node
	[
		id 49
		label "YPR026W"
		GO "acid\ntrehalase"
		graphics
		[
		w	20.0
		h	20.0
		type	"ellipse"
		width	1.00000
		fill	"#E1E1E1"
		outline	"#000000"
		]
	]
	edge [
		source 47
		target 48
		label "2 D-glucose"
		graphics 
		[
		width	2
		type	"line"
		fill	"#0000E1"
		]
	]
	edge [
		source 47
		target 48
		label "Alpha,alpha-trehalose"
		graphics 
		[
		width	2
		type	"line"
		fill	"#0000E1"
		]
	]
	edge [
		source 47
		target 49
		label "2 D-glucose"
		graphics 
		[
		width	2
		type	"line"
		fill	"#0000E1"
		]
	]
	edge [
		source 47
		target 49
		label "Alpha,alpha-trehalose"
		graphics 
		[
		width	2
		type	"line"
		fill	"#0000E1"
		]
	]

]