{
	"targets": [{
		"target_name": "openzwave_shared",
		"sources": [
			"src/callbacks.cc",
			"src/openzwave.cc",
			"src/openzwave-config.cc",
			"src/openzwave-driver.cc",
			"src/openzwave-groups.cc",
			"src/openzwave-management.cc",
			"src/openzwave-network.cc",
			"src/openzwave-nodes.cc",
			"src/openzwave-polling.cc",
			"src/openzwave-scenes.cc",
			"src/openzwave-values.cc",
			"src/utils.cc",
		],
		"conditions": [
			["OS=='linux'", {
				"variables": {
					"PKG_CONFIG_PATH" : "<!(find /usr/local -type d ! -perm -g+r,u+r,o+r -prune -o -type d -name 'pkgconfig' -printf \"%p:\" | sed s/:$//g)",
					"OZW_INC"         : "<!(PKG_CONFIG_PATH=<(PKG_CONFIG_PATH) pkg-config --cflags-only-I libopenzwave | sed s/-I//g)",
					"OZW_GITVERSION"  : "<!(PKG_CONFIG_PATH=<(PKG_CONFIG_PATH) pkg-config --variable=gitversion libopenzwave)",
					"OZW_ETC"         : "<!(PKG_CONFIG_PATH=<(PKG_CONFIG_PATH) pkg-config --variable=sysconfdir libopenzwave)",
					"OZW_DOC"         : "<!(PKG_CONFIG_PATH=<(PKG_CONFIG_PATH) pkg-config --variable=docdir libopenzwave)"
				},
        		"defines": [
					"OPENZWAVE_ETC=<!@(node -p -e \"'<(OZW_ETC)'.length ? '<(OZW_ETC)' : '/usr/local/etc/openzwave'\")",
					"OPENZWAVE_DOC=<!@(node -p -e \"'<(OZW_DOC)'.length ? '<(OZW_DOC)' : '/usr/local/share/doc/openzwave'\")",
					"OPENZWAVE_SECURITY=<!@(find <(OZW_INC) -name ZWSecurity.h | wc -l)"
        		],
				"link_settings": {
					"libraries": ["-lopenzwave"]
				},
				"include_dirs": [
					"<!(node -p -e \"require('path').dirname(require.resolve('nan'))\")",
					"<(OZW_INC)",
					"<(OZW_INC)/value_classes"
				],
				"cflags": [ "-Wno-ignored-qualifiers -Wno-write-strings -Wno-unknown-pragmas" ],
			}],
			['OS=="win"', {
				"include_dirs": [
					"deps/open-zwave/cpp/src/platform/windows"
				],
				'msvs_settings': {
					'VCLinkerTool': {
						'AdditionalDependencies': ['setupapi.lib']
					}
				}
			}]
		],
	}]
}
