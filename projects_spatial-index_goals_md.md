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

**Shipped:** 4 / 50
**Target:** 50 by December 31, 2025
**Missed:** ~2 (January–February)
**Remaining:** ~46

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

> Honest assessment as of scene_04.

| Skill | Level | Notes |
|---|---|---|
| Three.js / WebGL | Advanced− | Comfortable with shaders, particles, custom materials |
| WebXR / Quest 3 | Intermediate | Plane detection + hand tracking done across two projects |
| 3DGS / Gaussian Splats | Intermediate | SHARP pipeline working; followed existing repo closely |
| Python / ML | Beginner–Intermediate | Follows tutorials and existing repos |
| CV / Computer Vision | Not started | No project yet |
| LLMs / AI Integration | Intermediate | Gemini multimodal API fully integrated in Durée |
| GLSL / Shaders | Intermediate | Writing GPU color modes independently |
| Vercel Edge Functions | Intermediate | Rate-limited proxy built and deployed |
| DNS / Domain management | Intermediate+ | Subdomain CNAME setup done multiple times |

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
| 01 | SHARP — Monocular View Synthesis | 3DGS | Intermediate | Python / ML, 3DGS | [Demo](https://sharpview.spatial-index.xyz) · [Source](https://github.com/projectmehari/ml-sharp) |
| 02 | MARBLE — Spatial World Generation | World Models | Beginner | 3DGS | [World](https://marble.worldlabs.ai/world/4305a51d-e2f3-4127-a3b3-6a6c43c2b9fc) |
| 03 | DEPTHSHIFT — Depth Reprojection Hologram | WebXR / Quest 3 | Intermediate | Three.js, WebXR, GLSL, Particles | [Demo](https://depthshift.spatial-index.xyz) · [Source](https://github.com/projectmehari/depth-shift) |
| 04 | DURÉE — Video as Spatial Object | AI + Spatial | Advanced− | Three.js, WebCodecs, GLSL, Gemini API, Vercel Edge Functions | [Demo](https://duree.spatial-index.xyz) · [Source](https://github.com/projectmehari/spatial-index) |

---

## Backlog

> Ordered by recommended sequence. Earlier projects build skills needed for later ones.

### Beginner

| # | Scene | Theme | Skills Introduced | Depends On | Time Est. |
|---|---|---|---|---|---|
| 05 | SPLAT AUDIO | 3DGS | Three.js Web Audio API | scene_03 | 1–2 days |
| 06 | HAND TRAILS | WebXR | WebXR hand tracking (deeper) | scene_03 | 2–3 days |
| 07 | TIMELAPSE SPLAT | 3DGS | 3DGS multi-capture workflow | scene_01 | 2–3 days |
| 08 | ROOM ECHO | WebXR | WebXR geometry + spatial audio | scene_03 | 2–3 days |
| 09 | MONTREAL SERIES | World Models | None new | scene_02 | 1–2 days |

### Gallery Infrastructure

| # | Scene | Theme | Skills Introduced | Depends On | Time Est. |
|---|---|---|---|---|---|
| 09.5 | MÉTRO MÉMOIRE — Gallery Shell | 3DGS + World Models | Interactive SVG map, GaussianSplats3D embed | scene_09 | 3–5 days |
| 09.6 | MÉTRO MÉMOIRE — Submissions | 3DGS + World Models | Supabase free tier, URL-based splat linking | scene_09.5 | 3–5 days |
| 09.7 | MÉTRO MÉMOIRE — Voting | 3DGS + World Models | Supabase votes table, community ranking UI | scene_09.6 | 4–6 days |

### Intermediate

| # | Scene | Theme | Skills Introduced | Depends On | Time Est. |
|---|---|---|---|---|---|
| 10 | CAPTIONER | AI + Spatial | LLM API + Quest 3 passthrough | scene_04, scene_03 | 4–5 days |
| 11 | SURFACE TYPES | WebXR / AI | CV API (first time) | scene_04 | 4–5 days |
| 12 | SHARP → DEPTHSHIFT | 3DGS | 3DGS pipeline chaining (.ply → particles) | scene_01, scene_03 | 3–5 days |
| 13 | SPLAT PORTAL | 3DGS | Three.js scene transitions + stencil buffer | scene_03 | 4–6 days |
| 14 | SCENE DIFF | AI + Spatial | CV two-image comparison | scene_11 | 3–5 days |
| 15 | OBJECT MOOD | AI + Spatial | LLMs + CV combined | scene_10, scene_11 | 4–6 days |
| 16 | INTERIOR → EXTERIOR | World Models | 3DGS multi-world linking | scene_09 | 4–6 days |
| 17 | WORLD REMIX | World Models | Recursive 3DGS generation | scene_16 | 4–6 days |

### Advanced

| # | Scene | Theme | Skills Introduced | Depends On | Time Est. |
|---|---|---|---|---|---|
| 18 | PROXY LITE | AI + Spatial | Gaze-based WebXR selection + LLM labeling | scene_10, scene_06 | 1 week |
| 19 | SPATIAL MEMORY | AI + Spatial | Stateful LLM (conversation history) | scene_10, scene_18 | 1 week |
| 20 | SCENE GRAPH | AI + Spatial | CV + LLM knowledge graph | scene_14, scene_15 | 1–2 weeks |
| 21 | LIVING SPLAT | 3DGS | 3DGS from video input (feeds from Durée) | scene_12 | 1 week |
| 22 | SPATIAL JOURNAL | 3DGS | Python accumulation pipeline (feeds from Durée) | scene_07, scene_12 | 1–2 weeks |
| 23 | SPLAT BRUSH | 3DGS / WebXR | Unity / C# (first Unity project) | scene_03 | 1–2 weeks |

### Research-grade

| # | Scene | Theme | Skills Introduced | Depends On | Time Est. |
|---|---|---|---|---|---|
| 40–45 | REALITY PROXY PORT | WebXR / AI | Unity / C# deep, CV, LLMs in native build | scene_18, scene_20, scene_23 | 6 weeks |
| 46 | GENERATIVE CITY | World Models | 3DGS stitching, Python pipeline | scene_09, scene_17 | 3–4 weeks |
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
| Intelligence | CV models, LLMs, Gemini multimodal API |
| Output | Browser demos, HuggingFace Spaces, GitHub |

---

## MÉTRO MÉMOIRE — Project Scope

> Collaborative gallery where each Montreal metro station gets one community-chosen 3DGS scene. 68 slots total — one per STM station.

### Concept

Each station on the Montreal metro map is a slot. Contributors capture a moment at that station, process it into a `.splat` or `.ply`, host it themselves, and submit the URL. You curate and approve. One canonical splat per station, chosen by the community.

### Architecture (Zero-Cost)

| Layer | Tool | Cost |
|---|---|---|
| Site hosting | Cloudflare Pages or GitHub Pages | Free |
| Splat files (your own) | HuggingFace Spaces (existing) | Free |
| Splat files (contributors) | Self-hosted by contributor, URL submitted | Free |
| Database + submissions | Supabase free tier (500MB) | Free |
| Splat rendering | mkkellogg/GaussianSplats3D in-browser | Free |
| Domain | spatial-index.xyz/metro | Free (owned) |

---

## Inspiration

- [Kat / The Poet Engineer](https://www.patreon.com/thepoetengineer) · creative developer at the intersection of poetry, code, and spatial thinking
- [Reality Proxy — UIST 2025](https://dl.acm.org/doi/10.1145/3746059.3747709) · fluid MR interaction via abstract proxy representations
- [World Labs Marble](https://www.worldlabs.ai) · multi-image to navigable 3D world
- [Apple ML SHARP](https://huggingface.co/spaces/verymehari/SharpView) · single image to 3DGS

---

*Updated: March 9, 2026 · Montreal, QC*
*Scene 04 — Durée shipped. 4/50 complete.*
