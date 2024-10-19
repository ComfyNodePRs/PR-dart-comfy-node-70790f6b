from transformers import GenerationConfig

from ..models.utils import ModelWrapper


class UpsamplerNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "dart_model": ("MODEL",),
                "formatted_prompt": (
                    "STRING",
                    {
                        "lazy": True,
                        "forceInput": True,
                    },
                ),
                "generation_config": ("MODEL",),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("upsampled_tags",)

    FUNCTION = "upsample"

    OUTPUT_NODE = False

    CATEGORY = "prompt/Danbooru Tags Transformer"

    def check_lazy_status(self, dart_model, formatted_prompt, generation_config):
        return ["dart_model", "formatted_prompt", "generation_config"]

    def upsample(
        self,
        dart_model: ModelWrapper,
        formatted_prompt: str,
        generation_config: GenerationConfig,
    ):
        output = dart_model.generate(
            formatted_prompt,
            generation_config,
        )

        return (output,)
