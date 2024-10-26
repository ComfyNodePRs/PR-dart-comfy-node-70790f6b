from .src import nodes

NODE_CLASS_MAPPINGS = {
    "DartLoadModel": nodes.LoadModelNode,
    "DartUpsamplerNode": nodes.UpsamplerNode,
    "DartGenerationConfig": nodes.GenerationConfigNode,
    "DartBanTagsManagerNode": nodes.BanTagsManagerNode,
    #
    "DartV2AutoAspectRatioTag": nodes.V2AutoAspectRatioTagNode,
    "DartV3AutoAspectRatioTag": nodes.V3AutoAspectRatioTagNode,
    #
    "DartV1FormatterNode": nodes.V1FormatterNode,
    "DartV2FormatterNode": nodes.V2FormatterNode,
    "DartV3FormatterNode": nodes.V3FormatterNode,
    #
    "DartUtilsPrintString": nodes.PrintStringNode,
    "DartUtilsConcatString": nodes.ConcatStringNode,
    "DartUtilsEscapeBrackets": nodes.EscapeBracketsNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DartLoadModel": "Dart Load Model",
    "DartUpsamplerNode": "Dart Upsampler",
    "DartGenerationConfig": "Dart Generation Config",
    "DartBanTagsManagerNode": "Dart Ban Tags Manager",
    #
    "DartV2AutoAspectRatioTag": "Dart V2 Auto Aspect Ratio Tag",
    "DartV3AutoAspectRatioTag": "Dart V3 Auto Aspect Ratio Tag",
    #
    #
    "DartV1FormatterNode": "Dart V1 Formatter",
    "DartV2FormatterNode": "Dart V2 Formatter",
    "DartV3FormatterNode": "Dart V3 Formatter",
    #
    "DartUtilsPrintString": "Dart Print String",
    "DartUtilsConcatString": "Dart Concat String",
    "DartUtilsEscapeBrackets": "Dart Escape Brackets",
}

WEB_DIRECTORY = "./src/js"
