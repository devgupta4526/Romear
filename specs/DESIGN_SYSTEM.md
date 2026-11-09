# ROMEAR DESIGN SYSTEM / SCREEN DELIVERY RULES

## Visual DNA
- Brand: ROMEAR, city-first social network, real people & places, warm editorial rather than synthetic purple tech aesthetic.
- Colors: forest `#1F503A`, cream `#F7F4F1`, terracotta `#E07A5F`, sand `#E8DCCE`, olive `#8A9872`, charcoal `#282B2B`; generate accessible dark palette by contrast testing (not purple). Error/danger/success via accessible semantic palette.
- Typography: UI body (Inter or Android-safe equivalent) 14–16sp, metadata 12–13sp, headers 20–28sp, restrained editorial serif for product/brand display only; respect system font scaling.
- Geometry: corner radii 8, 12, 16, 24dp; spacing 4, 8, 12, 16, 24, 32dp; touch targets >=48dp; clear action hierarchy. Use subtle shadows/elevation, avoid nested cards and excessive decorative gradients.
- Navigation: XML + Fragment + bottom navigation Home/Explore/Create/Plans/Inbox; profile from top avatar. Create opens bottom sheet, not a dead-end tab. Mini tabs for each major surface; hide bottom nav on immersive chat, details, full-screen media, booking, checkout.
- Content: authentic, licensed local photos; no stolen brand assets; empty state illustration should be subtle and useful. Do not imply an inactive club is partnered, or a place/bookable slot is real without backend data.
- Android components: reusable `ProfileAvatarView`, `MediaPostView`, `PoolCardView`, `EventCardView`, `VenueCardView`, `ClubCardView`, `EmptyStateView`, `FailureStateView`, `VerifiedBadge` bound to server fields, `StatusChip`, `BottomActionBar` in XML/resources. All text from strings resources; drawables/vector XML instead of huge raster UI screenshots.
- All screens: accessibility/TalkBack/RTL where feasible, dynamic typography, offline/retry, keyboard resize, skeleton vs progress appropriately, state restoration, image loading/failed images, deep link/back behavior, and graceful permission denial.

## Reference boards
See `design_reference/` for broad visual direction: design-system, onboarding, social content, explore, events/bookings, Passport, chat/monetization, business tools, Pools. They are *not* pixel-perfect sources of truth (some AI board text/counts are illustrative). Implement the experience, not screenshots as bitmaps.

## Preview and review
Build one representative screen at a time and capture Android emulator screenshots with real device rendering. Compare spacing, hierarchy, cropping, color, touch target, legibility, system bars, large font size, empty states and loading states. Do not claim a UI is polished without reviewing real running layouts.
