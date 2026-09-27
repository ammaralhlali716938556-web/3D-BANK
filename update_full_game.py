import json
import os
from board_data import TILES, CHANCE_CARDS, CHEST_CARDS, LANDMARKS, CHARACTERS, WHEEL_ITEMS
from styles import STYLES_CSS
from sound_engine import SOUND_JS

print("Reading enriched SVG assets...")
with open("svg_assets.json", "r", encoding="utf-8") as f:
    svg_assets = json.load(f)

# Serialize data
tiles_json = json.dumps(TILES, ensure_ascii=False)
chance_json = json.dumps(CHANCE_CARDS, ensure_ascii=False)
chest_json = json.dumps(CHEST_CARDS, ensure_ascii=False)
landmarks_json = json.dumps(LANDMARKS, ensure_ascii=False)
characters_json = json.dumps(CHARACTERS, ensure_ascii=False)
wheel_json = json.dumps(WHEEL_ITEMS, ensure_ascii=False)
svg_assets_json = json.dumps(svg_assets, ensure_ascii=False)

# Enhanced 3D tile styles to append
ENHANCED_CSS = """
/* 3D Tile Bevels & Depth */
.tile {
  background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.18) !important;
  border-radius: 10px !important;
  box-shadow: 0 4px 0 #020617, 0 8px 12px rgba(0, 0, 0, 0.6) !important;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 4px 2px !important;
  transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
  cursor: pointer;
  overflow: visible !important;
}

.tile:hover {
  transform: translateY(-5px) scale(1.05) !important;
  box-shadow: 0 8px 0 #020617, 0 16px 24px rgba(0, 0, 0, 0.7) !important;
  border-color: #fbbf24 !important;
  z-index: 25 !important;
}

.tile-corner {
  background: radial-gradient(circle at 50% 30%, #1e293b 0%, #0b1021 100%) !important;
  border: 2px solid #64748b !important;
  box-shadow: 0 6px 0 #020617, 0 10px 16px rgba(0, 0, 0, 0.7) !important;
}

.tile-corner:hover {
  border-color: #f59e0b !important;
}

/* 3D Vector Art Container on Tiles */
.tile-3d-art {
  width: 90%;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 1px 0;
  filter: drop-shadow(0 3px 5px rgba(0, 0, 0, 0.5));
  transition: transform 0.2s ease;
}

.tile-3d-art svg {
  width: 100%;
  height: 100%;
  max-height: 44px;
  object-fit: contain;
}

.tile:hover .tile-3d-art {
  transform: scale(1.15) translateY(-2px);
}

.tile-corner .tile-3d-art {
  height: 52px;
}

.tile-corner .tile-3d-art svg {
  max-height: 52px;
}

/* 3D Houses & Hotels on Tiles */
.tile-buildings-3d {
  position: absolute;
  top: 10px;
  right: 2px;
  display: flex;
  gap: 1px;
  z-index: 10;
  filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.6));
}

.mini-house-3d {
  width: 16px;
  height: 16px;
  animation: pop-bounce 0.4s cubic-bezier(0.2, 0.8, 0.2, 1.2);
}

.mini-hotel-3d {
  width: 22px;
  height: 22px;
  animation: pop-bounce 0.5s cubic-bezier(0.2, 0.8, 0.2, 1.2);
}

@keyframes pop-bounce {
  0% { transform: scale(0); opacity: 0; }
  60% { transform: scale(1.2); }
  100% { transform: scale(1); opacity: 1; }
}

/* 3D Figurine Player Tokens */
.board-token-3d {
  width: 28px;
  height: 28px;
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.7));
  transition: transform 0.2s;
  animation: token-hop 0.4s ease-out;
  cursor: pointer;
}

.board-token-3d svg {
  width: 100%;
  height: 100%;
}

@keyframes token-hop {
  0% { transform: translateY(-16px) scale(1.3); }
  60% { transform: translateY(2px) scale(0.95); }
  100% { transform: translateY(0) scale(1); }
}

/* Center Diorama Container */
.center-diorama-container {
  width: 100%;
  max-width: 380px;
  height: 120px;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(245, 158, 11, 0.4);
  margin-bottom: 6px;
  position: relative;
}

.center-diorama-container svg {
  width: 100%;
  height: 100%;
  display: block;
}
"""

full_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>بنك الحظ - مونوبولي جو | النسخة العربية ثلاثية الأبعاد الكرتونية الكاملة</title>
  <style>
{STYLES_CSS}
{ENHANCED_CSS}
  </style>
</head>
<body>

  <!-- Confetti Canvas -->
  <canvas id="confettiCanvas"></canvas>

  <!-- Top App Navigation Header -->
  <header class="app-header">
    <div class="brand-title">
      <div class="brand-logo-icon">🎲</div>
      <div class="brand-text">
        <h1>بنك الحظ <span class="brand-badge">MONOPOLY GO 3D</span></h1>
      </div>
    </div>

    <div class="header-actions">
      <button class="btn-3d gold" id="btnOpenLandmarks">
        <span>🏛️</span>
        <span>معالم المدينة</span>
      </button>
      <button class="btn-3d purple" id="btnOpenWheel">
        <span>🎡</span>
        <span>عجلة الحظ</span>
      </button>
      <button class="btn-3d" id="btnToggle3D">
        <span id="perspectiveIcon">📐</span>
        <span id="perspectiveLabel">منظور 3D</span>
      </button>
      <button class="btn-3d" id="btnOpenRules">
        <span>📜</span>
        <span>القواعد</span>
      </button>
      <button class="btn-3d btn-icon-only" id="btnToggleSound" title="كتم / تشغيل الصوت">
        <span id="soundIcon">🔊</span>
      </button>
      <button class="btn-3d red btn-icon-only" id="btnResetGame" title="لعبة جديدة">
        <span>🔄</span>
      </button>
    </div>
  </header>

  <!-- Players Dashboard Bar -->
  <section class="players-bar" id="playersBar">
    <!-- Populated dynamically -->
  </section>

  <!-- Main Game Viewport -->
  <main class="game-viewport">
    
    <!-- 3D Perspective Wrapper -->
    <div class="board-container">
      <div class="board-perspective-wrapper mode-3d" id="boardWrapper">
        <div class="board-grid" id="boardGrid">
          
          <!-- Board Center Stage with 3D Animated Cairo Skyline Diorama -->
          <div class="board-center">
            
            <div class="center-top-row">
              <div class="free-parking-pot" title="حصيلة وعاء الاستراحة المجانية">
                <span class="pot-icon">🏺</span>
                <div>
                  <div style="font-size: 9px; color: #94a3b8;">وعاء الاستراحة</div>
                  <div class="pot-amount" id="potAmountDisplay">200 ج.م</div>
                </div>
              </div>

              <div class="board-title-emblem">
                <div class="emblem-title">بنك الحظ</div>
                <div class="emblem-sub" id="boardCityLabel">القاهرة التاريخية • لوحة 1 🌟</div>
              </div>

              <div class="free-parking-pot" style="border-color: #38bdf8;">
                <span class="pot-icon">⚡</span>
                <div>
                  <div style="font-size: 9px; color: #94a3b8;">طاقة النرد</div>
                  <div class="pot-amount" style="color: #38bdf8;" id="rollsLeftDisplay">50</div>
                </div>
              </div>
            </div>

            <!-- 3D Cairo Skyline Animated Diorama -->
            <div class="center-diorama-container" id="centerDioramaBox">
              <!-- Loaded from SVG assets -->
            </div>

            <!-- 3D Rolling Dice Stage -->
            <div class="dice-arena" id="diceArena">
              <!-- 3D Die 1 -->
              <div class="dice-cube" id="die1">
                <div class="dice-face face-1"><div class="dice-pip" style="grid-area: 2/2;"></div></div>
                <div class="dice-face face-2"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-3"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 2/2;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-4"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-5"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 2/2;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-6"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 2/1;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 2/3;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
              </div>

              <!-- 3D Die 2 -->
              <div class="dice-cube" id="die2">
                <div class="dice-face face-1"><div class="dice-pip" style="grid-area: 2/2;"></div></div>
                <div class="dice-face face-2"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-3"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 2/2;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-4"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-5"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 2/2;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-6"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 2/1;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 2/3;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
              </div>
            </div>

            <!-- Controls and Roll Section -->
            <div class="center-controls-row">
              
              <!-- Multiplier Selector -->
              <div class="multiplier-bar">
                <span class="multiplier-label">المضاعف:</span>
                <button class="multiplier-pill active" data-mult="1">1X</button>
                <button class="multiplier-pill" data-mult="2">2X</button>
                <button class="multiplier-pill" data-mult="3">3X</button>
                <button class="multiplier-pill" data-mult="5">5X</button>
                <button class="multiplier-pill" data-mult="10">10X</button>
              </div>

              <!-- Main Roll Button -->
              <button class="btn-big-roll" id="btnRollDice">
                <span>🎲</span>
                <span>ارمي النرد!</span>
              </button>

              <!-- Turn Banner -->
              <div class="turn-status-banner" id="turnStatusBanner">
                <span id="turnAvatarSpan">🎩</span>
                <span id="turnStatusText">دور مستر حظ... اضغط لرمي النرد!</span>
              </div>

            </div>

          </div>
          <!-- End Board Center -->

        </div>
      </div>
    </div>

    <!-- Sidebar Activity Log -->
    <aside class="game-sidebar">
      <div class="sidebar-header">
        <div class="sidebar-title">
          <span>📜</span>
          <span>سجل أحداث اللعبة</span>
        </div>
        <button class="btn-3d" style="padding: 4px 8px; font-size: 11px;" id="btnClearLog">مسح</button>
      </div>
      <div class="sidebar-content" id="activityLog">
        <!-- Log items dynamically added -->
      </div>
    </aside>

  </main>

  <!-- MODAL 1: Property Deed Card Modal -->
  <div class="modal-overlay" id="modalDeed">
    <div class="modal-box">
      <div class="modal-header">
        <div class="modal-title">
          <span>🏠</span>
          <span>سند ملكية العقار</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalDeed')">✕</button>
      </div>
      <div class="modal-body" id="deedModalBody">
        <!-- Rendered dynamically -->
      </div>
      <div class="modal-footer" id="deedModalFooter">
        <!-- Action buttons -->
      </div>
    </div>
  </div>

  <!-- MODAL 2: Chance & Community Chest Card Modal -->
  <div class="modal-overlay" id="modalCard">
    <div class="modal-box" style="text-align: center;">
      <div class="modal-header">
        <div class="modal-title" id="cardModalCategory">
          <span>❓</span>
          <span>كارت الحظ</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalCard')">✕</button>
      </div>
      <div class="modal-body" style="align-items: center;">
        <div style="width: 100px; height: 100px; margin-bottom: 8px;" id="cardModal3DArt"></div>
        <h2 style="font-size: 20px; color: #fbbf24; margin-bottom: 8px;" id="cardModalTitle">عنوان الكارت</h2>
        <p style="font-size: 14px; color: #e2e8f0; line-height: 1.6;" id="cardModalDesc">وصف وتأثير الكارت على اللاعب...</p>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <button class="btn-3d gold" id="btnExecuteCardAction" style="padding: 10px 28px; font-size: 15px;">
          <span>تنفيذ الأمر</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 3: Bank Heist Mini-Game -->
  <div class="modal-overlay" id="modalHeist">
    <div class="modal-box" style="width: min(560px, 95vw);">
      <div class="modal-header">
        <div class="modal-title">
          <span>🏦</span>
          <span>السطو على البنك (Bank Heist)</span>
        </div>
      </div>
      <div class="modal-body heist-container">
        <p style="text-align: center; font-size: 13px; color: #cbd5e1;">
          افتح أبواب الخزائن الذهبية! أول 3 عناصر متطابقة تكشفها تحدد جائزتك الكبرى!
        </p>

        <!-- Match Tracker -->
        <div class="heist-match-tracker">
          <div class="match-item">
            <span style="font-size: 18px;">🪙 فضة</span>
            <div class="match-icons" id="trackerSilver">
              <div class="match-slot"></div><div class="match-slot"></div><div class="match-slot"></div>
            </div>
            <span style="font-size: 10px; color: #94a3b8;">سرقة صغيرة</span>
          </div>
          <div class="match-item">
            <span style="font-size: 18px;">💰 أكياس</span>
            <div class="match-icons" id="trackerCash">
              <div class="match-slot"></div><div class="match-slot"></div><div class="match-slot"></div>
            </div>
            <span style="font-size: 10px; color: #fbbf24;">سرقة كبيرة</span>
          </div>
          <div class="match-item">
            <span style="font-size: 18px;">💎 ماس</span>
            <div class="match-icons" id="trackerDiamond">
              <div class="match-slot"></div><div class="match-slot"></div><div class="match-slot"></div>
            </div>
            <span style="font-size: 10px; color: #38bdf8;">إفلاس البنك!</span>
          </div>
        </div>

        <!-- 12 Vault Doors Grid -->
        <div class="heist-vault-grid" id="heistVaultGrid">
          <!-- Populated in JS -->
        </div>

        <div id="heistResultBanner" style="font-size: 16px; font-weight: 900; color: #fbbf24; text-align: center; min-height: 24px;"></div>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <button class="btn-3d gold" id="btnCollectHeist" style="display: none; padding: 10px 24px;">
          <span>استلام الغنائم 💰</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 4: Landmark Shutdown Mini-Game -->
  <div class="modal-overlay" id="modalShutdown">
    <div class="modal-box">
      <div class="modal-header">
        <div class="modal-title">
          <span>🔨</span>
          <span>الهجوم والتعطيل (Shutdown)</span>
        </div>
      </div>
      <div class="modal-body shutdown-stage">
        <p style="text-align: center; font-size: 13px; color: #cbd5e1;" id="shutdownSubtext">
          استهدف أحد معالم الخصم بالمطرقة الكرتونية! هل يمتلك درعاً لصد الهجوم؟
        </p>

        <div class="target-landmark-box" id="targetLandmarkBox">
          <div class="target-crosshair"></div>
          <div class="target-landmark-icon" id="targetLandmarkIcon" style="width: 100px; height: 100px;"></div>
          <div style="font-size: 14px; font-weight: 800; margin-top: 8px; color: #fbbf24;" id="targetLandmarkName">
            برج القاهرة للخصم
          </div>
        </div>

        <div id="shutdownResultText" style="font-size: 16px; font-weight: 900; text-align: center; min-height: 30px;"></div>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <button class="btn-3d red" id="btnLaunchShutdown" style="padding: 10px 30px; font-size: 16px;">
          <span>💥 أطلق الهجوم!</span>
        </button>
        <button class="btn-3d gold" id="btnFinishShutdown" style="display: none; padding: 10px 24px;">
          <span>تم الاستيلاء على الجائزة</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 5: City Landmarks Construction -->
  <div class="modal-overlay" id="modalLandmarks">
    <div class="modal-box" style="width: min(600px, 95vw);">
      <div class="modal-header">
        <div class="modal-title">
          <span>🏛️</span>
          <span>معالم المدينة (ترقية وبناء اللوحة ثلاثية الأبعاد)</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalLandmarks')">✕</button>
      </div>
      <div class="modal-body">
        <div style="background: rgba(15,23,42,0.6); padding: 10px; border-radius: 12px; margin-bottom: 6px;">
          <div style="display: flex; justify-content: space-between; font-size: 13px; font-weight: 800; margin-bottom: 4px;">
            <span style="color: #fbbf24;">إتمام لوحة القاهرة التاريخية</span>
            <span id="boardProgressText">0 / 25 نجمة</span>
          </div>
          <div style="width: 100%; height: 8px; background: #334155; border-radius: 4px; overflow: hidden;">
            <div id="boardProgressBar" style="width: 0%; height: 100%; background: linear-gradient(90deg, #f59e0b, #10b981); transition: width 0.4s;"></div>
          </div>
        </div>

        <div class="landmarks-list" id="landmarksListContainer">
          <!-- Populated dynamically with rich 3D SVGs -->
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn-3d" onclick="closeModal('modalLandmarks')">إغلاق</button>
      </div>
    </div>
  </div>

  <!-- MODAL 6: Wheel of Fortune Modal -->
  <div class="modal-overlay" id="modalWheel">
    <div class="modal-box" style="width: min(420px, 94vw); text-align: center;">
      <div class="modal-header">
        <div class="modal-title">
          <span>🎡</span>
          <span>عجلة الحظ الدوارة</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalWheel')">✕</button>
      </div>
      <div class="modal-body wheel-container">
        <div style="position: relative; display: flex; justify-content: center; align-items: center;">
          <div class="wheel-pointer"></div>
          <canvas id="wheelCanvas" width="280" height="280" class="wheel-canvas"></canvas>
        </div>
        <div id="wheelResultDisplay" style="font-size: 16px; font-weight: 900; color: #fbbf24; min-height: 24px;">
          أدر العجلة لتفوز بنرد، كاش، أو سطو مجاني!
        </div>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <button class="btn-3d gold" id="btnSpinWheel" style="padding: 10px 32px; font-size: 16px;">
          <span>🌀 تدوير العجلة!</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 7: Complete Game Rules & Guide -->
  <div class="modal-overlay" id="modalRules">
    <div class="modal-box" style="width: min(640px, 95vw);">
      <div class="modal-header">
        <div class="modal-title">
          <span>📜</span>
          <span>دليل وقواعد بنك الحظ & مونوبولي جو</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalRules')">✕</button>
      </div>
      <div class="modal-body" style="font-size: 13px; line-height: 1.8; color: #e2e8f0;">
        
        <h3 style="color: #fbbf24; margin-bottom: 6px;">🎲 قواعد بنك الحظ الكلاسيكية الكاملة:</h3>
        <ul style="padding-right: 20px; margin-bottom: 14px;">
          <li><b>نقطة البداية (انطلق):</b> كلما مررت أو هبطت عليها تقبض 200 ج.م مضروبة في مضاعف النرد.</li>
          <li><b>شراء الأراضي والمدن:</b> عند الهبوط على مدينة غير مملوكة يمكنك شراؤها بالسعر المحدد في السند.</li>
          <li><b>الاحتكار والإيجارات:</b> امتلاكك لجميع عقارات المجموعة اللونية الواحدة يضاعف إيجار الأرض الأساسي ويفتح لك حق بناء المنازل ثلاثية الأبعاد (1 إلى 4 منازل) ثم فندق فاخر!</li>
          <li><b>محطات القطار (سكك حديد مصر):</b> رمسيس، سيدي جابر، الأقصر، أسوان. يتضاعف الإيجار كلما ملكت محطات أكثر (25، 50، 100، 200 ج.م).</li>
          <li><b>المرافق العامة (الكهرباء والمياه):</b> الإيجار يحسب حسب مجموع رمية النرد (4 أضعاف لمرفق واحد، و 10 أضعاف لكلا المرفقين).</li>
          <li><b>الاستراحة المجانية:</b> تجمع كل ضرائب اللاعبين وغرامات الرادار في وعاء الجائزة، ومن يقف عليها يفوز بالحصيلة كاملة!</li>
          <li><b>سجن القلعة:</b> تدخل السجن بالوقوف على مربع "ادخل السجن"، أو سحب كارت السجن، أو رمي نرد دبل 3 مرات متتالية. للخروج: ارمِ دبل، أو ادفع كفالة 50 ج.م، أو استخدم كارت الخروج المجاني.</li>
        </ul>

        <h3 style="color: #38bdf8; margin-bottom: 6px;">🌟 ميزات وحركات مونوبولي جو الخارقة:</h3>
        <ul style="padding-right: 20px; margin-bottom: 14px;">
          <li><b>مضاعف النرد (1X إلى 10X):</b> ضاعف طاقتك ورميتك لتضاعف كل ما تجنيه من إيجارات، جوائز كاش، وجوائز الألعاب المصغرة!</li>
          <li><b>بناء معالم المدينة:</b> طوّر معالم القاهرة الـ 5 (الأهرامات، برج القاهرة، القلعة، المنارة، والكرنك) بنماذج ثلاثية الأبعاد مجسمة لترفع ثروتك الصافية، وإكمال جميع المعالم ينقلك للوحة جديدة مع مكافآت ضخمة!</li>
          <li><b>السطو على البنك (Bank Heist):</b> اقتحم الخزائن واختر الأبواب الآمنة لمطابقة 3 عناصر وسرقة أموال البنك والخصوم!</li>
          <li><b>الهجوم والتعطيل (Shutdown):</b> اضرب معالم منافسيك بالمطرقة الكرتونية لتعطيلها وربح أموال طائلة!</li>
          <li><b>نظام الدروع الحامية:</b> احمِ معالمك من ضربات الخصوم! يمتص الدرع الضربة ويتصدى للهجوم تلقائياً!</li>
        </ul>

      </div>
      <div class="modal-footer">
        <button class="btn-3d gold" onclick="closeModal('modalRules')">فهمت القواعد! هيا لنلعب</button>
      </div>
    </div>
  </div>

  <!-- JAVASCRIPT GAME LOGIC & SOUND ENGINE -->
  <script>
  // Injected Board Data & 3D SVGs
  const TILES = {tiles_json};
  const CHANCE_CARDS = {chance_json};
  const CHEST_CARDS = {chest_json};
  const LANDMARKS_DEF = {landmarks_json};
  const CHARACTERS_DEF = {characters_json};
  const WHEEL_ITEMS_DEF = {wheel_json};
  const SVG_ASSETS = {svg_assets_json};

  // Sound Engine
  {SOUND_JS}
  const sfx = new WebAudioSFX();

  // Core Game State
  const state = {{
    players: [],
    currentPlayerIdx: 0,
    multiplier: 1,
    freeParkingPot: 200,
    boardLevel: 1,
    cityName: 'القاهرة التاريخية',
    dice: [1, 1],
    doublesCount: 0,
    isRolling: false,
    tileOwnership: {{}}, // tileId -> {{ ownerId, houses: 0, mortgaged: false }}
    is3D: true,
    activeCard: null,
    heistState: null,
    shutdownState: null,
    wheelSpinning: false
  }};

  // Helper: Grid Position Formula for 11x11 Monopoly Board
  function getTileGridPos(tileId) {{
    if (tileId >= 0 && tileId <= 10) {{
      return {{ row: 11, col: 11 - tileId }};
    }} else if (tileId >= 11 && tileId <= 20) {{
      return {{ row: 11 - (tileId - 10), col: 1 }};
    }} else if (tileId >= 21 && tileId <= 30) {{
      return {{ row: 1, col: 1 + (tileId - 20) }};
    }} else {{
      return {{ row: 1 + (tileId - 30), col: 11 }};
    }}
  }}

  // 3D Model Mapper for Tiles
  function getTile3DArt(tile) {{
    if (tile.id === 0) return SVG_ASSETS.tile_go;
    if (tile.id === 1) return SVG_ASSETS.tile_oasis_villa;
    if (tile.id === 2 || tile.id === 17 || tile.id === 33) return SVG_ASSETS.tile_chest;
    if (tile.id === 3) return SVG_ASSETS.tile_lighthouse;
    if (tile.id === 4 || tile.id === 38) return SVG_ASSETS.tile_tax;
    if (tile.type === 'station') return SVG_ASSETS.tile_train;
    if (tile.id === 6 || tile.id === 8 || tile.id === 9) return SVG_ASSETS.tile_delta_townhouse;
    if (tile.id === 7 || tile.id === 22 || tile.id === 36) return SVG_ASSETS.tile_chance;
    if (tile.id === 10) return SVG_ASSETS.tile_jail;
    if (tile.id === 11 || tile.id === 13 || tile.id === 14) return SVG_ASSETS.tile_neoclassic_palace;
    if (tile.id === 12) return SVG_ASSETS.tile_electric;
    if (tile.id === 16 || tile.id === 18 || tile.id === 19) return SVG_ASSETS.tile_fayoum_waterwheel;
    if (tile.id === 20) return SVG_ASSETS.tile_parking;
    if (tile.id === 21 || tile.id === 23 || tile.id === 24) return SVG_ASSETS.tile_citadel;
    if (tile.id === 26 || tile.id === 27 || tile.id === 29) return SVG_ASSETS.tile_redsea_resort;
    if (tile.id === 28) return SVG_ASSETS.tile_water;
    if (tile.id === 30) return SVG_ASSETS.tile_gotojail;
    if (tile.id === 31 || tile.id === 32 || tile.id === 34) return SVG_ASSETS.tile_alex_palace;
    if (tile.id === 37) return SVG_ASSETS.tile_pyramid;
    if (tile.id === 39) return SVG_ASSETS.tile_cairo_tower;

    if (tile.group === 'brown') return SVG_ASSETS.tile_oasis_villa;
    if (tile.group === 'lightblue') return SVG_ASSETS.tile_delta_townhouse;
    if (tile.group === 'pink') return SVG_ASSETS.tile_neoclassic_palace;
    if (tile.group === 'orange') return SVG_ASSETS.tile_fayoum_waterwheel;
    if (tile.group === 'red') return SVG_ASSETS.tile_citadel;
    if (tile.group === 'yellow') return SVG_ASSETS.tile_redsea_resort;
    if (tile.group === 'green') return SVG_ASSETS.tile_alex_palace;
    if (tile.group === 'darkblue') return SVG_ASSETS.tile_cairo_tower;

    return SVG_ASSETS.tile_pyramid;
  }}

  // Player 3D Figurine Tokens
  const playerTokenArt = [
    SVG_ASSETS.token_tarboosh, // Player 0 (مستر حظ)
    SVG_ASSETS.token_pharaoh,  // Player 1 (كليوباترا كيد)
    SVG_ASSETS.token_bastet,   // Player 2 (العمدة فرفوش)
    SVG_ASSETS.token_roadster  // Player 3 (المكتشف الصغير)
  ];

  // Initialize Game
  function initGame() {{
    state.players = [
      {{
        id: 0,
        name: 'مستر حظ',
        title: 'الملياردير الطموح',
        avatar: '🎩',
        color: '#ef4444',
        isBot: false,
        money: 1500,
        position: 0,
        rolls: 50,
        shields: 3,
        inJail: false,
        jailTurns: 0,
        jailCards: 0,
        landmarks: {{ pyramids: 0, cairo_tower: 0, citadel: 0, alex_lighthouse: 0, luxor_temple: 0 }},
        netWorth: 1500,
        isBankrupt: false
      }},
      {{
        id: 1,
        name: 'كليوباترا كيد',
        title: 'أميرة الذهب',
        avatar: '👑',
        color: '#eab308',
        isBot: true,
        money: 1500,
        position: 0,
        rolls: 50,
        shields: 3,
        inJail: false,
        jailTurns: 0,
        jailCards: 0,
        landmarks: {{ pyramids: 0, cairo_tower: 0, citadel: 0, alex_lighthouse: 0, luxor_temple: 0 }},
        netWorth: 1500,
        isBankrupt: false
      }},
      {{
        id: 2,
        name: 'العمدة فرفوش',
        title: 'كبير الأعيان',
        avatar: '🧔',
        color: '#10b981',
        isBot: true,
        money: 1500,
        position: 0,
        rolls: 50,
        shields: 2,
        inJail: false,
        jailTurns: 0,
        jailCards: 0,
        landmarks: {{ pyramids: 0, cairo_tower: 0, citadel: 0, alex_lighthouse: 0, luxor_temple: 0 }},
        netWorth: 1500,
        isBankrupt: false
      }},
      {{
        id: 3,
        name: 'المكتشف الصغير',
        title: 'صياد الكنوز',
        avatar: '🧭',
        color: '#3b82f6',
        isBot: true,
        money: 1500,
        position: 0,
        rolls: 50,
        shields: 2,
        inJail: false,
        jailTurns: 0,
        jailCards: 0,
        landmarks: {{ pyramids: 0, cairo_tower: 0, citadel: 0, alex_lighthouse: 0, luxor_temple: 0 }},
        netWorth: 1500,
        isBankrupt: false
      }}
    ];

    state.currentPlayerIdx = 0;
    state.multiplier = 1;
    state.freeParkingPot = 200;
    state.boardLevel = 1;
    state.tileOwnership = {{}};

    // Load Center Diorama
    document.getElementById('centerDioramaBox').innerHTML = SVG_ASSETS.center_diorama;

    // Clear board and render
    renderBoardTiles();
    renderPlayersBar();
    updateUI();
    addLog('🎲 مرحباً بكم في لعبة بنك الحظ 3D - مونوبولي جو بنماذجها المعمارية ومجسماتها الكرتونية الفاخرة!', 'gold');
  }}

  // Render the 40 Tiles on CSS Grid with 3D Architectural SVGs
  function renderBoardTiles() {{
    const grid = document.getElementById('boardGrid');
    
    // Remove existing tile elements (keep .board-center)
    const oldTiles = grid.querySelectorAll('.tile');
    oldTiles.forEach(t => t.remove());

    TILES.forEach(tile => {{
      const pos = getTileGridPos(tile.id);
      const tileDiv = document.createElement('div');
      tileDiv.className = 'tile';
      tileDiv.id = `tile-${{tile.id}}`;
      tileDiv.style.gridRow = pos.row;
      tileDiv.style.gridColumn = pos.col;

      const art3D = getTile3DArt(tile);

      if ([0, 10, 20, 30].includes(tile.id)) {{
        tileDiv.classList.add('tile-corner');
        tileDiv.innerHTML = `
          <div class="corner-title">${{tile.name}}</div>
          <div class="tile-3d-art">${{art3D}}</div>
          <div class="corner-sub">${{tile.subtitle}}</div>
          <div class="player-tokens-container" id="tokens-${{tile.id}}"></div>
        `;
      }} else {{
        let bannerHtml = '';
        if (tile.type === 'property') {{
          bannerHtml = `<div class="color-bar" style="background: ${{tile.color}};"></div>`;
        }} else {{
          bannerHtml = `<div class="color-bar" style="background: rgba(255,255,255,0.15);"></div>`;
        }}

        tileDiv.innerHTML = `
          ${{bannerHtml}}
          <div class="tile-buildings-3d" id="buildings-${{tile.id}}"></div>
          <div class="tile-3d-art">${{art3D}}</div>
          <div class="tile-name">${{tile.name}}</div>
          ${{tile.price > 0 ? `<div class="tile-price">${{tile.price}} ج.م</div>` : `<div style="font-size:8px; color:#94a3b8;">${{tile.subtitle}}</div>`}}
          <div class="owner-indicator" id="owner-bar-${{tile.id}}"></div>
          <div class="player-tokens-container" id="tokens-${{tile.id}}"></div>
        `;
      }}

      // Click to open Deed Card
      tileDiv.addEventListener('click', () => {{
        openDeedModal(tile.id);
      }});

      grid.appendChild(tileDiv);
    }});

    renderTokens();
    updateTileOwnershipVisuals();
  }}

  // Update Player 3D Figurine Tokens on Tiles
  function renderTokens() {{
    TILES.forEach(t => {{
      const cont = document.getElementById(`tokens-${{t.id}}`);
      if (cont) cont.innerHTML = '';
    }});

    state.players.forEach((p, idx) => {{
      if (p.isBankrupt) return;
      const cont = document.getElementById(`tokens-${{p.position}}`);
      if (cont) {{
        const token = document.createElement('div');
        token.className = 'board-token-3d';
        token.innerHTML = playerTokenArt[idx] || playerTokenArt[0];
        token.title = `${{p.name}} (${{p.money}} ج.م)`;
        cont.appendChild(token);
      }}
    }});
  }}

  // Update Visual Indicators for Properties (3D Houses & Hotels)
  function updateTileOwnershipVisuals() {{
    TILES.forEach(t => {{
      const tileDiv = document.getElementById(`tile-${{t.id}}`);
      const buildingsCont = document.getElementById(`buildings-${{t.id}}`);
      const ownerBar = document.getElementById(`owner-bar-${{t.id}}`);
      if (!tileDiv) return;

      const record = state.tileOwnership[t.id];
      if (record && record.ownerId !== null) {{
        const owner = state.players[record.ownerId];
        tileDiv.classList.add('owned');
        tileDiv.style.setProperty('--owner-color', owner.color);
        if (ownerBar) ownerBar.style.background = owner.color;

        // Mortgaged?
        if (record.mortgaged) {{
          tileDiv.classList.add('mortgaged');
        }} else {{
          tileDiv.classList.remove('mortgaged');
        }}

        // 3D Houses / Hotel
        if (buildingsCont) {{
          buildingsCont.innerHTML = '';
          if (record.houses === 5) {{
            buildingsCont.innerHTML = `<div class="mini-hotel-3d">${{SVG_ASSETS.hotel_3d}}</div>`;
          }} else if (record.houses > 0) {{
            let hHtml = '';
            for (let i = 0; i < record.houses; i++) {{
              hHtml += `<div class="mini-house-3d">${{SVG_ASSETS.house_3d}}</div>`;
            }}
            buildingsCont.innerHTML = hHtml;
          }}
        }}
      }} else {{
        tileDiv.classList.remove('owned');
        tileDiv.classList.remove('mortgaged');
        if (ownerBar) ownerBar.style.background = 'transparent';
        if (buildingsCont) buildingsCont.innerHTML = '';
      }}
    }});
  }}

  // Update Top Players Dashboard Bar
  function renderPlayersBar() {{
    const bar = document.getElementById('playersBar');
    bar.innerHTML = '';

    state.players.forEach((p, idx) => {{
      const isTurn = idx === state.currentPlayerIdx;
      const card = document.createElement('div');
      card.className = `player-card ${{isTurn ? 'active-turn' : ''}} ${{p.isBankrupt ? 'bankrupt' : ''}}`;

      let shieldsHtml = '';
      for (let s = 0; s < 3; s++) {{
        shieldsHtml += `<span class="shield-icon ${{s < p.shields ? 'active' : ''}}">🛡️</span>`;
      }}

      card.innerHTML = `
        <div class="player-avatar-wrap">
          <div class="player-avatar" style="border-color: ${{p.color}}; padding: 4px;">${{playerTokenArt[idx]}}</div>
          ${{isTurn ? `<div class="turn-pulse-indicator"></div>` : ''}}
          ${{p.inJail ? `<div class="jail-badge">سجين ⛓️</div>` : ''}}
        </div>
        <div class="player-info-details">
          <div class="player-name-row">
            <span class="player-name-text">${{p.name}}</span>
            ${{p.isBot ? `<span class="player-bot-tag">ذكاء آلي</span>` : ''}}
          </div>
          <div class="player-money-val">${{p.money}} ج.م</div>
          <div class="player-net-worth">الثروة: ${{p.netWorth}} ج.م</div>
          <div class="player-shields">${{shieldsHtml}}</div>
        </div>
      `;
      bar.appendChild(card);
    }});
  }}

  // Update UI Stats and Labels
  function updateUI() {{
    const curr = state.players[state.currentPlayerIdx];
    document.getElementById('potAmountDisplay').innerText = `${{state.freeParkingPot}} ج.م`;
    document.getElementById('rollsLeftDisplay').innerText = curr.rolls;
    document.getElementById('turnAvatarSpan').innerText = curr.avatar;

    if (curr.isBot) {{
      document.getElementById('turnStatusText').innerText = `دور ${{curr.name}} (ذكاء آلي يفكر ويتصرف... 🤖)`;
      document.getElementById('btnRollDice').disabled = true;
    }} else {{
      document.getElementById('turnStatusText').innerText = `دورك يا ${{curr.name}}! اضغط "ارمي النرد!" للانطلاق 🎲`;
      document.getElementById('btnRollDice').disabled = state.isRolling;
    }}

    renderTokens();
    renderPlayersBar();
    updateTileOwnershipVisuals();
  }}

  // Activity Log
  function addLog(msg, colorClass = '') {{
    const logBox = document.getElementById('activityLog');
    const time = new Date().toLocaleTimeString('ar-EG', {{ hour: '2-digit', minute: '2-digit', second: '2-digit' }});
    const entry = document.createElement('div');
    entry.className = `log-entry ${{colorClass}}`;
    entry.innerHTML = `<div class="log-time">${{time}}</div><div>${{msg}}</div>`;
    logBox.insertBefore(entry, logBox.firstChild);
  }}

  // Floating Cash Visual FX (+200 / -100)
  function showFloatingFX(text, isPositive = true, targetTileId = null) {{
    const fx = document.createElement('div');
    fx.className = `floating-fx ${{isPositive ? 'plus' : 'minus'}}`;
    fx.innerText = text;

    let posX = window.innerWidth / 2;
    let posY = window.innerHeight / 2;

    if (targetTileId !== null) {{
      const tileElem = document.getElementById(`tile-${{targetTileId}}`);
      if (tileElem) {{
        const rect = tileElem.getBoundingClientRect();
        posX = rect.left + rect.width / 2;
        posY = rect.top + rect.height / 2;
      }}
    }}

    fx.style.left = `${{posX}}px`;
    fx.style.top = `${{posY}}px`;
    document.body.appendChild(fx);

    setTimeout(() => fx.remove(), 1500);
  }}

  // 3D Dice Rolling Physics & Face Transforms
  function rollDiceAction() {{
    if (state.isRolling) return;
    const player = state.players[state.currentPlayerIdx];
    if (player.isBankrupt) {{
      endTurn();
      return;
    }}

    // Check Rolls
    if (player.rolls < state.multiplier) {{
      player.rolls += 10;
      addLog(`⚡ تم منح ${{player.name}} حزمة طاقة نرد مجانية (+10 نرد)!`, 'gold');
    }}
    player.rolls = Math.max(0, player.rolls - state.multiplier);

    state.isRolling = true;
    document.getElementById('btnRollDice').disabled = true;

    // Play rolling sound
    sfx.playDiceRoll();

    const die1 = document.getElementById('die1');
    const die2 = document.getElementById('die2');
    die1.classList.add('rolling');
    die2.classList.add('rolling');

    const d1 = Math.floor(Math.random() * 6) + 1;
    const d2 = Math.floor(Math.random() * 6) + 1;
    state.dice = [d1, d2];

    setTimeout(() => {{
      die1.classList.remove('rolling');
      die2.classList.remove('rolling');

      // Set faces
      setDieTransform(die1, d1);
      setDieTransform(die2, d2);

      const isDoubles = d1 === d2;
      const totalSteps = d1 + d2;
      addLog(`🎲 رمى ${{player.name}} النرد: [${{d1}}] و [${{d2}}] = مجموع ${{totalSteps}}! ${{isDoubles ? '🔥 (دبل!)' : ''}}`, isDoubles ? 'gold' : '');

      // Check Jail
      if (player.inJail) {{
        if (isDoubles) {{
          player.inJail = false;
          player.jailTurns = 0;
          addLog(`🗝️ أطلق سراح ${{player.name}} من السجن بفضل رمية الدبل!`, 'green');
          sfx.playFanfare();
          movePlayerSteps(player, totalSteps);
        }} else {{
          player.jailTurns++;
          if (player.jailTurns >= 3) {{
            player.money = Math.max(0, player.money - 50);
            state.freeParkingPot += 50;
            player.inJail = false;
            player.jailTurns = 0;
            addLog(`💸 دفع ${{player.name}} كفالة 50 ج.م إجبارية بعد 3 جولات بالسجن وتم الإفراج عنه!`, 'red');
            movePlayerSteps(player, totalSteps);
          }} else {{
            addLog(`⛓️ ${{player.name}} لا يزال في السجن (المحاولة ${{player.jailTurns}} من 3).`, 'red');
            state.isRolling = false;
            endTurn();
          }}
        }}
        return;
      }}

      // Doubles tracker
      if (isDoubles) {{
        state.doublesCount++;
        if (state.doublesCount === 3) {{
          addLog(`🚨 رَمى ${{player.name}} الدبل 3 مرات متتالية! يُرسل فوراً إلى السجن لمخالفة السرعة!`, 'red');
          sendToJail(player);
          return;
        }}
      }} else {{
        state.doublesCount = 0;
      }}

      // Move player
      movePlayerSteps(player, totalSteps, isDoubles);

    }}, 1000);
  }}

  function setDieTransform(cubeElem, val) {{
    const transforms = {{
      1: 'rotateY(0deg) rotateX(0deg)',
      2: 'rotateY(90deg) rotateX(0deg)',
      3: 'rotateX(-90deg) rotateY(0deg)',
      4: 'rotateX(90deg) rotateY(0deg)',
      5: 'rotateY(-90deg) rotateX(0deg)',
      6: 'rotateY(180deg) rotateX(0deg)'
    }};
    cubeElem.style.transform = transforms[val];
  }}

  // Move Player Step by Step
  function movePlayerSteps(player, steps, isDoubles = false) {{
    let currentStep = 0;
    const interval = setInterval(() => {{
      currentStep++;
      player.position = (player.position + 1) % 40;
      
      // Passing GO (انطلق)
      if (player.position === 0) {{
        const goReward = 200 * state.multiplier;
        player.money += goReward;
        player.netWorth += goReward;
        sfx.playCoin();
        showFloatingFX(`+${{goReward}} ج.م`, true, 0);
        addLog(`🚀 مر ${{player.name}} بنقطة انطلق ونال جائزة ${{goReward}} ج.م!`, 'green');
      }}

      renderTokens();

      if (currentStep >= steps) {{
        clearInterval(interval);
        state.isRolling = false;
        handleTileArrival(player, isDoubles);
      }}
    }}, 140);
  }}

  // Handle Tile Arrival Actions
  function handleTileArrival(player, isDoubles) {{
    const tile = TILES[player.position];
    addLog(`📍 وصل ${{player.name}} إلى [${{tile.name}}] (${{tile.subtitle}})`);

    switch (tile.type) {{
      case 'go':
        const bonus = 200 * state.multiplier;
        player.money += bonus;
        player.netWorth += bonus;
        sfx.playCoin();
        showFloatingFX(`+${{bonus}} ج.م`, true, tile.id);
        finishArrivalAction(player, isDoubles);
        break;

      case 'property':
      case 'station':
      case 'utility':
        handlePropertyArrival(player, tile, isDoubles);
        break;

      case 'tax':
        const taxAmount = tile.price * state.multiplier;
        player.money = Math.max(0, player.money - taxAmount);
        state.freeParkingPot += taxAmount;
        sfx.playChaChing();
        showFloatingFX(`-${{taxAmount}} ج.م`, false, tile.id);
        addLog(`💸 دفع ${{player.name}} ضريبة قدرها ${{taxAmount}} ج.م وذهبت لوعاء الاستراحة!`, 'red');
        finishArrivalAction(player, isDoubles);
        break;

      case 'parking':
        const winPot = state.freeParkingPot;
        player.money += winPot;
        player.netWorth += winPot;
        state.freeParkingPot = 50;
        sfx.playFanfare();
        showFloatingFX(`+${{winPot}} ج.م`, true, tile.id);
        addLog(`🎉 هبط ${{player.name}} على الاستراحة المجانية وفاز بكامل وعاء الضرائب: ${{winPot}} ج.م!`, 'gold');
        finishArrivalAction(player, isDoubles);
        break;

      case 'chance':
        drawCard('chance', player, isDoubles);
        break;

      case 'chest':
        drawCard('chest', player, isDoubles);
        break;

      case 'gotojail':
        sendToJail(player);
        break;

      case 'jail':
        addLog(`👮 ${{player.name}} في زيارة بريئة لسجن القلعة.`);
        finishArrivalAction(player, isDoubles);
        break;

      default:
        finishArrivalAction(player, isDoubles);
    }}

    updateUI();
  }}

  // Handle Buying or Paying Rent on Properties
  function handlePropertyArrival(player, tile, isDoubles) {{
    const ownership = state.tileOwnership[tile.id];

    // Unowned property
    if (!ownership || ownership.ownerId === null) {{
      if (player.isBot) {{
        if (player.money >= tile.price + 150) {{
          buyPropertyDirect(player, tile);
        }} else {{
          addLog(`🤖 قرر ${{player.name}} توفير أمواله ولم يشترِ [${{tile.name}}].`);
        }}
        finishArrivalAction(player, isDoubles);
      }} else {{
        openDeedModal(tile.id, true, isDoubles);
      }}
      return;
    }}

    // Owned by someone else
    if (ownership.ownerId !== player.id) {{
      const owner = state.players[ownership.ownerId];
      if (ownership.mortgaged) {{
        addLog(`العقار [${{tile.name}}] مرهون، لم يتم دفع إيجار!`);
        finishArrivalAction(player, isDoubles);
        return;
      }}

      // Calculate rent
      let rent = 0;
      if (tile.type === 'station') {{
        const stationsOwned = countGroupOwned(ownership.ownerId, 'station');
        const stationRents = [25, 50, 100, 200];
        rent = (stationRents[stationsOwned - 1] || 25) * state.multiplier;
      }} else if (tile.type === 'utility') {{
        const utilsOwned = countGroupOwned(ownership.ownerId, 'utility');
        const factor = utilsOwned >= 2 ? 10 : 4;
        const diceSum = state.dice[0] + state.dice[1];
        rent = factor * diceSum * state.multiplier;
      }} else {{
        const hasFullSet = checkFullGroupOwned(ownership.ownerId, tile.group);
        if (ownership.houses === 0 && hasFullSet) {{
          rent = (tile.rent[0] * 2) * state.multiplier;
        }} else {{
          rent = (tile.rent[ownership.houses] || tile.rent[0]) * state.multiplier;
        }}
      }}

      // Pay rent
      const actualPaid = Math.min(player.money, rent);
      player.money -= actualPaid;
      owner.money += actualPaid;
      owner.netWorth += actualPaid;
      player.netWorth = Math.max(0, player.netWorth - actualPaid);

      sfx.playChaChing();
      showFloatingFX(`-${{actualPaid}} ج.م`, false, tile.id);
      showFloatingFX(`+${{actualPaid}} ج.م`, true, player.position);
      addLog(`🏠 دفع ${{player.name}} إيجاراً قدره ${{actualPaid}} ج.م للمالك ${{owner.name}} في [${{tile.name}}]!`, 'red');

      if (player.money <= 0) {{
        handleBankruptcy(player, owner);
      }}

      finishArrivalAction(player, isDoubles);
    }} else {{
      addLog(`✨ ${{player.name}} في ضيافة عقاره الخاص [${{tile.name}}].`);
      if (player.isBot && ownership.houses < 5 && player.money > tile.houseCost + 200) {{
        buildHouseDirect(ownership.ownerId, tile.id);
      }}
      finishArrivalAction(player, isDoubles);
    }}
  }}

  function countGroupOwned(ownerId, groupName) {{
    return TILES.filter(t => t.group === groupName && state.tileOwnership[t.id]?.ownerId === ownerId).length;
  }}

  function checkFullGroupOwned(ownerId, groupName) {{
    const allInGroup = TILES.filter(t => t.group === groupName);
    return allInGroup.length > 0 && allInGroup.every(t => state.tileOwnership[t.id]?.ownerId === ownerId);
  }}

  function buyPropertyDirect(player, tile) {{
    if (player.money < tile.price) return false;
    player.money -= tile.price;
    state.tileOwnership[tile.id] = {{ ownerId: player.id, houses: 0, mortgaged: false }};
    player.netWorth += tile.price;
    sfx.playChaChing();
    showFloatingFX(`-${{tile.price}} ج.م`, false, tile.id);
    addLog(`🎉 اشترى ${{player.name}} عقار [${{tile.name}}] مقابل ${{tile.price}} ج.م!`, 'green');
    updateTileOwnershipVisuals();
    updateUI();
    return true;
  }}

  function buildHouseDirect(ownerId, tileId) {{
    const tile = TILES[tileId];
    const player = state.players[ownerId];
    const rec = state.tileOwnership[tileId];
    if (!rec || rec.ownerId !== ownerId || rec.houses >= 5 || player.money < tile.houseCost) return false;

    player.money -= tile.houseCost;
    rec.houses++;
    player.netWorth += tile.houseCost;
    sfx.playChaChing();
    const typeLabel = rec.houses === 5 ? 'فندقاً فخماً مجسماً 🏨' : `منزلاً كرتونياً ثلاثي الأبعاد 🏡 (${{rec.houses}})`;
    addLog(`🏗️ بنى ${{player.name}} ${{typeLabel}} في [${{tile.name}}]!`, 'gold');
    updateTileOwnershipVisuals();
    updateUI();
    return true;
  }}

  // Send Player to Jail
  function sendToJail(player) {{
    player.position = 10;
    player.inJail = true;
    player.jailTurns = 0;
    state.doublesCount = 0;
    state.isRolling = false;
    sfx.playJail();
    addLog(`⛓️ دخل ${{player.name}} سجن القلعة! لا حراك حتى تفتديه أو ترمي دبل!`, 'red');
    renderTokens();
    updateUI();
    endTurn();
  }}

  // Draw Chance or Community Chest Card with 3D Illustration
  function drawCard(deckType, player, isDoubles) {{
    const deck = deckType === 'chance' ? CHANCE_CARDS : CHEST_CARDS;
    const card = deck[Math.floor(Math.random() * deck.length)];
    state.activeCard = {{ card, player, isDoubles }};

    sfx.playVaultOpen();

    document.getElementById('cardModalCategory').innerHTML = deckType === 'chance' ? '<span>❓</span> كارت الحظ' : '<span>🎁</span> صندوق الدنيا';
    document.getElementById('cardModal3DArt').innerHTML = deckType === 'chance' ? SVG_ASSETS.tile_chance : SVG_ASSETS.tile_chest;
    document.getElementById('cardModalTitle').innerText = card.title;
    document.getElementById('cardModalDesc').innerText = card.desc;

    openModal('modalCard');

    if (player.isBot) {{
      setTimeout(() => {{
        executeCardAction();
      }}, 1500);
    }}
  }}

  // Execute Active Card
  function executeCardAction() {{
    closeModal('modalCard');
    if (!state.activeCard) return;
    const {{ card, player, isDoubles }} = state.activeCard;
    state.activeCard = null;

    switch (card.action) {{
      case 'heist':
        startBankHeist(player);
        return;

      case 'shutdown':
        startShutdown(player);
        return;

      case 'wheel':
        openWheelModal();
        return;

      case 'cash':
        const cashWin = card.amount * state.multiplier;
        player.money += cashWin;
        player.netWorth += cashWin;
        sfx.playCoin();
        showFloatingFX(`+${{cashWin}} ج.م`, true, player.position);
        addLog(`💵 ${{player.name}} استلم ${{cashWin}} ج.م من الكارت!`, 'green');
        break;

      case 'pay_tax':
        const taxVal = card.amount * state.multiplier;
        player.money = Math.max(0, player.money - taxVal);
        state.freeParkingPot += taxVal;
        sfx.playChaChing();
        showFloatingFX(`-${{taxVal}} ج.م`, false, player.position);
        addLog(`💸 دفع ${{player.name}} ${{taxVal}} ج.م للوعاء العام!`, 'red');
        break;

      case 'shield':
        player.shields = Math.min(3, player.shields + 2);
        sfx.playShield();
        addLog(`🛡️ تم شحن دروع حماية ${{player.name}} بالكامل!`, 'gold');
        break;

      case 'jail_free':
        player.jailCards++;
        addLog(`🗝️ حصل ${{player.name}} على كارت خروج من السجن مجاني!`, 'gold');
        break;

      case 'jail':
        sendToJail(player);
        return;

      case 'move_to':
        player.position = card.target;
        addLog(`🚀 انتقل ${{player.name}} فوراً إلى [${{TILES[card.target].name}}]!`);
        renderTokens();
        handleTileArrival(player, false);
        return;

      case 'birthday':
        state.players.forEach(p => {{
          if (p.id !== player.id && !p.isBankrupt) {{
            const gift = Math.min(p.money, card.amount);
            p.money -= gift;
            player.money += gift;
          }}
        }});
        sfx.playCoin();
        addLog(`🎂 جمع ${{player.name}} هدايا عيد ميلاده من جميع اللاعبين!`, 'gold');
        break;

      default:
        break;
    }}

    finishArrivalAction(player, isDoubles);
  }}

  // Bank Heist Mini-Game
  function startBankHeist(attacker) {{
    const victim = state.players.find(p => p.id !== attacker.id && !p.isBankrupt) || state.players[0];
    state.heistState = {{
      attacker,
      victim,
      silverCount: 0,
      cashCount: 0,
      diamondCount: 0,
      completed: false,
      items: shuffleArray([
        'silver', 'silver', 'silver', 'silver', 'silver',
        'cash', 'cash', 'cash', 'cash',
        'diamond', 'diamond', 'diamond'
      ])
    }};

    const grid = document.getElementById('heistVaultGrid');
    grid.innerHTML = '';
    document.getElementById('heistResultBanner').innerText = '';
    document.getElementById('btnCollectHeist').style.display = 'none';

    resetTrackerSlots('trackerSilver');
    resetTrackerSlots('trackerCash');
    resetTrackerSlots('trackerDiamond');

    for (let i = 0; i < 12; i++) {{
      const door = document.createElement('div');
      door.className = 'vault-door';
      door.id = `vault-door-${{i}}`;
      door.innerHTML = '🔒';
      door.addEventListener('click', () => pickVaultDoor(i));
      grid.appendChild(door);
    }}

    openModal('modalHeist');

    if (attacker.isBot) {{
      botPlayHeist();
    }}
  }}

  function resetTrackerSlots(id) {{
    const cont = document.getElementById(id);
    const slots = cont.querySelectorAll('.match-slot');
    slots.forEach(s => s.classList.remove('filled'));
  }}

  function pickVaultDoor(idx) {{
    const h = state.heistState;
    if (!h || h.completed) return;
    const door = document.getElementById(`vault-door-${{idx}}`);
    if (door.classList.contains('opened')) return;

    door.classList.add('opened');
    sfx.playVaultOpen();

    const item = h.items[idx];
    if (item === 'silver') {{
      door.innerHTML = '🪙';
      h.silverCount++;
      fillTrackerSlot('trackerSilver', h.silverCount);
      if (h.silverCount === 3) finishHeist('silver');
    }} else if (item === 'cash') {{
      door.innerHTML = '💰';
      h.cashCount++;
      fillTrackerSlot('trackerCash', h.cashCount);
      if (h.cashCount === 3) finishHeist('cash');
    }} else if (item === 'diamond') {{
      door.innerHTML = '💎';
      h.diamondCount++;
      fillTrackerSlot('trackerDiamond', h.diamondCount);
      if (h.diamondCount === 3) finishHeist('diamond');
    }}
  }}

  function fillTrackerSlot(trackerId, count) {{
    const slots = document.getElementById(trackerId).querySelectorAll('.match-slot');
    if (slots[count - 1]) slots[count - 1].classList.add('filled');
  }}

  function finishHeist(type) {{
    const h = state.heistState;
    h.completed = true;

    let basePrize = 150;
    let label = 'سرقة فضية صغيرة 🪙';
    if (type === 'cash') {{
      basePrize = 350;
      label = 'سرقة أكياس نقدية كبرى! 💰';
    }} else if (type === 'diamond') {{
      basePrize = 800;
      label = '💎 إفلاس البنك الأسطوري (Mega Heist)!';
    }}

    const totalPrize = basePrize * state.multiplier;
    h.attacker.money += totalPrize;
    h.attacker.netWorth += totalPrize;

    sfx.playFanfare();
    launchConfetti();

    document.getElementById('heistResultBanner').innerText = `تهانينا! حققت ${{label}} وفزت بـ ${{totalPrize}} ج.م!`;
    const collectBtn = document.getElementById('btnCollectHeist');
    collectBtn.style.display = 'inline-flex';
    collectBtn.onclick = () => {{
      closeModal('modalHeist');
      addLog(`🏦 ${{h.attacker.name}} نفذ سطواً على البنك وحصل على ${{totalPrize}} ج.م!`, 'gold');
      finishArrivalAction(h.attacker, false);
    }};

    if (h.attacker.isBot) {{
      setTimeout(() => collectBtn.click(), 1200);
    }}
  }}

  function botPlayHeist() {{
    const interval = setInterval(() => {{
      const h = state.heistState;
      if (!h || h.completed) {{
        clearInterval(interval);
        return;
      }}
      const unopened = [];
      for (let i = 0; i < 12; i++) {{
        const door = document.getElementById(`vault-door-${{i}}`);
        if (door && !door.classList.contains('opened')) unopened.push(i);
      }}
      if (unopened.length === 0) {{
        clearInterval(interval);
        return;
      }}
      const randomIdx = unopened[Math.floor(Math.random() * unopened.length)];
      pickVaultDoor(randomIdx);
    }}, 600);
  }}

  // Landmark Shutdown Mini-Game with 3D Artwork
  function startShutdown(attacker) {{
    const victim = state.players.find(p => p.id !== attacker.id && !p.isBankrupt) || state.players[0];
    state.shutdownState = {{ attacker, victim }};

    document.getElementById('targetLandmarkIcon').innerHTML = SVG_ASSETS.tile_cairo_tower;
    document.getElementById('targetLandmarkName').innerText = `برج القاهرة الخاص بـ ${{victim.name}}`;
    document.getElementById('shutdownResultText').innerText = '';
    document.getElementById('btnLaunchShutdown').style.display = 'inline-flex';
    document.getElementById('btnFinishShutdown').style.display = 'none';

    const oldDome = document.querySelector('.shield-deflection-dome');
    if (oldDome) oldDome.remove();

    openModal('modalShutdown');

    if (attacker.isBot) {{
      setTimeout(() => {{
        executeShutdownHit();
      }}, 1000);
    }}
  }}

  function executeShutdownHit() {{
    const s = state.shutdownState;
    if (!s) return;

    document.getElementById('btnLaunchShutdown').style.display = 'none';
    const box = document.getElementById('targetLandmarkBox');

    if (s.victim.shields > 0) {{
      s.victim.shields--;
      sfx.playShield();

      const dome = document.createElement('div');
      dome.className = 'shield-deflection-dome';
      box.appendChild(dome);

      const consolation = 100 * state.multiplier;
      s.attacker.money += consolation;
      s.attacker.netWorth += consolation;

      document.getElementById('shutdownResultText').innerHTML = `
        <span style="color: #38bdf8;">🛡️ تم صد الهجوم بالدرع! خسر الخصم درعاً ونلت ترضية: ${{consolation}} ج.م</span>
      `;
      addLog(`🛡️ تصدى درع ${{s.victim.name}} لهجوم ${{s.attacker.name}}!`);
    }} else {{
      sfx.playSmash();
      box.style.animation = 'token-bounce 0.5s';

      const demolishPrize = 400 * state.multiplier;
      s.attacker.money += demolishPrize;
      s.attacker.netWorth += demolishPrize;

      document.getElementById('shutdownResultText').innerHTML = `
        <span style="color: #ef4444;">💥 ضربة مدمرة قاضية! تم تعطيل المعلم وربحت ${{demolishPrize}} ج.م!</span>
      `;
      addLog(`💥 ضرب ${{s.attacker.name}} معالم ${{s.victim.name}} بالمطرقة ونال ${{demolishPrize}} ج.م!`, 'red');
    }}

    const finishBtn = document.getElementById('btnFinishShutdown');
    finishBtn.style.display = 'inline-flex';
    finishBtn.onclick = () => {{
      closeModal('modalShutdown');
      finishArrivalAction(s.attacker, false);
    }};

    if (s.attacker.isBot) {{
      setTimeout(() => finishBtn.click(), 1200);
    }}
  }}

  // City Landmarks Construction View with 3D Architectural Models
  function openLandmarksModal() {{
    const curr = state.players[state.currentPlayerIdx];
    const container = document.getElementById('landmarksListContainer');
    container.innerHTML = '';

    let totalStars = 0;
    const landmarkSVGs = [
      SVG_ASSETS.tile_pyramid,
      SVG_ASSETS.tile_cairo_tower,
      SVG_ASSETS.tile_citadel,
      SVG_ASSETS.tile_lighthouse,
      SVG_ASSETS.tile_alex_palace
    ];

    LANDMARKS_DEF.forEach((lm, idx) => {{
      const stageIdx = curr.landmarks[lm.id] || 0;
      totalStars += stageIdx;
      const isMaxed = stageIdx >= 5;
      const nextStage = !isMaxed ? lm.stages[stageIdx] : null;

      let starsHtml = '';
      for (let s = 1; s <= 5; s++) {{
        starsHtml += `<span class="star-slot ${{s <= stageIdx ? 'filled' : ''}}">★</span>`;
      }}

      const card = document.createElement('div');
      card.className = 'landmark-builder-card';
      card.innerHTML = `
        <div class="landmark-icon-badge" style="width: 58px; height: 58px; padding: 4px;">
          ${{landmarkSVGs[idx]}}
        </div>
        <div class="landmark-meta">
          <div style="font-size: 14px; font-weight: 800; color: #f8fafc;">${{lm.name}}</div>
          <div style="font-size: 11px; color: #94a3b8;">${{isMaxed ? 'مكتمل بأعلى مستوى فخم!' : nextStage.name}}</div>
          <div class="landmark-stars-row">${{starsHtml}}</div>
        </div>
        <div>
          ${{isMaxed ? `
            <span style="font-size: 11px; color: #10b981; font-weight: 800;">مكتمل 👑</span>
          ` : `
            <button class="btn-3d gold" onclick="upgradeLandmark('${{lm.id}}')" ${{curr.money < nextStage.cost ? 'disabled' : ''}}>
              ترقية (${{nextStage.cost}} ج.م)
            </button>
          `}}
        </div>
      `;
      container.appendChild(card);
    }});

    const progressPct = Math.round((totalStars / 25) * 100);
    document.getElementById('boardProgressText').innerText = `${{totalStars}} / 25 نجمة (${{progressPct}}%)`;
    document.getElementById('boardProgressBar').style.width = `${{progressPct}}%`;

    openModal('modalLandmarks');
  }}

  function upgradeLandmark(landmarkId) {{
    const curr = state.players[state.currentPlayerIdx];
    const lm = LANDMARKS_DEF.find(l => l.id === landmarkId);
    const stageIdx = curr.landmarks[lm.id] || 0;
    if (stageIdx >= 5) return;

    const stage = lm.stages[stageIdx];
    if (curr.money < stage.cost) return;

    curr.money -= stage.cost;
    curr.landmarks[lm.id]++;
    curr.netWorth += stage.netWorth;

    sfx.playChaChing();
    addLog(`🏛️ طوّر ${{curr.name}} [${{lm.name}}] إلى المرحلة ${{curr.landmarks[lm.id]}} (+${{stage.netWorth}} ثروة)!`, 'gold');

    let totalStars = 0;
    LANDMARKS_DEF.forEach(l => {{ totalStars += curr.landmarks[l.id] || 0; }});

    if (totalStars === 25) {{
      state.boardLevel++;
      curr.rolls += 100;
      curr.money += 1500;
      curr.netWorth += 1500;
      sfx.playFanfare();
      launchConfetti();
      alert(`🎉 تهانينا الخالصة يا ${{curr.name}}! أتممت بناء لوحة القاهرة التاريخية بالكامل وفتحت اللوحة التالية بمكافأة 1500 ج.م و 100 نرد! 👑`);
      LANDMARKS_DEF.forEach(l => {{ curr.landmarks[l.id] = 0; }});
    }}

    openLandmarksModal();
    updateUI();
  }}

  // Wheel of Fortune Canvas & Spin
  function openWheelModal() {{
    drawWheel();
    openModal('modalWheel');
  }}

  function drawWheel() {{
    const canvas = document.getElementById('wheelCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const num = WHEEL_ITEMS_DEF.length;
    const arc = (2 * Math.PI) / num;
    const radius = canvas.width / 2;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    WHEEL_ITEMS_DEF.forEach((item, i) => {{
      const angle = i * arc;
      ctx.beginPath();
      ctx.fillStyle = item.color;
      ctx.moveTo(radius, radius);
      ctx.arc(radius, radius, radius - 4, angle, angle + arc);
      ctx.fill();
      ctx.stroke();

      ctx.save();
      ctx.translate(radius, radius);
      ctx.rotate(angle + arc / 2);
      ctx.textAlign = 'right';
      ctx.fillStyle = 'white';
      ctx.font = 'bold 13px Cairo, sans-serif';
      ctx.fillText(item.label, radius - 15, 5);
      ctx.restore();
    }});
  }}

  function spinWheelAction() {{
    if (state.wheelSpinning) return;
    state.wheelSpinning = true;
    document.getElementById('btnSpinWheel').disabled = true;

    const canvas = document.getElementById('wheelCanvas');
    const winningIdx = Math.floor(Math.random() * WHEEL_ITEMS_DEF.length);
    const num = WHEEL_ITEMS_DEF.length;
    const arcDeg = 360 / num;
    const targetDeg = (360 * 5) + (270 - (winningIdx * arcDeg + arcDeg / 2));

    canvas.style.transform = `rotate(${{targetDeg}}deg)`;

    let ticks = 0;
    const tickInterval = setInterval(() => {{
      sfx.playWheelTick();
      ticks++;
      if (ticks > 25) clearInterval(tickInterval);
    }}, 150);

    setTimeout(() => {{
      state.wheelSpinning = false;
      document.getElementById('btnSpinWheel').disabled = false;
      const prize = WHEEL_ITEMS_DEF[winningIdx];
      const player = state.players[state.currentPlayerIdx];

      sfx.playFanfare();
      document.getElementById('wheelResultDisplay').innerText = `مبروك! فزت بـ: ${{prize.label}}!`;

      if (prize.type === 'rolls') {{
        player.rolls += prize.amount;
      }} else if (prize.type === 'cash') {{
        player.money += prize.amount;
        player.netWorth += prize.amount;
      }} else if (prize.type === 'shield') {{
        player.shields = 3;
      }}

      addLog(`🎡 أدار ${{player.name}} عجلة الحظ وفاز بـ [${{prize.label}}]!`, 'gold');
      updateUI();
    }}, 4100);
  }}

  // Open Property Deed Modal with 3D Illustration
  function openDeedModal(tileId, showBuyOption = false, isDoubles = false) {{
    const tile = TILES[tileId];
    if (!tile) return;

    const body = document.getElementById('deedModalBody');
    const footer = document.getElementById('deedModalFooter');
    const rec = state.tileOwnership[tileId];
    const curr = state.players[state.currentPlayerIdx];

    let ownerName = 'شاغر للبيع (البنك)';
    let isOwner = false;
    if (rec && rec.ownerId !== null) {{
      ownerName = state.players[rec.ownerId].name;
      isOwner = rec.ownerId === curr.id;
    }}

    const art3D = getTile3DArt(tile);

    body.innerHTML = `
      <div class="deed-card">
        <div class="deed-header" style="background: ${{tile.color}};">
          <h2>${{tile.name}}</h2>
          <div style="font-size: 11px;">${{tile.subtitle}}</div>
        </div>
        <div style="width: 100%; height: 90px; display: flex; align-items: center; justify-content: center; background: #0f172a; padding: 6px;">
          <div style="width: 80px; height: 80px;">${{art3D}}</div>
        </div>
        <div class="deed-table">
          <div class="deed-row"><span>سعر الشراء:</span><span>${{tile.price}} ج.م</span></div>
          <div class="deed-row highlight"><span>المالك الحالي:</span><span>${{ownerName}}</span></div>
          ${{tile.rent ? `
            <div class="deed-row"><span>الإيجار الأساسي:</span><span>${{tile.rent[0]}} ج.م</span></div>
            <div class="deed-row"><span>مع منزل واحد:</span><span>${{tile.rent[1]}} ج.م</span></div>
            <div class="deed-row"><span>مع منزلين:</span><span>${{tile.rent[2]}} ج.م</span></div>
            <div class="deed-row"><span>مع 3 منازل:</span><span>${{tile.rent[3]}} ج.م</span></div>
            <div class="deed-row"><span>مع 4 منازل:</span><span>${{tile.rent[4]}} ج.م</span></div>
            <div class="deed-row"><span>مع فندق فاخر:</span><span>${{tile.rent[5]}} ج.م</span></div>
            <div class="deed-row"><span>تكلفة بناء المنزل:</span><span>${{tile.houseCost}} ج.م</span></div>
            <div class="deed-row"><span>قيمة الرهن:</span><span>${{tile.mortgage}} ج.م</span></div>
          ` : ''}}
        </div>
      </div>
    `;

    footer.innerHTML = '';

    if (showBuyOption && (!rec || rec.ownerId === null)) {{
      const buyBtn = document.createElement('button');
      buyBtn.className = 'btn-3d gold';
      buyBtn.innerHTML = `<span>شراء (${{tile.price}} ج.م)</span>`;
      buyBtn.onclick = () => {{
        buyPropertyDirect(curr, tile);
        closeModal('modalDeed');
        finishArrivalAction(curr, isDoubles);
      }};
      footer.appendChild(buyBtn);

      const declineBtn = document.createElement('button');
      declineBtn.className = 'btn-3d';
      declineBtn.innerHTML = `<span>تخطي</span>`;
      declineBtn.onclick = () => {{
        closeModal('modalDeed');
        finishArrivalAction(curr, isDoubles);
      }};
      footer.appendChild(declineBtn);
    }} else {{
      if (isOwner && tile.type === 'property') {{
        const buildBtn = document.createElement('button');
        buildBtn.className = 'btn-3d green';
        buildBtn.innerHTML = `<span>بناء منزل (${{tile.houseCost}} ج.م)</span>`;
        buildBtn.onclick = () => {{
          buildHouseDirect(curr.id, tileId);
          openDeedModal(tileId);
        }};
        footer.appendChild(buildBtn);
      }}

      const closeBtn = document.createElement('button');
      closeBtn.className = 'btn-3d';
      closeBtn.innerHTML = `<span>إغلاق</span>`;
      closeBtn.onclick = () => closeModal('modalDeed');
      footer.appendChild(closeBtn);
    }}

    openModal('modalDeed');
  }}

  // Bankruptcy Handling
  function handleBankruptcy(bankruptPlayer, creditor) {{
    bankruptPlayer.isBankrupt = true;
    sfx.playBuzzer();
    addLog(`☠️ أعلن ${{bankruptPlayer.name}} إفلاسه وخرج من اللعبة رسمياً!`, 'red');

    TILES.forEach(t => {{
      const rec = state.tileOwnership[t.id];
      if (rec && rec.ownerId === bankruptPlayer.id) {{
        rec.ownerId = creditor ? creditor.id : null;
      }}
    }});

    const activePlayers = state.players.filter(p => !p.isBankrupt);
    if (activePlayers.length === 1) {{
      const winner = activePlayers[0];
      sfx.playFanfare();
      launchConfetti();
      alert(`👑 مبروك الملياردير العظيم ${{winner.name}} هو الفائز بالعرش واللعبة بأكملها! 🏆`);
    }}
  }}

  // End Turn Cycle
  function finishArrivalAction(player, isDoubles) {{
    if (isDoubles && !player.inJail && !player.isBankrupt) {{
      addLog(`🎲 نرد دبل! يحصل ${{player.name}} على دور إضافي مجاني!`, 'gold');
      if (player.isBot) {{
        setTimeout(rollDiceAction, 1200);
      }} else {{
        state.isRolling = false;
        document.getElementById('btnRollDice').disabled = false;
      }}
    }} else {{
      setTimeout(endTurn, 1000);
    }}
  }}

  function endTurn() {{
    state.isRolling = false;
    do {{
      state.currentPlayerIdx = (state.currentPlayerIdx + 1) % state.players.length;
    }} while (state.players[state.currentPlayerIdx].isBankrupt);

    state.doublesCount = 0;
    updateUI();

    const curr = state.players[state.currentPlayerIdx];
    if (curr.isBot) {{
      setTimeout(() => {{
        rollDiceAction();
      }}, 1200);
    }}
  }}

  // Confetti Particle System
  function launchConfetti() {{
    const canvas = document.getElementById('confettiCanvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const particles = [];
    const colors = ['#f59e0b', '#ef4444', '#10b981', '#3b82f6', '#ec4899', '#8b5cf6'];

    for (let i = 0; i < 140; i++) {{
      particles.push({{
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height * 0.4,
        size: Math.random() * 8 + 4,
        color: colors[Math.floor(Math.random() * colors.length)],
        vx: (Math.random() - 0.5) * 6,
        vy: Math.random() * 4 + 3,
        rot: Math.random() * 360,
        vRot: (Math.random() - 0.5) * 10
      }});
    }}

    let frames = 0;
    function animate() {{
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach(p => {{
        p.x += p.vx;
        p.y += p.vy;
        p.rot += p.vRot;
        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rot * Math.PI) / 180);
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
        ctx.restore();
      }});

      frames++;
      if (frames < 140) {{
        requestAnimationFrame(animate);
      }} else {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }}
    }}
    animate();
  }}

  // Modal Helpers
  function openModal(id) {{
    document.getElementById(id).classList.add('active');
  }}

  function closeModal(id) {{
    document.getElementById(id).classList.remove('active');
  }}

  function shuffleArray(arr) {{
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {{
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }}
    return a;
  }}

  // Event Listeners Setup
  window.addEventListener('DOMContentLoaded', () => {{
    initGame();

    document.getElementById('btnRollDice').addEventListener('click', rollDiceAction);

    document.querySelectorAll('.multiplier-pill').forEach(btn => {{
      btn.addEventListener('click', (e) => {{
        document.querySelectorAll('.multiplier-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.multiplier = parseInt(btn.dataset.mult, 10);
        addLog(`⚡ تم تفعيل مضاعف النرد ${{state.multiplier}}X!`, 'gold');
      }});
    }});

    document.getElementById('btnToggle3D').addEventListener('click', () => {{
      state.is3D = !state.is3D;
      const wrap = document.getElementById('boardWrapper');
      const icon = document.getElementById('perspectiveIcon');
      const label = document.getElementById('perspectiveLabel');
      if (state.is3D) {{
        wrap.classList.add('mode-3d');
        icon.innerText = '📐';
        label.innerText = 'منظور 3D';
      }} else {{
        wrap.classList.remove('mode-3d');
        icon.innerText = '🗺️';
        label.innerText = 'منظور 2D';
      }}
    }});

    document.getElementById('btnToggleSound').addEventListener('click', () => {{
      const muted = sfx.toggleMute();
      document.getElementById('soundIcon').innerText = muted ? '🔇' : '🔊';
    }});

    document.getElementById('btnOpenLandmarks').addEventListener('click', openLandmarksModal);
    document.getElementById('btnOpenWheel').addEventListener('click', openWheelModal);
    document.getElementById('btnOpenRules').addEventListener('click', () => openModal('modalRules'));
    document.getElementById('btnResetGame').addEventListener('click', () => {{
      if (confirm('هل تريد بدء جولة لعب جديدة من البداية؟')) initGame();
    }});

    document.getElementById('btnLaunchShutdown').addEventListener('click', executeShutdownHit);
    document.getElementById('btnSpinWheel').addEventListener('click', spinWheelAction);
    document.getElementById('btnExecuteCardAction').addEventListener('click', executeCardAction);

    document.getElementById('btnClearLog').addEventListener('click', () => {{
      document.getElementById('activityLog').innerHTML = '';
    }});

    document.body.addEventListener('click', () => sfx.ensureContext(), {{ once: true }});
  }});
  </script>

</body>
</html>
"""

# Write to file
dest_path = "/bank_el_hazz/bank_el_hazz_monopoly_go.html"
with open(dest_path, "w", encoding="utf-8") as f:
    f.write(full_html)

# Also update index.html
with open("/bank_el_hazz/index.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Updated bank_el_hazz_monopoly_go.html successfully!")
print("New File size:", os.path.getsize(dest_path), "bytes")
