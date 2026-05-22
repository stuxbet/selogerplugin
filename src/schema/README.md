# Generated AVIV schema

`generated.py` is **machine-generated** from [../../context/aviv-classified-api-v4.json](../../context/aviv-classified-api-v4.json). Do not edit by hand.

## Regenerate

```bash
pip install datamodel-code-generator
datamodel-codegen \
  --input ../../context/aviv-classified-api-v4.json \
  --input-file-type openapi \
  --output generated.py \
  --target-python-version 3.11 \
  --use-standard-collections \
  --use-union-operator
```

Re-run whenever the upstream spec in `context/` is updated.
