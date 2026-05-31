import re
import hashlib
from collections import defaultdict

INPUT_VMF = "Path\To\Your\Input\Map.vmf"
OUTPUT_VMF = "Path\To\Your\Outpout\Map_clean.vmf"

def extract_blocks(text, name):
    blocks = []
    pos = 0
    pattern = name + "\n\t{"
    while True:
        start = text.find(pattern, pos)
        if start == -1:
            break

        brace = text.find("{", start)
        depth = 0

        for i in range(brace, len(text)):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1

                if depth == 0:
                    blocks.append((start, i + 1, text[start:i + 1]))
                    pos = i + 1
                    break
    return blocks

with open(INPUT_VMF, "r", encoding="utf-8", errors="ignore") as f:
    vmf = f.read()

solids = extract_blocks(vmf, "solid")

to_remove = []

seen = set()

for start, end, block in solids:
    normalized = re.sub(r'"id"\s+"\d+"', '"id" "X"', block)
    sig = hashlib.md5(normalized.encode()).hexdigest()

    if sig in seen:
        to_remove.append((start, end))
    else:
        seen.add(sig)

new_vmf = []
cursor = 0

for start, end in sorted(to_remove):
    new_vmf.append(vmf[cursor:start])
    cursor = end

new_vmf.append(vmf[cursor:])

with open(OUTPUT_VMF, "w", encoding="utf-8", errors="ignore") as f:
    f.write("".join(new_vmf))

print(f"Duplicates removed : {len(to_remove)}")
print(f"File created : {OUTPUT_VMF}")
