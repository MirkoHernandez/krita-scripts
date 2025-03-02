pykrita_dir=$(HOME)/.local/share/krita/pykrita
actions_dir=$(HOME)/.local/share/krita/actions

define install_plugin
	(cd tmp && git clone $1 $2 2>/dev/null) || true
	cp -r tmp/$2/$2 $(pykrita_dir)
	cp  tmp/$2/$2.desktop $(pykrita_dir)
endef

define install_plugin_nested_desktop_file
	(cd tmp && git clone $1 $2 2>/dev/null) || true
	cp -r tmp/$2/$2/$2 $(pykrita_dir)
	cp  tmp/$2/$2/$2.desktop $(pykrita_dir)
	cp  tmp/$2/$2/$2.action $(actions_dir)
endef


# Pixel Art
install_spritesheet_manager:
	$(call install_plugin,https://github.com/Falano/kritaSpritesheetManager,spritesheetExporter)

install_plugins:
	cp -r plugins $(pykrita_dir)

# Drawing Utils 
install_ten_brush_slots:
	$(call install_plugin,https://github.com/lucifer9683/TenBrushSlots,tenbrushslots)

install_composition_helper:
	$(call install_plugin_nested_desktop_file,https://github.com/Grum999/CompositionHelper,compositionhelper)

# UI
install_custom_preview:
	$(call install_plugin,https://github.com/Rolodophone/KritaCustomPreview,custompreview)

install_shortcut_composer:
	$(call install_plugin,https://github.com/wojtryb/Shortcut-Composer,shortcut_composer)

install_ui_redesign:
	$(call install_plugin,https://github.com/veryprofessionaldodo/Krita-UI-Redesign,krita-redesign)

install_tela:
	$(call install_plugin,https://github.com/EyeOdin/Tela,tela)

# Drawing Tablet
config_tablet:
	./bash-scripts/tablet-sway-config
