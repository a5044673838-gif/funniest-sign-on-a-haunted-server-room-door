import os

LINE = "DO NOT KNOCK. The ghost in rack 7 has rebooted the servers twice tonight and is not in the mood."


def main():
    assert 1 <= len(LINE) <= 120, "line must be 1-120 chars"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    assert LINE.endswith("."), "sign ends with a full stop"
    assert "\n" not in LINE, "must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
