# Publishing Checklist

- Confirm the target is one of the 12 active repositories.
- Stop immediately if the target is one of the 7 frozen repositories.
- Branch from the current default branch without force operations.
- Preserve target-only files unless removal is explicitly justified.
- Run baseline and final validation.
- Open a draft PR and inspect changed filenames.
- Require green CI and evidence artifacts where configured.
- Merge by squash after review.
- Update Roadmap release pins only for strict cross-repository dependencies.
- Keep credentials, local databases, caches, environments and generated transient outputs out of Git.
