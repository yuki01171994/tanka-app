#!/usr/bin/env python3
"""日付入りの Markdown 日報テンプレートを生成するスクリプト。"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def build_content() -> str:
    return """# 今日の記録

- やったこと
- 気づき
- 明日
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="YYYY-MM-DD.md 形式の日報ファイルを生成します。"
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="出力先フォルダ（省略時: カレントディレクトリ）",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.directory).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{date.today().isoformat()}.md"
    output_path = output_dir / filename
    output_path.write_text(build_content(), encoding="utf-8")

    print(f"作成しました: {output_path}")


if __name__ == "__main__":
    main()
