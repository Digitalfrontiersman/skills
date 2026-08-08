# Prompt system

## Contents

- Prompt compiler
- Image and asset prompts
- Single-shot video prompts
- Multi-shot prompts
- Dialogue and audio
- Negative constraints
- Prompt debugging

## Prompt compiler

Compile from decisions, not vibes. Use this order, removing unsupported or irrelevant fields:

1. **Format header** — number of shots, total duration, aspect ratio, resolution intent.
2. **Narrative job** — what the viewer must understand or feel.
3. **Reference bindings** — exact role of each character, location, product, style, video, or audio input.
4. **Visible scene** — subject, location, time, weather, production design.
5. **Blocking and action** — start state, action order, performance beats, end state.
6. **Camera** — framing, angle, height, lens intent, movement path, speed, stabilization.
7. **Light and color** — source, direction, quality, contrast, temperature, palette, exposure behavior.
8. **Material and physics** — mass, contact, inertia, reflections, fabric, hair, particles, environmental response.
9. **Performance** — eyelines, subtext, facial behavior, pauses, gestures, breath.
10. **Sound** — dialogue, ambience, effects, music relationship, or explicit silence.
11. **Finish** — capture texture, grain, halation, grade, frame rate/shutter intent where supported.
12. **Constraints** — forbidden drift, unwanted text/logos, cuts, fades, morphs, anatomy errors, or style violations.

Use plain, visual, chronological language. Avoid conflicting lenses, movements, light sources, or aesthetics. Do not add technical terms that lack a storytelling purpose.

## Image and asset prompts

### Character sheet

Specify identity source, full-body and portrait views, neutral pose, consistent wardrobe, scale/alignment, lighting, background, and immutable traits. Ask for clear silhouette and useful angles rather than cinematic drama.

### Location sheet

Specify plan logic, front/reverse/left/right perspectives, key landmarks, entrances, practical light sources, material palette, time/weather, and detail views. Keep architecture and light direction consistent.

### Product truth sheet

Specify front/back/side/top, dimensions and geometry, label/logo placement, color values, materials, closures, ports/buttons, reflections, and scale reference. Separate truth views from the later beauty shot.

### Hero frame

Use:

`[shot size and angle] of [subject/action] in [specific environment]. [Composition/blocking]. [Lens and depth intent]. [Key light source and direction], [fill/contrast], [palette]. [Texture/capture behavior]. [Continuity anchors]. [Constraints].`

## Single-shot video prompt

Use:

`[Duration/aspect]. Begin on [precise start state]. [Subject] performs [chronological action] with [performance]. Camera [framing/height] [specific movement path and speed] to reveal/emphasize [story purpose]. [Environment] reacts with [physical detail]. Lighting remains [source/direction/behavior]. End on [precise edit-ready state]. Audio: [dialogue/SFX/ambience]. Preserve [references/continuity]. Avoid [constraints].`

One shot should usually contain one primary subject action and one primary camera action. If the prompt needs several “then” clauses, consider separate shots.

## Multi-shot prompt

State structure first:

`[N] shots / [total duration] / [aspect ratio]. Hard cuts unless specified.`

Then write numbered blocks:

`Shot 1 — [time range, framing, visible action, camera, audio, endpoint].`

Each shot needs a distinct narrative job and must preserve named references. Give the sequence an escalation or reveal arc. Ensure the described actions fit the allotted seconds.

## Dialogue and audio

- Attribute every line to a named character.
- Specify who is visible, who is off-screen, and the desired delivery/subtext.
- Keep spoken word count realistic for duration.
- Use punctuation for pauses sparingly; describe meaningful beats directly.
- Define ambient bed and important synchronous effects.
- If speech is forbidden, state `No dialogue; no generated speech` when the model may otherwise infer it.
- Generate temporary audio only when it helps timing. Add licensed/final music during post unless the production route explicitly requires native music.

## Negative constraints

Use a small, prioritized constraint set. Prefer observable failures:

- preserve exact product geometry and label orientation
- no identity or wardrobe change
- no extra fingers/limbs/objects
- no camera cut, fade, or morph
- no added text, logos, subtitles, or watermarks
- no plastic skin, game-engine rendering, or synthetic glow when photorealism is required

Do not append a giant generic negative list. It dilutes the shot's actual direction.

## Prompt debugging

When a result fails, identify the failure class before rewriting:

- **Wrong concept:** revise treatment or reference, not adjectives.
- **Weak composition:** rebuild the hero frame.
- **Identity/product drift:** strengthen or replace the reference; reduce simultaneous action.
- **Ignored camera:** use one standard move with path, subject relationship, and speed.
- **Chaotic action:** shorten the beat, split the shot, or define start/action/end.
- **Plastic look:** improve material/light/capture cues and remove contradictory polish terms.
- **Bad dialogue:** shorten lines, define speaker and delivery, or separate coverage.
- **Unusable edit:** specify handles, endpoint, screen direction, and transition purpose.

Change one major variable, keep a version note, and compare against the acceptance criteria.
