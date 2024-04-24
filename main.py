from pyld import jsonld
import json
from pathlib import Path


def main():
    doc = json.load(open(Path("doc.json")))
    frame = json.load(open(Path("frame.json")))

    compacted = jsonld.compact(doc, {})
    print(json.dumps(compacted, indent=2))

    framed = jsonld.frame(doc, frame)
    print(json.dumps(framed, indent=2))


if __name__ == "__main__":
    main()
