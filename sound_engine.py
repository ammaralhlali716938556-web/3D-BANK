SOUND_JS = """
class WebAudioSFX {
  constructor() {
    this.ctx = null;
    this.muted = false;
  }

  ensureContext() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) {
        this.ctx = new AudioCtx();
      }
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  toggleMute() {
    this.muted = !this.muted;
    return this.muted;
  }

  playDiceRoll() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    // Series of 7 rhythmic tumbling clicks
    for (let i = 0; i < 7; i++) {
      const t = now + i * 0.08 + Math.random() * 0.02;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(220 + Math.random() * 260, t);
      osc.frequency.exponentialRampToValueAtTime(70 + Math.random() * 40, t + 0.06);

      gain.gain.setValueAtTime(0.3, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.06);

      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(t);
      osc.stop(t + 0.07);
    }
  }

  playChaChing() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    
    // Register clink
    const osc1 = this.ctx.createOscillator();
    const gain1 = this.ctx.createGain();
    osc1.type = 'sine';
    osc1.frequency.setValueAtTime(1400, now);
    osc1.frequency.exponentialRampToValueAtTime(2800, now + 0.08);
    gain1.gain.setValueAtTime(0.25, now);
    gain1.gain.exponentialRampToValueAtTime(0.001, now + 0.12);
    osc1.connect(gain1);
    gain1.connect(this.ctx.destination);
    osc1.start(now);
    osc1.stop(now + 0.12);

    // High cash bells
    [2093, 2637, 3135].forEach((freq, idx) => {
      const t = now + 0.08 + idx * 0.07;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, t);
      gain.gain.setValueAtTime(0.3, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.35);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(t);
      osc.stop(t + 0.36);
    });
  }

  playCoin() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    [1046, 1318, 1567, 2093].forEach((f, i) => {
      const t = now + i * 0.05;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(f, t);
      gain.gain.setValueAtTime(0.2, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.25);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(t);
      osc.stop(t + 0.26);
    });
  }

  playPawnHop() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(320, now);
    osc.frequency.exponentialRampToValueAtTime(640, now + 0.08);
    gain.gain.setValueAtTime(0.18, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.12);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + 0.12);
  }


  playSmash() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    // Bass boom
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(140, now);
    osc.frequency.exponentialRampToValueAtTime(30, now + 0.4);
    gain.gain.setValueAtTime(0.45, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.45);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + 0.46);

    // Crackle noise burst
    const bufferSize = this.ctx.sampleRate * 0.2;
    const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
      data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (bufferSize * 0.25));
    }
    const noise = this.ctx.createBufferSource();
    noise.buffer = buffer;
    const nGain = this.ctx.createGain();
    nGain.gain.setValueAtTime(0.3, now);
    nGain.gain.exponentialRampToValueAtTime(0.001, now + 0.2);
    noise.connect(nGain);
    nGain.connect(this.ctx.destination);
    noise.start(now);
  }

  playShield() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(450, now);
    osc.frequency.exponentialRampToValueAtTime(1300, now + 0.18);
    osc.frequency.exponentialRampToValueAtTime(800, now + 0.35);

    gain.gain.setValueAtTime(0.35, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.4);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + 0.41);
  }

  playVaultOpen() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    // Metal latch click
    const osc1 = this.ctx.createOscillator();
    const g1 = this.ctx.createGain();
    osc1.type = 'triangle';
    osc1.frequency.setValueAtTime(800, now);
    osc1.frequency.exponentialRampToValueAtTime(200, now + 0.05);
    g1.gain.setValueAtTime(0.3, now);
    g1.gain.exponentialRampToValueAtTime(0.001, now + 0.06);
    osc1.connect(g1);
    g1.connect(this.ctx.destination);
    osc1.start(now);
    osc1.stop(now + 0.06);

    // Chime
    const osc2 = this.ctx.createOscillator();
    const g2 = this.ctx.createGain();
    osc2.type = 'sine';
    osc2.frequency.setValueAtTime(1200, now + 0.05);
    g2.gain.setValueAtTime(0.25, now + 0.05);
    g2.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
    osc2.connect(g2);
    g2.connect(this.ctx.destination);
    osc2.start(now + 0.05);
    osc2.stop(now + 0.36);
  }

  playChanceMystery() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    // Sparkling magical mystery arpeggio
    const notes = [587.33, 739.99, 880.00, 1174.66, 1479.98];
    notes.forEach((freq, idx) => {
      const t = now + idx * 0.07;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, t);
      gain.gain.setValueAtTime(0.28, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.28);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(t);
      osc.stop(t + 0.29);
    });
  }

  playTaxStamp() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    // Heavy bureaucratic stamp impact thud
    const oscStamp = this.ctx.createOscillator();
    const gainStamp = this.ctx.createGain();
    oscStamp.type = "triangle";
    oscStamp.frequency.setValueAtTime(160, now);
    oscStamp.frequency.exponentialRampToValueAtTime(45, now + 0.12);
    gainStamp.gain.setValueAtTime(0.4, now);
    gainStamp.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
    oscStamp.connect(gainStamp);
    gainStamp.connect(this.ctx.destination);
    oscStamp.start(now);
    oscStamp.stop(now + 0.16);

    // Cash register bell clink
    [1760, 2637].forEach((freq, idx) => {
      const t = now + 0.08 + idx * 0.06;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, t);
      gain.gain.setValueAtTime(0.22, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.3);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(t);
      osc.stop(t + 0.31);
    });
  }

  playVisitJail() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    [523.25, 659.25].forEach((freq, idx) => {
      const t = now + idx * 0.1;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, t);
      gain.gain.setValueAtTime(0.2, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.25);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(t);
      osc.stop(t + 0.26);
    });
  }

  playJail() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    // Heavy cell door slam
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = "sawtooth";
    osc.frequency.setValueAtTime(130, now);
    osc.frequency.exponentialRampToValueAtTime(35, now + 0.4);
    gain.gain.setValueAtTime(0.5, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.45);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + 0.46);

    // Iron bars clang metallic resonance
    [320, 480, 640].forEach((freq, idx) => {
      const oscBar = this.ctx.createOscillator();
      const gainBar = this.ctx.createGain();
      oscBar.type = "triangle";
      oscBar.frequency.setValueAtTime(freq, now + 0.04);
      oscBar.frequency.exponentialRampToValueAtTime(freq * 0.9, now + 0.35);
      gainBar.gain.setValueAtTime(0.25 / (idx + 1), now + 0.04);
      gainBar.gain.exponentialRampToValueAtTime(0.001, now + 0.38);
      oscBar.connect(gainBar);
      gainBar.connect(this.ctx.destination);
      oscBar.start(now + 0.04);
      oscBar.stop(now + 0.39);
    });
  }

  playFanfare() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    const notes = [523.25, 659.25, 783.99, 1046.50];
    notes.forEach((freq, idx) => {
      const t = now + idx * 0.12;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(freq, t);
      gain.gain.setValueAtTime(0.3, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.35);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(t);
      osc.stop(t + 0.36);
    });
  }

  playWheelTick() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(1200, now);
    gain.gain.setValueAtTime(0.15, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.03);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + 0.04);
  }

  playBuzzer() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    [180, 160].forEach((freq, i) => {
      const t = now + i * 0.15;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(freq, t);
      gain.gain.setValueAtTime(0.2, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.12);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(t);
      osc.stop(t + 0.13);
    });
  }

  playPoliceSiren(duration = 2.0) {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sawtooth';

    const cycles = Math.max(2, Math.floor(duration * 2.5));
    const stepT = duration / (cycles * 2);
    for (let i = 0; i < cycles * 2; i++) {
      const t = now + i * stepT;
      const f = (i % 2 === 0) ? 960 : 620;
      osc.frequency.linearRampToValueAtTime(f, t + stepT);
    }

    gain.gain.setValueAtTime(0.01, now);
    gain.gain.linearRampToValueAtTime(0.18, now + 0.08);
    gain.gain.setValueAtTime(0.18, now + duration - 0.2);
    gain.gain.linearRampToValueAtTime(0.001, now + duration);

    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + duration);
  }

  playJailGateSlam() {
    if (this.muted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;

    // Heavy iron gate thud
    const osc1 = this.ctx.createOscillator();
    const gain1 = this.ctx.createGain();
    osc1.type = 'triangle';
    osc1.frequency.setValueAtTime(110, now);
    osc1.frequency.exponentialRampToValueAtTime(32, now + 0.35);
    gain1.gain.setValueAtTime(0.45, now);
    gain1.gain.exponentialRampToValueAtTime(0.001, now + 0.4);
    osc1.connect(gain1);
    gain1.connect(this.ctx.destination);
    osc1.start(now);
    osc1.stop(now + 0.42);

    // Metal bars ring
    [420, 880, 1320].forEach((freq, idx) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'square';
      osc.frequency.setValueAtTime(freq, now);
      gain.gain.setValueAtTime(0.07 / (idx + 1), now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.45);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now);
      osc.stop(now + 0.46);
    });

    // Padlock lock clack
    const clickOsc = this.ctx.createOscillator();
    const clickGain = this.ctx.createGain();
    clickOsc.type = 'sawtooth';
    clickOsc.frequency.setValueAtTime(1800, now + 0.16);
    clickOsc.frequency.exponentialRampToValueAtTime(260, now + 0.26);
    clickGain.gain.setValueAtTime(0.28, now + 0.16);
    clickGain.gain.exponentialRampToValueAtTime(0.001, now + 0.32);
    clickOsc.connect(clickGain);
    clickGain.connect(this.ctx.destination);
    clickOsc.start(now + 0.16);
    clickOsc.stop(now + 0.33);
  }

}
"""
print("sound_engine.py ready!")
