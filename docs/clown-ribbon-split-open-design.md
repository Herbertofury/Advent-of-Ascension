# Clown flag sight: paired split-open correction

Owner-directed revision, 22 October 2026. The focused first-person appearance is retained. The older broadside stretching transition is superseded and must not be treated as an approved mechanism.

## Correct motion

- Exactly three inline poles for the verified Clownimator, Clowno Pulse and Clownershot references.
- Each pole owns two separate cloth flag halves. A pair opens into its own aperture; cloth does not connect adjacent poles to make one enormous ring.
- Opening progresses along the three poles as a playful wave. Direction and timing are authoring parameters, not final native values.
- The three aperture planes face along the barrel. They are parallel to each other and perpendicular to the viewing/aim axis, not flat broadside diamonds facing a side camera.
- Poles and flags can rise or lower to align all three aperture centers on one sightline. Keep the bases in the front-to-back row, without sideways fan-out.
- From the player's eye, the three aligned openings appear as one clear focused sight. Keep the center and aim marker stable; flutter belongs outside the opening.
- On unfocus, each pair closes to its normal fluttering flag and every pole returns to its own original idle height. Attachment removal hides the whole attachment.
- Retain default-on and explicit-off persistence behavior. The existing serialized `converging` variant identifier is retained for compatibility; its intended motion is now paired split-open alignment, not stretching cloth between poles.

## Evidence and unfinished work

The prior first-person study is useful only for its focused appearance. Its lower side-transition panel and older gathering panels are obsolete. A corrected transition-art request returned no image; replacement artwork is still pending, not complete.

The authored pure Java component now supplies three independent aperture targets, two halves owned by each pole, vertical pole-tip adjustment, both selectable wave directions, hidden off-state and exact idle restoration. It deliberately supplies pose guides rather than a cloth mesh. At zero opening the renderer must use the authored fluttering flag shape, not collapse cloth vertices onto degenerate guide points.

Component validation passed 203 attachment-state assertions and 13,783 sampled pose assertions. These are not 13,986 independent gameplay tests. There is no installed Minecraft renderer, cloth solver, UI, network integration or native animation acceptance. Test AoA plus TaCZ together before claiming completion.
