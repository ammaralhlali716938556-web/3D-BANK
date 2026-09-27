with open("build_matte_full_game.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Inject I18N data and runtime functions after SVG_ASSETS
target_assets = "const SVG_ASSETS = {svg_assets_json};"
replacement_assets = """const SVG_ASSETS = {svg_assets_json};

  // Multilingual Internationalization (14 Languages)
  const I18N_LANGUAGES = {I18N_LANGUAGES_JSON};
  const I18N_TILES = {I18N_TILES_JSON};
  const I18N_UI = {I18N_UI_JSON};

  let currentLanguage = 'ar';
  try {
    const saved = localStorage.getItem('bank_el_hazz_lang');
    if (saved && I18N_UI[saved]) currentLanguage = saved;
  } catch (e) {}

  function t(key, fallback = '') {
    const cur = I18N_UI[currentLanguage] || I18N_UI['ar'];
    if (cur && cur[key] !== undefined) return cur[key];
    if (I18N_UI['ar'] && I18N_UI['ar'][key] !== undefined) return I18N_UI['ar'][key];
    return fallback || key;
  }

  function getCurrency() {
    return t('currency', 'ج.م');
  }

  function updateRulesModalContent() {
    const modalBody = document.querySelector('#modalRules .modal-body');
    const modalTitle = document.querySelector('#modalRules .modal-title span:last-child');
    const modalBtn = document.querySelector('#modalRules .modal-footer button');
    if (!modalBody) return;
    
    if (currentLanguage === 'ar') {
      if (modalTitle) modalTitle.innerText = 'دليل وقواعد بنك الحظ & مونوبولي جو (نزال 1 ضد 1)';
      if (modalBtn) modalBtn.innerText = 'فهمت القواعد! هيا لنلعب';
      modalBody.innerHTML = `
        <h3 style="color: #fef08a; margin-bottom: 6px;">⚔️ نظام المواجهة الثنائية (1 ضد 1):</h3>
        <ul style="padding-right: 20px; margin-bottom: 14px;">
          <li><b>المواجهة المباشرة:</b> مواجهة سريعة ومثيرة! كل رمية نرد وكل عقار تشتريه يقلص خيارات خصمك.</li>
          <li><b>شراء المدن وتأسيس الطوابق:</b> بعد امتلاك كامل مدن المجموعة اللونية يمكنك بناء طوابق ليمونية (من 1 إلى 4) بقيمة 33% من سعر العقار، وعند اكتمال 4 طوابق في المجموعة يُتاح بناء برج إيفل الذهبي (الطابق الخامس) لرفع الأرباح بنسبة 50% لكل طابق!</li>
          <li><b>المفاوضة والتبادل:</b> يمكنك في أي وقت بدء مفاوضة لشراء عقارات خصمك أو تبادل الأراضي.</li>
        </ul>
        <h3 style="color: #38bdf8; margin-bottom: 6px;">🎲 قواعد الرقعة الكلاسيكية (40 مربعاً):</h3>
        <ul style="padding-right: 20px; margin-bottom: 14px;">
          <li><b>نقطة البداية (انطلق):</b> مر أو اهبط عليها لتقبض 200 ج.م.</li>
          <li><b>الاستراحة المجانية:</b> تجمع كل ضرائب اللاعبين وغرامات الرادار، ومن يقف عليها يفوز بالحصيلة كاملة!</li>
          <li><b>سجن القلعة:</b> يدخله اللاعب عند مربع ادخل السجن أو كروت الحظ أو رمي دبل 3 مرات متتالية.</li>
        </ul>
      `;
    } else {
      const isEuro = ['en', 'fr', 'ru', 'es', 'pt', 'de', 'it', 'tr'].includes(currentLanguage);
      const regionName = isEuro ? 'European Capitals' : 'Asian Capitals';
      if (modalTitle) modalTitle.innerText = `${t('gameTitle')} - Rules & Guide`;
      if (modalBtn) modalBtn.innerText = t('btnStartGame', 'Got it! Let\'s Play');
      modalBody.innerHTML = `
        <h3 style="color: #fef08a; margin-bottom: 6px;">⚔️ Head-to-Head Duel Mode (1 vs 1):</h3>
        <ul style="padding-left: 20px; margin-bottom: 14px;">
          <li><b>Direct Clash:</b> Fast-paced, high-stakes duel on an authentic 40-tile board featuring ${regionName}!</li>
          <li><b>City Monopoly & Floors:</b> Own all properties of a color group to build lime floors (1 to 4) at 33% of base value. Reaching 4 floors unlocks the Golden Eiffel Tower (5th level), boosting rent by +50% of floor cost per level!</li>
          <li><b>Trade & Negotiation:</b> Negotiate buyouts and swap real estate with your rival at any time.</li>
        </ul>
        <h3 style="color: #38bdf8; margin-bottom: 6px;">🎲 Classic Board Rules:</h3>
        <ul style="padding-left: 20px; margin-bottom: 14px;">
          <li><b>GO (Start):</b> Collect 200 ${getCurrency()} as you pass or land.</li>
          <li><b>Free Parking Pot:</b> Collects all tax penalties. Land here to claim the entire accumulated fortune!</li>
          <li><b>Citadel Jail:</b> Sent to jail by landing on 'Go to Jail', drawing a jail card, or rolling doubles 3 times.</li>
        </ul>
      `;
    }
  }

  function setGameLanguage(langCode, save = true) {
    if (!I18N_LANGUAGES.some(l => l.code === langCode)) langCode = 'ar';
    currentLanguage = langCode;
    if (save) {
      try { localStorage.setItem('bank_el_hazz_lang', langCode); } catch (e) {}
    }

    const langInfo = I18N_LANGUAGES.find(l => l.code === langCode) || I18N_LANGUAGES[0];
    document.documentElement.lang = langCode;
    document.documentElement.dir = langInfo.dir || (langCode === 'ar' || langCode === 'fa' ? 'rtl' : 'ltr');

    // Sync all 3 dropdowns
    ['settingsLanguageSelect', 'setupLanguageSelect', 'headerLanguageSelect'].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.value = langCode;
    });

    // Update TILES property names & subtitles
    if (I18N_TILES[langCode]) {
      TILES.forEach(tile => {
        const trans = I18N_TILES[langCode][tile.id] || I18N_TILES[langCode][String(tile.id)];
        if (trans) {
          tile.name = trans.name;
          tile.subtitle = trans.sub;
        }
      });
    }

    // Update board city label
    const cityLbl = document.getElementById('boardCityLabel');
    if (cityLbl) cityLbl.innerText = t('boardCitySub');

    const titleElem = document.getElementById('boardTitleText');
    if (titleElem) titleElem.innerText = t('gameTitle');

    // Update bot name if applicable
    if (state.players && state.players[1] && state.players[1].isBot) {
      state.players[1].name = t('botDefault', 'روبوت');
      const p2Input = document.getElementById('setupPlayer2Name');
      if (p2Input) p2Input.value = t('botDefault', 'روبوت');
    }

    // Re-render board tiles with updated city names and currencies
    renderBoardTiles();

    // Update Header Buttons
    const btnLandmarksText = document.getElementById('btnLandmarksText');
    if (btnLandmarksText) btnLandmarksText.innerText = t('landmarksTitle', 'معالم المدينة');

    const btnWheelText = document.getElementById('btnWheelText');
    if (btnWheelText) btnWheelText.innerText = t('wheelTitle', 'عجلة الحظ');

    const btnTradeText = document.getElementById('btnTradeText');
    if (btnTradeText) btnTradeText.innerText = t('btnTrade');

    const btnCardRulesText = document.getElementById('btnCardRulesText');
    if (btnCardRulesText) btnCardRulesText.innerText = t('btnCardRules');

    const btnRulesText = document.getElementById('btnRulesText');
    if (btnRulesText) btnRulesText.innerText = t('btnRules');

    const btnSettingsNavText = document.getElementById('btnSettingsNavText');
    if (btnSettingsNavText) btnSettingsNavText.innerText = t('btnSettings');

    const btnReset = document.getElementById('btnResetGame');
    if (btnReset) btnReset.title = t('btnNewGame');

    // Update Center & Bottom Indicators
    const potLbl = document.getElementById('potLabelText');
    if (potLbl) potLbl.innerText = t('freeParkingPot');

    const energyLbl = document.getElementById('energyLabelText');
    if (energyLbl) energyLbl.innerText = t('diceEnergy');

    const rollBtnText = document.getElementById('btnRollDiceText');
    if (rollBtnText) rollBtnText.innerText = t('btnRollDice');

    const logTitle = document.getElementById('activityLogTitle');
    if (logTitle) logTitle.innerText = t('activityLogTitle');

    const clearLogBtn = document.getElementById('btnClearLog');
    if (clearLogBtn) clearLogBtn.innerText = t('clearLog');

    // Update Setup Modal Strings
    const setupTitle = document.getElementById('setupModalTitleText');
    if (setupTitle) setupTitle.innerText = t('setupModalTitle');

    const lblSetupLang = document.getElementById('lblSetupLang');
    if (lblSetupLang) lblSetupLang.innerText = t('setupLanguageLabel');

    const lblSetupMode = document.getElementById('lblSetupMode');
    if (lblSetupMode) lblSetupMode.innerText = t('setupModeLabel');

    const pillModeBot = document.getElementById('pillModeBotTitle');
    if (pillModeBot) pillModeBot.innerText = t('modeBot');

    const pillModeBotSub = document.getElementById('pillModeBotSub');
    if (pillModeBotSub) pillModeBotSub.innerText = t('modeBotSub');

    const pillModeHuman = document.getElementById('pillModeHumanTitle');
    if (pillModeHuman) pillModeHuman.innerText = t('modeHuman');

    const pillModeHumanSub = document.getElementById('pillModeHumanSub');
    if (pillModeHumanSub) pillModeHumanSub.innerText = t('modeHumanSub');

    const lblSetupNames = document.getElementById('lblSetupNames');
    if (lblSetupNames) lblSetupNames.innerText = t('setupNamesLabel');

    const p1Pfx = document.getElementById('p1Prefix');
    if (p1Pfx) p1Pfx.innerText = t('p1Prefix');

    const p2Pfx = document.getElementById('p2Prefix');
    if (p2Pfx) p2Pfx.innerText = t('p2Prefix');

    const lblSetupMoney = document.getElementById('lblSetupMoney');
    if (lblSetupMoney) lblSetupMoney.innerText = t('setupMoneyLabel');

    const pillM3 = document.getElementById('pillMoney3kSub');
    if (pillM3) pillM3.innerText = t('money3kSub');

    const pillM6 = document.getElementById('pillMoney6kSub');
    if (pillM6) pillM6.innerText = t('money6kSub');

    const pillM9 = document.getElementById('pillMoney9kSub');
    if (pillM9) pillM9.innerText = t('money9kSub');

    const lblSetupDiff = document.getElementById('lblSetupDiff');
    if (lblSetupDiff) lblSetupDiff.innerText = t('setupDifficultyLabel');

    const pillDiffEasy = document.getElementById('pillDiffEasyTitle');
    if (pillDiffEasy) pillDiffEasy.innerText = t('diffEasy');

    const pillDiffEasySub = document.getElementById('pillDiffEasySub');
    if (pillDiffEasySub) pillDiffEasySub.innerText = t('diffEasySub');

    const pillDiffMed = document.getElementById('pillDiffMediumTitle');
    if (pillDiffMed) pillDiffMed.innerText = t('diffMedium');

    const pillDiffMedSub = document.getElementById('pillDiffMediumSub');
    if (pillDiffMedSub) pillDiffMedSub.innerText = t('diffMediumSub');

    const pillDiffHard = document.getElementById('pillDiffHardTitle');
    if (pillDiffHard) pillDiffHard.innerText = t('diffHard');

    const pillDiffHardSub = document.getElementById('pillDiffHardSub');
    if (pillDiffHardSub) pillDiffHardSub.innerText = t('diffHardSub');

    const btnStartGame = document.getElementById('btnStartGameText');
    if (btnStartGame) btnStartGame.innerText = t('btnStartGame');

    // Update Settings Modal Strings
    const settingsTitle = document.getElementById('settingsModalTitle');
    if (settingsTitle) settingsTitle.innerText = t('btnSettings');

    const lblSettingsLang = document.getElementById('lblSettingsLang');
    if (lblSettingsLang) lblSettingsLang.innerText = t('setupLanguageLabel');

    const lblSettingsDiff = document.getElementById('lblSettingsDiff');
    if (lblSettingsDiff) lblSettingsDiff.innerText = t('setupDifficultyLabel');

    const sDiffEasy = document.getElementById('pillDiffEasyTitle');
    if (sDiffEasy) sDiffEasy.innerText = t('diffEasy');

    const sDiffMed = document.getElementById('pillDiffMediumTitle');
    if (sDiffMed) sDiffMed.innerText = t('diffMedium');

    const sDiffHard = document.getElementById('pillDiffHardTitle');
    if (sDiffHard) sDiffHard.innerText = t('diffHard');

    const btnSaveSettings = document.getElementById('btnSaveSettingsText');
    if (btnSaveSettings) btnSaveSettings.innerText = t('btnSaveSettings');

    updateRulesModalContent();
    updateUI();
  }"""

# Remember in python f-string, internal { and } must be doubled {{ and }}
# Except {I18N_LANGUAGES_JSON}, {I18N_TILES_JSON}, {I18N_UI_JSON}
replacement_assets_escaped = replacement_assets.replace("{", "{{").replace("}", "}}")
# Now restore the 3 variable interpolations
replacement_assets_escaped = replacement_assets_escaped.replace("{{I18N_LANGUAGES_JSON}}", "{I18N_LANGUAGES_JSON}")
replacement_assets_escaped = replacement_assets_escaped.replace("{{I18N_TILES_JSON}}", "{I18N_TILES_JSON}")
replacement_assets_escaped = replacement_assets_escaped.replace("{{I18N_UI_JSON}}", "{I18N_UI_JSON}")
replacement_assets_escaped = replacement_assets_escaped.replace("{{svg_assets_json}}", "{svg_assets_json}")

assert target_assets in code, "SVG_ASSETS target not found"
code = code.replace(target_assets, replacement_assets_escaped, 1)

with open("build_matte_full_game.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Part 2 applied successfully!")
