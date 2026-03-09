# Spatial Index — 2025 Goals

> 50 project demos across the full spatial pipeline.  
> capture · reconstruction · synthesis · navigation · interaction

---

## Mission

Ship one spatial experiment per week through end of 2025.  
Each project advances the stack: 3DGS, WebXR, AI + spatial, and world models.  
Projects are sequenced to **gradually increase technical difficulty** and build new skills each month.

---

## Progress

**Shipped:** 3 / 50  
**Target:** 50 by December 31, 2025  
**Missed:** ~2 (January–February)  
**Remaining:** ~47

---

## Difficulty Levels

| Level | Description | Typical Duration |
|---|---|---|
| Beginner | Uses familiar tools, minimal new APIs, ships fast | 1–3 days |
| Intermediate | One new skill or API introduced, some debugging expected | 3–7 days |
| Advanced | Multiple new systems, integration work, non-trivial debugging | 1–2 weeks |
| Research-grade | Reproduces or extends academic work, deep domain knowledge required | 2–4+ weeks |

---

## Skill Tracker

> Honest assessment as of scene_03. Used to calibrate project difficulty and sequencing.

| Skill | Level | Notes |
|---|---|---|
| Three.js / WebGL | Intermediate | Comfortable with shaders + particles; adapts from tutorials rather than writing from scratch |
| WebXR / Quest 3 | Beginner–Intermediate | Plane detection done; hand tracking still being figured out |
| 3DGS / Gaussian Splats | Intermediate | SHARP pipeline working; followed existing repo closely |
| Python / ML | Beginner–Intermediate | Follows tutorials and existing repos; not building from scratch |
| CV / Computer Vision | Not started | No project yet |
| LLMs / AI Integration | Not started | Never called an external API from JS or Python |
| Unity / C# | Not started | No experience yet |
| GLSL / Shaders | Beginner | Adapts examples; not authoring independently |

**Key implication:** Calling an external API for the first time is itself a milestone. LLM/CV projects need a dedicated warmup scene before anything depends on them.

---

## Scoping Criteria

Use this checklist when evaluating a new project idea:

**Fit**
- [ ] Does it advance at least one theme? (3DGS / WebXR / AI+Spatial / World Models)
- [ ] Does it build on a previously shipped scene or skill?
- [ ] Does it introduce at most 1–2 new skills?

**Difficulty**
- [ ] What is the difficulty level?
- [ ] What skills does it require that you don't have yet?
- [ ] What does it depend on?

**Scope**
- [ ] Can it ship as a demo in the target timeframe?
- [ ] Is there a simpler version that could ship faster?
- [ ] What is the output format? (browser demo / HuggingFace / Quest build / GitHub)

---

## Themes

| Theme | Focus |
|---|---|
| 3DGS / Gaussian Splats | Capture, reconstruction, and creative manipulation of splat scenes |
| WebXR / Quest 3 | Real-world AR anchoring, hand tracking, passthrough interaction |
| AI + Spatial | CV + LLMs applied to scene understanding and object semantics |
| World Models | Generative 3D worlds from images, navigable in-browser and in-headset |

---

## Shipped

| # | Scene | Theme | Difficulty | Skills Used | Links |
|---|---|---|---|---|---|
| 01 | SHARP — Monocular View Synthesis | 3DGS | Intermediate | Python / ML, 3DGS | [Demo](https://huggingface.co/spaces/verymehari/SharpView) · [Source](https://github.com/projectmehari/ml-sharp) |
| 02 | MARBLE — Spatial World Generation | World Models | Beginner | 3DGS | [World](https://marble.worldlabs.ai/world/4305a51d-e2f3-4127-a3b3-6a6c43c2b9fc) |
| 03 | DEPTHSHIFT — Depth Reprojection Hologram | WebXR / Quest 3 | Intermediate | Three.js / WebGL, WebXR / Quest 3, 3DGS | [Demo](https://depthshift.spatial-index.xyz) · [Source](https://github.com/projectmehari/depth-shift) |

---

## Backlog

> Ordered by recommended sequence. Earlier projects build skills needed for later ones.

### Beginner

| # | Scene | Theme | Skills Introduced | Depends On | Time Est. |
|---|---|---|---|---|---|
| 04 | SPLAT AUDIO | 3DGS | Three.js Web Audio API | scene_03 | 1–2 days |
| 05 | HAND TRAILS | WebXR | WebXR hand tracking (deeper) | scene_03 | 2–3 days |
| 06 | TIMELAPSE SPLAT | 3DGS | 3DGS multi-capture workflow | scene_01 | 2–3 days |
| 07 | ROOM ECHO | WebXR | WebXR geometry + spatial audio | scene_03 | 2–3 days |
| 08 | MONTREAL SERIES | World Models | None new | scene_02 | 1–2 days |

### Intermediate

| # | Scene | Theme | Skills Introduced | Depends On | Time Est. |
|---|---|---|---|---|---|
| 09 | FIRST API CALL | AI + Spatial | LLM API from JS (first time) — describe a hardcoded image | None | 2–3 days |
| 10 | CAPTIONER | AI + Spatial | LLM API + Quest 3 passthrough | scene_09, scene_03 | 4–5 days |
| 11 | SURFACE TYPES | WebXR / AI | CV API (first time) — classify surfaces | scene_09 | 4–5 days |
| 12 | SHARP → DEPTHSHIFT | 3DGS | 3DGS pipeline chaining (.ply → particles) | scene_01, scene_03 | 3–5 days |
| 13 | SPLAT PORTAL | 3DGS | Three.js scene transitions + stencil buffer | scene_03 | 4–6 days |
| 14 | SCENE DIFF | AI + Spatial | CV two-image comparison | scene_11 | 3–5 days |
| 15 | OBJECT MOOD | AI + Spatial | LLMs + CV combined | scene_10, scene_11 | 4–6 days |
| 16 | INTERIOR → EXTERIOR | World Models | 3DGS multi-world linking | scene_08 | 4–6 days |
| 17 | WORLD REMIX | World Models | Recursive 3DGS generation | scene_16 | 4–6 days |

### Advanced

| # | Scene | Theme | Skills Introduced | Depends On | Time Est. |
|---|---|---|---|---|---|
| 18 | PROXY LITE | AI + Spatial | Gaze-based WebXR selection + LLM labeling | scene_10, scene_05 | 1 week |
| 19 | SPATIAL MEMORY | AI + Spatial | Stateful LLM (conversation history) | scene_10, scene_18 | 1 week |
| 20 | SCENE GRAPH | AI + Spatial | CV + LLM knowledge graph | scene_14, scene_15 | 1–2 weeks |
| 21 | LIVING SPLAT | 3DGS | 3DGS from video input | scene_12 | 1 week |
| 22 | SPATIAL JOURNAL | 3DGS | Python accumulation pipeline | scene_06, scene_12 | 1–2 weeks |
| 23 | SPLAT BRUSH | 3DGS / WebXR | Unity / C# (first Unity project) | scene_03 | 1–2 weeks |

### Research-grade

| # | Scene | Theme | Skills Introduced | Depends On | Time Est. |
|---|---|---|---|---|---|
| 40–45 | REALITY PROXY PORT | WebXR / AI | Unity / C# deep, CV, LLMs in native build | scene_18, scene_20, scene_23 | 6 weeks (milestones) |
| 46 | GENERATIVE CITY | World Models | 3DGS stitching, Python pipeline | scene_08, scene_17 | 3–4 weeks |
| 47 | SEMANTIC NAVIGATOR | AI + Spatial | Full stack integration | scene_20, scene_40 | 3–4 weeks |

---

## Weekly Cadence

| Week Type | Focus |
|---|---|
| Week A | Quick WebXR / Quest demo — ship fast, stay sharp on hardware |
| Week B | 3DGS experiment — deepen splat expertise |
| Week C | AI + spatial integration — push the intelligence layer |
| Week D | World model or ambitious swing — one bigger project per month |

---

## Stack

| Layer | Tools |
|---|---|
| Capture | iPhone, Apple ML SHARP, multi-image photogrammetry |
| Reconstruction | 3DGS, .ply, World Labs Marble (.spz) |
| Rendering | Three.js, WebXR, GLSL, Particles |
| Interaction | Quest 3, hand tracking, plane detection, gaze + pinch |
| Intelligence | CV models, LLMs, semantic scene graphs |
| Output | Browser demos, HuggingFace Spaces, GitHub |

---

## Inspiration

- [Kat / The Poet Engineer](https://www.patreon.com/thepoetengineer) · *"interfacing with the future"* — creative developer at the intersection of poetry, code, and spatial thinking
- [Reality Proxy — UIST 2025](https://dl.acm.org/doi/10.1145/3746059.3747709) · fluid MR interaction via abstract proxy representations
- [World Labs Marble](https://www.worldlabs.ai) · multi-image to navigable 3D world
- [Apple ML SHARP](https://huggingface.co/spaces/verymehari/SharpView) · single image to 3DGS

---

## How to Scope a New Idea
```
## Idea: [NAME]

**One line:** What does it do?
**Theme:** 3DGS / WebXR / AI+Spatial / World Models
**Difficulty:** Beginner / Intermediate / Advanced / Research-grade
**Skills required:** List all
**New skills (ones I don't have yet):** List new ones only
**Depends on:** Prior scenes or external tools needed
**Time estimate:** X days / weeks
**Output format:** Browser demo / HuggingFace / Quest build / GitHub
**Simpler version:** Could this ship as a smaller scene first?
**Verdict:** Add to backlog / needs more scoping / too early (missing dependencies)
```

---

*Updated: March 2025 · Montreal, QC*
