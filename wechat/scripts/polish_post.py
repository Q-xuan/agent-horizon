#!/usr/bin/env python3
"""Extract digest items. Next step is a rewrite with wechat/STYLE.md.

This does not fill in 「我的疑问」. It only pulls items out of a Horizon
Chinese digest so a person or write_from_digest.py can write the article.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_from_digest import main


if __name__ == "__main__":
    main()
