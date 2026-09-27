# SHOAL images, icons, and page metadata

One reef. Every screen.

This presentation kit gives the README, share image, and project icons a common visual identity: deep teal water, sunlit coral, and fish swimming together. It supports the documentation project. It does not replace Open WebUI's identity or configure a reef.

## What is ready

| Surface | Asset | Status |
|---|---|---|
| README hero | [Social preview](../assets/brand/social-preview.jpg) | Referenced by the README |
| Website and repository share image | Same JPEG, 1774 × 887, under 1 MB | Prepared; not activated in GitHub settings or a hosted page |
| Scalable project mark | [icon.svg](../assets/brand/icon.svg) | Three fish on an opaque teal background |
| Browser tab | [favicon.ico](../assets/brand/favicon.ico), [16 px PNG](../assets/brand/favicon-16.png), [32 px PNG](../assets/brand/favicon-32.png) | Prepared; ICO contains 16, 32, 48, and 64 px sizes |
| Apple home-screen bookmark | [180 px touch icon](../assets/brand/apple-touch-icon.png) | Prepared; opaque square artwork |
| Other launcher uses | [192 px PNG](../assets/brand/icon-192.png), [512 px PNG](../assets/brand/icon-512.png) | Prepared; ordinary icons, not maskable assets |
| Safari pinned tab | [safari-pinned-tab.svg](../assets/brand/safari-pinned-tab.svg) | Prepared; black vector shapes on transparency |
| Hosted-page metadata | Example below | Template only; replace the example origin before publishing |

**Verified on 2026-09-27:** GitHub reported this repository as private, with no homepage and no Pages site. The former `https://overkillhill.com/projects/shoal/` link returned HTTP 404 and was removed from the README. No replacement public destination is assumed here.

## Where each setting belongs

**GitHub README:** Markdown embeds the hero and links to the guides and assets. HTML `<head>` tags pasted into a README do not configure the GitHub page's favicon or social metadata.

**GitHub repository link preview:** the image is a separate repository setting. GitHub's [social-preview instructions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview) describe the upload and private-repository restrictions. They recommend a 2:1 image under 1 MB. The supplied JPEG meets those size and aspect-ratio requirements. Its presence in Git alone does not select it as the repository preview. Do not change repository visibility to activate a preview.

**Hosted project page:** its HTML head controls favicons, pinned-tab art, and social cards. Publish the assets alongside that page and verify their public URLs. Social crawlers cannot use authenticated private-repository file links as public image endpoints.

**Your reef:** its application is Open WebUI. This kit does not change that application's icons, manifest, branding, or access controls.

## Hosted-page head template

This is an integration example, not a deployed page. It assumes a future project page at `https://example.com/shoal/` and the supplied files copied into that page's `assets/brand/` directory. Replace **every** `https://example.com/shoal/` occurrence with the final public page URL, retaining its trailing slash. Merge these tags into the destination's existing head rather than duplicating titles, canonical links, or social metadata.

```html
<title>SHOAL | Shared Home/Office AI, Locally</title>
<meta name="description" content="A field guide to shared local AI for homes and small offices. One reef, browser access from every device, and control over your setup.">
<link rel="canonical" href="https://example.com/shoal/">
<meta name="theme-color" content="#083E4B">
<meta name="apple-mobile-web-app-title" content="SHOAL">

<link rel="icon" href="https://example.com/shoal/assets/brand/favicon.ico" sizes="16x16 32x32 48x48 64x64">
<link rel="icon" type="image/png" sizes="16x16" href="https://example.com/shoal/assets/brand/favicon-16.png">
<link rel="icon" type="image/png" sizes="32x32" href="https://example.com/shoal/assets/brand/favicon-32.png">
<link rel="icon" type="image/svg+xml" sizes="any" href="https://example.com/shoal/assets/brand/icon.svg">
<link rel="apple-touch-icon" sizes="180x180" href="https://example.com/shoal/assets/brand/apple-touch-icon.png">
<link rel="mask-icon" href="https://example.com/shoal/assets/brand/safari-pinned-tab.svg" color="#083E4B">

<meta property="og:type" content="website">
<meta property="og:site_name" content="SHOAL">
<meta property="og:title" content="SHOAL | Shared Home/Office AI, Locally">
<meta property="og:description" content="One reef. Every screen. A field guide to shared local AI for homes and small offices.">
<meta property="og:url" content="https://example.com/shoal/">
<meta property="og:locale" content="en_US">
<meta property="og:image" content="https://example.com/shoal/assets/brand/social-preview.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1774">
<meta property="og:image:height" content="887">
<meta property="og:image:alt" content="SHOAL: fish gather around a small AI server in a sunlit coral reef. One reef. Every screen.">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="SHOAL | Shared Home/Office AI, Locally">
<meta name="twitter:description" content="One reef. Every screen. A field guide to shared local AI for homes and small offices.">
<meta name="twitter:image" content="https://example.com/shoal/assets/brand/social-preview.jpg">
<meta name="twitter:image:alt" content="SHOAL: fish gather around a small AI server in a sunlit coral reef. One reef. Every screen.">
```

No web-app manifest or offline behavior is claimed. The 192 px and 512 px icons are ready for a future site to reference if it defines a real installation experience. A documentation page does not become an AI application by adding a manifest.

Before treating a future integration as live, check the canonical page and every image URL without authentication, inspect the rendered head for duplicate tags, and check a browser tab, home-screen bookmark, Safari pinned tab, and a social-card preview on the intended platforms. Those platform checks have not been performed for this kit.

## Artwork and provenance

Created for this repository on 2026-09-27. The hero uses built-in image generation; the icons are original vector geometry with matching raster exports. The hero was exported to JPEG for delivery without changing its composition or dimensions. All delivered assets are covered by the repository's [MIT license](../LICENSE). The reef image is a conceptual illustration, not evidence of hardware performance or a photographed deployment.

| Color | Use |
|---|---|
| `#083E4B` | Deep teal icon background and template theme color |
| `#8AD8CE` | Seafoam fish |
| `#F5BB62` | Golden fish |
| `#FFF3CC` | Warm ivory fish |

The icon SVG is the editable master. Keep the pinned-tab version monochrome, and preserve enough contrast for the 16 px favicon. The hero uses illustrative variations of the same color family.

<details>
<summary>Hero generation prompt</summary>

Use case: illustration-story. Create one polished landscape 2:1 aspect ratio social preview illustration for SHOAL (Shared Home/Office AI, Locally), a documentation project about one local AI computer shared by home and small-office devices. Target 1280x640 if possible. Premium editorial paper-cut / screenprinted illustrated poster, subtle grain, warm ivory typography, deep ocean teal background, turquoise and sunlit seafoam, restrained golden-orange accents. An inviting shallow underwater scene with beautifully simplified fish swimming together around a small coral reef on the RIGHT HALF. Nestled into the reef is a tasteful tiny rounded rectangular server appliance with three softly glowing status lights, no brand logo. Sunbeams from above, sculptural coral and sea grasses along the bottom, a quiet feeling of ownership and shared intelligence. Not cyberpunk, not neon, not stock photography, no padlock shield or security promise, no cloud, no complex UI. LEFT HALF contains generous dark negative space and impeccably typeset exact text: large 'SHOAL', beneath in two readable lines 'Shared Home/Office AI,' and 'Locally.' Below, smaller 'One reef. Every screen.' Tiny top eyebrow 'A FIELD GUIDE TO LOCAL AI'. Text needs to remain very legible as a GitHub README banner and social card thumbnail. Keep all text and main illustration inset at least 7% from edges. Balanced, expressive, professional, calm. This is original conceptual artwork, not a screenshot or actual hardware product. Render the full finished image, not a mockup or frame.

</details>

## Reference pattern and specifications

The [Chai Chasers README](https://github.com/OKHP3/glee-fully-chai-chasers/blob/main/README.md) supplies the presentation pattern: title, concise promise, large image, prominent destination, then deeper context. Its [HTML head](https://github.com/OKHP3/glee-fully-chai-chasers/blob/main/index.html) supplies the complementary example of real website metadata and icon links. SHOAL uses its own imagery and documentation destinations.

Implementation references checked on 2026-09-27: [Open Graph](https://ogp.me/), [HTML link relations](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel), [manifest icons](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/icons), and Apple's [archived Safari pinned-tab specification](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/pinnedTabs/pinnedTabs.html). The Apple document describes the asset format; it is not a current-device test.

---

*Part of [SHOAL: Shared Home/Office AI, Locally](../README.md)*
