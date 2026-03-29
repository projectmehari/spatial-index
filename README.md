# Spatial Index
A scroll-driven portfolio navigator for spatial computing experiments. Each project is presented as a full-screen scene with staggered reveals, designed for browsing depth-based and WebXR work.

## Projects

**06 — Memoria**
A memory palace for music. Photogrammetric scans as spatial containers, with tracks, images, and notes pinned as positional nodes in 3D space. A mix is a temporal fragment — a moment of curation that captures a mood, a context, a way of listening that will never quite repeat. Memoria treats that fragment as something worth preserving spatially. Closer to an archive than a queue. Closer to a walk than a stream. Built with React Three Fiber, Three.js, and Bun. Supports .ply and .glb scenes with community submissions.

[memoria.spatial-index.xyz](https://memoria.spatial-index.xyz)

**05 — ATLAS**
3D semantic search engine for live performances. Four Boiler Room / Cercle sets decomposed into audio, video frames, video native, and text molecules — 1,788 atoms embedded with Gemini Embedding 2 at 768 dimensions, rendered as an orbitable 3D globe. Query a concept and cosine similarity lights up matches across all 16 molecules. An assemblage engine cuts a ~60s sequence from the highest-matched clips, edited by meaning, not by time.

[atlas.spatial-index.xyz](https://atlas.spatial-index.xyz)

**04 — Durée**
All frames of a video rendered simultaneously as stacked semi-transparent planes — treating time as a navigable spatial axis. Orbit the full timeline as a physical object. Gemini AI search lets you query frames by natural language. Built with Three.js, WebCodecs, and GLSL shaders.

[duree.spatial-index.xyz](https://duree.spatial-index.xyz)

**03 — DepthShift**
Depth-reprojected particle viewer and WebXR spatial hologram. Takes a flat image or video + depth map and extrudes it into a 3D particle field. The AR mode anchors the depth instance to a real-world surface via plane detection and hand tracking on Quest 3.

[depthshift.spatial-index.xyz](https://depthshift.spatial-index.xyz)

**02 — Marble**
Reference photos of David Chipperfield's brutalist SSENSE flagship reconstructed into a navigable 3D world via World Labs' Marble model. Outputs .spz at 100k–full resolution with collider meshes, explorable in-browser.

**01 — SHARP**
A single photograph enters a feedforward neural network and exits as a full 3D Gaussian Splat in under a second. No multi-view capture. No photogrammetry pipeline. Pure inference.

[sharpview.spatial-index.xyz](https://sharpview.spatial-index.xyz)

## Stack
- Vanilla HTML/CSS/JS
- Scroll-based scene transitions
- Hosted on Vercel

## Live
[spatial-index.xyz](https://spatial-index.xyz)
