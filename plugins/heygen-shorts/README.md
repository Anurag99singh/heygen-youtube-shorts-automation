# HeyGen Shorts plugin

Installable skills bundle following the public OpenAI/Codex `.codex-plugin/plugin.json` format. Three skills: `setup-shorts`, `write-shorts-script`, `run-shorts-pipeline`. No API server or key is embedded.

After installation say: **Set up my Shorts workflow.** Connect Google Drive, HeyGen and Buffer, select your avatar/channel, then let setup create a new owner-specific Sheet and three approval-based tasks. GitHub is not required to run this installed plugin.

Voice: Anshul -- 17, verified in receiving account. Avatar varies per row. Video Agent only; complete prompt; B-roll, title and burned-in subtitles; human script and video approval. No paid generation during setup.

Supported packaging reference: https://github.com/openai/plugins . The local Codex plugin format and marketplace discovery can be validated; this is not a published ChatGPT directory listing or a guarantee of custom-plugin import in every Plus interface. A normal chat ZIP upload is not installation. Receiving account still needs supported plugin installation, required OAuth connections and scheduled access to the installed skills/tools. Report missing capabilities instead of claiming success.

Google Drive and HeyGen canonical app IDs are declared in `.app.json`. Buffer is a mandatory runtime connection resolved during setup; no unverified Buffer ID or MCP endpoint is fabricated.
