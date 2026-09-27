import json
import i18n_module

new_ui_keys = {
    'btnAboutUs': {
        'ar': 'ℹ️ من نحن (عن اللعبة)',
        'en': 'ℹ️ About Us',
        'zh': 'ℹ️ 关于我们',
        'fr': 'ℹ️ À propos',
        'es': 'ℹ️ Sobre nosotros',
        'ru': 'ℹ️ О нас',
        'de': 'ℹ️ Über uns',
        'it': 'ℹ️ Chi siamo',
        'pt': 'ℹ️ Sobre nós',
        'tr': 'ℹ️ Hakkımızda',
        'hi': 'ℹ️ हमारे बारे में',
        'ja': 'ℹ️ このゲームについて',
        'ko': 'ℹ️ 게임 정보',
        'fa': 'ℹ️ درباره ما'
    },
    'btnTokenPicker': {
        'ar': '🎭 تغيير واختيار أيقونة البيدق',
        'en': '🎭 Change Player Token',
        'zh': '🎭 选择更换玩家棋子',
        'fr': '🎭 Choisir son pion',
        'es': '🎭 Cambiar ficha de jugador',
        'ru': '🎭 Выбрать фишку игрока',
        'de': '🎭 Spielfigur auswählen',
        'it': '🎭 Scegli la tua pedina',
        'pt': '🎭 Escolher peão do jogador',
        'tr': '🎭 Oyuncu Piyonunu Seç',
        'hi': '🎭 खिलाड़ी का मोहरा चुनें',
        'ja': '🎭 プレイヤーのコマ変更',
        'ko': '🎭 플레이어 말 선택',
        'fa': '🎭 تغییر مهره بازیکن'
    },
    'aboutUsModalTitle': {
        'ar': 'من نحن - بنك الحظ 3D',
        'en': 'About Us - Bank El Hazz 3D',
        'zh': '关于我们 - 3D幸运银行',
        'fr': 'À propos - Bank El Hazz 3D',
        'es': 'Sobre nosotros - Bank El Hazz 3D',
        'ru': 'О нас - Банк Удачи 3D',
        'de': 'Über uns - Bank El Hazz 3D',
        'it': 'Chi siamo - Bank El Hazz 3D',
        'pt': 'Sobre nós - Bank El Hazz 3D',
        'tr': 'Hakkımızda - Bank El Hazz 3D',
        'hi': 'हमारे बारे में - बैंक एल हज़ 3D',
        'ja': '概要 - バンク・エル・ハズ 3D',
        'ko': '정보 - 뱅크 엘 하즈 3D',
        'fa': 'درباره ما - بانک شانس 3D'
    },
    'tokenPickerModalTitle': {
        'ar': 'اختيار وتغيير أيقونة البيدق',
        'en': 'Choose Player Token',
        'zh': '选择玩家棋子',
        'fr': 'Choisir votre pion',
        'es': 'Elige tu ficha',
        'ru': 'Выберите фишку',
        'de': 'Spielfigur wählen',
        'it': 'Scegli la tua pedina',
        'pt': 'Escolha o seu peão',
        'tr': 'Piyonunu Seç',
        'hi': 'अपना मोहरा चुनें',
        'ja': 'コマを選択',
        'ko': '말 선택',
        'fa': 'انتخاب مهره بازی'
    }
}

ui_data = i18n_module.I18N_UI
for k, m in new_ui_keys.items():
    for l, val in m.items():
        if l in ui_data:
            ui_data[l][k] = val

# Generate clean options HTML for settings
options_html = "\n".join([f'            <option value="{l["code"]}">{l["flag"]} {l["name"]}</option>' for l in i18n_module.I18N_LANGUAGES])

modal_settings_html = f'''
  <!-- MODAL 14: Game Settings & Speed Modal -->
  <div class="modal-overlay" id="modalSettings">
    <div class="modal-box modal-setup-box" style="max-width: 500px;">
      <div class="modal-header">
        <div class="modal-title">
          <span>⚙️</span>
          <span id="settingsModalTitle">الإعدادات والخيارات</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalSettings')">&times;</button>
      </div>
      <div class="setup-modal-body">
        
        <!-- Language Selection Dropdown (Only in Settings) -->
        <div class="setup-group">
          <label class="setup-label" id="lblSettingsLang">🌐 اختر لغة اللعبة (Language):</label>
          <select class="setup-select" id="settingsLanguageSelect">
{options_html}
          </select>
        </div>

        <!-- Dice Roll Speed -->
        <div class="setup-group">
          <label class="setup-label" id="lblSettingsDiceSpeed">🎲 سرعة دحرجة النرد:</label>
          <div class="setup-pill-group" id="settingsDiceSpeedGroup">
            <button type="button" class="setup-pill" data-speed="slow">
              <span class="setup-pill-icon">🐢</span>
              <span class="setup-pill-title" id="pillDiceSlowTitle">بطيء</span>
            </button>
            <button type="button" class="setup-pill active" data-speed="normal">
              <span class="setup-pill-icon">🚶</span>
              <span class="setup-pill-title" id="pillDiceNormalTitle">عادي</span>
            </button>
            <button type="button" class="setup-pill" data-speed="fast">
              <span class="setup-pill-icon">⚡</span>
              <span class="setup-pill-title" id="pillDiceFastTitle">سريع</span>
            </button>
            <button type="button" class="setup-pill" data-speed="instant">
              <span class="setup-pill-icon">🚀</span>
              <span class="setup-pill-title" id="pillDiceInstantTitle">فائق</span>
            </button>
          </div>
        </div>

        <!-- Movement / Pawn Speed -->
        <div class="setup-group">
          <label class="setup-label" id="lblSettingsMoveSpeed">🏃 سرعة حركة اللاعبين:</label>
          <div class="setup-pill-group" id="settingsMoveSpeedGroup">
            <button type="button" class="setup-pill" data-speed="slow">
              <span class="setup-pill-icon">🐢</span>
              <span class="setup-pill-title" id="pillMoveSlowTitle">بطيء</span>
            </button>
            <button type="button" class="setup-pill active" data-speed="normal">
              <span class="setup-pill-icon">🚶</span>
              <span class="setup-pill-title" id="pillMoveNormalTitle">عادي</span>
            </button>
            <button type="button" class="setup-pill" data-speed="fast">
              <span class="setup-pill-icon">⚡</span>
              <span class="setup-pill-title" id="pillMoveFastTitle">سريع</span>
            </button>
            <button type="button" class="setup-pill" data-speed="instant">
              <span class="setup-pill-icon">🚀</span>
              <span class="setup-pill-title" id="pillMoveInstantTitle">فائق</span>
            </button>
          </div>
        </div>

        <!-- AI Difficulty In Settings -->
        <div class="setup-group">
          <label class="setup-label" id="lblSettingsDiff">⚡ صعوبة الذكاء الاصطناعي (الروبوت):</label>
          <div class="setup-pill-group" id="settingsDiffGroup">
            <button type="button" class="setup-pill" data-diff="easy">
              <span class="setup-pill-icon">🟢</span>
              <span class="setup-pill-title" id="settingsDiffEasyTitle">سهل</span>
            </button>
            <button type="button" class="setup-pill active" data-diff="medium">
              <span class="setup-pill-icon">🟡</span>
              <span class="setup-pill-title" id="settingsDiffMediumTitle">متوسط</span>
            </button>
            <button type="button" class="setup-pill" data-diff="hard">
              <span class="setup-pill-icon">🔴</span>
              <span class="setup-pill-title" id="settingsDiffHardTitle">صعب</span>
            </button>
          </div>
        </div>

        <!-- Change Player Token Button -->
        <div class="setup-group">
          <label class="setup-label" id="lblSettingsToken">🎭 مظهر البيدق والأيقونة:</label>
          <button type="button" class="btn-matte gold" id="btnOpenTokenPicker" style="width: 100%; padding: 12px; font-size: 15px; border-radius: 10px;">
            <span>🎭</span>
            <span id="btnTokenPickerText">تغيير واختيار أيقونة البيدق</span>
          </button>
        </div>

        <!-- Audio Quick Toggle -->
        <div class="setup-group">
          <label class="setup-label" id="lblSettingsAudio">🔊 المؤثرات الصوتية:</label>
          <button type="button" class="btn-matte" id="btnSettingsToggleAudio" style="width: 100%; padding: 12px; font-size: 15px; border-radius: 10px;">
            <span id="settingsAudioIcon">🔊</span>
            <span id="settingsAudioText">المؤثرات الصوتية: مفعلة</span>
          </button>
        </div>

        <!-- About Us Button -->
        <div class="setup-group">
          <button type="button" class="btn-matte" id="btnOpenAboutUs" style="width: 100%; padding: 12px; font-size: 15px; border-radius: 10px; background: rgba(56, 189, 248, 0.15); border-color: #0284c7;">
            <span>ℹ️</span>
            <span id="btnAboutUsText">من نحن (عن اللعبة)</span>
          </button>
        </div>

        <button class="btn-matte btn-start-game" id="btnSaveSettingsApply" style="margin-top: 14px;">
          <span id="btnSaveSettingsText">💾 حفظ وتطبيق الإعدادات</span>
        </button>

      </div>
    </div>
  </div>
'''

with open('i18n_module.py', 'w', encoding='utf-8') as f:
    f.write('# Multilingual Module for Bank El Hazz 3D (14 Languages)\n')
    f.write('import json\n\n')
    f.write(f'I18N_LANGUAGES = {json.dumps(i18n_module.I18N_LANGUAGES, ensure_ascii=False, indent=2)}\n\n')
    f.write(f'I18N_TILES = {json.dumps(i18n_module.I18N_TILES, ensure_ascii=False, indent=2)}\n\n')
    f.write(f'I18N_UI = {json.dumps(ui_data, ensure_ascii=False, indent=2)}\n\n')
    f.write(f'I18N_CSS = {json.dumps(i18n_module.I18N_CSS, ensure_ascii=False)}\n\n')
    f.write(f'SETTINGS_MODAL_HTML = {json.dumps(modal_settings_html, ensure_ascii=False)}\n\n')
    f.write('I18N_LANGUAGES_JSON = json.dumps(I18N_LANGUAGES, ensure_ascii=False)\n')
    f.write('I18N_TILES_JSON = json.dumps(I18N_TILES, ensure_ascii=False)\n')
    f.write('I18N_UI_JSON = json.dumps(I18N_UI, ensure_ascii=False)\n')

print("i18n_module.py updated with About Us and Token Picker buttons in Settings!")
