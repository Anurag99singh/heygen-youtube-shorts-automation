# Install HeyGen Shorts

## For your boss
1. Download/extract the shared plugin source package. Connect Google Drive, HeyGen and Buffer in the Work/Codex interface where the plugin will run.
2. In a Codex version with plugin support, register the extracted package root and install:

```sh
codex plugin marketplace add /absolute/path/to/extracted/package
codex plugin add heygen-shorts@anurag-shorts
```

These commands are supported by the tested Codex CLI. A private Git source can be used instead if the recipient has repo access. Installing from a local package avoids needing the sender's private repository access. GUI custom-marketplace/import support varies; do not assume uploading a ZIP into a normal ChatGPT conversation installs a plugin. Plus can sign into Codex, but Plus alone does not establish native ChatGPT custom-plugin import availability.

3. Start a fresh session where installed skills are available and say: **Use HeyGen Shorts to set up my Shorts workflow.** Follow app sign-ins, choose avatar/channel, and check the new Sheet and three enabled/blocked task states. Setup spends no HeyGen credits and publishes nothing.

Once ready, fill A Video ID, B Topic, C Original Source URL, G Avatar and L READY. Review D then E APPROVE/REVISE with feedback F. Review J then I APPROVE/REVISE with F.

## Contents and verification
- `.agents/plugins/marketplace.json`: marketplace registration.
- `plugins/heygen-shorts/.codex-plugin/plugin.json`: plugin manifest.
- `plugins/heygen-shorts/skills/`: setup, writer and pipeline.
- No copied queue, schedules, account tokens or signed media.

Package validation does not prove receiving-account installation, OAuth or scheduler access. The setup skill must verify them and leave tasks paused if dependencies are unavailable. Do not claim this private package is published in the ChatGPT plugin directory.
