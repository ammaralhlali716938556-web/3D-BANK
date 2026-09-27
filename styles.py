STYLES_CSS = """
:root {
  --bg-main: #090d16;
  --bg-card: #131d31;
  --bg-board: #1e293b;
  --accent-gold: #f59e0b;
  --accent-gold-light: #fbbf24;
  --accent-blue: #38bdf8;
  --accent-purple: #a855f7;
  --accent-green: #10b981;
  --accent-red: #ef4444;
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --font-family: 'Cairo', 'Segoe UI', system-ui, -apple-system, sans-serif;
  --tile-radius: 8px;
  --shadow-3d: 0 10px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.5);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
}

body {
  background: radial-gradient(circle at 50% 20%, #1e1b4b 0%, #090d16 100%);
  color: var(--text-main);
  font-family: var(--font-family);
  direction: rtl;
  min-height: 100vh;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
}

/* App Header */
.app-header {
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(12px);
  border-bottom: 2px solid rgba(245, 158, 11, 0.3);
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 4px 20px rgba(0,0,0,0.4);
}

.brand-title {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-logo-icon {
  width: 44px;
  height: 44px;
  background: linear-gradient(135deg, #f59e0b, #d97706);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  box-shadow: 0 4px 10px rgba(245, 158, 11, 0.4), inset 0 2px 0 rgba(255,255,255,0.4);
  border: 2px solid #fef08a;
  animation: pulse-gold 2.5s infinite;
}

@keyframes pulse-gold {
  0%, 100% { transform: scale(1); filter: brightness(1); }
  50% { transform: scale(1.04); filter: brightness(1.15); box-shadow: 0 0 20px rgba(245, 158, 11, 0.8); }
}

.brand-text h1 {
  font-size: 22px;
  font-weight: 900;
  background: linear-gradient(to left, #fbbf24, #ffffff, #f59e0b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 2px 10px rgba(245, 158, 11, 0.3);
  letter-spacing: -0.5px;
  line-height: 1.2;
}

.brand-badge {
  font-size: 11px;
  font-weight: 700;
  background: linear-gradient(90deg, #ec4899, #8b5cf6);
  color: white;
  padding: 2px 8px;
  border-radius: 20px;
  display: inline-block;
  margin-right: 6px;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

/* Playful 3D Buttons */
.btn-3d {
  background: linear-gradient(180deg, #3b82f6, #1d4ed8);
  border: none;
  color: white;
  font-family: inherit;
  font-weight: 800;
  font-size: 13px;
  padding: 8px 14px;
  border-radius: 12px;
  cursor: pointer;
  position: relative;
  box-shadow: 0 4px 0 #1e3a8a, 0 6px 12px rgba(0,0,0,0.3);
  transition: all 0.1s ease;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.btn-3d:active {
  transform: translateY(3px);
  box-shadow: 0 1px 0 #1e3a8a, 0 2px 4px rgba(0,0,0,0.3);
}

.btn-3d.gold {
  background: linear-gradient(180deg, #fbbf24, #d97706);
  box-shadow: 0 4px 0 #b45309, 0 6px 12px rgba(0,0,0,0.3);
  color: #451a03;
}
.btn-3d.gold:active {
  box-shadow: 0 1px 0 #b45309;
}

.btn-3d.purple {
  background: linear-gradient(180deg, #a855f7, #7e22ce);
  box-shadow: 0 4px 0 #581c87, 0 6px 12px rgba(0,0,0,0.3);
}
.btn-3d.purple:active {
  box-shadow: 0 1px 0 #581c87;
}

.btn-3d.green {
  background: linear-gradient(180deg, #10b981, #047857);
  box-shadow: 0 4px 0 #064e3b, 0 6px 12px rgba(0,0,0,0.3);
}
.btn-3d.green:active {
  box-shadow: 0 1px 0 #064e3b;
}

.btn-3d.red {
  background: linear-gradient(180deg, #ef4444, #b91c1c);
  box-shadow: 0 4px 0 #7f1d1d, 0 6px 12px rgba(0,0,0,0.3);
}
.btn-3d.red:active {
  box-shadow: 0 1px 0 #7f1d1d;
}

.btn-icon-only {
  padding: 8px 10px;
  font-size: 16px;
}

/* Players Top Dashboard Bar */
.players-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 10px 16px;
  background: rgba(15, 23, 42, 0.6);
  overflow-x: auto;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.player-card {
  background: #1e293b;
  border: 2px solid #334155;
  border-radius: 14px;
  padding: 8px 14px;
  min-width: 170px;
  display: flex;
  align-items: center;
  gap: 10px;
  transition: all 0.3s ease;
  position: relative;
  box-shadow: 0 4px 10px rgba(0,0,0,0.25);
}

.player-card.active-turn {
  border-color: #fbbf24;
  background: linear-gradient(135deg, #1e293b, #2d3748);
  box-shadow: 0 0 18px rgba(251, 191, 36, 0.4), inset 0 0 10px rgba(251, 191, 36, 0.2);
  transform: translateY(-2px);
}

.player-card.bankrupt {
  opacity: 0.4;
  filter: grayscale(1);
}

.player-avatar-wrap {
  position: relative;
}

.player-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  border: 3px solid;
  background: #0f172a;
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}

.turn-pulse-indicator {
  position: absolute;
  top: -3px;
  right: -3px;
  width: 14px;
  height: 14px;
  background: #10b981;
  border: 2px solid white;
  border-radius: 50%;
  animation: pulse-green 1.5s infinite;
}

@keyframes pulse-green {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.3); opacity: 0.8; }
}

.player-info-details {
  display: flex;
  flex-direction: column;
}

.player-name-row {
  display: flex;
  align-items: center;
  gap: 6px;
}

.player-name-text {
  font-size: 13px;
  font-weight: 800;
  white-space: nowrap;
}

.player-bot-tag {
  font-size: 9px;
  background: rgba(148, 163, 184, 0.2);
  color: #94a3b8;
  padding: 1px 5px;
  border-radius: 6px;
}

.player-money-val {
  font-size: 14px;
  font-weight: 900;
  color: #fbbf24;
}

.player-net-worth {
  font-size: 10px;
  color: #94a3b8;
}

.player-shields {
  display: flex;
  gap: 3px;
  margin-top: 2px;
}

.shield-icon {
  font-size: 11px;
  opacity: 0.3;
  filter: grayscale(1);
  transition: all 0.2s;
}

.shield-icon.active {
  opacity: 1;
  filter: drop-shadow(0 0 4px #38bdf8);
}

.jail-badge {
  position: absolute;
  top: -8px;
  left: 8px;
  background: #ef4444;
  color: white;
  font-size: 9px;
  font-weight: 800;
  padding: 2px 6px;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.3);
}

/* Main Layout: Board + Sidebar Feed */
.game-viewport {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 16px;
  gap: 20px;
  max-width: 1480px;
  margin: 0 auto;
  width: 100%;
}

/* 3D Board Perspective Container */
.board-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
}

.board-perspective-wrapper {
  perspective: 1200px;
  transition: perspective 0.5s ease;
}

.board-grid {
  width: min(840px, 94vw);
  height: min(840px, 94vw);
  background: #0f172a;
  border: 4px solid #334155;
  border-radius: 20px;
  display: grid;
  grid-template-columns: 1.35fr repeat(9, 1fr) 1.35fr;
  grid-template-rows: 1.35fr repeat(9, 1fr) 1.35fr;
  gap: 3px;
  padding: 6px;
  position: relative;
  box-shadow: 0 20px 50px rgba(0,0,0,0.6), 0 0 0 2px rgba(255,255,255,0.05);
  transform-origin: center center;
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.6s ease;
}

.board-perspective-wrapper.mode-3d .board-grid {
  transform: rotateX(24deg) rotateZ(0deg) scale(0.95);
  box-shadow: 0 35px 70px rgba(0, 0, 0, 0.7), 0 10px 25px rgba(0, 0, 0, 0.4);
}

/* Board Tiles Styling */
.tile {
  background: #1e293b;
  border-radius: 6px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 3px;
  position: relative;
  cursor: pointer;
  transition: all 0.2s ease;
  overflow: hidden;
  text-align: center;
}

.tile:hover {
  filter: brightness(1.25);
  transform: scale(1.04);
  z-index: 10;
  box-shadow: 0 4px 12px rgba(0,0,0,0.5);
  border-color: #fbbf24;
}

/* Corners */
.tile-corner {
  background: linear-gradient(135deg, #1e293b, #0f172a);
  border: 2px solid #475569;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 6px;
}

.tile-corner .corner-icon {
  font-size: 26px;
  margin-bottom: 2px;
}

.tile-corner .corner-title {
  font-size: 11px;
  font-weight: 900;
  color: #fbbf24;
}

.tile-corner .corner-sub {
  font-size: 8px;
  color: #94a3b8;
}

/* Edge orientation color bars */
.color-bar {
  width: 100%;
  height: 12px;
  border-radius: 4px 4px 0 0;
  box-shadow: inset 0 -1px 2px rgba(0,0,0,0.3);
}

.tile-name {
  font-size: 9.5px;
  font-weight: 800;
  line-height: 1.15;
  color: #f8fafc;
  margin: 1px 0;
  max-width: 95%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.tile-icon {
  font-size: 14px;
}

.tile-price {
  font-size: 8.5px;
  font-weight: 900;
  color: #fbbf24;
  background: rgba(0,0,0,0.3);
  padding: 1px 4px;
  border-radius: 4px;
}

/* House & Hotel visual tags on tiles */
.tile-buildings {
  position: absolute;
  top: 13px;
  right: 2px;
  display: flex;
  gap: 1px;
  z-index: 2;
}

.mini-house {
  width: 8px;
  height: 8px;
  background: #10b981;
  border: 1px solid #064e3b;
  border-radius: 1px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.5);
}

.mini-hotel {
  background: #ef4444;
  color: white;
  font-size: 7px;
  font-weight: 900;
  padding: 0 2px;
  border-radius: 2px;
  border: 1px solid #7f1d1d;
  box-shadow: 0 0 4px #ef4444;
}

/* Owner stripe */
.tile.owned {
  box-shadow: inset 0 0 0 2px var(--owner-color);
}

.owner-indicator {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--owner-color, transparent);
}

.tile.mortgaged::after {
  content: 'مرهون';
  position: absolute;
  inset: 0;
  background: rgba(185, 28, 28, 0.7);
  backdrop-filter: blur(1px);
  color: white;
  font-size: 10px;
  font-weight: 900;
  display: flex;
  align-items: center;
  justify-content: center;
  transform: rotate(-15deg);
  z-index: 5;
}

/* Player Tokens Layer */
.player-tokens-container {
  position: absolute;
  bottom: 2px;
  display: flex;
  gap: 2px;
  justify-content: center;
  align-items: center;
  z-index: 8;
  max-width: 95%;
  flex-wrap: wrap;
}

.board-token {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 2px solid white;
  background: #0f172a;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.7);
  animation: token-bounce 0.4s ease-out;
}

@keyframes token-bounce {
  0% { transform: translateY(-12px) scale(1.3); }
  60% { transform: translateY(2px) scale(0.9); }
  100% { transform: translateY(0) scale(1); }
}

/* Center of the Board */
.board-center {
  grid-column: 2 / 11;
  grid-row: 2 / 11;
  background: radial-gradient(circle at center, #1e1b4b 0%, #0f172a 100%);
  border-radius: 14px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 16px;
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 0 40px rgba(0,0,0,0.5);
  border: 1px solid rgba(255,255,255,0.06);
}

.board-center::before {
  content: '';
  position: absolute;
  width: 250%;
  height: 250%;
  background: radial-gradient(circle, rgba(245, 158, 11, 0.06) 0%, transparent 60%);
  animation: rotate-center 30s linear infinite;
  pointer-events: none;
}

@keyframes rotate-center {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.center-top-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  z-index: 3;
}

.free-parking-pot {
  background: rgba(15, 23, 42, 0.8);
  border: 2px solid #6366f1;
  padding: 6px 14px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 0 14px rgba(99, 102, 241, 0.4);
}

.pot-icon {
  font-size: 20px;
  animation: pot-wobble 2s infinite ease-in-out;
}

@keyframes pot-wobble {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(-8deg); }
  75% { transform: rotate(8deg); }
}

.pot-amount {
  font-size: 14px;
  font-weight: 900;
  color: #fbbf24;
}

.board-title-emblem {
  text-align: center;
  z-index: 3;
}

.emblem-title {
  font-size: 32px;
  font-weight: 900;
  background: linear-gradient(180deg, #fef08a 0%, #f59e0b 50%, #b45309 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 4px 15px rgba(245, 158, 11, 0.4);
  letter-spacing: -1px;
}

.emblem-sub {
  font-size: 11px;
  font-weight: 700;
  color: #94a3b8;
  letter-spacing: 2px;
}

/* 3D Rolling Dice Arena */
.dice-arena {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 28px;
  margin: 10px 0;
  z-index: 3;
  perspective: 600px;
  min-height: 80px;
}

.dice-cube {
  width: 54px;
  height: 54px;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 1s cubic-bezier(0.2, 0.9, 0.3, 1.2);
}

.dice-cube.rolling {
  animation: dice-tumble 1s linear infinite;
}

@keyframes dice-tumble {
  0% { transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg); }
  25% { transform: rotateX(180deg) rotateY(90deg) rotateZ(45deg); }
  50% { transform: rotateX(360deg) rotateY(180deg) rotateZ(180deg); }
  75% { transform: rotateX(540deg) rotateY(270deg) rotateZ(270deg); }
  100% { transform: rotateX(720deg) rotateY(360deg) rotateZ(360deg); }
}

.dice-face {
  position: absolute;
  width: 54px;
  height: 54px;
  background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
  border: 2px solid #cbd5e1;
  border-radius: 12px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  padding: 6px;
  box-shadow: inset 0 0 6px rgba(0,0,0,0.15);
}

.dice-pip {
  width: 9px;
  height: 9px;
  background: #ef4444;
  border-radius: 50%;
  box-shadow: inset 0 1px 2px rgba(0,0,0,0.4);
  place-self: center;
}

.dice-cube:last-child .dice-pip {
  background: #3b82f6;
}

.face-1 { transform: rotateY(0deg) translateZ(27px); }
.face-2 { transform: rotateY(-90deg) translateZ(27px); }
.face-3 { transform: rotateX(90deg) translateZ(27px); }
.face-4 { transform: rotateX(-90deg) translateZ(27px); }
.face-5 { transform: rotateY(90deg) translateZ(27px); }
.face-6 { transform: rotateY(180deg) translateZ(27px); }

/* Dice Multiplier & Big Roll Button */
.center-controls-row {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  width: 100%;
  z-index: 3;
}

.multiplier-bar {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(15, 23, 42, 0.8);
  padding: 4px 8px;
  border-radius: 20px;
  border: 1px solid rgba(255,255,255,0.1);
}

.multiplier-label {
  font-size: 11px;
  font-weight: 800;
  color: #fbbf24;
  margin-left: 4px;
}

.multiplier-pill {
  background: transparent;
  border: none;
  color: #94a3b8;
  font-family: inherit;
  font-size: 12px;
  font-weight: 900;
  padding: 4px 10px;
  border-radius: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.multiplier-pill.active {
  background: linear-gradient(135deg, #f59e0b, #d97706);
  color: #ffffff;
  box-shadow: 0 0 10px rgba(245, 158, 11, 0.6);
}

.btn-big-roll {
  background: linear-gradient(180deg, #fbbf24 0%, #f59e0b 50%, #d97706 100%);
  border: none;
  color: #451a03;
  font-family: inherit;
  font-size: 20px;
  font-weight: 900;
  padding: 12px 36px;
  border-radius: 18px;
  cursor: pointer;
  box-shadow: 0 6px 0 #b45309, 0 12px 25px rgba(245, 158, 11, 0.5);
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 10px;
  position: relative;
  overflow: hidden;
}

.btn-big-roll::after {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(60deg, transparent 40%, rgba(255,255,255,0.4) 50%, transparent 60%);
  animation: shine-sweep 3s infinite;
}

@keyframes shine-sweep {
  0% { transform: translateX(-100%); }
  20%, 100% { transform: translateX(100%); }
}

.btn-big-roll:hover {
  filter: brightness(1.1);
  transform: translateY(-2px);
  box-shadow: 0 8px 0 #b45309, 0 16px 30px rgba(245, 158, 11, 0.6);
}

.btn-big-roll:active {
  transform: translateY(4px);
  box-shadow: 0 2px 0 #b45309, 0 4px 10px rgba(245, 158, 11, 0.4);
}

.btn-big-roll:disabled {
  filter: grayscale(0.8);
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
  box-shadow: 0 4px 0 #78350f;
}

.energy-rolls-bar {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  font-weight: 800;
  color: #38bdf8;
}

.turn-status-banner {
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(251, 191, 36, 0.3);
  border-radius: 12px;
  padding: 6px 16px;
  font-size: 12px;
  font-weight: 800;
  color: #f8fafc;
  display: flex;
  align-items: center;
  gap: 8px;
  max-width: 90%;
  text-align: center;
  z-index: 3;
}

/* Sidebar / Activity Feed */
.game-sidebar {
  width: 320px;
  background: rgba(19, 29, 49, 0.8);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 18px;
  display: flex;
  flex-direction: column;
  height: min(840px, 94vw);
  box-shadow: var(--shadow-3d);
}

.sidebar-header {
  padding: 12px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.sidebar-title {
  font-size: 14px;
  font-weight: 800;
  color: #fbbf24;
  display: flex;
  align-items: center;
  gap: 6px;
}

.sidebar-content {
  flex: 1;
  padding: 12px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.log-entry {
  background: rgba(15, 23, 42, 0.6);
  border-radius: 10px;
  padding: 8px 10px;
  font-size: 12px;
  line-height: 1.4;
  border-right: 3px solid #3b82f6;
  animation: slide-in 0.3s ease-out;
}

@keyframes slide-in {
  from { opacity: 0; transform: translateX(10px); }
  to { opacity: 1; transform: translateX(0); }
}

.log-entry.gold { border-right-color: #fbbf24; }
.log-entry.green { border-right-color: #10b981; }
.log-entry.red { border-right-color: #ef4444; }
.log-entry.purple { border-right-color: #a855f7; }

.log-time {
  font-size: 9px;
  color: #64748b;
  margin-bottom: 2px;
}

/* Floating Cash FX Numbers */
.floating-fx {
  position: absolute;
  font-size: 18px;
  font-weight: 900;
  pointer-events: none;
  z-index: 1000;
  animation: float-up-fade 1.4s forwards cubic-bezier(0.1, 0.8, 0.2, 1);
  text-shadow: 0 2px 6px rgba(0,0,0,0.8);
}

.floating-fx.plus { color: #10b981; }
.floating-fx.minus { color: #ef4444; }

@keyframes float-up-fade {
  0% { opacity: 0; transform: translateY(0) scale(0.6); }
  20% { opacity: 1; transform: translateY(-15px) scale(1.2); }
  80% { opacity: 1; }
  100% { opacity: 0; transform: translateY(-50px) scale(0.9); }
}

/* Modals Overlay */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 500;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
  padding: 16px;
}

.modal-overlay.active {
  opacity: 1;
  pointer-events: auto;
}

.modal-box {
  background: #1e293b;
  border: 2px solid #fbbf24;
  border-radius: 20px;
  width: min(520px, 94vw);
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 25px 60px rgba(0,0,0,0.8), 0 0 30px rgba(251, 191, 36, 0.3);
  display: flex;
  flex-direction: column;
  position: relative;
  transform: scale(0.9);
  transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1.2);
}

.modal-overlay.active .modal-box {
  transform: scale(1);
}

.modal-header {
  padding: 16px 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-title {
  font-size: 18px;
  font-weight: 900;
  color: #fbbf24;
  display: flex;
  align-items: center;
  gap: 8px;
}

.modal-close-btn {
  background: transparent;
  border: none;
  color: #94a3b8;
  font-size: 20px;
  cursor: pointer;
  padding: 4px;
}

.modal-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.modal-footer {
  padding: 14px 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

/* Property Deed Modal Card */
.deed-card {
  background: white;
  color: #1e293b;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0,0,0,0.4);
  border: 3px solid #334155;
  font-size: 13px;
}

.deed-header {
  padding: 14px;
  text-align: center;
  color: white;
  font-weight: 900;
}

.deed-header h2 {
  font-size: 20px;
  text-shadow: 0 2px 4px rgba(0,0,0,0.4);
}

.deed-table {
  padding: 12px 16px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.deed-row {
  display: flex;
  justify-content: space-between;
  border-bottom: 1px dashed #cbd5e1;
  padding-bottom: 4px;
  font-weight: 700;
}

.deed-row.highlight {
  background: #fef08a;
  padding: 4px 6px;
  border-radius: 6px;
  border-bottom: none;
}

/* Bank Heist Mini-Game Styles */
.heist-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.heist-vault-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
  width: 100%;
}

.vault-door {
  aspect-ratio: 1;
  background: linear-gradient(135deg, #475569, #1e293b);
  border: 2px solid #94a3b8;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}

.vault-door:hover:not(.opened) {
  transform: scale(1.06);
  border-color: #fbbf24;
  box-shadow: 0 0 12px rgba(251, 191, 36, 0.6);
}

.vault-door.opened {
  background: linear-gradient(135deg, #1e1b4b, #312e81);
  border-color: #f59e0b;
  cursor: default;
  animation: vault-pop 0.4s cubic-bezier(0.2, 0.8, 0.2, 1.2);
}

@keyframes vault-pop {
  0% { transform: scale(0.6) rotateY(90deg); }
  100% { transform: scale(1) rotateY(0deg); }
}

.heist-match-tracker {
  display: flex;
  justify-content: space-around;
  width: 100%;
  background: rgba(15, 23, 42, 0.6);
  padding: 10px;
  border-radius: 12px;
}

.match-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.match-icons {
  display: flex;
  gap: 4px;
}

.match-slot {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #334155;
  border: 1px solid #64748b;
}

.match-slot.filled {
  background: #fbbf24;
  box-shadow: 0 0 8px #fbbf24;
}

/* Landmark Shutdown Mini-Game */
.shutdown-stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  position: relative;
}

.target-landmark-box {
  width: 100%;
  height: 180px;
  background: radial-gradient(circle at center, #1e293b 0%, #0f172a 100%);
  border-radius: 16px;
  border: 2px solid #ef4444;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.target-landmark-icon {
  font-size: 70px;
  transition: transform 0.3s;
}

.target-crosshair {
  position: absolute;
  width: 120px;
  height: 120px;
  border: 2px dashed #ef4444;
  border-radius: 50%;
  animation: rotate-crosshair 6s linear infinite;
  pointer-events: none;
}

@keyframes rotate-crosshair {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.shield-deflection-dome {
  position: absolute;
  width: 140px;
  height: 140px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(56, 189, 248, 0.3) 0%, rgba(56, 189, 248, 0.7) 100%);
  border: 3px solid #38bdf8;
  box-shadow: 0 0 25px #38bdf8;
  animation: shield-pulse 0.4s ease-out;
}

@keyframes shield-pulse {
  0% { transform: scale(0.3); opacity: 0; }
  50% { transform: scale(1.1); opacity: 1; }
  100% { transform: scale(1); opacity: 1; }
}

/* Landmarks City Builder View */
.landmarks-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.landmark-builder-card {
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 14px;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.landmark-icon-badge {
  width: 48px;
  height: 48px;
  background: #0f172a;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  border: 2px solid #475569;
}

.landmark-meta {
  flex: 1;
}

.landmark-stars-row {
  display: flex;
  gap: 4px;
  margin-top: 4px;
}

.star-slot {
  font-size: 14px;
  color: #475569;
}

.star-slot.filled {
  color: #fbbf24;
  filter: drop-shadow(0 0 4px #fbbf24);
}

/* Wheel of Fortune */
.wheel-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  position: relative;
}

.wheel-canvas {
  width: 260px;
  height: 260px;
  border-radius: 50%;
  border: 6px solid #fbbf24;
  box-shadow: 0 0 25px rgba(251, 191, 36, 0.5);
  transition: transform 4s cubic-bezier(0.15, 0.9, 0.2, 1);
}

.wheel-pointer {
  position: absolute;
  top: -10px;
  width: 0;
  height: 0;
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  border-top: 24px solid #ef4444;
  filter: drop-shadow(0 4px 6px rgba(0,0,0,0.5));
  z-index: 10;
}

/* Confetti Celebration Canvas */
#confettiCanvas {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 9999;
}

/* Responsive adjustments */
@media (max-width: 900px) {
  .game-viewport {
    flex-direction: column;
    align-items: center;
  }
  .game-sidebar {
    width: min(840px, 94vw);
    height: 220px;
  }
  .emblem-title {
    font-size: 22px;
  }
  .btn-big-roll {
    font-size: 16px;
    padding: 10px 24px;
  }
  .dice-cube {
    width: 44px;
    height: 44px;
  }
  .dice-face {
    width: 44px;
    height: 44px;
  }
  .face-1 { transform: rotateY(0deg) translateZ(22px); }
  .face-2 { transform: rotateY(-90deg) translateZ(22px); }
  .face-3 { transform: rotateX(90deg) translateZ(22px); }
  .face-4 { transform: rotateX(-90deg) translateZ(22px); }
  .face-5 { transform: rotateY(90deg) translateZ(22px); }
  .face-6 { transform: rotateY(180deg) translateZ(22px); }
}
"""

print("styles.py module ready!")
