"""Patch Horizon's OpenAI client to send Grok reasoning_effort."""
from pathlib import Path
import sys

NEEDLE = '''        if self.provider not in self._NO_RESPONSE_FORMAT:
            request_kwargs["response_format"] = {"type": "json_object"}
        return await self.client.chat.completions.create(**request_kwargs)
'''
PATCH = '''        if self.provider not in self._NO_RESPONSE_FORMAT:
            request_kwargs["response_format"] = {"type": "json_object"}
        request_kwargs["extra_body"] = {"reasoning_effort": "xhigh"}
        return await self.client.chat.completions.create(**request_kwargs)
'''

def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "src/ai/client.py")
    text = path.read_text()
    if 'reasoning_effort' in text:
        print(f"already patched: {path}")
        return
    if NEEDLE not in text:
        raise SystemExit(f"patch target not found in {path}")
    path.write_text(text.replace(NEEDLE, PATCH, 1))
    print(f"patched {path} with reasoning_effort=xhigh")

if __name__ == "__main__":
    main()
