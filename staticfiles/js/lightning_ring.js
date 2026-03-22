(() => {
  const RNG = (min, max) => Math.random() * (max - min) + min;

  const neonGreen = [
    "rgba(57, 255, 20, 0.95)",
  ];

  const drawLightningRing = (ctx, size) => {
    const center = size / 2;
    const lightningRadius = size * 0.485;

    ctx.clearRect(0, 0, size, size);

    // No center glow; keep the ring clean for the lightning effect.

    // No inner ring; keep only the lightning ring and outer glow

    // Lightning ring
    const boltCount = 8;
    for (let i = 0; i < boltCount; i++) {
      const startAngle = RNG(0, Math.PI * 2);
      const arcLen = RNG(0.7, 1.4);
      const segments = 12;
      const step = arcLen / segments;

      ctx.beginPath();
      for (let s = 0; s <= segments; s++) {
        const angle = startAngle + step * s;
      const jitter = RNG(-size * 0.03, size * 0.03);
        const radius = lightningRadius + jitter;
        const x = center + Math.cos(angle) * radius;
        const y = center + Math.sin(angle) * radius;
        if (s === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);

        if (Math.random() > 0.75) {
          const branchAngle = angle + RNG(-0.3, 0.3);
          const branchLen = RNG(size * 0.03, size * 0.06);
          ctx.lineTo(
            x + Math.cos(branchAngle) * branchLen,
            y + Math.sin(branchAngle) * branchLen
          );
          ctx.moveTo(x, y);
        }
      }
      const boltColor = neonGreen[i % neonGreen.length];
      ctx.strokeStyle = boltColor;
      ctx.lineWidth = RNG(size * 0.008, size * 0.016);
      ctx.shadowColor = boltColor;
      ctx.shadowBlur = size * 0.055;
      ctx.stroke();
    }

    ctx.shadowBlur = 0;
  };

  const setupRing = (canvas) => {
    const ctx = canvas.getContext("2d");
    const resize = () => {
      const rect = canvas.getBoundingClientRect();
      const ratio = window.devicePixelRatio || 1;
      canvas.width = rect.width * ratio;
      canvas.height = rect.height * ratio;
      ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
    };

    const render = () => {
      const size = Math.min(canvas.clientWidth, canvas.clientHeight);
      drawLightningRing(ctx, size);
    };

    resize();

    let raf;
    let lastFrame = 0;
    const loop = (ts) => {
      if (ts - lastFrame >= 260) { // ~3.85fps for much slower lightning flicker
        render();
        lastFrame = ts;
      }
      raf = requestAnimationFrame(loop);
    };
    loop();

    const observer = new ResizeObserver(() => {
      resize();
    });
    observer.observe(canvas);

    return () => {
      cancelAnimationFrame(raf);
      observer.disconnect();
    };
  };

  const init = () => {
    const activeRing = document.querySelector(".category-tile.is-active .story-ring");
    if (!activeRing) return;
    if (activeRing.querySelector(".lightning-ring-canvas")) return;

    const canvas = document.createElement("canvas");
    canvas.className = "lightning-ring-canvas";
    activeRing.appendChild(canvas);
    setupRing(canvas);
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
