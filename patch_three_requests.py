with open("build_matte_full_game.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add token_rocket and token_diamond to all_svgs
target_svgs = "all_svgs['golden_eiffel_3d'] = '''<svg viewBox=\"0 0 60 70\" xmlns=\"http://www.w3.org/2000/svg\">"
replacement_svgs = """all_svgs['token_rocket'] = '''<svg viewBox=\"0 0 60 60\" xmlns=\"http://www.w3.org/2000/svg\">
  <defs>
    <radialGradient id=\"rkt_ao\" cx=\"50%\" cy=\"50%\" r=\"50%\">
      <stop offset=\"0%\" stop-color=\"rgba(0,0,0,0.6)\"/>
      <stop offset=\"100%\" stop-color=\"rgba(0,0,0,0)\"/>
    </radialGradient>
    <linearGradient id=\"rkt_body\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">
      <stop offset=\"0%\" stop-color=\"#fef08a\"/>
      <stop offset=\"50%\" stop-color=\"#f59e0b\"/>
      <stop offset=\"100%\" stop-color=\"#b45309\"/>
    </linearGradient>
    <linearGradient id=\"rkt_fin\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">
      <stop offset=\"0%\" stop-color=\"#ef4444\"/>
      <stop offset=\"100%\" stop-color=\"#991b1b\"/>
    </linearGradient>
  </defs>
  <ellipse cx=\"30\" cy=\"54\" rx=\"20\" ry=\"4.5\" fill=\"url(#rkt_ao)\"/>
  <path d=\"M 30,8 C 24,18 20,34 22,46 L 38,46 C 40,34 36,18 30,8 Z\" fill=\"url(#rkt_body)\" stroke=\"#78350f\" stroke-width=\"0.8\"/>
  <path d=\"M 22,36 L 14,46 L 22,46 Z\" fill=\"url(#rkt_fin)\"/>
  <path d=\"M 38,36 L 46,46 L 38,46 Z\" fill=\"url(#rkt_fin)\"/>
  <circle cx=\"30\" cy=\"24\" r=\"4.5\" fill=\"#38bdf8\" stroke=\"#0284c7\" stroke-width=\"0.8\"/>
  <polygon points=\"26,46 30,53 34,46\" fill=\"#f97316\"/>
</svg>'''

all_svgs['token_diamond'] = '''<svg viewBox=\"0 0 60 60\" xmlns=\"http://www.w3.org/2000/svg\">
  <defs>
    <radialGradient id=\"dia_ao\" cx=\"50%\" cy=\"50%\" r=\"50%\">
      <stop offset=\"0%\" stop-color=\"rgba(0,0,0,0.55)\"/>
      <stop offset=\"100%\" stop-color=\"rgba(0,0,0,0)\"/>
    </radialGradient>
    <linearGradient id=\"dia_grad\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">
      <stop offset=\"0%\" stop-color=\"#a7f3d0\"/>
      <stop offset=\"40%\" stop-color=\"#10b981\"/>
      <stop offset=\"100%\" stop-color=\"#047857\"/>
    </linearGradient>
  </defs>
  <ellipse cx=\"30\" cy=\"54\" rx=\"20\" ry=\"4.5\" fill=\"url(#dia_ao)\"/>
  <polygon points=\"18,22 42,22 50,32 30,50 10,32\" fill=\"url(#dia_grad)\" stroke=\"#065f46\" stroke-width=\"0.8\"/>
  <polygon points=\"22,22 38,22 35,32 25,32\" fill=\"#d1fae5\" opacity=\"0.7\"/>
  <polygon points=\"18,22 22,22 25,32 10,32\" fill=\"#6ee7b7\" opacity=\"0.8\"/>
  <polygon points=\"38,22 42,22 50,32 35,32\" fill=\"#059669\" opacity=\"0.8\"/>
  <polygon points=\"25,32 35,32 30,50\" fill=\"#34d399\"/>
</svg>'''

all_svgs['golden_eiffel_3d'] = '''<svg viewBox=\"0 0 60 70\" xmlns=\"http://www.w3.org/2000/svg\">"""
assert target_svgs in code, "target_svgs not found"
code = code.replace(target_svgs, replacement_svgs, 1)

# 2. Add CSS for token picker grid
token_picker_css = """
/* Token Picker Modal Grid */
.token-picker-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-top: 10px;
}
@media (max-width: 500px) {
  .token-picker-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
.token-card {
  background: rgba(0, 0, 0, 0.45);
  border: 2px solid #78350f;
  border-radius: 12px;
  padding: 10px 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}
.token-card:hover {
  border-color: #f59e0b;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(245, 158, 11, 0.3);
}
.token-card.active {
  border-color: #10b981;
  background: rgba(16, 185, 129, 0.18);
  box-shadow: 0 0 16px rgba(16, 185, 129, 0.4);
}
.token-preview-box {
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.token-title-label {
  font-size: 12px;
  font-weight: 800;
  color: #fef08a;
  text-align: center;
}
"""

css_append_target = "MATTE_PHYSICAL_CSS += \"\\n\" + I18N_CSS"
css_append_replacement = f"MATTE_PHYSICAL_CSS += \"\\n\" + I18N_CSS + \"\"\"{token_picker_css}\"\"\""
assert css_append_target in code, "css_append_target not found"
code = code.replace(css_append_target, css_append_replacement, 1)

# 3. Remove btnPreviewCards from header-actions
target_header_cards = """      <button class="btn-matte" id="btnPreviewCards" title="استعراض شروط الكروت في رقعة اللعب مكان الأهرامات">
        <span>🃏</span>
        <span id="btnCardRulesText">شروط الكروت</span>
      </button>"""
assert target_header_cards in code, "target_header_cards not found"
code = code.replace(target_header_cards, "", 1)

# Guard btnPreviewCards listener in DOMContentLoaded
target_cards_listener = "document.getElementById('btnPreviewCards').addEventListener('click', () => openModal('modalCardsSelector'));"
replacement_cards_listener = "const btnPrevCards = document.getElementById('btnPreviewCards'); if (btnPrevCards) btnPrevCards.addEventListener('click', () => openModal('modalCardsSelector'));"
if target_cards_listener in code:
    code = code.replace(target_cards_listener, replacement_cards_listener, 1)

# 4. Inject modalAboutUs and modalTokenPicker after {SETTINGS_MODAL_HTML}
target_settings_inject = "{SETTINGS_MODAL_HTML}"
replacement_modals = """{SETTINGS_MODAL_HTML}

  <!-- MODAL 15: About Us Modal -->
  <div class="modal-overlay" id="modalAboutUs">
    <div class="modal-box modal-setup-box" style="max-width: 520px; text-align: center;">
      <div class="modal-header">
        <div class="modal-title">
          <span>ℹ️</span>
          <span id="aboutUsModalTitle">من نحن - بنك الحظ 3D</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalAboutUs')">✕</button>
      </div>
      <div class="setup-modal-body" style="line-height: 1.8; font-size: 13.5px; color: #fdfbf7;">
        <div style="text-align: center; margin-bottom: 14px;">
          <div style="font-size: 42px;">🎲 🏛️ 🇾🇪</div>
          <h2 style="color: #fef08a; font-size: 18px; margin: 4px 0;" id="aboutUsGameTitle">لعبة بنك الحظ 3D الفاخرة</h2>
          <div style="color: #38bdf8; font-size: 12px; font-weight: 700;" id="aboutUsVersionText">الإصدار 2.5 • نسخة النزال الثنائي الحقيقي</div>
        </div>
        <p id="aboutUsDescText" style="margin-bottom: 12px; text-align: justify;">
          لعبة بنك الحظ ثلاثية الأبعاد هي تجربة إلكترونية استراتيجية فريدة مستوحاة من رقعة المونوبولي الكلاسيكية وعواصم العالم العربي والأوروبي والآسيوي. تتميز بنظام نزالات تكتيكية حية (1 ضد 1)، وبناء الطوابق الليمونية، وتتويج برج إيفل الذهبي، وغرفة المفاوضات والتبادلات، وعجلة الحظ ذات المخاطر والأرباح، ومحرك صوتي تفاعلي متقدم.
        </p>
        <div style="background: rgba(0,0,0,0.4); padding: 12px; border-radius: 10px; border: 1px solid #b45309; text-align: right;">
          <div style="color: #f59e0b; font-weight: 800; margin-bottom: 6px;" id="aboutUsFeaturesTitle">✨ أبرز المزايا المطورة:</div>
          <ul style="padding-right: 18px; margin: 0; font-size: 12.5px; color: #e2e8f0; line-height: 1.7;" id="aboutUsFeaturesList">
            <li>رقعة لعب كلاسيكية حقيقية بـ 40 مربعاً ثلاثي الأبعاد.</li>
            <li>دعم 14 لغة عالمية مع تبديل العواصم جغرافياً والعلم اليمني 🇾🇪.</li>
            <li>بيادق ثلاثية الأبعاد ساكنة تماماً أثناء حركة المنافس.</li>
            <li>التحكم في سرعة دحرجة النرد وسرعة قفز اللاعبين.</li>
            <li>عجلة الحظ والمجازفة (ربح وخسارة) تظهر فقط عند الفوز بها.</li>
            <li>شروط الكروت مدمجة ومقروءة مباشرة داخل دليل القواعد.</li>
            <li>إمكانية تغيير واختيار أيقونة وشكل البيدق ثلاثي الأبعاد.</li>
          </ul>
        </div>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <button class="btn-matte gold" onclick="closeModal('modalAboutUs')">
          <span id="btnAboutUsClose">فهمت، حسناً</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 16: Token / Pawn Customization Modal -->
  <div class="modal-overlay" id="modalTokenPicker">
    <div class="modal-box modal-setup-box" style="max-width: 520px; text-align: center;">
      <div class="modal-header">
        <div class="modal-title">
          <span>🎭</span>
          <span id="tokenPickerModalTitle">اختيار وتغيير أيقونة البيدق</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalTokenPicker')">✕</button>
      </div>
      <div class="setup-modal-body">
        <div style="font-size: 13px; color: #cbd5e1; margin-bottom: 12px;" id="tokenPickerSubText">
          اختر البيدق ثلاثي الأبعاد المفضل لتمثيلك على رقعة اللعب:
        </div>
        <div class="token-picker-grid" id="tokenPickerGrid">
          <!-- Populated dynamically via JS -->
        </div>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <button class="btn-matte gold" onclick="closeModal('modalTokenPicker')">
          <span>تم الاختيار ✅</span>
        </button>
      </div>
    </div>
  </div>"""
assert target_settings_inject in code, "target_settings_inject not found"
code = code.replace(target_settings_inject, replacement_modals, 1)

# 5. Update updateRulesModalContent to include the rich non-interactive card rules section
target_rules_func = """    if (currentLanguage === 'ar') {
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
    } else {"""

replacement_rules_func = """    if (currentLanguage === 'ar') {
      if (modalTitle) modalTitle.innerText = 'دليل وقواعد بنك الحظ & مونوبولي جو (نزال 1 ضد 1)';
      if (modalBtn) modalBtn.innerText = 'فهمت القواعد! هيا لنلعب';
      modalBody.innerHTML = `
        <h3 style="color: #fef08a; margin-bottom: 6px;">⚔️ نظام المواجهة الثنائية (1 ضد 1):</h3>
        <ul style="padding-right: 20px; margin-bottom: 14px;">
          <li><b>المواجهة المباشرة:</b> مواجهة سريعة ومثيرة! كل رمية نرد وكل عقار تشتريه يقلص خيارات خصمك.</li>
          <li><b>شراء المدن وتأسيس الطوابق:</b> بعد امتلاك كامل مدن المجموعة اللونية يمكنك بناء طوابق ليمونية (من 1 إلى 4) بقيمة 33% من سعر العقار، وعند اكتمال 4 طوابق في المجموعة يُتاح بناء برج إيفل الذهبي (الطابق الخامس) لرفع الأرباح بنسبة 50% لكل طابق!</li>
          <li><b>المفاوضة والتبادل:</b> يمكنك في أي وقت بدء مفاوضة لشراء عقارات خصمك أو تبادل الأراضي.</li>
        </ul>

        <div style="background: rgba(245, 158, 11, 0.1); border: 1px solid #b45309; border-radius: 12px; padding: 12px; margin-top: 14px; margin-bottom: 14px;">
          <h3 style="color: #fbbf24; margin: 0 0 8px 0; font-size: 14.5px;">🃏 دليل وشروط كروت الرقعة (قراءة فقط):</h3>
          
          <div style="display: flex; flex-direction: column; gap: 8px; font-size: 12.5px;">
            <div style="background: rgba(0,0,0,0.35); padding: 8px 10px; border-radius: 8px; border-right: 3px solid #3b82f6;">
              <b style="color: #60a5fa;">🎁 كروت صندوق الدنيا:</b> كروت مفاجآت تمنح أرباحاً نقدية أو هدايا، أو تفرض فواتير مخفضة، أو تمنح تذكرة خاصة لدخول عجلة الحظ والمجازفة.
            </div>
            <div style="background: rgba(0,0,0,0.35); padding: 8px 10px; border-radius: 8px; border-right: 3px solid #ec4899;">
              <b style="color: #f472b6;">❓ كروت الحظ:</b> كروت مصيرية تقلب الموازين تشمل السطو على الخصم، هجوم التعطيل، شحن الدروع، لفة عجلة الحظ، أو أمر الحبس الفوري.
            </div>
            <div style="background: rgba(0,0,0,0.35); padding: 8px 10px; border-radius: 8px; border-right: 3px solid #ef4444;">
              <b style="color: #f87171;">💸 ضريبة الدخل (200 ج.م):</b> عند الهبوط على المربع رقم 4 يُسدد رسم حكومي بقيمة 200 ج.م يودع فوراً في وعاء الاستراحة المجانية.
            </div>
            <div style="background: rgba(0,0,0,0.35); padding: 8px 10px; border-radius: 8px; border-right: 3px solid #a855f7;">
              <b style="color: #c084fc;">💎 ضريبة الرفاهية (100 ج.م):</b> عند الهبوط على المربع رقم 38 يُسدد رسم أصول بقيمة 100 ج.م لحصيلة وعاء الاستراحة.
            </div>
            <div style="background: rgba(0,0,0,0.35); padding: 8px 10px; border-radius: 8px; border-right: 3px solid #e11d48;">
              <b style="color: #fb7185;">⛓️ أمر الحبس بسجن القلعة:</b> يصدر عند مربع ادخل السجن (رقم 30) أو كرت الحبس. للخروج: ارمِ دبل أو انتظر 3 أدوار مع كفالة 50 ج.م.
            </div>
            <div style="background: rgba(0,0,0,0.35); padding: 8px 10px; border-radius: 8px; border-right: 3px solid #10b981;">
              <b style="color: #34d399;">👮 سجن القلعة (زيارة بريئة):</b> الهبوط الطبيعي على المربع رقم 10 مجرد زيارة تفقدية آمنة دون أي غرامة أو توقيف.
            </div>
          </div>
        </div>

        <h3 style="color: #38bdf8; margin-bottom: 6px;">🎲 قواعد الرقعة الكلاسيكية (40 مربعاً):</h3>
        <ul style="padding-right: 20px; margin-bottom: 14px;">
          <li><b>نقطة البداية (انطلق):</b> مر أو اهبط عليها لتقبض 200 ج.م.</li>
          <li><b>الاستراحة المجانية:</b> تجمع كل ضرائب اللاعبين وغرامات الرادار، ومن يقف عليها يفوز بالحصيلة كاملة!</li>
          <li><b>سجن القلعة:</b> يدخله اللاعب عند مربع ادخل السجن أو كروت الحظ أو رمي دبل 3 مرات متتالية.</li>
        </ul>
      `;
    } else {"""

assert target_rules_func in code, "target_rules_func not found"
code = code.replace(target_rules_func, replacement_rules_func, 1)

# Also update the English/multilingual branch of updateRulesModalContent
target_rules_en_part = """        <h3 style="color: #38bdf8; margin-bottom: 6px;">🎲 Classic Board Rules:</h3>
        <ul style="padding-left: 20px; margin-bottom: 14px;">
          <li><b>GO (Start):</b> Collect 200 ${getCurrency()} as you pass or land.</li>
          <li><b>Free Parking Pot:</b> Collects all tax penalties. Land here to claim the entire accumulated fortune!</li>
          <li><b>Citadel Jail:</b> Sent to jail by landing on 'Go to Jail', drawing a jail card, or rolling doubles 3 times.</li>
        </ul>
      `;
    }
  }"""

replacement_rules_en_part = """        <div style="background: rgba(245, 158, 11, 0.1); border: 1px solid #b45309; border-radius: 12px; padding: 12px; margin-top: 14px; margin-bottom: 14px;">
          <h3 style="color: #fbbf24; margin: 0 0 8px 0; font-size: 14.5px;">🃏 Board Cards & Taxes Guide (Read-Only):</h3>
          <div style="display: flex; flex-direction: column; gap: 8px; font-size: 12.5px;">
            <div style="background: rgba(0,0,0,0.35); padding: 8px 10px; border-radius: 8px; border-left: 3px solid #3b82f6;">
              <b style="color: #60a5fa;">🎁 Community Chest:</b> Cash rewards, revenue bonuses, or a ticket to the Risk & Fortune Wheel.
            </div>
            <div style="background: rgba(0,0,0,0.35); padding: 8px 10px; border-radius: 8px; border-left: 3px solid #ec4899;">
              <b style="color: #f472b6;">❓ Chance Cards:</b> Direct impacts: Bank Heists, Shutdown hits, shield recharges, or immediate jail orders.
            </div>
            <div style="background: rgba(0,0,0,0.35); padding: 8px 10px; border-radius: 8px; border-left: 3px solid #ef4444;">
              <b style="color: #f87171;">💸 Income Tax (200):</b> Landing on Tile 4 incurs a 200 tax paid directly into the Free Parking Pot.
            </div>
            <div style="background: rgba(0,0,0,0.35); padding: 8px 10px; border-radius: 8px; border-left: 3px solid #a855f7;">
              <b style="color: #c084fc;">💎 Luxury Tax (100):</b> Landing on Tile 38 incurs a 100 fee deposited into Free Parking.
            </div>
            <div style="background: rgba(0,0,0,0.35); padding: 8px 10px; border-radius: 8px; border-left: 3px solid #e11d48;">
              <b style="color: #fb7185;">⛓️ Citadel Jail:</b> Sent directly to prison without passing GO. Roll doubles or pay 50 bail after 3 turns.
            </div>
            <div style="background: rgba(0,0,0,0.35); padding: 8px 10px; border-radius: 8px; border-left: 3px solid #10b981;">
              <b style="color: #34d399;">👮 Just Visiting:</b> Regular landing on Tile 10 is an innocent visit with no penalty or fine.
            </div>
          </div>
        </div>

        <h3 style="color: #38bdf8; margin-bottom: 6px;">🎲 Classic Board Rules:</h3>
        <ul style="padding-left: 20px; margin-bottom: 14px;">
          <li><b>GO (Start):</b> Collect 200 ${getCurrency()} as you pass or land.</li>
          <li><b>Free Parking Pot:</b> Collects all tax penalties. Land here to claim the entire accumulated fortune!</li>
          <li><b>Citadel Jail:</b> Sent to jail by landing on 'Go to Jail', drawing a jail card, or rolling doubles 3 times.</li>
        </ul>
      `;
    }
  }"""

assert target_rules_en_part in code, "target_rules_en_part not found"
code = code.replace(target_rules_en_part, replacement_rules_en_part, 1)

# 6. Add Token Picker JS functions and AVAILABLE_TOKENS definition
target_token_anchor = """  // Game Animation Speed Settings
  const gameSettings = {"""

token_picker_js = """  // Available 3D Board Tokens
  const AVAILABLE_TOKENS = [
    { id: 'fig_mr_hazz', nameAr: 'مستر حظ 🎩', nameEn: 'Mr. Hazz 🎩', avatar: '🎩' },
    { id: 'fig_cleopatra', nameAr: 'كليوباترا 👑', nameEn: 'Cleopatra 👑', avatar: '👑' },
    { id: 'token_tarboosh', nameAr: 'الطربوش الأصيل 🔴', nameEn: 'Tarboosh 🔴', avatar: '🔴' },
    { id: 'token_pharaoh', nameAr: 'القناع الفرعوني 🏺', nameEn: 'Pharaoh 🏺', avatar: '🏺' },
    { id: 'token_bastet', nameAr: 'تمثال باستيت 🐈', nameEn: 'Bastet Cat 🐈', avatar: '🐈' },
    { id: 'token_roadster', nameAr: 'سيارة رودستر 🏎️', nameEn: 'Roadster 🏎️', avatar: '🏎️' },
    { id: 'token_rocket', nameAr: 'الصاروخ الفضائي 🚀', nameEn: 'Rocket 🚀', avatar: '🚀' },
    { id: 'token_diamond', nameAr: 'الجوهرة الماسية 💎', nameEn: 'Diamond 💎', avatar: '💎' }
  ];

  function renderTokenPickerGrid() {
    const grid = document.getElementById('tokenPickerGrid');
    if (!grid) return;
    grid.innerHTML = '';

    let currentTokenId = 'fig_mr_hazz';
    try {
      currentTokenId = localStorage.getItem('bank_el_hazz_p1_token') || 'fig_mr_hazz';
    } catch (e) {}

    AVAILABLE_TOKENS.forEach(tok => {
      const card = document.createElement('div');
      card.className = `token-card ${tok.id === currentTokenId ? 'active' : ''}`;
      card.dataset.tokenId = tok.id;
      const svgArt = SVG_ASSETS[tok.id] || tok.avatar;
      const title = currentLanguage === 'ar' ? tok.nameAr : tok.nameEn;

      card.innerHTML = `
        <div class="token-preview-box">${svgArt}</div>
        <div class="token-title-label">${title}</div>
      `;

      card.addEventListener('click', () => {
        selectPlayerToken(tok.id);
      });

      grid.appendChild(card);
    });
  }

  function selectPlayerToken(tokenId) {
    const tokenDef = AVAILABLE_TOKENS.find(t => t.id === tokenId);
    if (!tokenDef || !SVG_ASSETS[tokenId]) return;

    if (state.players && state.players[0]) {
      state.players[0].tokenSvg = SVG_ASSETS[tokenId];
      state.players[0].avatar = tokenDef.avatar;

      // Update avatar in clash bar
      const p1Box = document.getElementById('avatarP1Box');
      if (p1Box) p1Box.innerHTML = SVG_ASSETS[tokenId];

      // Update turn avatar if P1 turn
      const turnSpan = document.getElementById('turnAvatarSpan');
      if (turnSpan && state.currentPlayerIdx === 0) turnSpan.innerText = tokenDef.avatar;

      // Update token on board
      const tokenOnBoard = document.getElementById(`player-token-${state.players[0].id}`);
      if (tokenOnBoard) tokenOnBoard.innerHTML = SVG_ASSETS[tokenId];
    }

    try {
      localStorage.setItem('bank_el_hazz_p1_token', tokenId);
    } catch (e) {}

    // Update active highlight in picker
    document.querySelectorAll('.token-card').forEach(c => {
      c.classList.toggle('active', c.dataset.tokenId === tokenId);
    });

    sfx.playFanfare();
    const tokenName = currentLanguage === 'ar' ? tokenDef.nameAr : tokenDef.nameEn;
    showFloatingFX(`✅ ${tokenName}`, true);
  }

  // Game Animation Speed Settings
  const gameSettings = {"""

assert target_token_anchor in code, "target_token_anchor not found"
code = code.replace(target_token_anchor, token_picker_js, 1)

# 7. Update initGame to apply saved token
target_init_avatar = """    // Load Player Avatars in Duel Bar
    document.getElementById('avatarP1Box').innerHTML = SVG_ASSETS.fig_mr_hazz;
    document.getElementById('avatarP2Box').innerHTML = SVG_ASSETS.fig_cleopatra;"""

replacement_init_avatar = """    // Apply saved Player 1 token if present
    let savedP1Token = 'fig_mr_hazz';
    try {
      savedP1Token = localStorage.getItem('bank_el_hazz_p1_token') || 'fig_mr_hazz';
    } catch (e) {}
    const p1TokDef = AVAILABLE_TOKENS.find(t => t.id === savedP1Token) || AVAILABLE_TOKENS[0];
    if (state.players[0] && SVG_ASSETS[p1TokDef.id]) {
      state.players[0].tokenSvg = SVG_ASSETS[p1TokDef.id];
      state.players[0].avatar = p1TokDef.avatar;
    }

    // Load Player Avatars in Duel Bar
    document.getElementById('avatarP1Box').innerHTML = state.players[0].tokenSvg || SVG_ASSETS.fig_mr_hazz;
    document.getElementById('avatarP2Box').innerHTML = SVG_ASSETS.fig_cleopatra;"""

assert target_init_avatar in code, "target_init_avatar not found"
code = code.replace(target_init_avatar, replacement_init_avatar, 1)

# 8. Update setGameLanguage for About Us and Token Picker
target_setlang_end = """    const btnSpinEl = document.getElementById('btnSpinWheelText');
    if (btnSpinEl) btnSpinEl.innerText = t('btnSpinWheelText');"""

replacement_setlang_end = """    const btnSpinEl = document.getElementById('btnSpinWheelText');
    if (btnSpinEl) btnSpinEl.innerText = t('btnSpinWheelText');

    const btnAboutUs = document.getElementById('btnAboutUsText');
    if (btnAboutUs) btnAboutUs.innerText = t('btnAboutUs');

    const btnTokPick = document.getElementById('btnTokenPickerText');
    if (btnTokPick) btnTokPick.innerText = t('btnTokenPicker');

    const aboutUsModalTitle = document.getElementById('aboutUsModalTitle');
    if (aboutUsModalTitle) aboutUsModalTitle.innerText = t('aboutUsModalTitle');

    const tokPickModalTitle = document.getElementById('tokenPickerModalTitle');
    if (tokPickModalTitle) tokPickModalTitle.innerText = t('tokenPickerModalTitle');"""

assert target_setlang_end in code, "target_setlang_end not found"
code = code.replace(target_setlang_end, replacement_setlang_end, 1)

# 9. Add event listeners for About Us and Token Picker in DOMContentLoaded
target_dom_listeners = """    const btnOpenSettings = document.getElementById('btnOpenSettings');"""

replacement_dom_listeners = """    const btnOpenAboutUs = document.getElementById('btnOpenAboutUs');
    if (btnOpenAboutUs) {
      btnOpenAboutUs.addEventListener('click', () => {
        openModal('modalAboutUs');
      });
    }

    const btnOpenTokenPicker = document.getElementById('btnOpenTokenPicker');
    if (btnOpenTokenPicker) {
      btnOpenTokenPicker.addEventListener('click', () => {
        renderTokenPickerGrid();
        openModal('modalTokenPicker');
      });
    }

    const btnOpenSettings = document.getElementById('btnOpenSettings');"""

assert target_dom_listeners in code, "target_dom_listeners not found"
code = code.replace(target_dom_listeners, replacement_dom_listeners, 1)

with open("build_matte_full_game.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Patch for all 3 user requests applied successfully!")
