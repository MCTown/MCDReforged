import re

from mcdreforged.constants import plugin_constant
from mcdreforged.plugin.meta.metadata import Metadata
from mcdreforged.plugin.type.regular_plugin import RegularPlugin
from mcdreforged.utils import misc_util, string_util


class SoloPlugin(RegularPlugin):
	def get_fallback_metadata_id(self) -> str:
		file_name = string_util.remove_suffix(self.file_name, plugin_constant.SOLO_PLUGIN_FILE_SUFFIX)
		return re.sub(r'[^a-z0-9]', '_', file_name.lower())

	def _get_module_instance(self):
		return misc_util.load_source_from_file_path(self.plugin_path)

	def _on_load(self):
		super()._on_load()
		self._load_entry_instance()
		self._set_metadata(Metadata(self, getattr(self.entry_module_instance, 'PLUGIN_METADATA', None)))
