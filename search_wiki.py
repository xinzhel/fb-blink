import json
entity_catalogue="models/entity.jsonl"
entities={"laptop", "mouse", "cup", "burger", "elephant"}

# load all the 5903527 entities
title2desc = {}
local_idx = 0
with open(entity_catalogue, "r") as fin:
    lines = fin.readlines()
    for line in lines:
        entity = json.loads(line)
        if entity["title"].lower() in  entities:
            print(entity["title"])
            # entities.remove(entity["title"])
            if "idx" in entity:
                
                split = entity["idx"].split("curid=")
                if len(split) > 1:
                    wikipedia_id = int(split[-1].strip())
                else:
                    wikipedia_id = entity["idx"].strip()

            title2desc[entity["title"]] = entity["text"]
            local_idx += 1
        if len(entities) == 0:
            break

with open("title2desc.json", "w") as f:
    json.dump(title2desc, f, indent = 6)