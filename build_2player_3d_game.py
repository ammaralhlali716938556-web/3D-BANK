import json
import os
from board_data import TILES, CHANCE_CARDS, CHEST_CARDS, LANDMARKS, WHEEL_ITEMS
from sound_engine import SOUND_JS

print("Building 2-Player Super 3D Bank El Hazz...")

with open("complete_3d_assets.json", "r", encoding="utf-8") as f:
    svg_assets = json.load(f)

# Two-Player Characters
CHARACTERS_2P = [
    {
        "id": "mr_hazz",
        "name": "مستر حظ",
        "title": "الملياردير الطموح",
        "avatar": "🎩",
        "color": "#ef4444",
        "accent": "#fbbf24",
        "token_svg": "fig_mr_hazz",
        "quote": "الفرصة لا تأتي مرتين، والحظ حليف الجريء!"
    },
    {
        "id": "cleo_queen",
        "name": "الملكة كليوباترا",
        "title": "أميرة العرش والذهب",
        "avatar": "👑",
        "color": "#3b82f6",
        "accent": "#eab308",
        "token_svg": "fig_cleopatra",
        "quote": "الأهرامات بُنيت بالذهب والعزيمة الملكية!"
    }
]

# Serialized data
tiles_json = json.dumps(TILES, ensure_ascii=False)
chance_json = json.dumps(CHANCE_CARDS, ensure_ascii=False)
chest_json = json.dumps(CHEST_CARDS, ensure_ascii=False)
landmarks_json = json.dumps(LANDMARKS, ensure_ascii=False)
characters_json = json.dumps(CHARACTERS_2P, ensure_ascii=False)
wheel_json = json.dumps(WHEEL_ITEMS, ensure_ascii=False)
svg_assets_json = json.dumps(svg_assets, ensure_ascii=False)

SUPER_3D_CSS = """
:root {
  --bg-main: #060913;
  --bg-board: #0f172a;
  --accent-gold: #f59e0b;
  --accent-gold-light: #fbbf24;
  --accent-red: #ef4444;
  --accent-blue: #3b82f6;
  --accent-purple: #a855f7;
  --accent-green: #10b981;
  --text-main: #f8fafc;
  --font-family: 'Cairo', 'Segoe UI', system-ui, -apple-system, sans-serif;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
}

body {
  background: radial-gradient(circle at 50% 15%, #1e1b4b 0%, #060913 100%);
  color: var(--text-main);
  font-family: var(--font-family);
  direction: rtl;
  min-height: 100vh;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
}

/* Header */
.app-header {
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(12px);
  border-bottom: 2px solid rgba(245, 158, 11, 0.35);
  padding: 8px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 4px 20px rgba(0,0,0,0.5);
}

.brand-title {
  display: flex;
  align-items: center;
  gap: 10px;
}

.brand-logo-icon {
  width: 42px;
  height: 42px;
  background: linear-gradient(135deg, #f59e0b, #d97706);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  box-shadow: 0 4px 10px rgba(245, 158, 11, 0.4), inset 0 2px 0 rgba(255,255,255,0.5);
  border: 2px solid #fef08a;
  animation: pulse-gold 2.5s infinite;
}

@keyframes pulse-gold {
  0%, 100% { transform: scale(1); filter: brightness(1); }
  50% { transform: scale(1.05); filter: brightness(1.2); box-shadow: 0 0 25px rgba(245, 158, 11, 0.9); }
}

.brand-text h1 {
  font-size: 20px;
  font-weight: 900;
  background: linear-gradient(to left, #fbbf24, #ffffff, #f59e0b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1.2;
}

.brand-badge {
  font-size: 10px;
  font-weight: 800;
  background: linear-gradient(90deg, #ef4444, #f59e0b);
  color: white;
  padding: 2px 8px;
  border-radius: 20px;
  margin-right: 6px;
  box-shadow: 0 2px 6px rgba(239, 68, 68, 0.4);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

/* 3D Chunky Buttons */
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
  box-shadow: 0 1px 0 #1e3a8a;
}

.btn-3d.gold {
  background: linear-gradient(180deg, #fbbf24, #d97706);
  box-shadow: 0 4px 0 #b45309, 0 6px 12px rgba(0,0,0,0.3);
  color: #451a03;
}
.btn-3d.gold:active { box-shadow: 0 1px 0 #b45309; }

.btn-3d.purple {
  background: linear-gradient(180deg, #a855f7, #7e22ce);
  box-shadow: 0 4px 0 #581c87;
}
.btn-3d.purple:active { box-shadow: 0 1px 0 #581c87; }

.btn-3d.green {
  background: linear-gradient(180deg, #10b981, #047857);
  box-shadow: 0 4px 0 #064e3b;
}

.btn-3d.red {
  background: linear-gradient(180deg, #ef4444, #b91c1c);
  box-shadow: 0 4px 0 #7f1d1d;
}

/* 2-Player Head-to-Head Duel Clash Arena Bar */
.versus-clash-bar {
  background: linear-gradient(180deg, rgba(15, 23, 42, 0.9) 0%, rgba(6, 9, 19, 0.95) 100%);
  border-bottom: 2px solid rgba(255, 255, 255, 0.08);
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
  position: relative;
  z-index: 50;
}

.player-duel-card {
  flex: 1;
  max-width: 480px;
  background: #1e293b;
  border-radius: 16px;
  padding: 10px 16px;
  display: flex;
  align-items: center;
  gap: 14px;
  border: 3px solid #334155;
  box-shadow: 0 6px 0 #0f172a, 0 10px 20px rgba(0,0,0,0.4);
  position: relative;
  transition: all 0.3s ease;
}

.player-duel-card.active-turn {
  border-color: #fbbf24;
  background: linear-gradient(135deg, #1e293b, #2e2640);
  box-shadow: 0 6px 0 #b45309, 0 0 25px rgba(251, 191, 36, 0.45);
  transform: translateY(-2px);
}

.player-duel-card.p1 {
  border-right: 6px solid #ef4444;
}

.player-duel-card.p2 {
  border-left: 6px solid #3b82f6;
  flex-direction: row-reverse;
  text-align: left;
}

.duel-avatar-3d {
  width: 58px;
  height: 58px;
  filter: drop-shadow(0 4px 8px rgba(0,0,0,0.6));
  animation: float-avatar 3s infinite ease-in-out;
  cursor: pointer;
}

@keyframes float-avatar {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-4px); }
}

.duel-info-col {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.duel-name-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.player-duel-card.p2 .duel-name-row {
  justify-content: flex-end;
}

.duel-name {
  font-size: 16px;
  font-weight: 900;
  color: #f8fafc;
}

.duel-bot-pill {
  font-size: 10px;
  background: rgba(59, 130, 246, 0.25);
  color: #93c5fd;
  border: 1px solid #3b82f6;
  padding: 1px 6px;
  border-radius: 8px;
  font-weight: 700;
}

.duel-money {
  font-size: 18px;
  font-weight: 900;
  color: #fbbf24;
  text-shadow: 0 2px 4px rgba(0,0,0,0.5);
}

.duel-net-worth {
  font-size: 11px;
  color: #94a3b8;
  font-weight: 700;
}

.duel-shields-row {
  display: flex;
  gap: 4px;
}

.player-duel-card.p2 .duel-shields-row {
  justify-content: flex-end;
}

.shield-3d-badge {
  font-size: 13px;
  opacity: 0.25;
  filter: grayscale(1);
  transition: all 0.3s;
}

.shield-3d-badge.active {
  opacity: 1;
  filter: drop-shadow(0 0 6px #38bdf8);
}

/* Center VS Badge */
.versus-center-emblem {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  position: relative;
}

.vs-icon-badge {
  width: 44px;
  height: 44px;
  background: radial-gradient(circle, #ef4444 0%, #991b1b 100%);
  border: 3px solid #fef08a;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 900;
  color: #ffffff;
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.6), 0 0 20px rgba(251, 191, 36, 0.5);
  animation: vs-pulse 2s infinite ease-in-out;
}

@keyframes vs-pulse {
  0%, 100% { transform: scale(1); filter: brightness(1); }
  50% { transform: scale(1.1); filter: brightness(1.25); }
}

.versus-sub-label {
  font-size: 10px;
  font-weight: 800;
  color: #fbbf24;
  letter-spacing: 1px;
}

/* Main Layout */
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
  perspective: 1400px;
  transition: perspective 0.6s ease;
}

.board-grid {
  width: min(850px, 94vw);
  height: min(850px, 94vw);
  background: #0b1120;
  border: 6px solid #b45309;
  border-radius: 26px;
  display: grid;
  grid-template-columns: 1.35fr repeat(9, 1fr) 1.35fr;
  grid-template-rows: 1.35fr repeat(9, 1fr) 1.35fr;
  gap: 3px;
  padding: 8px;
  position: relative;
  box-shadow: 0 20px 0 #0f172a, 0 24px 0 #78350f, 0 35px 60px rgba(0, 0, 0, 0.85);
  transform-origin: center center;
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.6s ease;
}

.board-perspective-wrapper.mode-3d .board-grid {
  transform: rotateX(28deg) rotateZ(-3deg) scale(0.95);
  box-shadow: 0 30px 0 #0f172a, 0 36px 0 #78350f, 0 50px 80px rgba(0, 0, 0, 0.9);
}

/* 3D Chunky Board Tiles */
.tile {
  background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 10px;
  box-shadow: 0 5px 0 #020617, 0 8px 12px rgba(0, 0, 0, 0.6);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 3px 2px;
  position: relative;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
  overflow: visible;
  text-align: center;
}

.tile:hover {
  transform: translateY(-6px) scale(1.06);
  box-shadow: 0 9px 0 #020617, 0 16px 24px rgba(0, 0, 0, 0.7);
  border-color: #fbbf24;
  z-index: 30;
}

.tile-corner {
  background: radial-gradient(circle at 50% 30%, #1e293b 0%, #060913 100%);
  border: 2px solid #64748b;
  box-shadow: 0 6px 0 #020617, 0 10px 16px rgba(0, 0, 0, 0.7);
}

.tile-corner:hover {
  border-color: #f59e0b;
}

.corner-title {
  font-size: 11px;
  font-weight: 900;
  color: #fbbf24;
}

.corner-sub {
  font-size: 8px;
  color: #94a3b8;
}

/* Metallic Glossy Color Bar */
.color-bar {
  width: 100%;
  height: 13px;
  border-radius: 6px 6px 0 0;
  box-shadow: inset 0 2px 2px rgba(255,255,255,0.4), 0 1px 3px rgba(0,0,0,0.4);
  position: relative;
  overflow: hidden;
}

.color-bar::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 45%;
  background: linear-gradient(180deg, rgba(255,255,255,0.45) 0%, transparent 100%);
}

.tile-name {
  font-size: 9.5px;
  font-weight: 800;
  color: #f8fafc;
  line-height: 1.15;
  white-space: nowrap;
  max-width: 95%;
  overflow: hidden;
  text-overflow: ellipsis;
}

.tile-price {
  font-size: 8.5px;
  font-weight: 900;
  color: #fbbf24;
  background: rgba(0,0,0,0.45);
  padding: 1px 4px;
  border-radius: 4px;
  border: 1px solid rgba(251, 191, 36, 0.3);
}

/* 3D Art inside Tiles */
.tile-3d-art {
  width: 92%;
  height: 46px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 1px 0;
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.6));
  transition: transform 0.2s ease;
}

.tile-3d-art svg {
  width: 100%;
  height: 100%;
  max-height: 46px;
  object-fit: contain;
}

.tile:hover .tile-3d-art {
  transform: scale(1.15) translateY(-2px);
}

.tile-corner .tile-3d-art {
  height: 54px;
}

.tile-corner .tile-3d-art svg {
  max-height: 54px;
}

/* 3D Houses & Hotels on Tiles */
.tile-buildings-3d {
  position: absolute;
  top: 10px;
  right: 2px;
  display: flex;
  gap: 1px;
  z-index: 10;
  filter: drop-shadow(0 3px 4px rgba(0, 0, 0, 0.6));
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
.player-tokens-container {
  position: absolute;
  bottom: 2px;
  display: flex;
  gap: 3px;
  justify-content: center;
  align-items: center;
  z-index: 15;
  width: 100%;
}

.board-token-3d {
  width: 32px;
  height: 32px;
  filter: drop-shadow(0 5px 8px rgba(0, 0, 0, 0.75));
  animation: token-hop 0.4s ease-out;
  cursor: pointer;
  transition: transform 0.2s;
}

.board-token-3d svg {
  width: 100%;
  height: 100%;
}

.board-token-3d:hover {
  transform: scale(1.25) translateY(-4px);
}

@keyframes token-hop {
  0% { transform: translateY(-18px) scale(1.3); }
  60% { transform: translateY(2px) scale(0.9); }
  100% { transform: translateY(0) scale(1); }
}

/* Owner Stripe */
.tile.owned {
  box-shadow: inset 0 0 0 2px var(--owner-color), 0 5px 0 #020617, 0 8px 12px rgba(0, 0, 0, 0.6);
}

.owner-indicator {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: var(--owner-color, transparent);
  border-radius: 0 0 8px 8px;
}

.tile.mortgaged::after {
  content: 'مرهون';
  position: absolute;
  inset: 0;
  background: rgba(185, 28, 28, 0.75);
  backdrop-filter: blur(1px);
  color: white;
  font-size: 11px;
  font-weight: 900;
  display: flex;
  align-items: center;
  justify-content: center;
  transform: rotate(-15deg);
  z-index: 8;
  border-radius: 8px;
}

/* Board Center Stage */
.board-center {
  grid-column: 2 / 11;
  grid-row: 2 / 11;
  background: radial-gradient(circle at center, #1e1b4b 0%, #060913 100%);
  border-radius: 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 14px;
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 0 45px rgba(0,0,0,0.6);
  border: 1px solid rgba(255,255,255,0.08);
}

.center-top-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  z-index: 3;
}

.free-parking-pot {
  background: rgba(15, 23, 42, 0.85);
  border: 2px solid #6366f1;
  padding: 6px 14px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 0 15px rgba(99, 102, 241, 0.4);
}

.pot-icon {
  font-size: 20px;
}

.pot-amount {
  font-size: 15px;
  font-weight: 900;
  color: #fbbf24;
}

.board-title-emblem {
  text-align: center;
  z-index: 3;
}

.emblem-title {
  font-size: 28px;
  font-weight: 900;
  background: linear-gradient(180deg, #fef08a 0%, #f59e0b 50%, #b45309 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 4px 15px rgba(245, 158, 11, 0.4);
  letter-spacing: -1px;
}

.emblem-sub {
  font-size: 11px;
  font-weight: 800;
  color: #94a3b8;
  letter-spacing: 1.5px;
}

/* 3D Animated Cairo Skyline Diorama */
.center-diorama-container {
  width: 100%;
  max-width: 420px;
  height: 125px;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(245, 158, 11, 0.4);
  margin-bottom: 6px;
  position: relative;
  z-index: 3;
}

.center-diorama-container svg {
  width: 100%;
  height: 100%;
  display: block;
}

/* 3D Rolling Dice Arena */
.dice-arena {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 30px;
  margin: 6px 0;
  z-index: 3;
  perspective: 700px;
  min-height: 80px;
}

.dice-cube {
  width: 56px;
  height: 56px;
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
  width: 56px;
  height: 56px;
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

.face-1 { transform: rotateY(0deg) translateZ(28px); }
.face-2 { transform: rotateY(-90deg) translateZ(28px); }
.face-3 { transform: rotateX(90deg) translateZ(28px); }
.face-4 { transform: rotateX(-90deg) translateZ(28px); }
.face-5 { transform: rotateY(90deg) translateZ(28px); }
.face-6 { transform: rotateY(180deg) translateZ(28px); }

/* Multiplier Bar & Roll Button */
.center-controls-row {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  width: 100%;
  z-index: 3;
}

.multiplier-bar {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(15, 23, 42, 0.85);
  padding: 4px 8px;
  border-radius: 20px;
  border: 1px solid rgba(255,255,255,0.12);
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
  box-shadow: 0 0 12px rgba(245, 158, 11, 0.7);
}

.btn-big-roll {
  background: linear-gradient(180deg, #fbbf24 0%, #f59e0b 50%, #d97706 100%);
  border: none;
  color: #451a03;
  font-family: inherit;
  font-size: 20px;
  font-weight: 900;
  padding: 12px 40px;
  border-radius: 20px;
  cursor: pointer;
  box-shadow: 0 6px 0 #b45309, 0 14px 28px rgba(245, 158, 11, 0.55);
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 10px;
  position: relative;
  overflow: hidden;
}

.btn-big-roll:hover {
  filter: brightness(1.1);
  transform: translateY(-2px);
  box-shadow: 0 8px 0 #b45309, 0 18px 32px rgba(245, 158, 11, 0.65);
}

.btn-big-roll:active {
  transform: translateY(4px);
  box-shadow: 0 2px 0 #b45309;
}

.btn-big-roll:disabled {
  filter: grayscale(0.8);
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
  box-shadow: 0 4px 0 #78350f;
}

.turn-status-banner {
  background: rgba(15, 23, 42, 0.92);
  border: 1px solid rgba(251, 191, 36, 0.4);
  border-radius: 12px;
  padding: 6px 16px;
  font-size: 13px;
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
  background: rgba(19, 29, 49, 0.85);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  height: min(850px, 94vw);
  box-shadow: 0 15px 35px rgba(0,0,0,0.5);
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
  background: rgba(15, 23, 42, 0.65);
  border-radius: 10px;
  padding: 8px 10px;
  font-size: 12px;
  line-height: 1.45;
  border-right: 3px solid #3b82f6;
}

.log-entry.gold { border-right-color: #fbbf24; }
.log-entry.green { border-right-color: #10b981; }
.log-entry.red { border-right-color: #ef4444; }

.log-time {
  font-size: 9px;
  color: #64748b;
  margin-bottom: 2px;
}

/* Modals */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.8);
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
  border-radius: 22px;
  width: min(540px, 94vw);
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 25px 60px rgba(0,0,0,0.85), 0 0 35px rgba(251, 191, 36, 0.35);
  display: flex;
  flex-direction: column;
  position: relative;
  transform: scale(0.9);
  transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1.2);
}

.modal-overlay.active .modal-box { transform: scale(1); }

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

/* Deed Modal Card */
.deed-card {
  background: white;
  color: #1e293b;
  border-radius: 16px;
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
  font-size: 22px;
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

/* Bank Heist Mini-Game */
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
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}

.vault-door:hover:not(.opened) {
  transform: scale(1.08);
  border-color: #fbbf24;
  box-shadow: 0 0 14px rgba(251, 191, 36, 0.6);
}

.vault-door.opened {
  background: linear-gradient(135deg, #1e1b4b, #312e81);
  border-color: #f59e0b;
  cursor: default;
}

.heist-match-tracker {
  display: flex;
  justify-content: space-around;
  width: 100%;
  background: rgba(15, 23, 42, 0.7);
  padding: 10px;
  border-radius: 12px;
}

.match-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.match-icons { display: flex; gap: 4px; }

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

/* Shutdown Mini-Game */
.shutdown-stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  position: relative;
}

.target-landmark-box {
  width: 100%;
  height: 190px;
  background: radial-gradient(circle at center, #1e293b 0%, #0f172a 100%);
  border-radius: 18px;
  border: 2px solid #ef4444;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.target-crosshair {
  position: absolute;
  width: 130px;
  height: 130px;
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
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(56, 189, 248, 0.3) 0%, rgba(56, 189, 248, 0.7) 100%);
  border: 3px solid #38bdf8;
  box-shadow: 0 0 30px #38bdf8;
  animation: shield-pulse 0.4s ease-out;
}

@keyframes shield-pulse {
  0% { transform: scale(0.3); opacity: 0; }
  50% { transform: scale(1.1); opacity: 1; }
  100% { transform: scale(1); opacity: 1; }
}

/* City Landmarks */
.landmarks-list { display: flex; flex-direction: column; gap: 12px; }

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
  width: 60px;
  height: 60px;
  background: #0f172a;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #475569;
  padding: 4px;
}

.landmark-meta { flex: 1; }
.landmark-stars-row { display: flex; gap: 4px; margin-top: 4px; }
.star-slot { font-size: 14px; color: #475569; }
.star-slot.filled { color: #fbbf24; filter: drop-shadow(0 0 4px #fbbf24); }

/* Wheel of Fortune */
.wheel-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  position: relative;
}

.wheel-canvas {
  width: 280px;
  height: 280px;
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

/* Floating Cash FX */
.floating-fx {
  position: absolute;
  font-size: 20px;
  font-weight: 900;
  pointer-events: none;
  z-index: 1000;
  animation: float-up-fade 1.5s forwards cubic-bezier(0.1, 0.8, 0.2, 1);
  text-shadow: 0 2px 6px rgba(0,0,0,0.9);
}

.floating-fx.plus { color: #10b981; }
.floating-fx.minus { color: #ef4444; }

@keyframes float-up-fade {
  0% { opacity: 0; transform: translateY(0) scale(0.6); }
  20% { opacity: 1; transform: translateY(-16px) scale(1.2); }
  80% { opacity: 1; }
  100% { opacity: 0; transform: translateY(-55px) scale(0.9); }
}

#confettiCanvas {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 9999;
}

@media (max-width: 900px) {
  .game-viewport { flex-direction: column; align-items: center; }
  .game-sidebar { width: min(850px, 94vw); height: 220px; }
  .versus-clash-bar { flex-direction: column; gap: 10px; }
  .player-duel-card { width: 100%; max-width: 100%; }
}
"""

full_2p_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>بنك الحظ 3D - مواجهة مونوبولي جو (لاعبان 1 ضد 1)</title>
  <style>
{SUPER_3D_CSS}
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

  <!-- Head-to-Head 2-Player Clash Bar -->
  <section class="versus-clash-bar">
    
    <!-- Player 1 Card: مستر حظ -->
    <div class="player-duel-card p1" id="cardP1">
      <div class="duel-avatar-3d" id="avatarP1Box" title="مستر حظ (أنت)"></div>
      <div class="duel-info-col">
        <div class="duel-name-row">
          <span class="duel-name">مستر حظ</span>
          <span style="font-size: 10px; color: #ef4444; font-weight: 800;">(أنت)</span>
        </div>
        <div class="duel-money" id="moneyP1Display">1500 ج.م</div>
        <div class="duel-net-worth" id="netWorthP1Display">الثروة: 1500 ج.م</div>
        <div class="duel-shields-row" id="shieldsP1Row">
          <span class="shield-3d-badge active">🛡️</span>
          <span class="shield-3d-badge active">🛡️</span>
          <span class="shield-3d-badge active">🛡️</span>
        </div>
      </div>
    </div>

    <!-- Center VS Emblem -->
    <div class="versus-center-emblem">
      <div class="vs-icon-badge">VS</div>
      <div class="versus-sub-label">مواجهة ثنائية</div>
    </div>

    <!-- Player 2 Card: الملكة كليوباترا -->
    <div class="player-duel-card p2" id="cardP2">
      <div class="duel-avatar-3d" id="avatarP2Box" title="الملكة كليوباترا"></div>
      <div class="duel-info-col">
        <div class="duel-name-row">
          <span class="duel-name">الملكة كليوباترا</span>
          <span class="duel-bot-pill">ذكاء آلي 🤖</span>
        </div>
        <div class="duel-money" id="moneyP2Display">1500 ج.م</div>
        <div class="duel-net-worth" id="netWorthP2Display">الثروة: 1500 ج.م</div>
        <div class="duel-shields-row" id="shieldsP2Row">
          <span class="shield-3d-badge active">🛡️</span>
          <span class="shield-3d-badge active">🛡️</span>
          <span class="shield-3d-badge active">🛡️</span>
        </div>
      </div>
    </div>

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
                <div class="emblem-title">بنك الحظ 3D</div>
                <div class="emblem-sub" id="boardCityLabel">القاهرة التاريخية • مواجهة ثنائية ⚔️</div>
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
            <div class="center-diorama-container" id="centerDioramaBox"></div>

            <!-- 3D Rolling Dice Stage -->
            <div class="dice-arena" id="diceArena">
              <!-- 3D Die 1 (Mr. Hazz - Red Pips) -->
              <div class="dice-cube" id="die1">
                <div class="dice-face face-1"><div class="dice-pip" style="grid-area: 2/2;"></div></div>
                <div class="dice-face face-2"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-3"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 2/2;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-4"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-5"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 2/2;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-6"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 2/1;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 2/3;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
              </div>

              <!-- 3D Die 2 (Cleopatra - Blue Pips) -->
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
                <span class="multiplier-label">مضاعف النرد:</span>
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
          <span>سجل وقائع النزال (1 ضد 1)</span>
        </div>
        <button class="btn-3d" style="padding: 4px 8px; font-size: 11px;" id="btnClearLog">مسح</button>
      </div>
      <div class="sidebar-content" id="activityLog"></div>
    </aside>

  </main>

  <!-- MODAL 1: Property Deed Card Modal with 3D Illustration -->
  <div class="modal-overlay" id="modalDeed">
    <div class="modal-box">
      <div class="modal-header">
        <div class="modal-title">
          <span>🏠</span>
          <span>سند ملكية العقار ثلاثي الأبعاد</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalDeed')">✕</button>
      </div>
      <div class="modal-body" id="deedModalBody"></div>
      <div class="modal-footer" id="deedModalFooter"></div>
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
        <div style="width: 110px; height: 110px; margin-bottom: 8px;" id="cardModal3DArt"></div>
        <h2 style="font-size: 20px; color: #fbbf24; margin-bottom: 8px;" id="cardModalTitle">عنوان الكارت</h2>
        <p style="font-size: 14px; color: #e2e8f0; line-height: 1.6;" id="cardModalDesc">وصف وتأثير الكارت...</p>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <button class="btn-3d gold" id="btnExecuteCardAction" style="padding: 10px 28px; font-size: 15px;">
          <span>تنفيذ الأمر</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 3: Bank Heist Mini-Game (Direct Rival Heist) -->
  <div class="modal-overlay" id="modalHeist">
    <div class="modal-box" style="width: min(560px, 95vw);">
      <div class="modal-header">
        <div class="modal-title">
          <span>🏦</span>
          <span>السطو على خزنة الخصم (Bank Heist)</span>
        </div>
      </div>
      <div class="modal-body heist-container">
        <p style="text-align: center; font-size: 13px; color: #cbd5e1;" id="heistTargetText">
          أنت الآن تقتحم خزينة منافسك! افتح الأبواب وطابق 3 عناصر لتحديد غنيمتك!
        </p>

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

        <div class="heist-vault-grid" id="heistVaultGrid"></div>
        <div id="heistResultBanner" style="font-size: 16px; font-weight: 900; color: #fbbf24; text-align: center; min-height: 24px;"></div>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <button class="btn-3d gold" id="btnCollectHeist" style="display: none; padding: 10px 24px;">
          <span>استلام الغنائم 💰</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 4: Landmark Shutdown Mini-Game (Direct Rival Mallet Smash) -->
  <div class="modal-overlay" id="modalShutdown">
    <div class="modal-box">
      <div class="modal-header">
        <div class="modal-title">
          <span>🔨</span>
          <span>الهجوم والتعطيل على معالم الخصم (Shutdown)</span>
        </div>
      </div>
      <div class="modal-body shutdown-stage">
        <p style="text-align: center; font-size: 13px; color: #cbd5e1;" id="shutdownSubtext">
          استهدف معالم منافسك بالمطرقة الكرتونية! هل يمتلك درعاً لصد الهجوم؟
        </p>

        <div class="target-landmark-box" id="targetLandmarkBox">
          <div class="target-crosshair"></div>
          <div class="target-landmark-icon" id="targetLandmarkIcon" style="width: 110px; height: 110px;"></div>
          <div style="font-size: 15px; font-weight: 800; margin-top: 8px; color: #fbbf24;" id="targetLandmarkName">
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

        <div class="landmarks-list" id="landmarksListContainer"></div>
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
          <span>دليل وقواعد بنك الحظ & مونوبولي جو (نزال 1 ضد 1)</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalRules')">✕</button>
      </div>
      <div class="modal-body" style="font-size: 13px; line-height: 1.8; color: #e2e8f0;">
        
        <h3 style="color: #fbbf24; margin-bottom: 6px;">⚔️ نظام المواجهة الثنائية (1 ضد 1):</h3>
        <ul style="padding-right: 20px; margin-bottom: 14px;">
          <li><b>أنت (مستر حظ) ضد منافستك (الملكة كليوباترا):</b> مواجهة مباشرة وسريعة! كل رمية نرد وكل عقار تشتريه يقلص خيارات خصمك.</li>
          <li><b>السطو المباشر (Bank Heist):</b> تقتحم خزينة منافسك مباشرة لتسرق من أمواله نقداً!</li>
          <li><b>الهجوم والتعطيل (Shutdown):</b> تضرب معالم خصمك بالمطرقة الكرتونية لهدمها، فإن كان لديه درع تصدى لهجومك وخسر درعاً!</li>
        </ul>

        <h3 style="color: #38bdf8; margin-bottom: 6px;">🎲 قواعد بنك الحظ الكلاسيكية الكاملة (40 مربعاً):</h3>
        <ul style="padding-right: 20px; margin-bottom: 14px;">
          <li><b>نقطة البداية (انطلق):</b> مر أو اهبط عليها لتقبض 200 ج.م مضروبة في مضاعف النرد.</li>
          <li><b>شراء المدن والاحتكار:</b> امتلاك كامل مدن المجموعة اللونية يضاعف إيجار الأراضي ويفتح بناء المنازل (1 إلى 4) ثم الفندق الفاخر!</li>
          <li><b>محطات القطار والمرافق:</b> 4 محطات قطار تصاعدية الإيجار وشركتا الكهرباء والمياه التي تحسب الإيجار حسب رمية النرد.</li>
          <li><b>الاستراحة المجانية:</b> تجمع كل ضرائب اللاعبين وغرامات الرادار، ومن يقف عليها يفوز بالحصيلة كاملة!</li>
          <li><b>سجن القلعة:</b> يدخله اللاعب عند مربع ادخل السجن أو كروت الحظ أو رمي دبل 3 مرات متتالية.</li>
        </ul>

      </div>
      <div class="modal-footer">
        <button class="btn-3d gold" onclick="closeModal('modalRules')">فهمت القواعد! هيا لنلعب</button>
      </div>
    </div>
  </div>

  <!-- JAVASCRIPT GAME LOGIC & SOUND ENGINE -->
  <script>
  // Injected 2-Player Data & 3D SVGs
  const TILES = {tiles_json};
  const CHANCE_CARDS = {chance_json};
  const CHEST_CARDS = {chest_json};
  const LANDMARKS_DEF = {landmarks_json};
  const CHARACTERS_DEF = {characters_json};
  const WHEEL_ITEMS_DEF = {wheel_json};
  const SVG_ASSETS = {svg_assets_json};

  // Web Audio SFX
  {SOUND_JS}
  const sfx = new WebAudioSFX();

  // Core Game State (2 Players Only)
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

  // 3D Architectural Model Mapper for All 40 Tiles
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

  // Initialize strictly 2 Players
  function initGame() {{
    state.players = [
      {{
        id: 0,
        name: 'مستر حظ',
        title: 'الملياردير الطموح',
        avatar: '🎩',
        color: '#ef4444',
        accent: '#fbbf24',
        tokenSvg: SVG_ASSETS.fig_mr_hazz,
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
        name: 'الملكة كليوباترا',
        title: 'أميرة العرش والذهب',
        avatar: '👑',
        color: '#3b82f6',
        accent: '#eab308',
        tokenSvg: SVG_ASSETS.fig_cleopatra,
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
      }}
    ];

    state.currentPlayerIdx = 0;
    state.multiplier = 1;
    state.freeParkingPot = 200;
    state.boardLevel = 1;
    state.tileOwnership = {{}};

    // Load Center Diorama
    document.getElementById('centerDioramaBox').innerHTML = SVG_ASSETS.center_diorama;

    // Load Player Avatars in Duel Bar
    document.getElementById('avatarP1Box').innerHTML = SVG_ASSETS.fig_mr_hazz;
    document.getElementById('avatarP2Box').innerHTML = SVG_ASSETS.fig_cleopatra;

    renderBoardTiles();
    updateUI();
    addLog('⚔️ انطلقت مواجهة العمالقة الثنائية: مستر حظ ضد الملكة كليوباترا!', 'gold');
  }}

  // Render the 40 Tiles on CSS Grid
  function renderBoardTiles() {{
    const grid = document.getElementById('boardGrid');
    
    // Remove existing tile elements
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

    state.players.forEach(p => {{
      if (p.isBankrupt) return;
      const cont = document.getElementById(`tokens-${{p.position}}`);
      if (cont) {{
        const token = document.createElement('div');
        token.className = 'board-token-3d';
        token.innerHTML = p.tokenSvg;
        token.title = `${{p.name}} (${{p.money}} ج.م)`;
        cont.appendChild(token);
      }}
    }});
  }}

  // Update Visual Indicators for Properties
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

        if (record.mortgaged) {{
          tileDiv.classList.add('mortgaged');
        }} else {{
          tileDiv.classList.remove('mortgaged');
        }}

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

  // Update UI for 2-Player Clash Arena
  function updateUI() {{
    const p1 = state.players[0];
    const p2 = state.players[1];
    const curr = state.players[state.currentPlayerIdx];

    // Player 1 Stats
    document.getElementById('moneyP1Display').innerText = `${{p1.money}} ج.م`;
    document.getElementById('netWorthP1Display').innerText = `الثروة: ${{p1.netWorth}} ج.م`;
    updateShieldsRow('shieldsP1Row', p1.shields);
    document.getElementById('cardP1').className = `player-duel-card p1 ${{state.currentPlayerIdx === 0 ? 'active-turn' : ''}}`;

    // Player 2 Stats
    document.getElementById('moneyP2Display').innerText = `${{p2.money}} ج.م`;
    document.getElementById('netWorthP2Display').innerText = `الثروة: ${{p2.netWorth}} ج.م`;
    updateShieldsRow('shieldsP2Row', p2.shields);
    document.getElementById('cardP2').className = `player-duel-card p2 ${{state.currentPlayerIdx === 1 ? 'active-turn' : ''}}`;

    // Center Indicators
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
    updateTileOwnershipVisuals();
  }}

  function updateShieldsRow(rowId, shieldCount) {{
    const badges = document.getElementById(rowId).querySelectorAll('.shield-3d-badge');
    badges.forEach((b, idx) => {{
      if (idx < shieldCount) b.classList.add('active');
      else b.classList.remove('active');
    }});
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

  // Floating Cash Visual FX
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

  // 3D Dice Roll
  function rollDiceAction() {{
    if (state.isRolling) return;
    const player = state.players[state.currentPlayerIdx];
    if (player.isBankrupt) return;

    if (player.rolls < state.multiplier) {{
      player.rolls += 10;
      addLog(`⚡ تم تزويد ${{player.name}} بـ 10 نرد إضافي تلقائياً!`, 'gold');
    }}
    player.rolls = Math.max(0, player.rolls - state.multiplier);

    state.isRolling = true;
    document.getElementById('btnRollDice').disabled = true;

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

      setDieTransform(die1, d1);
      setDieTransform(die2, d2);

      const isDoubles = d1 === d2;
      const totalSteps = d1 + d2;
      addLog(`🎲 رمى ${{player.name}} النرد: [${{d1}}] و [${{d2}}] = مجموع ${{totalSteps}}! ${{isDoubles ? '🔥 (دبل!)' : ''}}`, isDoubles ? 'gold' : '');

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
            addLog(`💸 دفع ${{player.name}} كفالة 50 ج.م إجبارية وتم إخلاء سبيله!`, 'red');
            movePlayerSteps(player, totalSteps);
          }} else {{
            addLog(`⛓️ ${{player.name}} لا يزال في سجن القلعة (${{player.jailTurns}} من 3).`, 'red');
            state.isRolling = false;
            endTurn();
          }}
        }}
        return;
      }}

      if (isDoubles) {{
        state.doublesCount++;
        if (state.doublesCount === 3) {{
          addLog(`🚨 رمى ${{player.name}} الدبل 3 مرات متتالية! إلى السجن فوراً!`, 'red');
          sendToJail(player);
          return;
        }}
      }} else {{
        state.doublesCount = 0;
      }}

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

  // Step-by-Step Hop Movement
  function movePlayerSteps(player, steps, isDoubles = false) {{
    let currentStep = 0;
    const interval = setInterval(() => {{
      currentStep++;
      player.position = (player.position + 1) % 40;
      
      if (player.position === 0) {{
        const goReward = 200 * state.multiplier;
        player.money += goReward;
        player.netWorth += goReward;
        sfx.playCoin();
        showFloatingFX(`+${{goReward}} ج.م`, true, 0);
        addLog(`🚀 مر ${{player.name}} بنقطة انطلق ونال مكافأة ${{goReward}} ج.م!`, 'green');
      }}

      renderTokens();

      if (currentStep >= steps) {{
        clearInterval(interval);
        state.isRolling = false;
        handleTileArrival(player, isDoubles);
      }}
    }}, 140);
  }}

  // Tile Actions
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
        addLog(`💸 دفع ${{player.name}} ضريبة قدرها ${{taxAmount}} ج.م لوعاء الاستراحة!`, 'red');
        finishArrivalAction(player, isDoubles);
        break;

      case 'parking':
        const winPot = state.freeParkingPot;
        player.money += winPot;
        player.netWorth += winPot;
        state.freeParkingPot = 50;
        sfx.playFanfare();
        showFloatingFX(`+${{winPot}} ج.م`, true, tile.id);
        addLog(`🎉 هبط ${{player.name}} على الاستراحة المجانية واستولى على كامل الوعاء: ${{winPot}} ج.م!`, 'gold');
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

  // Property Rent & Buy in 1v1
  function handlePropertyArrival(player, tile, isDoubles) {{
    const ownership = state.tileOwnership[tile.id];

    if (!ownership || ownership.ownerId === null) {{
      if (player.isBot) {{
        if (player.money >= tile.price + 100) {{
          buyPropertyDirect(player, tile);
        }} else {{
          addLog(`🤖 قررت ${{player.name}} عدم شراء [${{tile.name}}] للحفاظ على السيولة.`);
        }}
        finishArrivalAction(player, isDoubles);
      }} else {{
        openDeedModal(tile.id, true, isDoubles);
      }}
      return;
    }}

    if (ownership.ownerId !== player.id) {{
      const rival = state.players[ownership.ownerId];
      if (ownership.mortgaged) {{
        addLog(`العقار [${{tile.name}}] مرهون، لم يتم دفع إيجار!`);
        finishArrivalAction(player, isDoubles);
        return;
      }}

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

      const actualPaid = Math.min(player.money, rent);
      player.money -= actualPaid;
      rival.money += actualPaid;
      rival.netWorth += actualPaid;
      player.netWorth = Math.max(0, player.netWorth - actualPaid);

      sfx.playChaChing();
      showFloatingFX(`-${{actualPaid}} ج.م`, false, tile.id);
      showFloatingFX(`+${{actualPaid}} ج.م`, true, rival.position);
      addLog(`🏠 دفع ${{player.name}} إيجاراً مباشراً قدره ${{actualPaid}} ج.م لمنافسه ${{rival.name}} في [${{tile.name}}]!`, 'red');

      if (player.money <= 0) {{
        handleBankruptcy(player, rival);
      }}

      finishArrivalAction(player, isDoubles);
    }} else {{
      addLog(`✨ ${{player.name}} في ضيافة عقاره الخاص [${{tile.name}}].`);
      if (player.isBot && ownership.houses < 5 && player.money > tile.houseCost + 150) {{
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

  function sendToJail(player) {{
    player.position = 10;
    player.inJail = true;
    player.jailTurns = 0;
    state.doublesCount = 0;
    state.isRolling = false;
    sfx.playJail();
    addLog(`⛓️ دخل ${{player.name}} سجن القلعة!`, 'red');
    renderTokens();
    updateUI();
    endTurn();
  }}

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
      }}, 1400);
    }}
  }}

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
        const rival = state.players[player.id === 0 ? 1 : 0];
        const gift = Math.min(rival.money, card.amount);
        rival.money -= gift;
        player.money += gift;
        sfx.playCoin();
        addLog(`🎂 قدم ${{rival.name}} هدية ${{gift}} ج.م لـ ${{player.name}} بمناسبة عيد ميلاده!`, 'gold');
        break;

      default:
        break;
    }}

    finishArrivalAction(player, isDoubles);
  }}

  // 1v1 Bank Heist Mini-Game
  function startBankHeist(attacker) {{
    const rival = state.players[attacker.id === 0 ? 1 : 0];
    state.heistState = {{
      attacker,
      rival,
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

    document.getElementById('heistTargetText').innerText = `أنت الآن تقتحم خزينة منافسك [${{rival.name}}]! افتح الأبواب وطابق 3 عناصر لتحديد غنيمتك!`;

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
      basePrize = 750;
      label = '💎 إفلاس البنك الأسطوري (Mega Heist)!';
    }}

    const totalPrize = basePrize * state.multiplier;
    const stolenFromRival = Math.min(h.rival.money, totalPrize);
    h.rival.money -= stolenFromRival;
    h.attacker.money += totalPrize;
    h.attacker.netWorth += totalPrize;

    sfx.playFanfare();
    launchConfetti();

    document.getElementById('heistResultBanner').innerText = `مبروك! حققت ${{label}} ونلت ${{totalPrize}} ج.م (سُرقت ${{stolenFromRival}} ج.م من ${{h.rival.name}} مباشرة)!`;
    const collectBtn = document.getElementById('btnCollectHeist');
    collectBtn.style.display = 'inline-flex';
    collectBtn.onclick = () => {{
      closeModal('modalHeist');
      addLog(`🏦 سطا ${{h.attacker.name}} على خزينة ${{h.rival.name}} ونهب ${{totalPrize}} ج.م!`, 'gold');
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

  // 1v1 Landmark Shutdown Mini-Game
  function startShutdown(attacker) {{
    const rival = state.players[attacker.id === 0 ? 1 : 0];
    state.shutdownState = {{ attacker, rival }};

    document.getElementById('shutdownSubtext').innerText = `استهدف معالم منافسك [${{rival.name}}] بالمطرقة الكرتونية! هل يمتلك درعاً لصد الهجوم؟`;
    document.getElementById('targetLandmarkIcon').innerHTML = SVG_ASSETS.tile_cairo_tower;
    document.getElementById('targetLandmarkName').innerText = `برج القاهرة الخاص بـ ${{rival.name}}`;
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

    if (s.rival.shields > 0) {{
      s.rival.shields--;
      sfx.playShield();

      const dome = document.createElement('div');
      dome.className = 'shield-deflection-dome';
      box.appendChild(dome);

      const consolation = 100 * state.multiplier;
      s.attacker.money += consolation;
      s.attacker.netWorth += consolation;

      document.getElementById('shutdownResultText').innerHTML = `
        <span style="color: #38bdf8;">🛡️ تصدى درع ${{s.rival.name}} للهجوم! خسر درعاً ونلت ترضية: ${{consolation}} ج.م</span>
      `;
      addLog(`🛡️ درع ${{s.rival.name}} يصد هجوم ${{s.attacker.name}} بالمطرقة!`);
    }} else {{
      sfx.playSmash();
      box.style.animation = 'token-hop 0.5s';

      const demolishPrize = 400 * state.multiplier;
      s.attacker.money += demolishPrize;
      s.attacker.netWorth += demolishPrize;

      document.getElementById('shutdownResultText').innerHTML = `
        <span style="color: #ef4444;">💥 ضربة قاضية! تم تعطيل معالم ${{s.rival.name}} وربحت ${{demolishPrize}} ج.م!</span>
      `;
      addLog(`💥 ضرب ${{s.attacker.name}} معالم ${{s.rival.name}} ونال غنيمة ${{demolishPrize}} ج.م!`, 'red');
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

  // City Landmarks Construction View
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
        <div class="landmark-icon-badge" style="width: 60px; height: 60px; padding: 4px;">
          ${{landmarkSVGs[idx]}}
        </div>
        <div class="landmark-meta">
          <div style="font-size: 14px; font-weight: 800; color: #f8fafc;">${{lm.name}}</div>
          <div style="font-size: 11px; color: #94a3b8;">${{isMaxed ? 'مكتمل بالكامل! 👑' : nextStage.name}}</div>
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

  // Wheel of Fortune
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

  // Open Property Deed Modal with 3D Showcase
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
        <div style="width: 100%; height: 95px; display: flex; align-items: center; justify-content: center; background: #0b1120; padding: 6px;">
          <div style="width: 85px; height: 85px;">${{art3D}}</div>
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

  // Bankruptcy in 1v1
  function handleBankruptcy(bankruptPlayer, creditor) {{
    bankruptPlayer.isBankrupt = true;
    sfx.playBuzzer();
    addLog(`☠️ أعلن ${{bankruptPlayer.name}} إفلاسه! الفائز بالنزال هو ${{creditor.name}}!`, 'red');

    sfx.playFanfare();
    launchConfetti();
    alert(`👑 ألف مبروك! الفائز العظيم بنزال بنك الحظ 3D هو: ${{creditor.name}}! 🏆`);
  }}

  // Turn Cycle
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
    state.currentPlayerIdx = state.currentPlayerIdx === 0 ? 1 : 0;
    state.doublesCount = 0;
    updateUI();

    const curr = state.players[state.currentPlayerIdx];
    if (curr.isBot) {{
      setTimeout(() => {{
        rollDiceAction();
      }}, 1200);
    }}
  }}

  // Confetti FX
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

  function openModal(id) {{ document.getElementById(id).classList.add('active'); }}
  function closeModal(id) {{ document.getElementById(id).classList.remove('active'); }}

  function shuffleArray(arr) {{
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {{
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }}
    return a;
  }}

  // DOM Event Listeners
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
      if (confirm('هل تريد بدء نزال ثنائي جديد من البداية؟')) initGame();
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

# Save to destination
dest_path = "/bank_el_hazz/bank_el_hazz_monopoly_go.html"
with open(dest_path, "w", encoding="utf-8") as f:
    f.write(full_2p_html)

with open("/bank_el_hazz/index.html", "w", encoding="utf-8") as f:
    f.write(full_2p_html)

print("Saved complete 2-player 3D game to:", dest_path)
print("File size:", os.path.getsize(dest_path), "bytes")
