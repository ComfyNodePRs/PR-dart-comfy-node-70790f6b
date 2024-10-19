from transformers import GenerationConfig, set_seed

from ..models.utils import ModelWrapper
from .type import DART_MODEL_TYPE, DART_GENERATION_CONFIG_TYPE


class UpsamplerNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "dart_model": (DART_MODEL_TYPE,),
                "formatted_prompt": (
                    "STRING",
                    {
                        "lazy": True,
                        "forceInput": True,
                        "tooltip": "Formatted prompt that will be passed to the dart model to upsample tags",
                    },
                ),
                "generation_config": (
                    DART_GENERATION_CONFIG_TYPE,
                    {
                        "tooltip": "Generation configuration for the upmsapling tags",
                    },
                ),
                "seed": (
                    "INT",
                    {
                        "default": 0,
                        "step": 1,
                        "min": 0,
                        "max": 0xFFFFFFFFFFFFFFFF,
                        "display": "number",
                        "lazy": True,
                    },
                ),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("upsampled_tags",)

    FUNCTION = "upsample"

    OUTPUT_NODE = False

    CATEGORY = "prompt/Danbooru Tags Transformer"

    def check_lazy_status(self, dart_model, formatted_prompt, generation_config, seed):
        return ["dart_model", "formatted_prompt", "generation_config", "seed"]

    def upsample(
        self,
        dart_model: ModelWrapper,
        formatted_prompt: str,
        generation_config: GenerationConfig,
        seed: int,
    ):
        set_seed(seed)
        output = dart_model.generate(
            formatted_prompt,
            generation_config,
        )

        return (output,)
